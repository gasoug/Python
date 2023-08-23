from os import link
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import PySimpleGUI as sg

def send(locale):
    contacts_df = pd.read_excel(locale)
    browser = webdriver.Chrome(executable_path=r".\chromedriver.exe")
    browser.get("https://web.whatsapp.com/")
    text = "Você já foi cliente nosso, e trago uma oferta especial e exclusiva para você!"

    while len(browser.find_elements_by_id("side")) < 1:
        time.sleep(1)
    aut.hotkey('win','up')
    for i, nome in enumerate(contacts_df["Nome"]):
        message = urllib.parse.quote(f"Olá {nome}, tudo bem ? {text}")
        num = contacts_df.loc[i, "Número"]
        link = f"https://web.whatsapp.com/send?phone={num}&text={message}"
        browser.get(link)
        while len(browser.find_elements_by_id("side")) < 1:
            time.sleep(1)
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(4) 

def main():
    my_theme = {'BACKGROUND': '#000000',
                    'TEXT': '#94E81C',
                    'INPUT': '#212121',
                    'TEXT_INPUT': '#ffffff',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('#ffffff', '#212121'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    # Add your dictionary to the PySimpleGUI themes
    sg.theme_add_new('MyNewTheme', my_theme)  
    sg.theme('My New Theme')
    font = ("Arial,12")

    layout = [  [sg.Push(), sg.Text('Automatic Send', size=(0,2),font=font), sg.Push()],
                [sg.In(key="-file-"), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx")))],
                [sg.Push(), sg.Button('Enviar'), sg.Cancel(), sg.Push()],
                [sg.Push(), sg.Text("",key="-complete-"), sg.Push()]]

    # Create the Window
    window = sg.Window('Envio WhatsApp', layout)

    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'Enviar':
            arquivo = values["-file-"]
            window["-complete-"].update("Message sent successfully!")
            send(arquivo)
            #print(arquivo)  
    window.close()
main()

   
