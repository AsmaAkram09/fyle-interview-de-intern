# Your imports go here
import logging
import os
import json
import re
logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount
    Parameters:
    dirpath (str): directory path containing receipt and ocr output
    Returns:
    float: returns the extracted amount
'''

def extract_amount(dirpath: str) -> float:
    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    input_filpath = os.path.join(dirpath, 'ocr.json')
    price_list=[]

    with open(input_filpath, mode='r', encoding="utf-8") as f:
        data = json.load(f)
        for i in data['Blocks']:
            if i["BlockType"] == "LINE" or i['BlockType'] == "WORD":
                text=str('\033[94m' +  i["Text"] + '\033[0m')
                x=re.findall(r'[\$\£\€](\d+(?:\.\d{1,2})?)',i["Text"]) 
                x=list(map(float,x))
                print(x)
                if len(x)>0:
                    price_list.append(x)
              
    y=list(map(float,max(price_list))) 
    print(y[0])
    return y[0]
