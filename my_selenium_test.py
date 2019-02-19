# --------MY COMMANDS Template-----WINDOWS 10---------------------

# CTRL + ATL + p    Running .py files on my VS Code terminal. 

# touch + name of the file. - Creates file
# RM + name of the file.  - Removes file

# pipenv shell - start VE
# exit - Exit VE

# --------MY COMMANDS Template-----WINDOWS 10---------------------

# Learning Selenium Web Driver with Python3
"""https://selenium-python.readthedocs.io/getting-started.html"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
# Explore wait methods in Selenum, may not need time/sleep
test_message = "selenium"
print(test_message)

# Init browser 
browser = webdriver.Firefox()
# browser = webdriver.Firefox(executable_path ="") 
print(browser.name) 

# Grab site url & grab some tabs via text 

def get_link(link):
   browser.get(link)

get_link("https://www.python.org/")


def click_element_text(one,two,three):

   elem = browser.find_element_by_link_text(one)
   elem.click()
   elem = browser.find_element_by_link_text(two)
   elem.click()
   elem = browser.find_element_by_link_text(three)
   elem.click()

click_element_text("About","Documentation","Docs")


# browser.get("https://www.python.org/")
browser.back() # this is a better way
elem = browser.find_element_by_id("id-search-field")
searchbar = elem.send_keys(test_message)
enter = elem.send_keys(Keys.RETURN)
sleep(1.5)
browser.get("https://selenium-python.readthedocs.io/getting-started.html")
sleep(2)
browser.close()

# Note to self: make function where I can pass multi elements

def get_elem(enter_string):
   pass 

