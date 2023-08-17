import random
from generator_js import porysuj_background
import asyncio
import threading
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchWindowException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

JS_STYLE_RED_RECT = '2px solid red'
DRAW_RECT_TIME = 3
WEBDRIVER_AWAIT = 7
css_alltext_without_children = " *:not(:empty):not(:has(*)):not(script):not(title):not(style)"


class FactoryDriver():
    def __init__(self, driver):
        self.driver = driver

    def click_webelement(self, element):
        try:
            if self.driver:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except ElementNotInteractableException:
            pass
        except Exception as e:
            print('click ', e)

    def get_all_webelements_contains_text(self):
        text_elements = self.driver.find_elements(By.CSS_SELECTOR, css_alltext_without_children)
        text_elements = [ele for ele in text_elements if not ele.text == ""]
        return text_elements

    def find_text_element_in_webdriver(self, text_in_element):
        elements_all_text = self.get_all_webelements_contains_text()
        start_time = time.time()
        word_all, word_one = [], []

        calytext = text_in_element.strip().lower()
        slowa = re.split(r"[,  !?]", calytext)

        if not isinstance(elements_all_text, list):
            print(f'{text_in_element} is no elements with text, check errors')

        for ele in elements_all_text:
            ele_text = ele.text

            if not ele_text:
                continue

            ele_text = ele_text.lower()

            if calytext in ele_text:  # checking cale zdanie
                word_all.append(ele)
            # else:
            #     print(calytext, ele_text)
            # if check_word_phrase(slowa, ele_text):  # checking one word
            #     word_one.append(ele)

        print('all', len(word_all), 'one', len(word_one), 'fin time', time.time() - start_time)
        if not word_all:
            if not word_one:
                print('nic nima', text_in_element)
            else:
                return word_one
        else:
            print('word_one', len(word_one))
            return word_all

    def hightlight_element(self, element, color):
        self.driver.execute_script(porysuj_background, element, color)

    def get_random_color(self):
        colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#FF1493",
                  "#00FF7F", "#FF4500"]
        rand_color = random.choice(colors)
        return rand_color

    def highlight_rect_on_elements(self, elements, color):
        if 'random' in color:
            color = self.get_random_color()

        if isinstance(elements, list):
            for element in elements:
                self.hightlight_element(element, color)
