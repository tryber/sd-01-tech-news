from news_exporter import json_exporter
from news_importer import json_importer
from news_scrapper import scrape


scrape()
json_exporter()
json_importer()
