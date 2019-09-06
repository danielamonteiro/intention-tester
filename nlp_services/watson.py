import time

import ibm_watson

username = ""
password = ""
version = ""
skill_id = ""
url = ""

def watson_conversation(username, password, version):
    conversation = ibm_watson.AssistantV1(username=username, password=password, version=version)
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
    if 'input' in response:
        utterance = response['input']['text']
    else:
        utterance = ""

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
    
    result_list = [utterance, expected_intent, watson_intent, watson_confidence, result]
    return result_list