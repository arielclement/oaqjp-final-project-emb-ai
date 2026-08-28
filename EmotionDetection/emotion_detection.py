"""Provides emotion detection functionality for customer feedback.

This module uses an AI-based emotion detection service to analyze
customer feedback and identify the emotion expressed in the text.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """Detects the emotion expressed in the given text.
    """

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1'
        '/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers, timeout = 5)
    json_response = json.loads(response.text)

    formatted_response = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if response.status_code == 400:
        return formatted_response

    emotions = json_response["emotionPredictions"][0]["emotion"]

    for emotion in formatted_response:
        if emotion != "dominant_emotion":
            formatted_response[emotion] = emotions[emotion]

    formatted_response["dominant_emotion"] = max(emotions, key=emotions.get)

    return formatted_response
