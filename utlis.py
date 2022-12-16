import json
from os import listdir

IMG_FILE_EXT = ('.jpg', '.jpeg', '.bmp', '.png')


def set_config(key, value, *args, **kwargs):
  try:
    with open("./config.json", 'w') as f:
      data = json.load(f)
      data[key] = value
      print(data)
      f.write(json.dump())
  except Exception as e: 
    print(e)


def get_key(key): 
  with open("./config.json", 'r') as f:
    data = json.load(f)
    return data.get(key, False) 




def create_image_arr(file): 
  with open(file, 'r') as f: 
    lines = f.readlines()

    array = []
    for line in lines: 
      line = line[:-2]
      array.append(list(line))
    return array


def images_to_binary_txt(folder: str = "./images/", size:tuple[int,int] = (70,70)) -> None:
  # NOT A CircuitPy function
  from PIL import Image
  import numpy as np
  from os.path import isfile, join, splitext

  # Grab all image files 
  files = [f for f in listdir(folder) if isfile(join(folder, f)) and f.lower().endswith(IMG_FILE_EXT)]
  for file in files:
    im = Image.open(f'{folder}/{file}', 'r')
    im.load() # required for png.split()

    # Get bounding box of image
    im = im.crop(im.getbbox())
    # resize image keeping aspect ratio
    im.thumbnail(size,Image.Resampling.LANCZOS)

    try: 
      background = Image.new("RGB", im.size, (255, 255, 255))
      background.paste(im, mask=im.split()[3]) # 3 is the alpha channel

      arr = np.array(im.convert("L"))
    except Exception as e: 
      arr = np.array(im)


    transformed = np.where(arr == 0, 0, 1)
    np.savetxt(f'./images/output/{splitext(file)[0]}.txt', transformed, fmt='%i', delimiter="")


if __name__ == "__main__":
  images_to_binary_txt()