import pandas as pd
from customers.models import Customer
from django.db import IntegrityError

def run():
    # Load the CSV file
    file_path = "data/customers.csv"  
    df = pd.read_csv(file_path)

    # Iterate over each row in the DataFrame and create a Customer instance
    for _, row in df.iterrows():
        try:
            Customer.objects.create(
                id=row['ID'],
                warehouse_block=row['Warehouse_block'],
                mode_of_shipment=row['Mode_of_Shipment'],
                customer_care_calls=row['Customer_care_calls'],
                customer_rating=row['Customer_rating'],
                cost_of_the_product=row['Cost_of_the_Product'],
                prior_purchases=row['Prior_purchases'],
                product_importance=row['Product_importance'],
                gender=row['Gender'],
                discount_offered=row['Discount_offered'],
                weight_in_gms=row['Weight_in_gms'],
                reached_on_time=bool(row['Reached.on.Time_Y.N'])
            )
        except IntegrityError as e:
            print(f"Error inserting row {row['ID']}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("Data loaded successfully.")
