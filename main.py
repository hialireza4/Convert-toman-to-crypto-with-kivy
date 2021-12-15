#UI and Kivy library
import kivy
kivy.require('2.0.0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.uix.list.list import  TwoLineAvatarListItem , ImageLeftWidget
from kivy.clock import Clock
from kivy.core.window import Window
#version -android
Window.size = (400, 800)
#library for get price
import requests
from bs4 import BeautifulSoup
from lxml import etree
import datetime
#library for showing icon path
import glob

#The function for the get usd price

def get_USD_price():
    try:
        url = 'https://www.tgju.org/profile/price_dollar_rl'
        response = requests.get(url)

        if response.status_code==200:

            soup = BeautifulSoup(response.text, 'html.parser')
            dom = etree.HTML(str(soup))
            res = dom.xpath('//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]')[0].text

            return res.replace(",", "")[:-1]

    except:

        return False




##The Function for convert toman to the crypto

def convert_toman2crypto(toman,usd,crypto):
    #toman is value of toman of converted

    try:
        toman = float(toman)
        crypto = float(crypto)
        usd = float(usd)
        
        return str(toman*(1/usd)*(1/crypto))
    except:
        return("Value is bad")

