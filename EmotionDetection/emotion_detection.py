
# Import the requests library to handle HTTP requests
import requests  
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header)


    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    #print(formatted_response)

    # Extracting anger,disgust,fear,joy,sadness from the response

    anger_value = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_value = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_value = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_value = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_value = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Define dominant emotion

    emotions = {
        'anger': anger_value,
        'disgust': disgust_value,
        'fear': fear_value,
        'joy': joy_value,
        'sadness': sadness_value
    }

    dominant_emotion = max(emotions, key=emotions.get)

    # Returning a dictionary containing sentiment analysis results
    return {
            'anger': anger_value,
            'disgust': disgust_value,
            'fear': fear_value,
            'joy': joy_value,
            'sadness': sadness_value,
            'dominant emotion': dominant_emotion
            }
