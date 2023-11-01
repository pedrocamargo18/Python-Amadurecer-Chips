import PySimpleGUI as sg


def janela_menu():
    sg.theme('DefaultNoMoreNagging')
    columns_menu_center = [
                           [sg.Text('Bem-Vindo!', font=("Arial", 32), text_color="White", background_color="red", justification='center')],
                           [sg.Text('Selecione uma das opções:', font=("Arial", 20),justification='center')],
                            [sg.Image('teste.png',expand_x=True, expand_y=True)],
                           ]
    columns_right= [
        [sg.Button('Iniciar Aquecimento', font=("Arial", 12),size=(20,1), border_width=0),
         sg.Button('Iniciar Disparo', font=("Arial", 12),size=(20,1),border_width=0)],
        [sg.Button('Configurações', font=("Arial", 12),size=(20,1),border_width=0)],
        [sg.Checkbox('Caminho dos navegadores definidos manualmente.', key='path_check', enable_events=True, font=("Arial", 12))],
    ]
    margem = [
        [sg.Text('', size=(5, 0))]
    ]
    layout = [[sg.VPush(),sg.Column(columns_menu_center), sg.VSeparator( color='white'), sg.Column(columns_right),sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1', layout, icon='icone.ico', size=(800, 400), finalize=True)


def janela_aquecer():
    sg.theme('DefaultNoMoreNagging')
    layout_center_aquecer = [ [sg.Text('Aquecendo!', font=("Arial", 22), size=(40,1))],
        [sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
        [sg.Button('COMEÇAR', font=("Arial", 16), size=(20, 1), button_color="green")],
        [sg.ProgressBar(3, orientation='h', size=(100,20), border_width=4, key='-PROGRESS-BAR-')]]
    layout2 = [[sg.VPush(), sg.Column(layout_center_aquecer, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1',layout=layout2, icon='icone.ico', size=(600, 200), finalize=True)


def janela_disparar():
    sg.theme('DefaultNoMoreNagging')
    layout_center_disparar = [[sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
               [sg.Button('COMEÇAR', font=("Arial", 16), size=(40, 1), button_color="green")]]
    layout3 = [[sg.VPush(), sg.Column(layout_center_disparar, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 1.0.1', layout3, icon='icone.ico', size=(600, 600), finalize=True)


def janela_config():
    sg.theme('DefaultNoMoreNagging')
    layout3 = [[sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
               [sg.Button('COMEÇAR', font=("Arial", 16), size=(40, 1), button_color="green")]]
    return sg.Window('PoupaZap - 1.0.1', layout3, icon='icone.ico', size=(600, 600), finalize=True)
