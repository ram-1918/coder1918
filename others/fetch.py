rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
service = Service(
    '/Users/nagapriya/Desktop/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("http://sdetchallenge.fetch.com/")


def weigh(bars_left, bars_right, idx):
    try:
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, f"left{bars_left[0]}")))
        for bar in bars_left:
            driver.find_element(By.ID, f"left_{bar}").send_keys(str(bar))
        for bar2 in bars_right:
            driver.find_element(By.ID, f"right_{bar2}").send_keys(str(bar2))
        driver.find_element(By.ID, "weigh").click()
        WebDriverWait(driver, 20).until(lambda d: len(d.find_elements(
            By.XPATH, "//*[@id='root']/div/div[1]/div[5]/ol/li")) > 0)

        if idx < 1:
            results = driver.find_elements(
                By.XPATH, f"//*[@id='root']/div/div[1]/div[5]/ol/li")
        else:
            results = driver.find_elements(
                By.XPATH, f"//*[@id='root']/div/div[1]/div[5]/ol/li[{idx}]")
        
        result_text = results[-1].text
        print(result_text)
        print(results)
        driver.find_element(By.ID, "reset").click()
        return result_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# //*[@id="root"]/div/div[1]/div[5]/ol/li[2]/text()
# //*[@id="root"]/div/div[1]/div[5]/ol/li[1]/text()
# //*[@id= "root"]/div/div[1]/div[5]/ol/li/text()


def find_fake_bar():
    weighings = []
    # while True:
    result = weigh([0, 1, 2], [3, 4, 5], 0)
    if result:
        weighings.append(result)
        if '<' in result:
            suspect_group = [0, 1, 2]
        elif '>' in result:
            suspect_group = [3, 4, 5]
        else:
            suspect_group = [6, 7, 8]

        result = weigh([suspect_group[0]], [suspect_group[1]], 1)
        if result:
            weighings.append(result)
            if '<' in result:
                fake_bar = suspect_group[0]
            elif '>' in result:
                fake_bar = suspect_group[1]
            else:
                fake_bar = suspect_group[2]

            driver.find_element(By.ID, f"coin_{fake_bar}").click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_message = alert.text
            alert.accept()

            print("Alert message:", alert_message)
            print("Fake bar identified as bar number:", fake_bar)
            print("Number of weighings:", len(weighings))
            print("List of weighings made:", weighings)
        else:
            print("Failed to perform second weighing.")
    else:
        print("Failed to perform first weighing.")


find_fake_bar()
driver.quit()