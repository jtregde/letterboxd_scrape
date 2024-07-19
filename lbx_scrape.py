# %%
# import pandas as pd
# import requests
from bs4 import BeautifulSoup as BS
import urllib.request
# import xmltodict
# import os
# import json

# Set header
header = {
    # "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

url = "https://letterboxd.com"
# %%
#####################################
# Using requets
#####################################
# # Make the request to url and return raw html
# req = requests.get(url, headers=header)
# # Unpack the response
# resonse = req.json()

# %%
#####################################
# Using urllib.request
#####################################
req = urllib.request.Request(url, headers=header)
page = urllib.request.urlopen(req)
soup = BS(page, 'lxml')
# %%
