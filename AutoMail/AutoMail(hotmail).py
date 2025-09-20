import pyautogui,time,pyperclip, openpyxl

pyautogui.mouseInfo()
pyautogui.PAUSE = 1
pyautogui.alert('Abra o Chrome para começar o robo')

pyautogui.hotkey("ctrl", "t")

pyperclip.copy('https://outlook.live.com/mail/0/?deeplink=mail%2F0%2F%3Fnlp%3D0&culture=pt-pt&country=pt') #link da pagina incial do gmail

pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

time.sleep(5)


wb = openpyxl.load_workbook('testeAuto.xlsx')  #nome da planilha que sera usada
sheet = wb['Planilha1']
print(sheet)
products = {}
for row in sheet.iter_rows(min_row=2, max_row=10, min_col=1, max_col=3, values_only=True):
    product ={
        "to": row[0],
        "Object": row[1],
        "mail": row[2]
    }

    pyautogui.moveTo(134,191,duration=0.2)
    pyautogui.click()

    pyautogui.write(product['to'])
    pyautogui.press('enter')

    pyautogui.press('tab')
    pyautogui.write(product['Object'])

    pyautogui.press('tab')
    pyautogui.write(product['mail'])   

    pyautogui.hotkey("ctrl","enter")
    pyautogui.press('enter')