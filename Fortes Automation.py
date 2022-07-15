from ast import Num
from numpy import number
import pyautogui
import time

'''time.sleep can chance in diferents computer and/or in diferents campanys.'''

pyautogui.alert(text='Centralize o VSCode em modo janela na tela do computador.', title='Alerta')
confirmation = pyautogui.confirm(
text='Antes de iniciar o código, abra o Fortes ou clique em cima dele (para ficar como programa secundário.)', 
title='Confirmação de execução')
pyautogui.PAUSE = (0.05)

user = 'Allan'
nome = ('Minha Empresa')
competência = ('062022')
provisãoI = ('062021')
provisãoF = ('052022')
provisão13 = ('012022')
ultimodia = ('30062022')


if (confirmation == 'OK'):
    pyautogui.alert('O código vai iniciar, não mexa no computador.', title='Alerta')
else: exit(pyautogui.alert('O código foi encerrado'))
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)

'''Folha de Pagamento'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('folha de pagamento')
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.25)
pyautogui.press('enter')
time.sleep(0.75)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(competência)
for x in range (13):
    pyautogui.press('enter')
    time.sleep(0.25)
time.sleep(5)
pyautogui.press('enter')
for x in range(4):
    pyautogui.press('esc')
    time.sleep(0.5)
time.sleep(1)

'''GPS'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('gps')
time.sleep(0.25)
pyautogui.press('enter')
time.sleep(0.75)
pyautogui.press('f2')
time.sleep(0.5)
pyautogui.write(competência)
pyautogui.press('tab')
pyautogui.press('pgdn')
time.sleep(0.5)
for x in range(3):
    pyautogui.press('enter')
pyautogui.press('f9')
time.sleep(0.5)
for x in range(4):
    pyautogui.press('esc')
    time.sleep(0.25)
time.sleep(1)

'''Provisão de férias'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('provisao de ferias')
time.sleep(0.75)
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(competência)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('pgdn')
pyautogui.press('enter')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(provisãoI)
pyautogui.press('tab')
pyautogui.write(provisãoF)
for x in range(13):
    pyautogui.press('enter')
    time.sleep(0.5)
time.sleep(1)
for x in range(4):
    pyautogui.press('esc')
    time.sleep(0.5)
time.sleep(1)

'''Provisão de 13° salário'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('provisao de 13')
time.sleep(0.75)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(competência)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('pgdn')
pyautogui.press('enter')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(provisão13)
pyautogui.press('tab')
pyautogui.write(provisãoF)
for x in range(13):
    pyautogui.press('enter')
    time.sleep(0.5)
time.sleep(1)
for x in range(4):
    pyautogui.press('esc')
    time.sleep(0.5)
time.sleep(1)

relatorios = pyautogui.confirm('Deseja salvar os relatórios da folha?', title='Salvar relatórios', buttons=['SIM', 'NAO'])
if (relatorios == 'SIM'):
    pyautogui.alert('Os relatórios serão salvos.', title='Alerta')
else: exit(pyautogui.alert('O código foi encerrado'))
time.sleep(0.5)
'''Salvar Relatórios'''
'''listagem de pagameto'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('listagem de pagamento')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write(competência)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.write(ultimodia)
pyautogui.press('enter')
pyautogui.press('pgdn')
for x in range(5):
    pyautogui.press('enter')
    time.sleep(0.25)
pyautogui.press('enter')

pyautogui.alert('O processo terminou', title='Obrigado')
