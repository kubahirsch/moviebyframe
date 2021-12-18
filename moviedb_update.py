from bs4 import BeautifulSoup
from requests import get, request
import json
from selenium import webdriver
import os 
import time 





def updatingMoviedbFilmweb(movies):
    os.environ["PATH"] += r"D:\program files\chromedriver_win32"
    driver = webdriver.Chrome()
    driver.get('https://www.filmweb.pl/ranking/film')

    driver.find_element_by_class_name('didomi-components-button.didomi-button.didomi-dismiss-button.didomi-components-button--color.didomi-button-highlight.highlight-button').click()

    driver.execute_script("window.scrollTo(0, 4000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 7000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 11000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 15000)")
    time.sleep(2)
    bsFw = BeautifulSoup(driver.page_source)

    filmwebIds = []
    for rankingType in bsFw.find_all('h2', class_='rankingType__title'):
        a = rankingType.find_all('a', href=True)
        filmwebIds.append(a[0]['href'])

    i= 0
    for id in filmwebIds:
        driver.get("https://www.filmweb.pl" + id)
        if i==0:
            time.sleep(5)
            driver.find_element_by_id('sas_labelClose_10563134').click()
            time.sleep(2)
        title = driver.title[:-16]
        try:
            titleAng = driver.find_element_by_class_name('filmCoverSection__orginalTitle').text
        except:
            titleAng = title
        year = driver.find_element_by_class_name('filmCoverSection__year').text
        try:
            driver.find_element_by_class_name('gallery__photo-item__wrapper.gallery__photo-item__wrapper--3.slideshowStart').click()
        except:
            continue
        time.sleep(2)
        try:
            img = driver.find_element_by_class_name('lightBoxPhoto__image').get_attribute("src")
        except:
            continue

        movie = {
            'title': title,
            'url': img,
            'year': year,
            'titleAng': titleAng,
        }
        movies.append(movie)
        i+=1
    

###############################################################
popularPage = get('https://www.imdb.com/search/title/?title_type=feature,tv_movie&num_votes=500000,&count=250')

bs = BeautifulSoup(popularPage.content, features='html.parser')

movieIds = []

for itemContent in bs.find_all('h3', class_='lister-item-header'):
    a = itemContent.find_all('a', href=True)
    movieIds.append(a[0]['href'][7:16])


url = "https://imdb8.p.rapidapi.com/title/get-images"

querystring = {"tconst":id,"limit":"1"}


def updatingMoviedbImdb(movies):
    i = 0
    for id in movieIds:
        querystring = {"tconst":id,"limit":"1"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "20dab78eb2mshe94cb382a5e744ep1a3e2ajsn7391cbaaa5bc"
            }

        response = request("GET", url, headers=headers, params=querystring)
        output = response.json()
        movies.append({'id': i, 'title': output['images'][0]['relatedTitles'][0]['title'], 'url': output['images'][0]["url"]})
    return movies



