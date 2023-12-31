from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Python program to find user's instagram followers

# url of user
url = "https://www.instagram.com/zafar_akber/"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the dynamic content to load
driver.implicitly_wait(10)

# Get the page source after dynamic content has loaded
page_source = driver.page_source

# Find the user_name classname
user_name_element = driver.find_elements("css selector", "h2.x1lliihq")


if (user_name_element):
    # User's name
    user_name = user_name_element[0].text

    # Find the followers classname
    followers_element = driver.find_elements("css selector", "span._ac2a")

    # User's followers
    followers = followers_element[1].text

    # Preparing data to append in file
    data = 'Username: ' + user_name + ',' + 'followers: ' + followers + '\n'

    with open('data/data.txt', 'a') as f:
        f.write(data)

else:
    print('User doesnot exists')


# Close the WebDriver
driver.quit()