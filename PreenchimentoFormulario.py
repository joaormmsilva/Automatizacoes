import pyautogui,time
nome = ['fabio','joao','nicolas','marcos']
filme = ['A chegada','coraline','os incriveis','sela']
idade = [20,56,12,86]
nota = [3,5,1,2]
comentario = ['bom','top','ruim','medio']
# pyautogui.scroll(-200)
# pyautogui.mouseInfo()
pyautogui.alert('Abra o fomulario')
for i in range(4):
    print(idade[i])
    pyautogui.moveTo(677,430, duration=0.25)
    pyautogui.click()
    pyautogui.write(nome[i])

    pyautogui.scroll(-200)
    
    pyautogui.moveTo(694,407, duration=0.25)
    pyautogui.click()
    pyautogui.write(filme[i])

    pyautogui.moveTo(724,577, duration=0.25)
    pyautogui.click()
    if idade[i] >= 0 and idade[i] <= 18:
        pyautogui.moveTo(729,634, duration=0.25)
        pyautogui.click()
    elif idade[i] >= 19 and idade[i] <= 35:
        pyautogui.moveTo(730,688, duration=0.25)
        pyautogui.click()
    elif idade[i] >= 36 and idade[i] <= 50:
        pyautogui.moveTo(735,731, duration=0.25)
        pyautogui.click()
    elif idade[i] >= 51 and idade[i] <= 70:
        pyautogui.moveTo(725,774, duration=0.25)
        pyautogui.click()
    elif idade[i] >= 71:
        pyautogui.moveTo(718,824, duration=0.25)
        pyautogui.click()
    
    if nota[i] == 1:

        pyautogui.moveTo(788,761, duration=0.25)
        pyautogui.click()
    elif nota[i] == 2:
        pyautogui.moveTo(867,766, duration=0.25)
        pyautogui.click()
    elif nota[i] == 3:
        pyautogui.moveTo(941,765, duration=0.25)
        pyautogui.click()
    elif nota[i] == 4:
        pyautogui.moveTo(1017,763, duration=0.25)
        pyautogui.click()
    elif nota[i] == 5:
        pyautogui.moveTo(1083,764, duration=0.25)
        pyautogui.click()

    pyautogui.moveTo(719,958, duration=0.25)
    pyautogui.click()
    pyautogui.write(comentario[i])

    pyautogui.moveTo(691,1024, duration=0.25)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(702,247, duration=0.25)
    pyautogui.click()