import requests
from bs4 import BeautifulSoup

def scrap_cnn():
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

def scrap_times():
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

def scrap_nbc():
    url = 'https://www.nbcnews.com/latest-stories/'
    url2 = 'https://www.nbcnews.com/'
    lista_de_diccionarios = []

    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    news_1 = soup2.find_all('h2', class_='multistoryline__headline founders-cond fw6 lead')
    for element in news_1:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'title': titulo2, 'link': link2, 'portal': 'nbc'})  

    news_2 = soup2.find_all('h2', class_='storyline__headline founders-cond fw6 large')
    for element in news_2:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'title': titulo2, 'link': link2, 'portal': 'nbc'})

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all('h2', class_='multistoryline__headline founders-cond fw6 large noBottomSpace')
    for element in content:
        titulo= element.text
        link= element.a['href']
        lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'nbc'})  

    return lista_de_diccionarios

def scrap_clarin():
    url = 'https://www.clarin.com/'
    lista_de_diccionarios = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    noticia_destacada = soup.find('div', class_='sc-458ac523-0 bvJehW')
    link1 = noticia_destacada.a['href']
    lista_de_diccionarios.append({'title': noticia_destacada.text, 'link': link1, 'portal': 'clarin'})

    content = soup.find_all('div', class_='sc-86b8ec52-0 gPQASe onexone')
    for element in content:
        link = element.a['href']
        lista_de_diccionarios.append({'title': element.text, 'link': link, 'portal': 'clarin'})

    return lista_de_diccionarios

def cnn_español():
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

    return lista_de_diccionarios

def cnn_tecno():
    url = 'https://cnnespanol.cnn.com/ciencia'
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

    return lista_de_diccionarios
