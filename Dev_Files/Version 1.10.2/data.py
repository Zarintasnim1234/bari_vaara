# data.py
import csv

class Data:
    @staticmethod
    def save_user_details(user_details):
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_details)
    
    @staticmethod
    def read_user_details():
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
