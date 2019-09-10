import time
import ibm_watson
import sys
sys.path.append("..")
from skills.skill_selector import get_skill_credentials

'''
username = "798d9946-1cd1-4760-8159-dc5994aa529b"
password = "AaueW82kHTcV"
version = "2018-07-10"
skill_id = "ebb90339-b69c-41a9-8030-51891bede0f0"
url = "https://gateway.watsonplatform.net/assistant/api"
'''
version, skill_id, username, password, url = get_skill_credentials()


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
        result = "Sucess"
    else:
        result = "Failed"
    
    result_list = [utterance, expected_intent, watson_intent, watson_confidence, result]
    return result_list

resposta = get_watson_response("hola")
print(resposta)