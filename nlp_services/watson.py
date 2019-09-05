from datetime import time

import watson_developer_cloud

username = ""
password = ""
version = ""
skill_id = ""

def watson_conversation(username, password, version):
    conversation = watson_developer_cloud.ConversationV1(username=username, password=password, version=version)
    return conversation

def get_watson_response(utterance):
    try_again = True

    while try_again == True:
        try:
            conversation = watson_conversation(username, password, version)
            response = conversation.message(skill_id, input={'text': utterance}).get_result()
            try_again == False
            break   
        except KeyboardInterrupt:
            break      
        except:
            print("Não consegui me conectar com o Watson, 1 segundo vou tentar de novo, pera aí...")
            time.sleep(1)
    
    return response

def check_intent(response, expected_intent):
    if len(response['intents']) > 0:
        watson_intent = str(response['intents'][0]['intent'])
        watson_confidence = str(round(float(response['intents'][0]['confidence']),2))
    else:
        watson_intent = 'Irrelevant'
        watson_confidence = '0'
    
    if expected_intent == watson_intent:
        print("SUCCESS! :)")
        result = "sucess"
    else:
        print("FAILED! :(")
        result = "failed"
    
    return result
