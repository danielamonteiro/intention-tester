import os

from files.manipulate_files import get_test_files, create_file, edit_file
from nlp_services.watson import get_watson_response, check_intent


def generate_results():
    try:
        result_file = create_file()
        list_to_test = get_test_files()
        result_list = []
        for utterance in list_to_test:
            print("Testando Utterance:", utterance[0])
            watson_response = get_watson_response(utterance[0])
            utterance_result = check_intent(watson_response, utterance[1])
            result_list.append(utterance_result)
        edit_file(result_file, result_list)
        print(f"Testes finalizados! ;)\nVerifique os resultados em 'files/result_files/{result_file}.xlsx'")        
    except KeyboardInterrupt:
        print("[ATENÇÃO] Aplicação parada pelo usuário")
    except Exception as e:
        print("[ERRO]", e)

if __name__ == "__main__":
    generate_results()



            


