import logging
import os
import json
import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# URL of website
url = []  # Enter list of urls here,
# I used this extension to get hyperlink of webpages : https://chrome.google.com/webstore/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma
# Copy this hyper links at : https://delim.co/        (in column data)
# Converter Settings : Quotes - Double or Single , rest of the settings leave them as default
# Now click on right arrow click to convert urls to string which goes into "url = []" as a list of strings.

# Below are the print settings
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",  # save as pdf
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",  # Save as PDF
    "version": 2,
    # To disable footer and headers False is assigned
    "isHeaderFooterEnabled": False,
    # To enable Background Graphics True is assigned
    "isCssBackgroundEnabled": True,
}

# Path variable for destination where we will save all webpages as pdf
path = "/home/atom/Downloads/Documents/DailyCoding/"

# initialize the log settings
logging.basicConfig(filename='app.log', level=logging.INFO)

# This is the profile which we will use for saving webpages as PDF
profile = {
    "printing.print_preview_sticky_settings.appState": json.dumps(appState)}


chrome_options = webdriver.ChromeOptions()  # chromium options
# This will add automatic saving so you don't have to click on save every tiem print popup appears in the browser
chrome_options.add_argument('--kiosk-printing')

# this adds profile that we created earlier
chrome_options.add_experimental_option('prefs', profile)
# To enable background graphics while saving a webpage this argument is necessary
chrome_options.add_argument('--enable-print-browser')

# this adds options and open chromium
driver = webdriver.Chrome(options=chrome_options)

print(len(url))  # for debug purpose

# if you have a long list of url then use try catch to catch any exceptions that may occur

try:
  for i in range(0, len(url)):
    driver.get(url[i])
    logging.info('Trying to save {} file to pdf'.format(url[i]))
    time.sleep(2)
    # This finds the button by id "cta.mobile.yellow"
    button = driver.find_element_by_class_name("cta.mobile.yellow")
    time.sleep(1)
    button.click()  # this will click on the button which expands the webpage
    time.sleep(0.3)
    driver.execute_script('window.print();')  # Initiates print popup
    time.sleep(2)
    os.rename('/home/atom/Downloads/filename.pdf',
              path + 'filename({}).pdf'.format(i + 1))  # You can change here as per your requirement
    time.sleep(0.3)
    driver.execute_script("window.open('');")  # This will open a new tab
    time.sleep(1)
    driver.close()  # closes old tab from which webpage is already saved as pdf
    time.sleep(1)
    # this will move to newly opened tab which stands at zeroth index
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
except Exception as e:
  logging.error('Error occurred ' + str(e))
  os.system('shutdown -s -t 0')  # shutdowns the system
