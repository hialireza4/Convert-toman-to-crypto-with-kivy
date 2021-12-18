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
#Window.size = (440, 775)
#library for get price
import requests
from bs4 import BeautifulSoup
from lxml import etree
import datetime
from pycoingecko import CoinGeckoAPI
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
    FloatLayout:    
##icon in the up of page

#goto select crypto
        MDIconButton:
            icon: 'plus-outline'
            pos_hint: {"center_x": .1, "center_y": .95}
            user_font_size: "35sp"
            on_press:
                root.manager.current = "selectwindow"
#goto setting icon
        MDIconButton:
            icon: 'account-cog-outline'
            pos_hint: {"center_x": .5, "center_y": .95}
            user_font_size: "35sp"
            on_press:
                root.manager.current = "settingwindow"
#update_data icon                        
        MDIconButton:
            id:update_database
            icon: 'update'
            pos_hint: {"center_x": .9, "center_y": .95}
            user_font_size: "35sp"
            on_press:
                app.update_data()
##label in the down of window
#for show status
        MDLabel:
            id:last_update_text
            text: "last update:"
            font_size:12
            pos_hint: {"center_x": 0.55, "center_y": 0.09}
##center main window object
#
        MDIconButton:
            icon: 'assets/crypptoicon/irr.png'
            pos_hint: {"center_x": .1, "center_y": .80}
            user_font_size: "18sp"


        
        MDLabel:
            text: "TOMAN"
            font_size:16
            pos_hint: {"center_x": .7, "center_y": .80}

        MDTextField:
            id:toman
            hint_text: "Enter Price"
            mode: "fill"
            text: "10000"
            font_size:16
            pos_hint: {"center_x": .65, "center_y": .80}
            size_hint:.5,None

            
        #----
        MDIconButton:
            icon: 'assets/crypptoicon/usd.png'
            pos_hint: {"center_x": .1, "center_y": 0.70}
            user_font_size: "18sp"
        
        MDLabel:
            text: "USD"
            font_size:16
            pos_hint: {"center_x": .7, "center_y": 0.70}

        MDLabel:
            id:usd
            text: "10000"
            font_size:16
            pos_hint: {"center_x": 1.1, "center_y": .70}
        #---
        MDIconButton:
            id:selcoinicon
            icon: 'assets/crypptoicon/btc.png'
            pos_hint: {"center_x": .1, "center_y": 0.60}
            user_font_size: "18sp"
        
        MDLabel:
            id:selcointext
            text: "BTC"
            font_size:16
            pos_hint: {"center_x": .7, "center_y": 0.60}
        
        MDLabel:
            id:cryptovalue
            text: "10000"
            font_size:16
            pos_hint: {"center_x": 1.1, "center_y": .60}
        #---
        MDRoundFlatIconButton:
            icon: "account-cash-outline"
            text: "Convert"
            font_size:16
            pos_hint: {"center_x": 0.5, "center_y": .50}
            
            on_press:app.cvn()
    

<SelectWindow>:
    name:"selectwindow"
<SettingWindow>:
    name:"settingwindow"



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

    def update_data(self):  #this function for get data from internet and update the status.
        self.mainwindow = MDApp.get_running_app().root.get_screen('mainwindow') #get the windows path
        try:
            self.usd_price = get_USD_price()
            self.cg = CoinGeckoAPI()
            st = "(success connection)"
        except:
            st = "(failure connection)"
        self.mainwindow.ids.last_update_text.text = "last update:" + str(datetime.datetime.now())[:-7]+st

        






#func for the run app
def start_app():
    MrAsaConvertor().run()

if __name__ == "__main__":
    start_app()