import cv2 as cv
import os 
from glob import glob
import json
from models.read_tex import ReadText


read_text = ReadText()
caminho = 'prosseso'

for path_img in glob(caminho + "/*.jpg"):
    img = cv.imread(path_img)
    #nova_img_crop = read_text.crop_img(img)
    resultado = str(read_text.img_text(img))
    name_img = str(os.path.basename(path_img))
    name_json = name_img[:-4] + '.json'
    dados = {'nome': name_img, resultado: 'resultado'}
    with open('prosseso/' + name_json, 'w') as jason_files:
        json.dump(dados, jason_files)
    

