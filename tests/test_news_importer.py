import os
from tech_news_data_collector.news_importer import *

CURRENT_PATH = os.path.dirname(__file__)

def test_csv_importer_arquivo_nao_existe():
    assert False


def test_csv_importer_extensao_invalida():
    assert False


def test_csv_importer_cabecalho_invalido():
    assert False


def test_csv_importer_informacoes_incompletas():
    assert False


def test_csv_importer_urls_duplicadas():
    assert False


def test_csv_importer_importacao_interrompida_em_caso_de_erro():
    assert False


def test_csv_importer_sucesso():
    assert False


def test_json_importer_arquivo_nao_existe():
    assert False


def test_json_importer_extensao_invalida():
    assert False


def test_json_importer_json_invalido():
    assert False


def test_json_importer_informacoes_incompletas():
    assert False


def test_json_importer_urls_duplicadas():
    assert False


def test_json_importer_importacao_interrompida_em_caso_de_erro():
    assert False


def test_json_importer_sucesso():
    file_path = os.path.join(CURRENT_PATH, 'samples', 'doc.json')
    res = json_importer(file_path)
    assert len(res) == 1
    assert res[0]['title'] == 'Alemanha já trabalha na regulamentação de carros autônomos'
    assert len(res[0]['categories']) == 4
    for cat in res[0]['categories']:
        assert cat in ["Mobilidade Urbana/Smart Cities", "Veículos autônomos", "Carro", "Política"]
