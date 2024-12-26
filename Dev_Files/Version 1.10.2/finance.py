# finance.py
from rent import Rent  # Import Rent class to access house listings

class Finance:
    @staticmethod
    def calculate_payment(user_id):
        print("Calculating rent payment...")
        
        house_id = int(input("Enter the house ID for rent calculation: "))
        
        # Find the house details using Rent.houses
        house = next((house for house in Rent.houses if house['id'] == house_id), None)
        
        if house:
            # For simplicity, let's calculate rent (no advanced payment beyond 1 month as per your requirement)
            print(f"House Location: {house['location']}")
            print(f"Rent for {house['area']} sq.ft: {house['rent']}")
            print("You do not need to pay more than 1 month in advance.")
        else:
            print("House not found.")
