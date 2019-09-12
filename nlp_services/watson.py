import time
import ibm_watson
import sys

sys.path.append("..")
from skills.skill_selector import get_skill_credentials, get_skills_list

version, skill_id, username, password, url = get_skill_credentials()


def watson_conversation(username, password, version):
    conversation = ibm_watson.AssistantV1(username=username, password=password, version=version)
    return conversation

def get_watson_response(utterance):
    try_again = True
    retry = 0

    while try_again == True:
        try:
            if retry > 4:
                print("[ATENÇÃO] Não estou conseguindo me conectar com o Watson. Por favor, verifique se as informações do arquivo 'service_credentials.json' está preenchido corretamente e tente novamente")  
                break  
            conversation = watson_conversation(username, password, version)
            response = conversation.message(skill_id, input={'text': utterance}).get_result()
            try_again == False
            break   
        except:
            print("Não consegui me conectar com o Watson, 1 segundo vou tentar de novo, pera aí...")
            time.sleep(1)
            retry = retry+1
    
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