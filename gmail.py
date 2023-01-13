import pyautogui 

print('Function /n -gmail /n -search')
asks = input('Hi! what do you want: ')

if asks == 'gmail':
    pyautogui.press('win')
    pyautogui.moveTo(x=161,y=743,duration=1)
    pyautogui.write('chrome',interval=0.3)
    pyautogui.press('enter')
    pyautogui.moveTo(x=287, y=49,duration=1)
    pyautogui.click(clicks=1)
    pyautogui.write('gmail.com',interval=0.1)
    pyautogui.press('enter')
    pyautogui.moveTo(x=1323, y=137,duration=1.5)
    pyautogui.click(clicks=1)
    pyautogui.moveTo(x=1132, y=423,duration=1)
    pyautogui.click(clicks=1)

ans =input('yes or no: ')
if ans =='y':
    pyautogui.moveTo(x=471, y=14,duration=1)
    pyautogui.click(clicks=1)

else if:
    print('THX')

else:
    pyautogui.moveTo(x=35, y=149,duration=0)
    pyautogui.click(clicks=2)
    pyautogui.moveTo(x=287, y=49,duration=1)
    pyautogui.write('youtube.com', interval=0.1)
    pyautogui.press('enter')
    pyautogui.moveTo(x=552, y=131,duration=2)
    pyautogui.click(x=552, y=131)
    pyautogui.write('9arm',interval=0.1)    
    pyautogui.press('enter')
    pyautogui.moveTo(x=654, y=478, duration=1)
    pyautogui.click(clicks=2)