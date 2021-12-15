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





##The Function for get price

