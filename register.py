# register_user.py
from db import create_connection
from mysql.connector import Error

def create_table():
    """Create the users table if it does not exist."""
    connection = create_connection()
    if connection:
        try:

            print("Users table created or already exists.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
          
            connection.close()

def register_user():
    """Register a new user based on user input."""
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    role = input("Enter the role (e.g., user, admin): ")

    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Insert user details
            insert_user_query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s);
            """
            hashed_password = password  # For simplicity; hash it in production
            cursor.execute(insert_user_query, (username, hashed_password, role))
            connection.commit()
            print(f"User '{username}' registered successfully.")
        except Error as e:
            print(f"Error registering user: {e}")
        finally:
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    create_table()
    register_user()
