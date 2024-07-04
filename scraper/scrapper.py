from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def get_data():
    
        driver_path = '/usr/bin/chromedriver'
        options = Options()
        options.add_argument("--headless") 
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("https://www.nvidia.com/en-in/geforce/buy/")

      
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".aem-Grid .nv-title.text"))
        )

        data = []
        containers = driver.find_elements(By.CSS_SELECTOR, ".aem-Grid .nv-title.text")

        for i in range(len(containers) - 1):
            name_container = containers[i]
            price_container = containers[i + 1]

            name_title = name_container.find_element(By.CSS_SELECTOR, ".general-container-text .title").text.strip()
            
            try:
                price_text = price_container.find_element(By.CSS_SELECTOR, ".general-container-text .title").text.strip()
                if "Starting at" in price_text:
                    price = price_text.split("Starting at ")[1].strip()
                else:
                    price = "N/A"
            except NoSuchElementException:
                price = "N/A"

            if "Starting at" in name_title:
                continue  

            data.append({"name": name_title, "price": price})

        driver.quit()
        return data[1:-4]
    

