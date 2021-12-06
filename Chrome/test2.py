import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class CoffeeMachineBorkBig(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'.\chromedriver\chromedriver.exe'
        )

    def test_coffee_machine(self):
        driver = self.driver
    #текст запроса
        request='КУПИТЬ КОФЕМАШИНУ BORK C804'
    #переходим на стартовую страницу и вводим запрос
        driver.get('https://www.google.com/')
        time.sleep(1)
        searchform = driver.find_element(By.NAME, 'q')
        time.sleep(1)
        searchform.click()
        searchform.send_keys(request)
        time.sleep(1)
        searchform.send_keys(Keys.ENTER)
        time.sleep(1)
    #цепляем строку с результатами поиска, удаляем из нее пробелы
        result_stats = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
        print(result_stats)
        import re
        RStext = result_stats.replace(" ", "")
        response = re.findall("\d+", RStext)[0]
    #делаем строку целым числом и проверяем, больше она 10 или нет
        c=int(response)
        if c<10:
            print("***НЕУДАЧА:", c ,"- меньше 10. Проверяем, есть ли в результатах М.Видео***")
        elif c>10:
            print("***УСПЕХ:", c ,"- больше 10. Проверяем, есть ли в результатах М.Видео***")
        else:
            print("Что-то сломалось. Пожалуйста, повторите позже")
    
    #проверяем, есть ли 'https://www.mvideo.ru' на странице
        try:
            mvideo_http = driver.find_elements(By.XPATH, "//*[contains(text(), 'Кофейная станция Bork C804 - М.Видео')]")
            time.sleep(2)
            print("***УСПЕХ. Ссылка на М.Видео найдена на странице.")
            time.sleep(2)
        except:
            print("НЕУДАЧА. Ссылки на М.Видео нет на странице")
            time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()