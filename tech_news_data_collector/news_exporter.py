import json
import csv
from news_scrapper import scrape


def csv_exporter():
    news_data = scrape()
    with open('tech_news.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["url", "title", "timestamp", "writer", "shares_count", "comments_count", "summary", "sources", "categories"])

        for news in news_data:
            writer.writerow([news['url'], news['title'], news['timestamp'], news['writer'], news['shares_count'], news['comments_count'], news['summary'], news['sources'], news['categories']])


def json_exporter():
    news_data = scrape()
    f = open('tech_news.json', 'w')
    f.write(json.dumps(news_data, indent=2))


json_exporter()
csv_exporter()
