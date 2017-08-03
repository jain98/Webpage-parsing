"""
--------------------------------------------------------------------------------
Descriptive Name     : Parsing tutorial 2
Author               : Kshitij Jain
Contact Info         : jain98@purdue.edu
Date Written         : 08/02/17
Description          : Parsing a site that uses Google Maps API
Command to run script: parsingTutorial2.py
Usage                : N/A
Input file format    : N/A
Output               :
Note                 :
Other files required by : N/A
this script and where
located

----For Parsing Scripts---------------------------------------------------------
Website Parsed       : <insert url>
In database (Y/N)    :
Date added to Database :
--------------------------------------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select
import urllib
from Geocoding import Geocoding
import re
import time

def earthcam():
    with open("GPS_info.txt", "w") as f:
        # create an instance of the Chrome web driver
        driver = webdriver.Chrome()
        # navigate to the url using driver.get method
        driver.get("http://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1")
        # locate the static map image element on the page using one of the selenium locators and get the img src value
        url = urllib.parse.quote(driver.find_element_by_id("static_map_image").get_attribute("src"), safe = ':?,=/&')
        # extract the gps data from url
        gps = re.search("markers=(?P<one>[0-9]*\.[0-9]*),(?P<two>-?[0-9]*\.[0-9]*)", url)
        f.write(gps.group('one') + "\n" + gps.group('two'))
        driver.close()



if __name__ == '__main__':
    earthcam()
