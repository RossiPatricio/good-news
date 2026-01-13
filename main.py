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
    "Putin",
    "Nirvana",
    "Michael Jackson",
    "Milei",
    "nvidia",
    "Quilmes",
    "Oasis",
    "Zelensky",
    "Musk",
    "Burton",
    "Cobain",
    "Ukraine",
    "Potter",
    "Rowling",
    "SpaceX",
    "NASA",
    "Depp",
    "Ucrania",
    "chess",
    "Magnus Carlsen",
    "argentino",
    "Argentina",
    "Argentinian",
    "tim burton",
    "jesus",
    "programming",
    "python",
    "skateboarding",
    "skate",
    "inteligencia artifical",
    "artificial intelligence",
    "specie",
    "species",
    "Egypt",
    "world cup",
    "war",
    "openai",
    "chatgpt",
    "deepseek",
    "grok",
    "ai",
    "harry potter",
    "daniel radcliffe",
    "rupert grint",
    "emma watson",
    "harry potter",
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
    seen_titles = set()  # esto me ayudo la ia, no entiendo todavia

    for articles in results.values():
        for article in articles:
            title = article["title"].casefold()

            if title in seen_titles:
                continue

            for key in keys:
                if key.casefold() in title:
                    top_news.append(article)
                    seen_titles.add(title)  # add
                    break  # evita repetir por otra keyword

    results["top_news"] = top_news


top_news(keys_1)


# 3: Genero las plantillas html

for portal, article in results.items():
    try:
        html_generator(article, portal)
    except:
        continue
