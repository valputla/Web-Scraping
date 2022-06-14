from asyncore import dispatcher_with_send
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import time


mars_data = {}

def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    mars_webpage = browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    browser.quit()

    mars_data['news_p'] = news_p
    mars_data['news_title'] = news_title

    space_image_url = "https://spaceimages-mars.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    space_image_webpage = browser.visit(space_image_url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_result = soup.find('div', class_='floating_text_area')
    img_url = img_result.find('a')['href']
    img_complete_url = [space_image_url + img_url]  
    mars_data['img_complete_url'] = img_complete_url
    browser.quit()

    mars_table_url = "https://galaxyfacts-mars.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_table_webpage = browser.visit(mars_table_url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 
    table_html = soup.find('table', class_='table table-striped')
    table = pd.read_html("https://galaxyfacts-mars.com/")
    df = table[0]
    df = table[0]
    df.columns = ["", "Mars", "Data"]
    mars_table = df.set_index("Mars")
    mars_table_html = mars_table.to_html(classes='table table-stripped')
    mars_table_html = mars_table_html.replace('\n', '')
    mars_data["mars_table"] = mars_table_html
    browser.quit()

    astrology_url = "https://marshemispheres.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(astrology_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   
    mars_hemis = []
    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        time.sleep(3)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = astrology_url + partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()

        mars_data['mars_hemis'] = mars_hemis
    browser.quit()
    return mars_data


    
    

