import asyncio
from asyncore import loop
from cgitb import lookup
from dataclasses import dataclass
from os import times
from pickle import FALSE
from timeit import repeat, timeit
from tkinter.messagebox import QUESTION
from tracemalloc import stop
import pyautogui
import time

'''Monitor resolution: 1920 x 1080 (you've to chance the mouse atributes'''
'''time.sleep can chance in diferents computer and/or in diferents campanys.'''

pyautogui.alert('Minimize o VSCode e o centralize em modo janela na tela do computador') '''Minimize the (system that you use) in the middle of scream'''
confirmation = pyautogui.confirm(
text='Antes de iniciar o código, abra a direita do computador a planilha de ocorrências e a esquerda o Fortes.', '''before the code start's, in the right open the excel and in the left open the Fortes'''
title='Confirmação de execução.') '''Execution confirmation'''
pyautogui.PAUSE = (0.1)

competência = ('062022') '''show the month of payment'''

if (confirmation == 'OK'):
    pyautogui.alert('O código vai iniciar, não mexa no computador') '''the code will start, don't touch in your pc'''
else: exit()
pyautogui.click(x=272, y=129)
pyautogui.press('enter')
pyautogui.write(competência) '''take the date on the line 22'''
for x in range (12):
    pyautogui.press('enter')
    time.sleep(0.1)
time.sleep(2)
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.click(x=780, y=739)
pyautogui.click(x=123, y=55)
pyautogui.moveTo(x=323, y=115)
time.sleep(0.5)
pyautogui.moveTo(x=663, y=197)
time.sleep(0.5)
pyautogui.click(x=901, y=205)
pyautogui.write(competência)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.click(x=1833, y=874)
pyautogui.hotkey('ctrl', 'home')
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'tab')
pyautogui.rightClick(x=325, y=520)
pyautogui.click(x=433, y=634)
pyautogui.press('enter')
