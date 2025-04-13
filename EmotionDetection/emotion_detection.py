import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    dominant_emotion = ''
    max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
    for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
        if score == max_score:
            dominant_emotion = emotion

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
     'sadness': sadness_score, 'dominant_emotion': dominant_emotion}