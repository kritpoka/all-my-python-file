import autopy as at

screen = at.bitmap.capture_screen()
positions = screen.find_color(0,0,0)
print(positions)
