# rent.py

class Rent:
    houses = [
        {"id": 1, "location": "Downtown", "area": 500, "rent": 1000},
        {"id": 2, "location": "Suburbs", "area": 800, "rent": 1200},
        {"id": 3, "location": "City Center", "area": 600, "rent": 1500}
    ]
    
    @staticmethod
    def display_houses():
        print("Available Houses for Rent:")
        for house in Rent.houses:
            print(f"ID: {house['id']}, Location: {house['location']}, Area: {house['area']} sq.ft, Rent: {house['rent']}")
