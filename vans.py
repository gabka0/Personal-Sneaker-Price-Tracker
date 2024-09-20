from selenium import webdriver
from selenium.webdriver.common.by import By

def find_item(shoe_link):
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(shoe_link)
        shoe_name = driver.find_element(By.CLASS_NAME, "base").text
        print(shoe_name)
            # Attempt to find the discounted price first
        price_dollar = driver.find_element(By.CLASS_NAME, "price")
        print(price_dollar.text)

        current_price_text = price_dollar.text
        current_price = int(current_price_text[1:-3])
        
        
        
        driver.quit()
        
        return current_price, shoe_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None