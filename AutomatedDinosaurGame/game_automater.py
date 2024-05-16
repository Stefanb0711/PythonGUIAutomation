import pyautogui
import PIL
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class DinoGameAutomater:
    def __init__(self):
        self.game_over = False
        self.x_dinosaur = None
        self.y_dinosaur = None
        #R,G-B- Values alle 83
        self.obstacle_color_r = 83
        self.chrome_dino_url = "https://dino-chrome.com/de"

        self.restart_game_img = "Pics/restartGameButton.png"


    def game(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(self.chrome_dino_url)
        driver.implicitly_wait(10)
        pyautogui.typewrite(" ")


        while True:
            try:
                restart_game_button = pyautogui.locateCenterOnScreen(self.restart_game_img, confidence=0.7)
                if restart_game_button:

                    time.sleep(1.5)
                    pyautogui.click(restart_game_button)
            except:
                for x in range(720, 790):
                    if pyautogui.pixel(x, 460)[0] == 83:
                        pyautogui.typewrite(" ")


