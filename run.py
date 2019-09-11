import os

from files.manipulate_files import *
from nlp_services.watson import *


def generate_results():
    list_to_test = get_test_files()
    result_list = []
    for utterance in list_to_test:
        print("Testando Utterance:", utterance[0])
        watson_response = get_watson_response(utterance[0])
        utterance_result = check_intent(watson_response, utterance[1])
        result_list.append(utterance_result)
    print("Testes finalizados!")
    
    return result_list

result_file = create_file()
resultado_final = generate_results()
edit_file(result_file, resultado_final)



            


