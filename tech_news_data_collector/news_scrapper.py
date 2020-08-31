import requests
import parsel
import json
import csv
import service

dataJson = []


def getAllLinks(url):
    print(url)
    response = requests.get(url)
    selector = parsel.Selector(response.text)
    linksNotice = selector.xpath("//a[@class='tec--card__title__link']/@href").getall()
    print(linksNotice)
    return linksNotice


def getTitle(content):
    selector = parsel.Selector(content)
    title = selector.xpath("//h1[@class='tec--article__header__title']/text()").get()
    return title.strip()


def getTimestamp(content):
    selector = parsel.Selector(content)
    timestamp = selector.css(".tec--timestamp__item").xpath('./time/@datetime').get()
    return timestamp


def getWriter(content):
    selector = parsel.Selector(content)
    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        return writer.strip()
    return writer


def getSharesCount(content):
    selector = parsel.Selector(content)
    shares_count = selector.css(".tec--toolbar__item ::text").getall()
    return shares_count[3].split(' ')[4]


def getCommentsCount(content):
    selector = parsel.Selector(content)
    CommentsCount = selector.css("#js-comments-btn").xpath('./@data-count').get()
    return CommentsCount


def getSummary(content):
    selector = parsel.Selector(content)
    summary = selector.css(".tec--article__body p").get()
    selectorSummary = parsel.Selector(summary)
    text = selectorSummary.css("*::text").getall()
    text2 = " ".join(text)
    return text2


def formatValue(value):
    newValue = value.strip()
    return newValue


def getSources(content):
    selector = parsel.Selector(content)
    allSources = selector.xpath("//a[@class='tec--badge']/text()").getall()
    if allSources:
        sources = map(formatValue, allSources)
        return list(sources)
    return allSources


def getCategories(content):
    selector = parsel.Selector(content)
    categories = selector.css("#js-categories a::text").getall()
    if categories:
        text = map(formatValue, categories)
        return list(text)
    return categories


def getData(content, link):
    if '/minha-serie/' in link:
        return
    objData = {
        "url": link,
        "title": getTitle(content),
        "timestamp": getTimestamp(content),
        "writer": getWriter(content),
        "shares_count": getSharesCount(content),
        "comments_count": getCommentsCount(content),
        "summary": getSummary(content),
        "sources": getSources(content),
        "categories": getCategories(content),
    }
    dataJson.append(objData)


def getAllData(url):
    links = getAllLinks(url)
    for link in links:
        success = False
        retrives = 1
        while not success and retrives <= 3:
            response = requests.get(link)
            contentEncoding = response.headers['Content-Encoding']
            success = contentEncoding == 'gzip'
            retrives += 1
            if response.status_code == 404:
                retrives = 4
            if success:
                result = response.text
                getData(result, link)


def scrape(num=1):
    print("loading...")
    repeat = 1
    while repeat <= num:
        if repeat == 1:
            getAllData("https://www.tecmundo.com.br/novidades/")
            print('aq')
        else:
            getAllData("https://www.tecmundo.com.br/novidades?page=2")
            print('aq2')
        print(repeat)
        repeat += 1
    # print(dataJson, 'dataJson')
    createFile(dataJson)
    print('Raspagem de notícias finalizada')


def createFile(value):
    with open('data.json', 'w', encoding='utf-8-sig') as outfile:
        json.dump(value, outfile, indent=4, separators=(',', ': '), ensure_ascii=False)
    with open('data.csv', 'w', encoding='utf-8-sig') as file:
        fieldnames = service.valid_Header
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in value:
            writer.writerow(item)


scrape(2)
