#  Description

This repo contains the solution of the Uruit Machine Learning position (v1).

# Requeriments

1. Python3
2. Selenium for python
3. chromedriver (install for your SO)

# Downloading the dataset

If you have mac and a default configuration just Use python to execute: `downloadRawDataset.py` .

Otherwise, go to python console (or create an script to be executed) and run:

```python

import sys
from lib import util

# Create the folder structure for the dataset if you haven't it yet
util.createDatasetFolderStructure()
# Run this function to download the images
util.downloadImagesFromGoogle(
    "momo historia", # Search term on google images
    "momo_historia", # Prefix of the stored images
    10, # Max of download images
    googleSource="www.google.com", # Google domain if you want to use .co or .in domains
    downloadpath="dataset/raw/", # Path where the images will be downloaded
    chromedriver="/usr/local/bin/chromedriver" # Path of your chromedriver app 
)
```