import os.path
import os
from os import path

import openpyxl
from openpyxl.utils import get_column_letter

def create_file():
    name_file = input("Insira o nome do arquivo que será gerado com os resulados dos testes: ")
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, f"../files/result_files/{name_file}.xlsx")
    while path.exists(file_path) == True:
        name_file = input(f"O arquivo '{name_file}' já existe. Escolha outro nome: ")
        file_path = os.path.join(my_path, f"../files/result_files/{name_file}.xlsx")
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Resultados"
        wb.save(file_path)
        print(f"Arquivo '{name_file}.xlsx' criado com sucesso!")
    except:
        print(f"[ATENÇÃO] Erro ao criar o arquivo '{name_file}.xlsx'")
    
    return name_file


def see_files_infos(name_file):
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../files/result_files/{name_file}.xlsx")
        workbook_file = openpyxl.load_workbook(path)
        print(workbook_file.sheetnames)
    except:
        print(f"[ATENÇÃO] Erro ao abrir o arquivo '{name_file}.xlsx' verifique se ele existe na pasta result_files!")


def edit_file(name_file, result_list):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, f"../files/result_files/{name_file}.xlsx")
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    headers = ["Utterance","Intenção Esperada","Intenção Retornada","Confiança","Resultado"]
    ws.append(headers)
    for result in result_list:
        ws.append(result)

    ws.delete_rows(1, 1)
    wb.save(path)