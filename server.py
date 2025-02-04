"""
server.py: A Flask application to detect emotions in text using
the Watson NLP EmotionPredict service.
"""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in the given text.

    Returns:
        json: A JSON response containing the formatted message with emotion scores
              and the dominant emotion. If the input is invalid, returns an error message.
    """
    data = request.json
    text_to_analyze = data.get('text', '')
    emotions = emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again."})
    response = {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": emotions['dominant_emotion']
    }
    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
    return jsonify({"message": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
