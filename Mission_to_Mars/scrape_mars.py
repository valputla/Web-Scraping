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
    print(img_complete_url)
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
    mars_table = df.rename(columns={0: 'Mars-Earth Comparison', 1:'Mars', 2: 'Earth'})
    mars_table.set_index('Mars-Earth Comparison')
    mars_table = mars_table.to_html(classes='table table-stripped', justify='left', border=1)
    mars_table = mars_table.replace('\n', '')
    browser.quit()

    astrology_url = "https://marshemispheres.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(astrology_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    img_link_html = soup.find('div', class_='collapsible results')
    anchor = img_link_html.find_all('h3')
    titles = []
    links = []

    for h3 in range(0, len(anchor)):
        descriptions = anchor[h3].text
        titles.append(descriptions)

    for title in titles:
        browser.links.find_by_partial_text(title).click()
        browser.links.find_by_text('Open').click()
        time.sleep(5)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find('img', class_="wide-image")['src']
        image_link = astrology_url + partial
        title_img_dict = {}
        title_img_dict['title'] = title
        title_img_dict['img_url'] = image_link
        
        links.append(title_img_dict)
        browser.links.find_by_text('Close').click()
        browser.links.find_by_partial_text('Back').click()

    print(links)
    browser.quit()

    
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    mars_data['img_complete_url'] = img_complete_url
    mars_data['mars_table'] = mars_table
    mars_data['links'] = links

    return mars_data


    
    

