import pyautogui
plt = input('name platfrom:')
name = input('name:')

pyautogui.moveTo(x=35, y=149,duration=0)
pyautogui.click(clicks=2)
pyautogui.moveTo(x=287, y=49,duration=1)
pyautogui.write(plt +'.com', interval=0.1)
pyautogui.press('tab')
pyautogui.write(name)
pyautogui.press('enter')

pyautogui.moveTo(x=648, y=250,duration=1)
pyautogui.click()

pyautogui.moveTo(x=552, y=131,duration=2)
pyautogui.click(x=552, y=131)
pyautogui.write('9arm',interval=0.1)
pyautogui.press('enter')
pyautogui.moveTo(x=654, y=278, duration=1)
pyautogui.click(clicks=2)
