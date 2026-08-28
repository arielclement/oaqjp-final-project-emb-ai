"""Unit tests for the emotion detection function."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_detector(self):
        """Verify that emotion_detector identifies the dominant emotion."""

        test_case_1 = emotion_detector("I am glad this happened")
        test_case_2 = emotion_detector("I am really mad about this")
        test_case_3 = emotion_detector("I feel disgusted just hearing about this")
        test_case_4 = emotion_detector("I am so sad about this")
        test_case_5 = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(test_case_1["dominant_emotion"], "joy")
        self.assertEqual(test_case_2["dominant_emotion"], "anger")
        self.assertEqual(test_case_3["dominant_emotion"], "disgust")
        self.assertEqual(test_case_4["dominant_emotion"], "sadness")
        self.assertEqual(test_case_5["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
