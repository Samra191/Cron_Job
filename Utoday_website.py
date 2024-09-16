from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import json
import re

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the URL
driver.get("https://u.today/latest-cryptocurrency-news")

def date_checkseven(Date):
    given_date = datetime.strptime(Date, "%b %d, %Y - %H:%M")

    current_date = datetime.now()
    # Calculate the date for seven days ago
    seven_days_ago = current_date - timedelta(days=7)
    
    # Check if the given date is within the last seven days
    if seven_days_ago <= given_date <= current_date:
        return True
    else:
        return False

article_links=[]
last_news=[]
news_list=[]

main_container=driver.find_element(By.CLASS_NAME, 'categories-list')
container1=main_container.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div')
news_items=container1.find_elements(By.CLASS_NAME,'news__item')
for news_item in news_items:
    items_date=news_item.find_element(By.CLASS_NAME,"news__item-head")
    date=items_date.find_element(By.CLASS_NAME,"humble").text
    res = date_checkseven(date)
    Url=news_item.find_element(By.CLASS_NAME,"news__item-body").get_attribute('href')
    news_list.append(Url)
    
with open ("bitcoin_news_data.json","w") as f:
    json.dump(news_list, f, indent=4)
    if res==True:
         article_links.append(Url)
    else:
          last_news.append(Url)
        
len(news_list)


news_data = []

main_container = driver.find_element(By.CLASS_NAME, 'categories-list')
news_items = main_container.find_elements(By.CLASS_NAME, 'news__item')

for news_item in news_items:

    date_element = news_item.find_element(By.CLASS_NAME, "humble")
    news_date = date_element.text
    
    if date_checkseven(news_date):
        # Extract the title
        title_element = news_item.find_element(By.CLASS_NAME, "news__item-head")
        news_title = title_element.text
        
        # Extract the URL
        url_element = news_item.find_element(By.CLASS_NAME, "news__item-body")
        news_url = url_element.get_attribute('href')
        
        # Add the data to the list
        news_data.append({
            "News_Title": news_title,
            "News_Date": news_date,
            "News_Source_url": news_url
        })

with open("Bitcoin_News_Data.json", "w") as f:
    json.dump(news_data, f, indent=4)

