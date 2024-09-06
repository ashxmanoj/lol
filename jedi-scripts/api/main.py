# API - Application Programming Interface
# An API is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system.

"""
Using the rules that an API has, we make a request to the external system for some piece of data.
The external system responds and sends the data as we follow the rules prescribed by them.
"""
# Analogy: Kitchen is the external system/or data in it, menu is the API

# JSON (JavaScript Object Notation) is a lightweight data interchange format
# It's similar to Python dictionaries but with less whitespace and different syntax
# Analogy: JSON is like compressed furniture from IKEA - compact and efficient

# Example of making an API request using the requests library
import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")  # Fetches data from the API endpoint
# print(response)  # Prints a response object
# print(response.status_code)  # Prints the HTTP status code
# response.raise_for_status()  # Raises an exception for unsuccessful status codes
# data = response.json()  # Parses the JSON response into a Python dictionary
# print(data)

# HTTP Response Codes
# 1xx : Informational - Request received, continuing process
# 2xx : Success - The action was successfully received, understood, and accepted
# 3xx : Redirection - Further action needs to be taken in order to complete the request
# 4xx : Client Error - The request contains bad syntax or cannot be fulfilled
# 5xx : Server Error - The server failed to fulfill an apparently valid request

# More detailed explanation of common status codes:
# 200 : OK - Standard response for successful HTTP requests
# 201 : Created - Request has been fulfilled, resulting in the creation of a new resource
# 204 : No Content - Server successfully processed the request but is not returning any content
# 400 : Bad Request - Server cannot or will not process the request due to an apparent client error
# 401 : Unauthorized - Authentication is required and has failed or has not been provided
# 403 : Forbidden - Request was valid, but the server is refusing action
# 404 : Not Found - Requested resource could not be found
# 500 : Internal Server Error - Generic error message when server encounters an unexpected condition

# API Endpoints
# An endpoint is a specific URL where an API can be accessed. It's like an address for the API.

# API Parameters
#  allow you to send additional data with your request to customize the response.
# They can be part of the URL (query parameters) or sent in the request body.

# Example of an API request with parameters:
# response = requests.get(url="https://api.example.com/data", params={"key1": "value1", "key2": "value2"})

# API Authentication
# Many APIs require authentication to ensure that only authorized users can access the data.
# Common methods include API keys, OAuth, and JWT (JSON Web Tokens).

# from tkinter import *
# import requests
#
# def get_quote():
# 	global quote_text
# 	response = requests.get(url="https://api.kanye.rest")
# 	data = response.json()
# 	canvas.itemconfig(quote_text, text=data["quote"])
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
# 								fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
# window.mainloop()

