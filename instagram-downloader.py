#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup


def downloadAvatar(link_):
    
    #request to link
    html_doc = requests.get(link_)
    #Make a soup
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    #Finding the URL of the picture
    tag = soup.find('meta' ,property="og:image")
    imageUrl = tag['content']
    #Download picture
    image = requests.get(imageUrl)
    f = open(f'{name}.jpg', 'wb')
    f.write(image.content)
    f.close()


#Making URL of page Instagram
name = input('Enter username: ')
link = f'https://www.instagram.com/{name}/'


downloadAvatar(link)
