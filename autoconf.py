import os

lista_com = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']




try:
    import pyautogui
    import time
    import pyautogui, sys
except ModuleNotFoundError:
    os.system("clear")
    print("instale o pyautogui com o pip")


def function01():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


def function02():
    time.sleep(5)
    pyautogui.click(x=1018, y=571)
    time.sleep(2)
    pyautogui.click(x=1361, y=729) #canto inferior direito
    time.sleep(2)
    time.sleep(2)
    pyautogui.click(x=950, y=690)
    time.sleep(2)
    pyautogui.click(x=862, y=326)
    pyautogui.click(x=862, y=326)
    pyautogui.click(x=862, y=326)
    pyautogui.write('ubnt', interval=0.25,)
    time.sleep(2)

    pyautogui.click(x=988, y=313)
    time.sleep(3)
    pyautogui.click(x=850, y=354)
    pyautogui.click(x=850, y=354)
    pyautogui.click(x=850, y=354)
    pyautogui.write('ubnt', interval=0.25,)

    time.sleep(2)
    pyautogui.click(x=903, y=375)#país
    time.sleep(2)
    pyautogui.click(x=797, y=731)#brazil
    time.sleep(2)
    pyautogui.click(x=481, y=619)#i igreee
    time.sleep(3)
    pyautogui.click(x=899, y=658)#iniciar sessão

    time.sleep(20)
    pyautogui.click(x=796, y=279)#system
    time.sleep(3)
    pyautogui.click(x=1361, y=729)#canto direito + click
    time.sleep(3)
    pyautogui.click(x=850, y=674)#procurar arquivo de configuração
    time.sleep(4)

    pyautogui.click(x=476, y=125)
    pyautogui.click(x=476, y=125)
    pyautogui.click(x=476, y=125)
    time.sleep(4)

    pyautogui.click(x=1312, y=735) #click
    time.sleep(2)
    pyautogui.click(x=1090, y=673)#carregar
    time.sleep(2)
    pyautogui.click(x=1019, y=315)#aplicar
    time.sleep(10)
    time.sleep(6)

    pyautogui.press('f5')



    '''pyautogui.press('enter')  # press the Enter key
    pyautogui.press('f1')     # press the F1 key
    pyautogui.press('left')   # press the left arrow key
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.write('text', interval=0.25,)
    pyautogui.press('enter')
    pyautogui.scroll(10)   # scroll up 10 "clicks"
    pyautogui.scroll(-10)  # scroll down 10 "clicks"
    pyautogui.click(button='right')  # right-click the mouse'''

print("1 ver localização do mouse")
print("2 para executar automação")

x = int(input("digite um numero: "))

if x == 1:
    try:
        function01()
    except NameError:
        os.system("clear")
        print("instale o pyautogui com o pip")


if x == 2:
    try:
        function02()
    except NameError:
        os.system("clear")
        print("instale o pyautogui com o pip")
