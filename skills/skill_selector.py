import json

def get_skills():
    try:
        with open('service_credentials.json') as json_file:
            skill_list_file = json.load(json_file)
            skill_list = []
            for skill in skill_list_file['skills']:
                skill_list.append(skill['name'])
    
        return skill_list
    except:
        print("[ERRO] Não foi possível carregar a lista de skills. Por favor, verifique se o arquivo service_credentials.json está preenchido corretamente.")
    json_file.close()

def choose_skill(skill_list):
    valid_skill = False
    while valid_skill == False:
        try:
            print("Escolha o skill que você deseja usar (escolha o número): ")
            for skill in skill_list:
                index = skill_list.index(skill)+1
                print(f"{index} - {skill}")
            skill_input = int(input("Skill: "))
            chosen_index = skill_input-1
            if chosen_index not in range(len(skill_list)):
                print("[ATENÇÃO] Skill selecionado inválido, escolha outro.\n")
            else:
                chosen_skill = skill_list[chosen_index]
                print("Skill selecionado:", chosen_skill)
                valid_skill = True
                return chosen_skill
        except:
            print("[ATENÇÃO] Erro ao selecionar o skill. Tente novamente.\n")

def get_skill_credentials(skill_name):
    with open('service_credentials.json') as json_file:
        skill_list_file = json.load(json_file)['skills']
        skill_to_use = next((skill for skill in skill_list_file if skill['name'] == skill_name), None)
    json_file.close()
    
    return skill_to_use