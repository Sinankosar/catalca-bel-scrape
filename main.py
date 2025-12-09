import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.catalca.bel.tr/baskana-mesaj-gonder")

message = """
Bu mesaj bir python botu tarafından gönderilmektedir, lütfen dikkate almayınız.
Rahatsız ettiğimiz için özür dileriz.
İyi çalışmalar...
"""
telefon_numarasi = "(511) 111-1111" 

wait = WebDriverWait(driver, 10)


name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
name_input.send_keys("Python Bot")
name_input.send_keys(Keys.TAB)

time.sleep(0.5)

actions = ActionChains(driver)

# Email
actions.send_keys("bot@catalcabel.com.tr")
actions.send_keys(Keys.TAB)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

# Telefon
actions.send_keys(telefon_numarasi)
actions.send_keys(Keys.TAB)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

# Konu
actions.send_keys("Bot deneme")
actions.send_keys(Keys.TAB)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

# İlçe
actions.send_keys("Çatalca")
actions.send_keys(Keys.TAB)
actions.perform()
actions.reset_actions()
time.sleep(0.5)

# Mesaj
actions.send_keys(message)
actions.perform()
actions.send_keys(Keys.TAB)
actions.perform()
actions.send_keys(Keys.ENTER) #mesaj gönder butonu.
actions.perform()

actions.reset_actions()
time.sleep(5)
driver.close()