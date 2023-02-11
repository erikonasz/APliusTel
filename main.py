import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import random

linkas = input("Autopliuso masinu linkas: ")

def randomlaikas():
    _sleep = random.randint(3,10)
    time.sleep(_sleep)


def scrape_phone_numbers():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(linkas)
    time.sleep(4)
    accept_cookies = driver.find_element(By.XPATH, '//button[text()="Sutinku"]')
    accept_cookies.click()
    time.sleep(3)

    results = []
    num_cars = int(input("Kiek nuskreipinti automobiliu: "))
    current_window_handle = driver.current_window_handle

    while len(results) < num_cars:
        cars = driver.find_elements(By.XPATH, '//div[@class="announcement-title"]')

        for i, car in enumerate(cars):
            if i == num_cars:
                break
            current_window_handle = driver.current_window_handle
            car.click()
            time.sleep(3)
            for handle in driver.window_handles:
                if handle != current_window_handle:
                    driver.switch_to.window(handle)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            phone = soup.find("div", class_="button seller-phone-number js-phone-number")
            if phone is not None:
                phone_number = phone.text.replace(" ", "")
                if "+370" in phone_number and phone_number not in results:
                    results.append(phone_number)
            driver.close()
            driver.switch_to.window(current_window_handle)

        try:
            next_page = driver.find_element(By.XPATH, '//a[@rel="next" and @class="next"]')
            next_page.click()
            time.sleep(3)
        except Exception as e:
            break

    with open("phones.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Phone Number"])
        for phone_number in results:
            phone_number = phone_number.strip('"\n')
            if "+370" not in phone_number:
                continue
            writer.writerow([phone_number])
        print(results)


scrape_phone_numbers()
#01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100111 01101001 01110100 01101000 01110101 01100010 00101110 01100011 01101111 01101101 00101111 01100101 01110010 01101001 01101011 01101111 01101110 01100001 01110011 01111010