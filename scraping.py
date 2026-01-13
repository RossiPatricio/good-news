import requests
from bs4 import BeautifulSoup

def scrap_cnn():
    try: 
        url = 'https://edition.cnn.com/'
        lista_de_diccionarios = []

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        content = soup.find('h2', class_='container__title_url-text container_lead-plus-headlines-with-images__title_url-text')
        if content:
            titulo = content.text.strip()
            enlace_padre = content.find_parent('a')
            if enlace_padre:
                link = url + enlace_padre['href']
                lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})

        content1 = soup.find_all('div', class_='container__text container_lead-plus-headlines-with-images__text')
        for e in content1:
            titulo = e.text.strip()
            enlace_padre = e.find_parent('a')
            if enlace_padre:
                link = url + enlace_padre['href']
                lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})  

        return lista_de_diccionarios
    except Exception as e:
        return e

def scrap_times():
    try:
        link = 'https://www.nytimes.com/international/'
        lista_de_diccionarios = []

        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        elements = soup.find_all('p', class_='indicate-hover css-91bpc3')
        for element in elements:
            titulo = element.get_text().strip()
            enlace_padre = element.find_parent('a')
            if enlace_padre:
                noticia_link = enlace_padre['href']
                lista_de_diccionarios.append({'title': titulo, 'link': noticia_link, 'portal': 'times'})

        return lista_de_diccionarios
    except  Exception as e:
        return e

def scrap_nbc():
    try:
        lista_de_diccionarios = []

        ## PRINCIPAL
        
        headlines = "https://www.nbcnews.com/"
        response = requests.get(headlines)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Portada

        portada = soup.find("h2", class_="storyline__headline founders-cond fw6 lead")
        title = portada.text
        link = portada.a['href']
        lista_de_diccionarios.append({"title": title, "link": link, "image_path": "", "portal": "nbc"})

        
        #Primera pagina
        
        first_news = soup.find_all(
            "h2", class_="storyline__headline founders-cond fw6 large"
        )     
        
        vistos = set()

        for article in first_news:

            link = article.a["href"]

            if link in vistos:
                continue

            vistos.add(link)
            title = article.text
            link = article.a['href'] 
            lista_de_diccionarios.append({"title": title, "link": link, "image_path": "", "portal": "nbc"})        
        

        # Latest news

        latest_news = soup.find_all("h2", class_="styles_teaseTitle__ClSV0")

        for article in latest_news:
            title = article.text
            link = article.a["href"]
            lista_de_diccionarios.append(
                {"title": title, "link": link, "image_path": "", "portal": "nbc"}
            )
            
        print("Latest:", len(latest_news))

        
        ## WORLD NEWS:

        world_news = "https://www.nbcnews.com/world"
        response_2 = requests.get(world_news)
        soup_2 = BeautifulSoup(response_2.content, "html.parser")

       
        # More world news

        news_3 = soup_2.find_all("h2", class_="wide-tease-item__headline")

        for article in news_3:
            enlace_padre = article.find_parent("a")
            title = article.text
            link = enlace_padre["href"]
            lista_de_diccionarios.append(
                {"title": title, "link": link, "image_path": "", "portal": "nbc"}
            )

        print("More world news:", len(news_3))

        # Latest world news

        news_2 = soup_2.find_all("h2", class_="styles_headline__Gk6tj")

        for article in news_2:
            title = article.text
            link = article.a["href"]
            lista_de_diccionarios.append(
                {"title": title, "link": link, "image_path": "", "portal": "nbc"}
            )

        print("Latest world news:", len(news_2))

        return lista_de_diccionarios
    except Exception as e:
        return e

def scrap_clarin():
    try:
        url = 'https://www.clarin.com/'
        lista_de_diccionarios = []

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        noticia_destacada = soup.find('div', class_='sc-6f7fdbd5-0 cHotwD')
        link1 = noticia_destacada.a['href']
        lista_de_diccionarios.append({'title': noticia_destacada.text, 'link': link1, 'portal': 'clarin'})

        content = soup.find_all('div', class_='sc-d645642f-0 cqfesC onexone')
        for element in content:
            link = element.a['href']
            lista_de_diccionarios.append({'title': element.text, 'link': link, 'portal': 'clarin'})

        return lista_de_diccionarios
    except Exception as e:
        return e

def cnn_español():
    try:
        url = 'https://cnnespanol.cnn.com/entretenimiento/cine'
        lista_de_diccionarios = []

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        content2 = soup.find_all('span', class_='container__headline-text')
        for e in content2:
            titulo = e.text.strip()
            enlace_padre = e.find_parent('a')
            if enlace_padre:
                link = url + enlace_padre['href']
                lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})   

        url = 'https://cnnespanol.cnn.com/'
        lista_de_diccionarios = []

        response2 = requests.get(url)
        soup2 = BeautifulSoup(response2.content, 'html.parser')

        content3 = soup2.find_all('span', class_='container__headline-text')
        for e in content3:
            titulo = e.text.strip()
            enlace_padre = e.find_parent('a')
            if enlace_padre:
                link = url + enlace_padre['href']
                lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})       

        return lista_de_diccionarios
    except Exception as e:
        return e

def scrap_cbs():
    try:
        response = requests.get('https://www.cbsnews.com/')
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify)
        lista_de_diccionarios= []

        contents = soup.find_all('div', class_='item__title-wrapper')

        for article in contents:
            title = article.h4.text.strip()
            enlace_padre = article.find_parent('a')

            if enlace_padre and enlace_padre.find('span'):
                link = enlace_padre['href']
                img_span = enlace_padre.find('span')
                img_tag = img_span.find('img')  

                if img_tag:
                    img = img_tag['src']

            lista_de_diccionarios.append({'title': title, 'link': link, 'image_path': img, 'portal': 'cbs'})

        return lista_de_diccionarios
    except Exception as e:
        return e

def scrap_infobae():
    try:
        url = 'https://www.infobae.com'
        articles = []
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        elements = soup.find_all('h2', class_='story-card-hl headline-link headline')
        for e in elements:
            title = e.text.strip()
            enlace_padre = e.find_parent('a')
            if enlace_padre:
                href = enlace_padre.get('href', '')
                if not href.startswith('http'):
                    article_link = url + href
                else:
                    article_link = href
                image = enlace_padre.find('img', class_='global-image story-card-img')
                if image:
                    image_path = image.get('src', 'No image found')
                else:
                    image_path = 'No image found'
                articles.append({'title': title, 'link': article_link, 'image_path': image_path, 'portal': 'infobae'})
        return articles
    except Exception as e:
        return e