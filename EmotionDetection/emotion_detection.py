import json
import requests

def emotion_detector(text_to_analyse):

    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    payload = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=payload, headers=headers)

    #Convert the response text into a dictionary using the json library functions
    data = json.loads(response.text)

    # Get the predicted emotions from the JSON
    emotions = data['emotionPredictions'][0]['emotion']

    # Get the max. value and corresponding key for the dominant emotion
    dominant = max(emotions, key=emotions.get)

    # Sort the emotions alphabetically by key for output
    emotions_sorted = dict(sorted(emotions.items()))

    # Use ** to flatten the emotions dict,
    # then add the dominant emotion to the result to be output
    result = {
        **emotions_sorted,
        'dominant_emotion': dominant
    }

    # Return a dictionary containing emotions results
    return result
