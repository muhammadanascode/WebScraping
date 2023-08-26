from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Pyhton program to find user's followers

# Set up the Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# url of user
url = "https://www.instagram.com/username/"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Wait for the dynamic content to load (you might need to adjust this)
driver.implicitly_wait(10)

# Get the page source after dynamic content has loaded
page_source = driver.page_source


# Find the followers classname
followers_element = driver.find_elements("css selector", "span._ac2a")

# User's followers
followers = followers_element[1].text

# Find the user_name classname
user_name_element = driver.find_elements("css selector", "h2.x1lliihq")

# User's name
user_name=user_name_element[0].text

# Preparing data to append in file
data = 'Username: ' + user_name + ',' + 'followers: ' + followers + '\n'

# appending data in file
with open('data/data.txt','a') as f:
    f.write(data)

# Close the WebDriver
driver.quit()

