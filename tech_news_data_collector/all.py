from news_exporter import csv_exporter, json_exporter
from news_scrapper import scrape2
from news_importer import init


scrape2("https://www.tecmundo.com.br/novidades/")
init()
csv_exporter()
json_exporter()
