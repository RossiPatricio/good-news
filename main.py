from scraping import *
from html_generator import *

portals = {
    "cnn": scrap_cnn,
    "clarin": scrap_clarin,
    "times": scrap_times,
    "cnn_esp": cnn_español,
    "nbc": scrap_nbc,
    "cbs": scrap_cbs,
    "infobae": scrap_infobae,
}

keys_1 = [
    "Francisco",
    "Messi",
    "2026",
    "programming",
    "movie",
    "Putin",
    "Nirvana",
    "Michael Jackson",
    "Milei",
    "nvidia",
    "Quilmes",
    "Oasis",
    "Zelensky",
    "Kirchner",
    "Musk",
    "Burton",
    "Cobain",
    "Ukraine",
    "Potter",
    "Rowling",
    "Webb",
    "SpaceX",
    "NASA",
    "Depp",
    "Ucrania",
    "Poe",
    "chess",
    "Magnus Carlsen",
    "argentino",
    "Argentina",
    "Argentinian",
    "tim burton",
    "gothic",
    "church",
    "jesus",
    "yisus",
    "ia",
    "programming",
    "python",
    "skateboarding",
    "skate",
    "inteligencia artifical",
    "artificial intelligence",
    "specie",
    "species",
    "Egypt",
    "discovery",
    "death",
    "died",
    "die",
    "2026 world cup",
    "war",
    "openai",
    "chatgpt",
    "deepseek",
    "grok",
    "ia china",
    "rowling",
    "harry potter",
    "daniel radcliffe",
    "rupert grint",
    "emma watson",
    "harry potter hbo",
    "harry potter series",
]


# 1: Scrapeo cada portal y lo guardo en results:

results = {}

for portal, scraper in portals.items():
    try:
        results[portal] = scraper()
    except:
        continue


# 2: Top news: Escaneo results buscando coincidencias con keywords

def top_news(keys):
    top_news = []
    for articles in results.values():
        for article in articles:
            for key in keys:
                if key.casefold() in article['title'].casefold() :
                    top_news.append(article)
    results['top_news'] = top_news

top_news(keys_1)


# 3: Genero las plantillas html

for portal, article in results.items():
    try:
        html_generator(article, portal)
    except:
        continue

