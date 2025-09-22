import pyautogui
from datetime import datetime
import time

pyautogui.alert('Abra o genesys')
while True:
    # Atualiza o horário a cada iteração
    agora = datetime.now()
    horario = agora.hour
    minuto = agora.minute

    print('ola')

    # Sai do loop quando for 14:55
    if horario == 15 and minuto == 10:
        
        pyautogui.moveTo(570,579, duration=0.25)
        pyautogui.click()
        
        pyautogui.moveTo(22,1063, duration=0.25)
        pyautogui.click()
        
        time.sleep(2)

        pyautogui.moveTo(17,1009, duration=0.25)
        pyautogui.click()
        break


    time.sleep(10)  # Aguarda 10 segundos para evitar sobrecarregar a CPU

print('acabou')
