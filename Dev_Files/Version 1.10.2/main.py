# main.py
from user import User
from security import Security
from rent import Rent
from finance import Finance
from graph import Graph  # Import Graph class to generate rent graph

def main():
    print("Welcome to the House Rental Application!")
    
    registered = input("Have you registered already? (yes/no): ").strip().lower()
    user = None
    
    if registered == 'yes':
        user = Security.authenticate_user()
    else:
        User.register()
        user = Security.authenticate_user()
    
    if user:
        print(f"Welcome back, {user['name']}!")
        
        while True:
            print("\n1. View Available Houses")
            print("2. Bid for Rent")
            print("3. Calculate Rent Payments")
            print("4. View Rent Graph")  # Added option for graph
            print("5. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                Rent.display_houses()
            elif choice == '2':
                house_id = int(input("Enter the house ID you want to bid for: "))
                house = next((house for house in Rent.houses if house['id'] == house_id), None)
                if house:
                    bid = int(input(f"Enter your bid for the house in {house['location']}: "))
                    print(f"You have successfully placed a bid of {bid} for the house at {house['location']}")
                else:
                    print("House not found.")
            elif choice == '3':
                Finance.calculate_payment(user['id'])
            elif choice == '4':
                Graph.generate_rent_graph()  # Call the function to generate the graph
            elif choice == '5':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Exiting the application.")

if __name__ == "__main__":
    main()
