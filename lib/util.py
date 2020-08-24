# Resources:
# https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from sys import stdout

import json
import os
import urllib3
import argparse
import urllib.request
import time
import socket

def downloadImagesFromGoogle(
    searchterm,
    prefix,
    maxResults=50,
    googleSource="www.google.com",
    downloadpath="dataset/raw/positive",
    chromedriver="/usr/local/bin/chromedriver",
    timeout=800
):

    socket.setdefaulttimeout(timeout)

    createFolderIfNotExist(downloadpath)

    url = "https://"+googleSource+"/search?q="+searchterm+"&source=lnms&tbm=isch"

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    browser.get(url)

    print("Searching ... " + searchterm)
    print("  > Scrolling to the bottom")

    scriptPath = os.path.dirname(
        __file__) + "/selenium-scripts/seleniumScrollToBottom.js"
    scrapperJsScript = open(scriptPath).read()
    scrapperJsScript += "scrollToTheEndOrToMax({"
    scrapperJsScript += "onFinish: getFunctionToExtractFullResImages({"
    scrapperJsScript += "onNext: console.log,"
    scrapperJsScript += "onFinish: results => window.__GoogleImagesFullRessImages__ = results,"
    scrapperJsScript += "onError: console.log,"
    scrapperJsScript += "maxImageToProcess:" + str(maxResults) + ","
    scrapperJsScript += "}),"
    scrapperJsScript += "onError: console.log,"
    scrapperJsScript += "});"

    browser.execute_script(scrapperJsScript)

    waitForScrollToEnd = True
    urls = None

    while waitForScrollToEnd:
        urls = browser.execute_script(
            "return window.__GoogleImagesFullRessImages__")
        waitForScrollToEnd = urls == None

    browser.close()

    print("  > Start scrapping ", len(urls), " images")

    counter = 0
    for img in urls:
        counter += 1

        new_filename = prefix + "image"+str(counter)+".jpg"

        try:
            path = downloadpath
            if path[-1:] != "/":
                path += "/"
            path += new_filename

            print("  > Downloading: ", img)
            urllib.request.urlretrieve(img, path)
            print("  > Saving in: ", path, "\n")

        except Exception as e:
            print(e)


def createDatasetFolderStructure():
    createFolderIfNotExist("dataset")
    createFolderIfNotExist("dataset/raw")


def createFolderIfNotExist(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


def test():
    createDatasetFolderStructure()
