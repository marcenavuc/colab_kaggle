!pip install kaggle
from google.colab import drive
import os
import json
drive.mount('/content/gdrive')
json_data = open("gdrive/My Drive/kaggle/kaggle.json", "r").readlines()[0]
print(json_data)
os.chdir("..")
os.chdir("root")
os.mkdir(".kaggle")
os.chdir(".kaggle")
file = open("kaggle.json", "w")
file.write(json_data)
os.chdir("../..")
os.chdir("content")
