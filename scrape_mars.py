# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

def init_browser():
executable_path = {'executable_path': 'chromedriver.exe'}
return browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    

        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)

        # HTML 
        html_news = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_news, 'html.parser')

        news_title = soup.find("div", class_="content_title").text
        news_p = soup.find("div", class_ ="article_teaser_body").text

        news_p 

        browser.quit()

# Feature Image

        featured_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_img_url)

        browser.links.find_by_partial_text('FULL IMAGE')
        browser.links.find_by_partial_text('more info')
        browser.links.find_by_partial_text('jpg')

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        featured_img_url = soup.find('img')['src']

        featured_img_url

        
# Mars Weather

        weather_url = 'https://twitter.com/marswxreport?lang=en'
        
        browser.visit(weather_url)

        # time.sleep(5)
        
        html_weather = browser.html
        
        weather_soup = BeautifulSoup(html_weather, "html.parser")
        
        mars_weather=weather_soup.find('div', class_ ='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text
        
        mars_weather


# Mars Facts


    mars_df = pd.read_html("https://space-facts.com/mars/")[0]

    #Panda DataFrame
    #mars_df.columns=["Des", "MARS PLANET PROFILE"]
    #mars_df.set_index("Des", inplace=True)
    #mars_df

    mars_df.columns=["Description", "Value"]
    mars_df.set_index("Description", inplace = True)
    mars_facts = mars_df.to_html(classes="table")
    mars_facts =mars_df.replace("'","")
    mars_facts

    

# MARS HEMISPHERES

    # Cerberus Hemisphere 

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    html_mars_hemi = browser.html
    soup_mars_hemi = BeautifulSoup(mars_hemi_url, 'html.parser')

    #Pull specific data from webpage
    hemi_title1_url = soup_mars_hemi.find('h2', class_ ='title').text
    img1_url =soup_mars_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    one ={'title':hemi_title1_url, "img_url":img1_url}
    one


    # Schiaparelli Hemisphere 

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html_mars_hemi = browser.html
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')

    #Pull specific data from webpage
    hemi_title2_url = soup_mars_hemi.find('h2', class_ ='title').text
    img2_url =soup_mars_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    two ={'title':hemi_title2_url, "img_url":img2_url}
    two
                                      

    # Syrtis Major Hemisphere 

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    # Click to URL of page to be scraped and extract data
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html_mars_hemi = browser.html
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')

    # Pull specific data from webpage
    hemi_title3_url = soup_mars_hemi.find('h2', class_ ='title').text
    img3_url =soup_mars_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    three ={'title':hemi_title3_url, "img_url":img3_url}
    three

    # Valles Marineris Hemisphere 

    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html_mars_hemi = browser.html
    soup_mars_hemi = BeautifulSoup(html_mars_hemi, 'html.parser')

    #Pull specific data from webpage
    hemi_title4_url = soup_mars_hemi.find('h2', class_ ='title').text
    img4_url =soup_mars_hemi.find('a', text ='Sample').get("href")

    #Put data into a dictionary
    four ={'title':hemi_title4_url, "img_url":img4_url}
    four


     #Summary

    hemisphere_url = [one, two, three, four]
    hemisphere_url
                                                    
    # Store data in a dictionary
    mars_data = {


        "News_Title" : news_p,
        "Featured_Image" : featured_img_url,
        "Mars_Weather" : mars_weather,
        "Mars_Facts" : mars_facts,
        "Hemisphere_Images" : hemisphere_img_url

    }

    browser.quit()

    # Return results
    return mars_data

pass