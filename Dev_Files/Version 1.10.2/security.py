# security.py
from user import User

class Security:
    @staticmethod
    def authenticate_user():
        nid = input("Enter your National ID: ")
        user = User.get_user_by_nid(nid)
        
        if user:
            print("Enter your password: ")
            password = input()
            # Check if the entered password matches the stored password
            if password == user['password']:
                return user
        print("Authentication failed.")
        return None
