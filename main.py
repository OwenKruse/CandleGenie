from selenium import webdriver
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
options.add_argument(r"user-data-dir=C:\Users\oweno\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)

i = 1
total = 100
def timer():


    while i == 1:
        driver.switch_to.window(driver.window_handles[1])

        timer = driver.find_element_by_xpath\
            ("/html/body/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div[1]")

        def get_sec(time_str):
            """Get Seconds from time."""
            m, s = time_str.split(':')
            return int(m) * 60 + int(s)
        if timer.text.isnumeric():
            return timer.text



        total = (get_sec(timer.text))
        print(total)


        if total < 35\
            :

            driver.switch_to.window(driver.window_handles[0])
            time.sleep(6)


            upTrend = \
                driver.find_element_by_xpath \
                    ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[2]")


            downTrend = \
                driver.find_element_by_xpath \
                    ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[5]/div[2]/div[4]/div[2]")


            u = False
            d = False
            try:
                if (upTrend.text != "n/a"):
                    print("up")
                    u = True
            except StaleElementReferenceException:
                continue
            try:
                if (downTrend.text != "n/a"):
                    print("down")
                    d = True
            except StaleElementReferenceException:
                continue
            driver.switch_to.window(driver.window_handles[1])


            if (d == True):
                EnterDown = driver.find_elements_by_xpath("//*[contains(text(), 'Enter DOWN')]")[0]
                EnterDown.click()
                time.sleep(1)
                pyautogui.moveTo(x=1289, y=598)

                pyautogui.click()

                pyautogui.write(".001")

                pyautogui.moveTo(x=1290, y=773)

                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x=1912, y=562)

                pyautogui.click()

                pyautogui.moveTo(x=1817, y=566)

                pyautogui.click()






            if (u == True):
                EnterUp = driver.find_elements_by_xpath("//*[contains(text(), 'Enter UP')]")[0]
                EnterUp.click()
                time.sleep(1)
                pyautogui.moveTo(x=1289, y=598)

                pyautogui.click()

                pyautogui.write(".001")

                pyautogui.moveTo(x=1290, y=773)

                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x=1912, y=562)

                pyautogui.click()

                pyautogui.moveTo(x=1817, y=566)

                pyautogui.click()





            time.sleep(45)

if __name__ == '__main__':
    timer()

