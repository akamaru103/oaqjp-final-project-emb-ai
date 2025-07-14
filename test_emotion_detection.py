import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):

        # List of all test cases
        test_cases = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear'),
        ]

        # Loop to perform tests
        for text, expected_emotion in test_cases:

            # Get result and dominant emotion returned
            result = emotion_detector(text)
            returned_emotion = result['dominant_emotion']

            # Print out returned vs. expectation
            print (f'Returned: {returned_emotion}, Expected: {expected_emotion}')

            # run test to make sure they are equal
            self.assertEqual(returned_emotion, expected_emotion)


unittest.main()
