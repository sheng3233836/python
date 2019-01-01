import pyautogui as pag
import time

# 楚留香自动换线采集
# 坐标点是取自：windows 7 分辨率1366*768 右侧任务栏 全屏

line = 0


def find_img_and_click(img, region, offset_x=0, offset_y=0, confidence=0.99):
    center = pag.locateCenterOnScreen(img, region=region, confidence=confidence)
    if center:
        pag.click(center[0] + offset_x, center[1] + offset_y)
    return center


# 选定至游戏界面

while True:
    if line == 0: pag.click(1185, 430)
    pag.click(854, 408)
    time.sleep(1)
    # 自动换工具
    if pag.pixelMatchesColor(760, 362, (1, 219, 0)):
        pag.click(760, 342)
    time.sleep(8.5)
    # 遇到需要‘食用’道具
    find_img_and_click('image/eat_button.bmp', (900, 380, 1070, 520))
    # 遇到需要‘学习’道具
    learn_center = find_img_and_click('image/learn_button.bmp', (900, 380, 1070, 520))
    if learn_center:
        # 可能已经学习，需点击‘确认’
        time.sleep(0.5)
        find_img_and_click('image/yes_button.bmp', (700, 500, 1000, 600))
    # 换线
    time.sleep(0.5)
    # 点击所在线
    pag.click(1287, 60)
    time.sleep(0.5)
    # 切换所在线
    pag.click(1000, 100 + (line * 75))
    line = line + 1
    if line > 7:
        line = 0
    time.sleep(2)
