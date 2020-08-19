# from tech_news_data_collector.news_scrapper import scrape

from tech_news_data_collector.news_exporter import csv_exporter

# scrape()

path_csv = "files_import/news.csv"

csv_exporter(path_csv)
