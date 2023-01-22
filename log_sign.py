import sqlite3
from flask import Flask,jsonify

app = Flask(__name__)

def signup():
  # Get user information
  username = input("Enter a username: ")
  password = input("Enter a password: ")
  
  # Connect to the database
  conn = sqlite3.connect('users.db')
  c = conn.cursor()
  
  # Create the table if it does not exist
  c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
  
  # Insert the new user into the table
  c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
  
  # Save and close the connection
  conn.commit()
  conn.close()
  print("Signup Successful!")

def login():
  # Get the user's login information
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  
  # Connect to the database
  conn = sqlite3.connect('users.db')
  c = conn.cursor()
  
  # Check if the username and password match a user in the database
  c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
  if c.fetchone() is not None:
    print("Login Successful!")
  else:
    print("Incorrect username or password.")
    
  # Close the connection
  conn.close()

login()
