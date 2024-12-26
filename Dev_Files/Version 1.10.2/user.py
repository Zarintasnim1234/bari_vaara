# user.py
import csv
import os

class User:
    @staticmethod
    def ensure_csv_exists():
        # Check if the users.csv file exists, if not create it with header
        if not os.path.exists('users.csv'):
            with open('users.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "NID", "Contact", "Email", "Password"])  # Add Password to the header

    @staticmethod
    def register():
        User.ensure_csv_exists()  # Ensure the CSV file exists
        
        print("Registering new user...")
        name = input("Enter your name: ")
        nid = input("Enter your National ID: ")
        contact = input("Enter your contact number: ")
        email = input("Enter your email: ")
        password = input("Set your password: ")  # Prompt for password
        
        # Save user info to CSV
        user_details = [name, nid, contact, email, password]
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_details)
        
        print("Registration successful.")
    
    @staticmethod
    def get_user_by_nid(nid):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[1] == nid:
                    return {'name': row[0], 'id': row[1], 'contact': row[2], 'email': row[3], 'password': row[4]}
        return None
