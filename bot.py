#selenium python
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class jobstart():

    def sart_jobs(self):
        print(" starting download ")
        options = uc.ChromeOptions()
        options.add_argument("--profile-directory=Profile 1")
        options.add_argument("user-data-dir=C:\\Users\\HAMIT\\AppData\\Local\\Google\\Chrome\\User Data")
        driver = uc.Chrome(options=options)
        #account details hidden
        account = "*****"
        password = "*****"
        url = "https://*****.co"
        my_files = "https://*****.co/"
        # load the page
        driver.get(url)
        wait = WebDriverWait(driver, 15)
        driver.implicitly_wait(5)
        # after DOM has loaded login to the account
        print("Bot login to account")
        mail = driver.find_element(By.XPATH, value="//*[@id='root']/div/div/div[2]/form/div[1]/div[2]/input")
        time.sleep(1)
        mail.clear()
        mail.send_keys(account)
        driver.find_element(By.XPATH, value="//*[@id='root']/div/div/div[2]/form/button").click()
        time.sleep(2)
        key = driver.find_element(By.XPATH, value="//*[@id='root']/div/div/div[2]/form/div[2]/div[2]/input")
        key.clear()
        key.send_keys(password)
        driver.find_element(By.XPATH, value="//*[@id='root']/div/div/div[2]/form/button").click()
        time.sleep(6)
        print("finished login process")
        # after login try to find jobs at my files page
        i = 0
        while True:
            i += 1
            tries = 0
            print("---")
            Job = False

            while True:
                tries += 1
                print("!___________!")
                try:
                    print("++++try!!++++")
                    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Waiting for')))
                    print("************Trying************")
                    Job = True
                except NoSuchElementException:
                    print("-*-*-*-*-*-*-No Job-*-*-*-*-*-*-")
                    Job = False
                except TimeoutException:
                    Job = False

                # if job is true try to pick a job and notify the user
                if Job == True:
                    driver.find_element(By.LINK_TEXT, "File").click()
                    print("-----------Tried to pick a job-----------")
                    time.sleep(3)
                    if driver.current_url != my_files:
                        # if not true means job is picked
                        print("*************************Job Picked*************************")
                        input()
                        print("*****-------*********Job Picked code paused*****-------*********")
                    else:
                        Job = False
                        print("********")


                if Job == False:
                    print("--No Job--")
                    time.sleep(5)
                    print("---No Job Refresh page---")
                    driver.refresh()
                if tries == 7: break
            if i == 6:
                # initiate the logout
                driver.find_element(By.XPATH, value="//*[@id='content-wrapper']/header/div[5]/div/span/a").click()
                driver.find_element(By.XPATH, value="//*[@id='content-wrapper']/header/div[5]/div/span/ul/li[3]/a").click()
                loged_out = True
                if loged_out == True: break



start = jobstart()
start.sart_jobs()
