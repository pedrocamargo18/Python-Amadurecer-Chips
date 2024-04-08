import pandas as pd
import pyautogui as pg
import numpy as np
import logging
import tempfile
import pywhatkit as pwt
import funcoes as fn
import PySimpleGUI as sg
import windows as win


tmp = tempfile.gettempdir()
logging.basicConfig(level=logging.INFO, filename=f"{tmp}\\registro.log", format="%(asctime)s - %(message)s ")
data = pd.read_csv("dados.CSV", sep=";", converters={0: str})
df = pd.DataFrame(data)
data_dict = data.to_dict('list')
leads = data_dict['WhatsApp']
df_leads = df[~df['WhatsApp'].isin(['', np.nan])]['WhatsApp'].dropna(ignore_index=True).astype(str)
msg = data_dict['msg']
cont_num = len(df_leads)
cont = 0
cont_lin_percent = 100/len(msg)
nav = 0

# chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
# edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
# opera_path = "C:/Users/Poupacred/AppData/Local/Programs/Opera/opera.exe %s"

chrome_path = ''
brave_path = ''
edge_path = ''
opera_path = ''


janela1, janela2 = win.janela_menu(), None
janela3, janela4 = None, None

while True:
    window, event, values = sg.read_all_windows(5000)
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'path_check':
        arquivo = open('path_navegadores.txt', 'r')
        chrome_path = arquivo.readline()
        brave_path = arquivo.readline()
        edge_path = arquivo.readline()
        opera_path = arquivo.readline()
        sg.popup('Alterado o PATH com sucesso!')

    if event == 'chrome_check':
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    if event == 'edge_check':
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    if event == 'brave_check':
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    if event == 'opera_check':
        opera_path = "C:/Users/Poupacred/AppData/Local/Programs/Opera/opera.exe %s"

    ##AQUECIMENTO
    elif window == janela1 and event == 'Iniciar Aquecimento':
        terminou = False
        WIDTH, HEIGHT = pg.size()
        janela2 = win.janela_aquecer()
        janela1.hide()
    elif window == janela2 and event == 'COMEÇAR':
        window['COMEÇAR'].update(disabled=True)
        cont = 0
        for m in msg:
            logging.info("INICIADO O PROGRAMA !!")
            fn.aquecer(df, df_leads, cont_num, chrome_path, brave_path, edge_path, opera_path, WIDTH, HEIGHT)
            cont = round(cont+cont_lin_percent,1)
            cancel = [sg.popup_timed('Cancelar o aquecimento?', auto_close_duration=15, icon='icone.ico')]
            if event == sg.WINDOW_CLOSED or cancel[0] == 'OK':
                event = 'SAIR'
                window['COMEÇAR'].update(disabled=False)
                break
            window['loading-frase'].update(f'Aquecendo Chips...                 {cont}%')
            window['-PROGRESS-BAR-'].update(cont)
        window['loading-frase'].update('Finalizado o Aquecimento!')
        terminou = True
        logging.info("FINALIZADO TODOS OS ENVIOS!")
    elif window == janela2 and event == 'SAIR':
        janela2.hide()
        janela1.un_hide()
    ##

    ##DISPAROS
    elif window == janela1 and event == 'Iniciar Disparo':

        janela3 = win.janela_aquecer()
        janela1.hide()
        image = input("Insira o nome da Imagem que será enviada ( Nome com a extensão do arquivo ): ")
        path = r"Imagens"
        file = image
        busca = fn.search(file, path)
        if not image:
            print("vazio")
        else:
            for n in df_leads:
                pwt.sendwhats_image(f'+{n}', f'{image}')

    elif window == janela3 and event == 'SAIR':
        janela3.hide()
        janela1.un_hide()

    elif window == janela1 and event == 'Configurações':
        janela4 = win.janela_config()
        janela1.hide()

    elif window == janela4 and event == 'Personalizar':
        custom = win.custom_program()
        if window == janela4 and event == 'Voltar':
            custom.hide()
            janela1.un_hide()
    if event == 'Salvar':
        logo = values["-LOGO-"]
        fn.salvarImagens(logo)
        window.refresh()
        custom.hide()
    if event == 'Sair':
        custom.hide()
    elif window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()
window.close()
