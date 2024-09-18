from connection import mycursor, db

def store_user_data(brand_name, shoe_link, max_price):
    try:
        mycursor.execute(
            "INSERT INTO sneakers (Brand, SneakerLink, SneakerWantedPrice) VALUES (%s, %s, %s)",
            (brand_name, shoe_link, max_price)
        )
        db.commit()
    except Exception as e:
        print(f"An error occurred while storing user data: {e}")
    
def store_scrapped_info(current_price, shoe_name, shoe_link):
    try:
        mycursor.execute(
            "UPDATE sneakers SET SneakerCurrentPrice=%s, SneakerName=%s WHERE SneakerLink=%s",
            (current_price, shoe_name, shoe_link)
        )
        db.commit()
    except Exception as e:
        print(f"An error occurred while storing scrapped data: {e}")
