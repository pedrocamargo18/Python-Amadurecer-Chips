import PySimpleGUI as sg


def janela_menu():
    sg.theme('BlueMono')
    columns_menu_center = [[sg.Image('teste.png',expand_x=True, expand_y=True)],
                           [sg.Text('Bem-Vindo, Selecione uma das opções:', font=("Arial", 24))],
                           [sg.Button('Iniciar Aquecimento', font=("Arial", 16), size=(20, 1))],
                           [sg.Button('Iniciar Disparo', font=("Arial", 16), size=(20, 1))],
                           [sg.Button('Configurações', font=("Arial", 16), size=(20, 1))],
                           [sg.Text("", key="texto_acao", font=("Arial", 18))]
                           ]
    layout = [[sg.VPush(), sg.Column(columns_menu_center, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1', layout, icon='icone.ico', size=(600, 600), finalize=True)


def janela_aquecer():
    layout_center_aquecer = [ [sg.Text('Finalizado o Aquecimento dos CHIPS!', font=("Arial", 22), size=(40,1))],
        [sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")]]
    layout2 = [[sg.VPush(), sg.Column(layout_center_aquecer, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1', layout2, icon='icone.ico', size=(600, 200), finalize=True)


def janela_disparar():
    layout_center_disparar = [[sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
               [sg.Button('COMEÇAR', font=("Arial", 16), size=(40, 1), button_color="green")]]
    layout3 = [[sg.VPush(), sg.Column(layout_center_disparar, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1', layout3, icon='icone.ico', size=(600, 600), finalize=True)


def janela_config():
    layout3 = [[sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
               [sg.Button('COMEÇAR', font=("Arial", 16), size=(40, 1), button_color="green")]]
    return sg.Window('PoupaZap - 1.0.1', layout3, icon='icone.ico', size=(600, 600), finalize=True)
