import nike, adidas, newBalance, asics, vans
from connection import mycursor, db
import storeData
import schedule
import time
import smtplib
from email.mime.text import MIMEText

def check_prices():
    # Fetch all sneakers from database
    mycursor.execute("SELECT * FROM sneakers")
    sneakers = mycursor.fetchall()

    for sneaker in sneakers:
        brand_name, shoe_link, max_price = sneaker[1], sneaker[3], sneaker[5]
        current_price = None
        
        if brand_name.lower() == "nike":
            current_price = nike.find_item(shoe_link)
            current_price_int = current_price[0]   
               
        if brand_name.lower() == "adidas":
            current_price = adidas.find_item(shoe_link)
            current_price_int = current_price[0]

        if brand_name.lower() == "new balance":
            current_price = newBalance.find_item(shoe_link)
            current_price_int = current_price[0]

        if brand_name.lower() == "asics":
            current_price = asics.find_item(shoe_link)
            current_price_int = current_price[0]

        if brand_name.lower() == "vans":
            current_price = vans.find_item(shoe_link)
            current_price_int = current_price[0]


        if current_price_int < max_price:
            send_email_notification(brand_name, shoe_link, current_price_int, max_price)
        

def send_email_notification(brand_name, shoe_link, current_price, max_price):
    sender_email = "kassymgabdushev@gmail.com"
    receiver_email = "kassymgabdushev@gmail.com"
    password = 'yptpiyiyhakznczu'
    subject = f"Price Alert: {brand_name} sneaker price dropped!"
    body = f"The price of the sneaker has dropped below your desired price of ${max_price}. Current price is ${current_price}.\nLink: {shoe_link}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
            msg=f'Subject: {subject}"\n\n{body}')
  
if __name__ == "__main__":
    brand_name = input("Enter the brand of the shoe/cloth: ")
    shoe_link = input("Enter the link of the shoe/cloth: ")
    max_price = float(input("Enter maximum price you are willing to pay: "))
    
    storeData.store_user_data(brand_name, shoe_link, max_price)
    
    if brand_name.lower() == "nike":
        current_price, shoe_name = nike.find_item(shoe_link)
        storeData.store_scrapped_info(current_price, shoe_name, shoe_link)
    
    if brand_name.lower() == "adidas":
        current_price, shoe_name = adidas.find_item(shoe_link)
        storeData.store_scrapped_info(current_price, shoe_name, shoe_link)
    
    if brand_name.lower() == "asics":
        current_price, shoe_name = asics.find_item(shoe_link)
        storeData.store_scrapped_info(current_price, shoe_name, shoe_link)

    if brand_name.lower() == "new balance":
        current_price, shoe_name = newBalance.find_item(shoe_link)
        storeData.store_scrapped_info(current_price, shoe_name, shoe_link)

    if brand_name.lower() == "vans":
        current_price, shoe_name = vans.find_item(shoe_link)
        storeData.store_scrapped_info(current_price, shoe_name, shoe_link)
        
    check_prices()
        

    # Schedule daily price check 

    schedule.every().day.at("09:00").do(check_prices)
    while True:
        schedule.run_pending()
        time.sleep(1)



