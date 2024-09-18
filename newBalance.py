from selenium import webdriver
from selenium.webdriver.common.by import By

def find_item(shoe_link):
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(shoe_link)
        try:
            # Attempt to find the discounted price first
            price_element = driver.find_element(By.XPATH, "//span[contains(@class, 'sales') and contains(@class, 'font-body-large')]")
        except:
            # If discounted price is not found, try to find the regular price
            price_element = driver.find_element(By.XPATH, "//span[contains(@class, 'sales') and contains(@class, 'font-body-large')]")


        current_price_text = price_element.text
        current_price = int(current_price_text[3:])
        
        shoe_name = driver.find_element(By.XPATH, "//h1[contains(@class, 'product-name') and contains(@class, 'font-header-1') and contains(@class, 'mb-0')]").text
        
        driver.quit()
        
        return current_price, shoe_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None