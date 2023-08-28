from paddleocr import PaddleOCR,draw_ocr
import numpy as np
import cv2 as cv

class ReadText:
    
    def __init__(self):
        pass

    
    def crop_img(self, img:np.ndarray) -> np.ndarray:
        img_arr = np.array(img)
        nova_img_crop = img_arr[0:80, 253:480]
        return nova_img_crop

    def img_text(self, img):
        result_final = []
        ocr = PaddleOCR(lang='en')
        result = ocr.ocr(img, cls=False)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                result_final.append(line[1:][0][0])

        return result_final
    

