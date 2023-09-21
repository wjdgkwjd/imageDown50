import os
import requests
import random
import string

def rnd_str(n=5):
  characters = string.ascii_letters + string.digits 
  return ''.join(random.choices(characters, k=n))

def imageDown(url):

  try:
      folder_name = "images"
      if not os.path.exists( folder_name ):
        os.makedirs(folder_name)

      response = requests.get(url)
      fileName=f"image-{rnd_str()}.jpg"
      
      file_path = os.path.join(folder_name, fileName )
    
      with open(file_path, "wb") as file:
          file.write(response.content)
    
      return fileName
      
  except :
      return (" Not Image!")

    