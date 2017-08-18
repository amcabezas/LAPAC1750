#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
from datetime import datetime

report = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

display = Display(visible=0, size=(800, 600))
display.start()


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.implicitly_wait(30)
# IP de Linksys LAPAC1750 Cluster. 
base_url = "http://IP/"
driver.get(base_url)
#Busca las etiquetas e introduce usuario y contraseña.
driver.find_element_by_name("login_name").clear()
driver.find_element_by_name("login_name").send_keys("sistemas")
driver.find_element_by_name("login_pwd").clear()
driver.find_element_by_name("login_pwd").send_keys("iebsistemas")
driver.find_element_by_css_selector("input[name=\"login\"]").click()
driver.get(base_url+'Cluster_client.htm')
#Vemos el código fuente de la página.
web = driver.page_source.encode('utf-8')
#Luego buscamos las etiquetas que poseen los campos de los clientes conectados y los recorremos para contarlos.
html = BeautifulSoup(web,'lxml')
tabla = html.find_all('tr', attrs={'class':'section-row'})
i = 0
for row in tabla:
    i = i+1

print i,report

driver.quit()
display.stop()
