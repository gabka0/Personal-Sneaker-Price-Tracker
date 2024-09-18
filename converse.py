from selenium import webdriver
from selenium.webdriver.common.by import By

def add_item(shoe_link):
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(shoe_link)
        try:
            # Attempt to find the discounted price first
            price_dollar = driver.find_element(By.CLASS_NAME, "orange")
        except:
            # If discounted price is not found, try to find the regular price
            price_dollar = driver.find_element(By.CSS_SELECTOR, 'span[class=""]')
            print(price_dollar)

        current_price_text = price_dollar.text
        current_price = int(current_price_text[3:])
        
        shoe_name = driver.find_element(By.CLASS_NAME, "pdp-right-name").text
        
        driver.quit()
        
        return current_price, shoe_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None