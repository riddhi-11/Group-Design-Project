import json

def access_user_details():
    try:
        with open("user_details.json", "r") as user_details_file:
            user_details = json.load(user_details_file)

        print("User Details:")
        for user_id, details in user_details.items():
            print(f"User ID: {user_id}")
            print(f"Name: {details['name']}")
            print(f"Pronouns: {details['pronouns']}")
            print(f"Country: {details['country']}")
            print(f"Interests: {details['interests']}")
            print(f"Looking for: {details['looking_for']}")
            print("\n")

    except FileNotFoundError:
        print("user_details.json not found.")

def access_login_credentials():
    try:
        with open("login_credentials.json", "r") as login_credentials_file:
            login_credentials = json.load(login_credentials_file)

        print("Login Credentials:")
        for user_id, password in login_credentials.items():
            print(f"User ID: {user_id}")
            print(f"Password: {password}")
            print("\n")

    except FileNotFoundError:
        print("login_credentials.json not found.")

if __name__ == "__main__":
    access_user_details()
    access_login_credentials()
