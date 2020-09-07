from news_exporter import json_exporter
from news_importer import json_importer
from news_scrapper import scrape
import sys


def instruction():
    return {            
        "1": "Importar notícias a partir de um arquivo",
        "2": "Exportar notícias para JSON",
        "3": "Raspar notícias online",
        "4": "Sair",
    }


def instruction2(choice):
    print("choice", choice)
    instruct = {
        "1": "Digite o path do arquivo JSON a ser importado",
        "2": "Digite o nome do arquivo JSON a ser exportado:",
        "3": "Digite a quantidade de páginas a serem raspadas:",
    }
    write_input = input(instruct[str(choice)])
    instruct2 = {
        "1": f"{json_importer(write_input)}",
        "2": f"{json_exporter(write_input)}",
        "3": f"{scrape(write_input)}",
    }
    return instruct2[choice](write_input)


def input_master():
    choice = input(f"Selecione uma das opções a seguir: \n\n {instruction()}")
    choice = int(choice)

    if choice == 1:
        instruction2(choice)
    elif choice == 2:
        instruction2(choice)
    elif choice == 3:
        instruction2(choice)
    elif choice == 4:
        print("até mais")
    else:
        try:
            raise ValueError('Opção invalida')
        except Exception as error:
            print(error, file=sys.stderr)
        input_master()


input_master()
