import pyautogui as pag
from game import game_utils

# screen size
# width, height = pag.size()
# print('width:{},height:{}'.format(width, height))

# screen shot
# img = pag.screenshot()
# img = pag.screenshot(region=(0, 0, 300, 400))
# img.save('screen.bmp')

# find color
# print(img.getpixel((50, 200)))
# ifEqual = pag.pixelMatchesColor(50, 200, (255, 255, 255))
# print(ifEqual)

# find img
# print(pag.locateOnScreen('image/temp.bmp'))  # (13, 297, 57, 73)
# 需要下载opencv-python 和numpy
scale = 1
print(pag.locateCenterOnScreen(game_utils.resize_image('image/temp.bmp', scale, scale), confidence=0.9))  # (41, 333)

# mouse
# pag.click(rubbish_center[0], rubbish_center[1], clicks=2, interval=0.25, button='right') # 右击2次间隔0.25
# pag.moveTo(600, 100, 0.2)
# pag.click()

# key
# pag.hotkey('ctrl', 'l')  # 组合键
# pag.typewrite('hello', interval=0.25)
# pag.press('=')
