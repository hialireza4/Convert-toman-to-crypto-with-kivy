#UI and Kivy library
import kivy
kivy.require('2.0.0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.uix.list.list import  TwoLineAvatarListItem , ImageLeftWidget
from kivy.clock import Clock
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

def convert_Toman2USD(toman,usd_price):
    try:
        toman = float(toman)
        usd_price = float(usd_price)
        return str((1/usd_price)*toman)
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
    MainWindow:
	SelectWindow:
    SettingWindow:

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
            icon: 'assets/crypptoicon/main page/irr.png'
            pos_hint: {"center_x": .1, "center_y": .80}
            user_font_size: "18sp"


        
        MDLabel:
            text: "TOMAN"
            font_size:16
            pos_hint: {"center_x": .7, "center_y": .80}

        MDTextField:
            id:toman
            hint_text: "Enter Price"
            mode: "rectangle"
            text: ""
            font_size:16
            pos_hint: {"center_x": .65, "center_y": .80}
            size_hint:.5,None

            
        #----
        MDIconButton:
            icon: 'assets/crypptoicon/main page/usd.png'
            pos_hint: {"center_x": .1, "center_y": 0.70}
            user_font_size: "18sp"
        
        MDLabel:
            text: "USD"
            font_size:16
            pos_hint: {"center_x": .7, "center_y": 0.70}

        MDLabel:
            id:usd
            text: ""
            font_size:16
            pos_hint: {"center_x": 1, "center_y": .70}
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
            text: ""
            font_size:16
            pos_hint: {"center_x": 1, "center_y": .60}
        #---
        MDRoundFlatIconButton:
            icon: "account-cash-outline"
            text: "Convert"
            font_size:16
            pos_hint: {"center_x": 0.5, "center_y": .50}
            
            on_press:app.cvn()
    

<SelectWindow>:
    name:"selectwindow"

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"top": 1}
        spacing: dp(10)
        MDToolbar:
            title: "Select Crypto"
            left_action_items: [["arrow-left", lambda x: app.go_to_main_page()]]
        MDBoxLayout:
            padding: dp(20)
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'search cryptocurrency(beta test)'
        ScrollView:
            MDList:
                id: text_container
<SettingWindow>:
    name:"settingwindow"

    MDToolbar:
        title: "Select Crypto"
        left_action_items: [["arrow-left", lambda x: app.go_to_main_page()]]
        pos_hint: {"center_y": 0.98}
    
    MDSwitch:
        pos_hint: {"center_x": .5, "center_y": .5}
        on_active:
            app.on_checkbox_active(*args)

    MDLabel:
        pos_hint: {"center_x": .5, "center_y": .7}
        text:"this is a beta test "

'''

##create class of pages

class MainWindow(Screen):
	pass

class SelectWindow(Screen):
	pass

class SettingWindow(Screen):
	pass
#create screenmanager and add the pages in to the screenmanager
sm = ScreenManager()
sm.add_widget(MainWindow(name='mainwindow'))
sm.add_widget(SelectWindow(name='selectwindow'))
sm.add_widget(SettingWindow(name="settingwindow"))

#main class for the run app
class MrAsaConvertor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.first = "Bit Coin"
        icon_path = glob.glob("assets/crypptoicon/*.png")
        for _ in range(len(icon_path)):
            icon_path[_]=icon_path[_].replace("\\","//")
        self.coin_screen = MDApp.get_running_app().root.get_screen('selectwindow')
        for i in icon_path:
            text2 = i[20:].replace(".png","").upper()
            text1 = list_crypto[text2]
            icons = ImageLeftWidget(source=i)
            items = TwoLineAvatarListItem(text=text1,
            secondary_text= text2,
            on_release=self.sel_crypto)
            items.add_widget(icons)
            self.coin_screen.ids.text_container.add_widget(items)


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

    def sel_crypto(self, TwoLineAvatarListItem):
        self.mainwindow = MDApp.get_running_app().root.get_screen('mainwindow')
        self.first =  TwoLineAvatarListItem.text
        self.coin_selected = TwoLineAvatarListItem.secondary_text
        self.mainwindow.ids.selcointext.text =self.coin_selected
        self.mainwindow.ids.selcoinicon.icon = "assets/crypptoicon/"+str(self.coin_selected).casefold()+".png"
        MDApp.get_running_app().root.current = "mainwindow"

    def cvn(self):
        self.mainwindow = MDApp.get_running_app().root.get_screen('mainwindow')
        try:
            self.mainwindow.ids.usd.text = convert_Toman2USD(self.mainwindow.ids.toman.text,self.usd_price)
            self.val = self.cg.get_price(ids=self.first, vs_currencies='usd')
            if self.val!={}:
                self.val=self.val.get(list(self.val.keys())[0]).get("usd")
            else:
                self.val=0

            self.mainwindow.ids.cryptovalue.text = convert_toman2crypto(self.mainwindow.ids.toman.text,
            self.val,
            self.usd_price)
        except:
            self.mainwindow.ids.usd.text ="Eroor"
            self.mainwindow.ids.cryptovalue.text ="Eroor"
    
    def on_checkbox_active(self, _,value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


class ErorrApp(MDApp):
    def build(self):
        return Builder.load_string('''
        MDLabel:
            text:"Error please close the app"
        ''')


#func for the run app
def start_app():
    try:
        MrAsaConvertor().run()
    except:
        ErorrApp().run()

if __name__ == "__main__":
    start_app()
