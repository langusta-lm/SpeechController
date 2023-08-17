import threading
import time

import speech_recognition as sr
import asyncio

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from matrix_of_words.func_on_words import check_command_in_query, remove_command_from_query
from matrix_of_words.word_matrix import *
from driver_factor.operations_on_element import highlight_rect_on_elements, find_text_element_in_webdriver, \
    click_webelement, highlight_rect_on_element

INFO_DEBUG = True
THREADERS_RED_RECT: threading = []


# def init_driver_js_scripts(driver):
#     with open("analyazers.js", "r") as file:
#         script_content = file.read()
#     driver.execute_script(script_content)


def do_action_in_command(recognized, driver):
    def check_command(command):
        res = check_command_in_query(recognized, command)
        return res

    def cut_qcommmand(command):
        res = remove_command_from_query(recognized, command)
        return res

    # init_driver_js_scripts(driver)
    # Wykonanie odpowiedniej akcji w zależności od komendy

    if check_command(mw_scroll_down):
        # if mw_scroll_down in command:
        driver.execute_script("window.scrollBy(0, 400);")

    elif check_command(mw_scroll_up):
        driver.execute_script("window.scrollBy(0, -400);")

    # KLIKANIE
    elif check_command(mw_click):
        query = cut_qcommmand(mw_click)
        if query:
            print('query', query)
            elements = find_text_element_in_webdriver(driver, query)

            if elements:
                highlight_rect_on_elements(driver, elements)
                if len(elements) == 1:
                    click_webelement(elements[0], driver)
                elif len(elements) > 1:
                    highlight_rect_on_elements(driver, elements)

    # PODŚWIETL OBIEKTY
    elif check_command(mw_localize):
        query = cut_qcommmand(mw_localize)
        # query =
        # query = recognized.split("znajdź")[-1]
        if query:

            elements = find_text_element_in_webdriver(driver, query)
            if elements:
                highlight_rect_on_elements(driver, elements)
                print(f"wykryto {len(elements)}")
                # highlight_rect_on_elements(driver, elements, '#FFFF00')
                # rect_thread = draw_rect_on_element(driver, element)
                # rect_thread.join()
                pass

    # WPISYWANIE TEKSTU
    elif check_command(mw_type):
        query = cut_qcommmand(mw_type)
        # query = recognized.split("wpisz")[-1]
        if query:
            element = driver.switch_to.active_element
            highlight_rect_on_element(driver, element)
            # rect_thread = draw_rect_on_element(driver, element)
            # rect_thread.start()
            element.send_keys(query)
            # rect_thread.join()
            time.sleep(1)
            element.send_keys(Keys.RETURN)

    elif check_command(mw_browse):
        query = cut_qcommmand(mw_browse)
        driver.get(f"https://www.google.com/search?q={query}")

    elif check_command(mw_finish):
        query = cut_qcommmand(mw_finish)
        return driver.quit()


def get_chrome_driver():
    return webdriver.Chrome(ChromeDriverManager().install())


def init_driver(url="https://www.google.com/"):
    driver = get_chrome_driver()
    driver.get(url)
    return driver


async def voice_control():
    driver = init_driver()
    r = sr.Recognizer()
    r.pause_threshold = 2
    r.operation_timeout = 4
    while True:
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source)
            # et = r.energy_threshold
            # print("Mów teraz!   %s" % str(et))
            print("Mów teraz!", end='')
            audio = r.listen(source, phrase_time_limit=8)
            print('..checking', end='\r')
        try:
            # Rozpoznanie komendy głosowej
            command = r.recognize_google(audio, language="pl-PL")
            command = command.lower()
            print(f"Wykonuję polecenie: {command}")

            # Wykonanie odpowiedniej akcji w zależności od komendy
            do_action_in_command(command, driver)

        except sr.UnknownValueError:
            print("Nie udało się zrozumieć polecenia.", end='\r')
        except sr.RequestError as e:
            print(f"Błąd rozpoznawania mowy: {e}")


asyncio.run(voice_control())


def ppp(self):
    ele = self.driver.switch_to.active_element()
    self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)


def t1():
    driver = init_driver()
    # setattr(driver, 'ppp', ppp)
    elements = find_text_element_in_webdriver(driver, "Zaakceptuj Wszys")
    if elements:
        highlight_rect_on_elements(driver, elements, '#FFFF00')
        time.sleep(1)
        click_webelement(driver, elements[0])
    # driver.ppp()
    # type_text(driver, 'ziemniak')
    # type_enter(driver)
    time.sleep(2)
    element = driver.switch_to.active_element
    click_webelement(driver, element)
    # highlight_rect_on_element(driver, element)
    # rect_thread = draw_rect_on_element(driver, element)
    # rect_thread.start()
    element.send_keys('ziemniak')
    # rect_thread.join()
    element.send_keys(Keys.RETURN)

    elements = find_text_element_in_webdriver(driver, "ziemniak")
    highlight_rect_on_elements(driver, elements)
    time.sleep(20)
    driver.quit()
    return


# t1()
