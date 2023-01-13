import pyautogui

for i in range(100):
    screen = autopy.bitmap.capture_screen()

positions = screen.file_color((255,199,99),0.03)
print(positions)