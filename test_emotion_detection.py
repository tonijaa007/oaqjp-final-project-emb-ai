import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        expected_dominant_emotion = "joy"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_anger(self):
        text = "I am really mad about this"
        expected_dominant_emotion = "anger"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        expected_dominant_emotion = "disgust"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_sadness(self):
        text = "I am so sad about this"
        expected_dominant_emotion = "sadness"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_fear(self):
        text = "I am really afraid that this will happen"
        expected_dominant_emotion = "fear"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

if __name__ == '__main__':
    unittest.main()