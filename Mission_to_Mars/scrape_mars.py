from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    mars_webpage = browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   

    result = soup.find('div', class_='col-md-12')
    titles = result.find_all('div', class_='content_title')
    paragraphs = result.find_all('div', class_='article_teaser_body')
    browser.quit()


    space_image_url = "https://spaceimages-mars.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    space_image_webpage = browser.visit(space_image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_result = soup.find('div', class_='floating_text_area')
    img_url = img_result.find('a')['href']
    img_complete_url = [space_image_url + img_url]  
    browser.quit()

    mars_table_url = "https://galaxyfacts-mars.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_table_webpage = browser.visit(mars_table_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    table_html = soup.find('table', class_='table table-striped')
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    astrology_url = "https://marshemispheres.com/"
    browser.visit(astrology_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_link_html = soup.find('div', class_='collapsible results')
    results = img_link_html.find_all('div', class_='item')
    mars_img_link = []
    mars_dict = {}

    for link in range(len(results)):
        title = results[link].find('div', class_='description')
        title = results[link].find('h3').text
    
        mars_url_list = results[link].a['href']
        browser.visit(astrology_url + mars_url_list)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
        image = soup.find('div', class_='container')
        image = image.find('div', class_='wide-image-wrapper')
        image = image.find('img', class_='wide-image')
        image = astrology_url + image['src']
        mars_dict[f"title: {link}"] = title
        mars_dict[f"img_url : {link}"] = image
    
    mars_img_link.append(mars_dict)
    browser.quit()
