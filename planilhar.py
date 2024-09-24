from typing import Self
from botcity.core import DesktopBot
#from botcity.web import By
#from ruralsei import ruralsei
from RetificaçãoImu import RetificaçãoImu
from RestituiçãoRural import RestituiçãoRural
#from ruralgerados import ruralgerados
#from baixaisencaogerados import baixaisencaogerados
#from Restituicao import Restituição
#from isencaosei2 import isencaosei2
from isencaosei import isencaosei
from isencaogerados import isencaogerados
from ruralgerados import ruralgerados
#from isencaoseigerados import isencaoseigerados
#from etapas2 import etapas2
import webbrowser
from PySimpleGUI import PySimpleGUI as sg
import sys
import os
import keyboard
import threading
import time
#eimport pyperclip

contagem = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "35", "40", "45", "50", "100", "150", "200", "250", "300", "350"  ]
#linkpaste= pyperclip.paste()
#print(linkpaste)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def interromper():
        while True:
                if keyboard.is_pressed('e'):
                       os._exit(0)

def parar():
        while True:
                if keyboard.is_pressed('p'):
                        #break
                        #os.system("pause")
                        #input("Pressione <enter> para continuar")
                        time.sleep(30)                      
  
class Bot(DesktopBot):      
                def action(self, execution=None):  
                                try:     
                                        sg.theme('DarkBlue4')
                                        layout = [
                                                [sg.Text('Link', justification='center'), sg.Input(key='link')],
                                                [sg.Text('', justification='center')],
                                                [sg.Text('Quantidade de processos para planilhar:', justification='center'), sg.Combo(contagem, default_value=contagem[0], key='contagem', bind_return_key=True, s=10)],
                                                [sg.Text('', justification='center')],
                                                [sg.Text('Para interromper, pressionar E',justification='center')],
                                                [sg.Text('', justification='center')],
                                                [sg.Text('PLANIHAR PROCESSOS SEI:',justification='center')],
                                                [sg.Button('ISENÇÃO DE IPVA /ICMS -- TAXI / PCD - SEI', pad=(0, 5))],  
                                                [sg.Button('RETIFICAÇÃO / RESSARCIMENTO / IMUN-SEI', pad=(0, 5))],
                                                [sg.Button('RESTITUIÇÃO / PRODUTOR RURAL - SEI', pad=(0, 5))],
                                                                       
                                                [sg.Text('',justification='center')],
                                                [sg.Text('PLANILHAR PROCESSOS GERADOS:',justification='center')],
                                                [sg.Button('ISENÇÃO DE IPVA/ICMS-TAXI,PCD /// PRODUTOR RURAL /// BAIXA - IMUN /// IMUNIDADES /// - GERADOS', pad=(0, 5))],
                                                 [sg.Button('PRODUTOR RURAL - GERADOS', pad=(0, 5))],
                                                #[sg.Button('ELÉTRICOS', pad=(0, 5))],   
                                                #[sg.Button('IMU - ITD,TRAB,EDU,PJ', pad=(0, 5))], 
                                                #[sg.Button('PRODUTOR RURAL - GERADOS', pad=(0, 5)) ],      
                                                                                                                                   
                                                ]
                                        
                                        janela1 =  sg.Window('PLANILHAR', layout)
                                        while True:  
                                                contador = int(0)
                                                eventos, valores = janela1.read()
                                                if eventos == sg.WINDOW_CLOSED:
                                                        break
                                                if eventos == 'RESTITUIÇÃO / PRODUTOR RURAL - SEI':
                                                        cont= int(valores['contagem'])                                               
                                                        threading.Thread(target=interromper).start()
                                                        webbrowser.open(valores['link'])                                         
                                                        RestituiçãoRural(contador, cont, bot=self, self=self)

                                                if eventos == 'RETIFICAÇÃO / RESSARCIMENTO / IMUN-SEI':
                                                        cont= int(valores['contagem'])                                               
                                                        threading.Thread(target=interromper).start()
                                                        webbrowser.open(valores['link'])                                         
                                                        RetificaçãoImu(contador, cont, bot=self, self=self)

                                                if eventos == 'ISENÇÃO DE IPVA /ICMS -- TAXI / PCD - SEI':
                                                        cont= int(valores['contagem'])                                               
                                                        threading.Thread(target=interromper).start()
                                                        webbrowser.open(valores['link'])                                         
                                                        isencaosei(contador, cont, bot=self, self=self)

                                                        
                                                if eventos == 'ISENÇÃO DE IPVA/ICMS-TAXI,PCD /// PRODUTOR RURAL /// BAIXA - IMUN /// IMUNIDADES /// - GERADOS':
                                                        cont= int(valores['contagem'])                                               
                                                        threading.Thread(target=interromper).start()
                                                        webbrowser.open(valores['link'])                                         
                                                        isencaogerados(contador, cont, bot=self, self=self)

                                                if eventos == 'PRODUTOR RURAL - GERADOS':
                                                        cont= int(valores['contagem'])                                               
                                                        threading.Thread(target=interromper).start()
                                                        webbrowser.open(valores['link'])                                         
                                                        ruralgerados(contador, cont, bot=self, self=self)

                                                                      
                 
                                except:  
                                        janela1.Close()
                                        #pass
                                        #Bot(DesktopBot)
                                        sg.theme('DarkBlue4')
                                        layout2 = [     
                                                        [sg.Text('OCORREU UM ERRO!!', justification='center')],
                                                        [sg.Text('GENTILEZA REINICIAR O APLICATIVO !!! ', justification='center')],
                                                        [sg.Text('COPIAR E COLAR LINK - FECHAR NAVEGADOR ', justification='center')],
                                                        [sg.Text('', justification='center')],
                                                        [sg.Text('EM SEGUIDA CLICAR NO BOTÃO CORRESPONDENTE AO PROCESSO"!!', justification='center')],
                                                        [sg.Text('', justification='center')],
                                                        [sg.Button('REINICIAR')],  
                                                ]

                                        janela2 =  sg.Window('ERRO', layout2)                                                                                                                                                                                                                                                                                                                                                           

                                        while True:    
                                                eventos, valores = janela2.read()
                                                if eventos == sg.WINDOW_CLOSED:
                                                        restart_program()
                                                if eventos == 'REINICIAR':
                                                                restart_program()
                                                                #return janela1.read()
                                                                #eventos, valores = janela.read()
                                                #if eventos == 'SAIR':
                                                                #exit()
                                                                #return janela1.read()
                                                                #eventos, valores = janela.read()
                        

                def not_found(self, label):
                                print(f"Element not found: {label}")    

if __name__ == '__main__':
        Bot.main()