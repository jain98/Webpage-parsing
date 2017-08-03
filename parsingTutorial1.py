""" 
--------------------------------------------------------------------------------
Descriptive Name     : Parsing tutorial 1
Author               : Kshitij Jain
Contact Info         : jain98@purdue.edu
Date Written         : 08/02/17
Description          : Parsing a site that uses Google Maps API
Command to run script: parsingTutorial1.py
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
from bs4 import BeautifulSoup
import urllib2
import re
import sys
import time
import json
from selenium import webdriver
import platform

def nycdot():
    JSonURL = "http://dotsignals.org/new-data.php"  # url to the JSON file containing Map data
    CameraPopURL = "http://dotsignals.org/google_popup.php?cid="    # url to access the camera popup

    # Open an output file for writing the Camera info obtained from JSonURL
    with open("nycdot_list", "w") as f:
        # write header
        f.write("description#snapshot_url#latitude#longitude#country#city\n")

        # load JSON file into response
        response = urllib2.urlopen(JSonURL).read()
        # Parse the JSON file with the json module
        parsed_json = json.loads(response)
        # navigate to the markers key which contains all the camera data
        cameras = parsed_json['markers']

        for camera in cameras:
            cam_id = camera['id']
            content = camera['content']
            latitude = camera['latitude']
            longitude = camera['longitude']
            url = CameraPopURL+cam_id

            browser.get(url)
            soup = BeautifulSoup(browser.page_source)
            snapshot_url = soup.find('img').get('src')
            if re.search(r'img/inactive', snapshot_url) == None:
                snapshot_url = re.search(r'(?P<URL>[\w\.\/:\\]*)', snapshot_url).group('URL')
                f.write(content+"#"+str(snapshot_url)+"#"+latitude+"#"+longitude+"#"+"USA#NY#New York\n")
    return



if __name__ == '__main__':
    if platform.system() == 'Windows':
        PHANTOMJS_PATH = './phantomjs.exe'
    else:
        PHANTOMJS_PATH = './phantomjs'

    browser = webdriver.PhantomJS(PHANTOMJS_PATH)
    nycdot()
