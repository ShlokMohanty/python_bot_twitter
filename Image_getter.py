import random 
import urllib.request
import dotenv
import os
import requests 
import wget 
from os import remove 
from shutil import move 

from PIL import Image 
import numpy as np 

dotenv.load_dotenv()
api_key = os.getenv('')
query =['Random','Tokyo Life','flowers','Sea','Night sky','Stars','Love','Moon','Film','Street photography','Book','Friendship']

def download_image(url,i):
filename = str(i)+'.jpg'
print(filename)
urllib.request.urlretrieve(url, filename)
