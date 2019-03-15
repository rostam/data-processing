import shutil
from io import BytesIO
import os
import pandas as pd
import requests
import wptools
from PIL import Image

folder_name = 'dog_images'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

images_paths = pd.read_csv('image-predictions.tsv', sep='	')
for index, row in images_paths.iterrows():
    r = requests.get(row['jpg_url'], stream=True)
    if r.status_code == 200:
        i = Image.open(BytesIO(r.content))
        i.save(folder_name + "/" + row['p1']+".jpg")
