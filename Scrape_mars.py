# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Create global dictionary for Mongo 
mars_db = {}

# Nasa Mars News
def scrape_news():
    try: 

        browser = init_browser()

        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)

        # HTML 
        html_news = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_news, 'html.parser')

        news_title = soup.find("div", class_="content_title").text
        news_p = soup.find("div", class_ ="article_teaser_body").text

        # Dictionary entry from MARS NEWS
        mars_db['news_title'] = news_title
        mars_db['news_paragraph'] = news_p

        return mars_db

    finally:

        browser.quit()

# Feature Image
def scrape_mars_img():

    try: 

        browser = init_browser()

        featured_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_img_url)

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        featured_img_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]


        main_url = 'https://www.jpl.nasa.gov'

        featured_img_url = main_url + featured_img_url

        featured_img_url
        
        # Dictionary entry from FEATURED IMAGE
        mars_db['featured_img_url'] = featured_img_url 
        
        return mars_db
    
        finally:

        browser.quit()

        

# Mars Weather
def scrape_mars_weather():

    try: 

        browser = init_browser()

        weather_url = 'https://twitter.com/marswxreport?lang=en'
        
        browser.visit(weather_url)

        time.sleep(5)
        
        html_weather = browser.html
        
        weather_soup = BeautifulSoup(html_weather, "html.parser")
        
        mars_weather=weather_soup.find('div', class_ ='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text
        
        mars_weather

        # Dictionary entry from WEATHER
        mars_db['mars_weather'] = mars_weather 

        return mars_db
    
        finally:

        browser.quit()


# Mars Facts
def scrape_mars_facts():

 
    try:
        
    browser = init_browser()
        
    mars_df = pd.read_html("https://space-facts.com/mars/")[0]
   
    #print(mars_df)
    
    mars_df.columns=["Des", "MARS PLANET PROFILE"]
    
    mars_df.set_index("Des", inplace=True)
    
    mars_df

    # Dictionary entry from FACTS
    
    mars_db['mars_df'] = mars_df

    return mars_db

    finally:

    browser.quit()
    

# MARS HEMISPHERES


    # Cerberus Hemisphere Enhanced

    browser = init_browser()
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    time.sleep(5)

    html_mars_hemi = browser.html
    
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(mars_hemi_url, 'html.parser')

    hemi_page = browser.click_link_by_partial_text('Cerberus Hemisphere')
    hemi_html = browser.html
    soup_first_hemi = BeautifulSoup(hemi_html, 'html.parser')
    img1_url =soup_first_hemi.find('div', class_ ='content')

    img1_url

    #Summary
    summary_title =img1_url.find('h2', class_ = 'title').text
    summary_img =img1_url.find('a')['href']
    one ={'title':summary_title, "image_url":summary_img}
    one

    # Schiaparelli Hemisphere Enhanced

    browser = init_browser()
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    time.sleep(5)
    html_mars_hemi = browser.html
    
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')
    
    hemi_page2 = browser.click_link_by_partial_text('Schiaparelli Hemisphere')
    hemi_html2 = browser.html
    soup_second_hemi = BeautifulSoup(hemi_html2, 'html.parser')
    img2_url =soup_second_hemi.find('div', class_ ='content')

    img2_url

    #Summary
    summary_title2 =img2_url.find('h2', class_ = 'title').text
    summary_img2 =img2_url.find('a')['href']
    two ={'title':summary_title2, "image_url":summary_img2}
    two
    
    #Summary 
    
    summary_title2 =img2_url.find('h2', class_ = 'title').text
    summary_img2 =img2_url.find('a')['href']
    two ={'title':summary_title2, "image_url":summary_img2}
    two
                                                    

    # Syrtis Major Hemisphere Enhanced

    browser = init_browser()

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)
    
    time.sleep(5)
    html_mars_hemi = browser.html
                                                    
    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')


    hemi_page3 = browser.click_link_by_partial_text('Syrtis Major Hemisphere')
    hemi_html3 = browser.html
    soup_third_hemi = BeautifulSoup(hemi_html3, 'html.parser')
    img3_url =soup_third_hemi.find('div', class_ ='content')
    
    img3_url

    #Summary
    summary_title3 =img3_url.find('h2', class_ = 'title').text
    summary_img3 =img3_url.find('a')['href']
    three ={'title':summary_title3, "image_url":summary_img3}
    three

    # Valles Marineris Hemisphere Enhanced

    browser = init_browser()

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    time.sleep(5)
    html_mars_hemi = browser.html

    # Parse HTML with Beautiful Soup
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')


    hemi_page4 = browser.click_link_by_partial_text('Valles Marineris Hemisphere')
    hemi_html4 = browser.html
    soup_third_hemi = BeautifulSoup(hemi_html4, 'html.parser')
    img4_url =soup_third_hemi.find('div', class_ ='content')

    img4_url

    #Summary
    summary_title4 =img4_url.find('h2', class_ = 'title').text
    summary_img4 =img4_url.find('a')['href']
    four ={'title':summary_title4, "image_url":summary_img4}
    four

     # Dictionary entry from FACTS

    hemisphere_url = [one, two, three, four]
    hemisphere_url
                                                    
    mars_db['hemisphere_url'] = hemisphere_url                                            

    return mars_db

    finally:

    browser.quit()
    

pass