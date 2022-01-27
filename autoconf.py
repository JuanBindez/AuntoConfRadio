import os

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

    time.sleep(25)
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
    pyautogui.click(button='right')  # right-click the mouse
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
    pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
    pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
    pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
    pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while hold
    im2 = pyautogui.screenshot('my_screenshot.png')'''

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
