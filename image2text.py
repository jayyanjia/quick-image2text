#! /usr/bin/env python3
import os
from PIL import Image
import pytesseract

img_dir = './'

def get_images(path):
    '''get supported image formats'''
    img_ext = ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif', 'tiff')
    img_list =[]
    for files in os.listdir(path):
        if files.endswith(img_ext):
            img_list.append('{}{}'.format(path, files))
    return img_list

def get_images_text(filename):
    '''import image as RGB and convert to grayscale image for tesseract'''
    im = Image.open(filename).convert('RGB')
    gray = im.convert('L')
    text = pytesseract.image_to_string(gray)
    return text
    
def count_alnum(text):
    count = 0 
    for char in text:
        if char.isalnum():
            count += 1
    return count

def main():
    for image_path in get_images(img_dir):
        text = get_images_text(image_path)
        count = count_alnum(text)
        if count:
            with open("{}.txt".format(image_path), 'w') as text_file:
                text_file.write(text)
            print("Image: {}, Number of Alphanumeric Characters: {}, Captured Text File: {}.txt".format(image_path, count, image_path))
        else:
            print("Image: {}, No Alphanumeric Characters Found".format(image_path))

if __name__ == "__main__":
    main()
