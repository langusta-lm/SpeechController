import random
from generator_js import porysuj_background
import asyncio
import threading
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchWindowException, NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import re

JS_STYLE_RED_RECT = '2px solid red'
JS_STYLE_BLUE_RECT = "5px solid blue"
DRAW_RECT_TIME = 3
WEBDRIVER_AWAIT = 7
css_alltext_without_children = " *:not(:empty):not(:has(*)):not(script):not(title):not(style)"



########################################################################


def get_random_color():
    jaskrawe_kolory = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#FF1493",
                       "#00FF7F", "#FF4500"]
    wylosowany_kolor = random.choice(jaskrawe_kolory)
    return wylosowany_kolor


def click_webelement(driver, element):
    try:
        if driver:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    except ElementNotInteractableException:
        pass
    except Exception as e:
        print('click ')
        # print(e)


def get_all_webelements_contains_text(driver):
    def get_elements():
        return driver.find_elements(By.CSS_SELECTOR, css_alltext_without_children)

    text_elements = get_elements()
    if not text_elements:
        print("get_all_webelements_contains_text", "WEB DRIVERWAIT EMPTY")
        time.sleep(3)
        text_elements = get_elements()
    if text_elements:
        text_elements = [ele for ele in text_elements if not ele.text == ""]
        return text_elements


def check_word_phrase(words, query):
    good, bad = 0, 0
    for word in words:
        if word not in query:  # checking pojedyczne slowa
            bad += 1
        elif word in query:
            good += 1
    if good >= bad:
        # print(words, query)
        return True
    else:
        return False


def find_text_element_in_webdriver(driver, text_in_element):
    """
    return [ word_all, word_one ]
    :param driver:
    :param text_in_element:
    :return:
    """
    elements_all_text = get_all_webelements_contains_text(driver)
    start_time = time.time()
    word_all, word_one = [], []

    calytext = text_in_element.strip().lower()
    slowa = re.split(r"[,  !?]", calytext)

    if not isinstance(elements_all_text, list):
        print(f'{text_in_element} is no elements with text, check rerrors')

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
        # print('word_one', len(word_one))
        return word_all


class RectJS():
    thickness = '3px'
    structure = 'solid'
    color = 'red'

    def __init__(self, thickness='3px', structure='solid', color='red'):
        self.thickness = thickness.strip()
        self.structure = structure.strip()
        self.color = color.strip()

    def __str__(self):
        total_name = f"{self.thickness} {self.structure} {self.color}"
        return total_name


def highlight_rect_on_element(driver, element=None, color="3px solid red", start_time=1000, end_time=6000):
    if not element:
        element = driver.switch_to.active_element
    if element:
        driver.execute_script(porysuj_background, element, color, start_time, end_time)


def highlight_rect_on_elements(driver, elements, color='random', start_time=1000, end_time=6000):
    used_color = []
    if not isinstance(elements, list) and elements:
        elements = [elements]

    for element in elements:
        if 'random' in color:
            col = get_random_color()
        else:
            col = color
        highlight_rect_on_element(driver, element, col, start_time, end_time)


def type_text(driver, query, element=None):
    if not element:
        element = driver.switch_to.active_element
    if not element:
        element = driver.find_elements_by_css_selector('input')
    if element and len(element) > 1:
        print(f'znaleziono input {len(element)} elementów ')
    if element:
        element[0].send_keys(query)
        highlight_rect_on_element(driver, element[0], color=JS_STYLE_BLUE_RECT)
    else:
        print(f"nieznaleziono input elementów")


def type_enter(driver):
    element = driver.switch_to.active_element
    if element:
        element.send_keys(Keys.RETURN)


########################################################################

def oldfind_text_element_in_webdriver(driver, browse_phrases):
    # def get_elements_contains_text(text_in_element):
    #     try:
    #         # contains_elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{text_in_element}')]")
    #         contains_elements = driver.find_elements(By.XPATH, f"//*[text()= '{text_in_element}']")
    #         return contains_elements
    #     except NoSuchWindowException:
    #         return []
    # def alternative(text_in_element):
    #     try:
    #         text = text_in_element.capitalize()
    #         contains_elements = driver.find_elements(By.XPATH, f"//*[contains(@*, '{text}')]")
    #         return contains_elements
    #     except Exception as e:
    #         print(e)
    elements = []
    browse_phrases = browse_phrases.strip().lower()
    text_elements = get_all_webelements_contains_text(driver)

    for element in text_elements:

        if element and element.text:
            pass

        if element and element.text:
            pass

        # check pojedyczne slowa

    # if not elements:
    # text_in_element lower
    # text_in_element = text_in_element.lower()
    # elements += get_elements_contains_text(text_in_element)

    print(browse_phrases, '-', len(elements))
    return elements


def dis_highlight_element(driver, element):
    current_styles = driver.execute_script("var element = arguments[0]; return element.getAttribute('style');", element)
    driver.execute_script(f"arguments[0].style.border = '{JS_STYLE_RED_RECT}';", element)
    time.sleep(DRAW_RECT_TIME)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, current_styles)


# disable
def dis_draw_rect_on_element(driver, element):
    # elements = find_text_element_in_webdriver(driver, query)
    # global THREADERS_RED_RECT
    if element:
        thread = threading.Thread(target=dis_highlight_element, args=(driver, element,))
        # thread.start()
        return thread


# disable
def dis_draw_rect_on_elements(driver, elements):
    threads = []
    for element in elements:
        threads.append(dis_draw_rect_on_element(driver, element))
    return threads
