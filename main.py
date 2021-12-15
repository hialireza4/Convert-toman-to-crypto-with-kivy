#UI and Kivy library
import kivy
import PIL
kivy.require('2.0.0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.uix.list.list import  TwoLineAvatarListItem , ImageLeftWidget
from kivy.clock import Clock
from kivy.core.window import Window
#version -android
Window.size = (440, 775)
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


##add list of crypto
list_crypto = {"BTC":"Bitcoin",
    "BNB":"Binance Coin",
    "MATIC":"Polygon-Pos",
    "SOL":"Solana",
    "ADA":"Cardano",
    "DOT":"Polkadot",
    "TRX":"TRON",
    "LINK":"Chainlink",
    "ZEC":"Zcash",
    "ETC":"Ethereum-Classic",
    "BCH":"Bitcoin-Cash",
    "USDT":"Tether",
    "XMR":"Monero",
    "DAI":"Dai",
    "EOS":"Eos",
    "LTC":"Litecoin",
    "MANA":"Decentraland",
}


#kivy design code

KV = '''
ScreenManager:
    id:"screen_manager"
	Splash:
    MainWindow:
	SelectWindow:
    SettingWindow:

<Splash>:
    Image:
        source:"assets\splash.png"
<Mainwindow>:
    name:"mainwindow"




'''

##create class of pages
class Splash(Screen):
    pass

class MainWindow(Screen):
	pass

class SelectWindow(Screen):
	pass

class SettingWindow(Screen):
	pass
#create screenmanager and add the pages in to the screenmanager
sm = ScreenManager()
sm.add_widget(Splash(name = "splash"))
sm.add_widget(MainWindow(name='mainwindow'))
sm.add_widget(SelectWindow(name='selectwindow'))
sm.add_widget(SettingWindow(name="settingwindow"))

#main class for the run app
class MrAsaConvertor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(self.go_to_main_page,5)

    def go_to_main_page(self,*args):
        MDApp.get_running_app().root.current = 'mainwindow'






#func for the run app
def start_app():
    MrAsaConvertor().run()

if __name__ == "__main__":
    start_app()