import os
from groq import Groq
from dotenv import load_dotenv
import logging
import pandas as pd
import numpy as np
import re

# Load values from the .env file
load_dotenv()

# Pull the Groq API key from the environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Set up logging so we can keep track of all chats in a log file
logging.basicConfig(
    filename="livehealthy_support_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

'''
Since this is a customer support assistant, I will assume a generic company called LiveHealthy.
This company sells healthy, nutritious and affordable food items.
Their main customers are people that  are intentional about what they eat.
'''


products=pd.read_csv("livehealthy_products.csv")
sales = pd.read_csv("livehealthy_sales_data.csv")

# Convert product info to readable text
product_info = products.to_string(index=False)

# Convert sales info to readable text
#sales_info = sales.to_string(index=False)  

# Show a personalized welcome message for our company
print("Dear Khadijah,\nWelcome to the LiveHealthy Customer Support Assistant.")

# These are the menu options the user can choose from
menu_options = {
    "1": "Complaints",
    "2": "Inquiries",
    "3": "Feedback",
}

# Set up the Groq chat client using your API key
client = Groq(api_key=GROQ_API_KEY)

# Keep asking until the user picks a valid menu option
def get_valid_option():
    while True:
        print("\nPlease select the corresponding option:")
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        choice = input("Your choice ('Exit' to quit): ").strip()

        # Quit the program if the user types 'exit'
        if choice.lower() == 'exit':
            exit()

        # If the input is valid (1, 2, or 3), return the corresponding value
        elif choice in menu_options:
            return menu_options[choice]

        # Handle anything else as invalid
        else:
            print("Invalid choice. Please enter 1, 2, or 3. or 'Exit'")

def get_order_details(order_id):
    order = sales[sales['Order ID'] == order_id]
    if not order.empty:
        return order.to_string(index=False)
    else:
        return "Sorry, no order found with that ID."

# This function sends a message to Groq and returns the assistant’s reply
def get_response(user_message, query_type): # Check if user_message contains something like 'ORD0001'
    match = re.search(r'\bORD\d{4}\b', user_message)
    if match:
        order_id = match.group()
        sales_info = get_order_details(order_id)
    else:
        sales_info = "No specific order ID detected in the query."

    # Tell the model what kind of role it’s playing (customer support)
    system_message = (
        f"You are a professional support agent for an online store that sells healthy food. "
        f"The user has selected '{query_type}'. The products we sell and their prices are in {product_info}. You can get sales information from {sales_info}. Respond accordingly, being clear, polite, and concise."
    )

    # Make a chat completion request with user + system messages
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
    )

    # Return only the model’s reply text
    return completion.choices[0].message.content


# This is the main loop of the program – keeps the support session running
while True:
    # Ask what the user's message is about (complaint, inquiry, etc.)
    query_type = get_valid_option()

    # Keep handling messages within that category
    while True:
        user_query = input(f"\nHow can I help with your {query_type.lower()}? (type 'menu' to go back, 'exit' to quit): ").strip()

        # If the user wants to quit
        if user_query.lower() == "exit":
            print("Thank you for contacting LiveHealthy Support. Have a nice day")
            exit()

        # If the user wants to go back to the main menu
        elif user_query.lower() == "menu":
            break  

        # If the user submits a real question
        else: 
            # Get and show the response from Groq
            response = get_response(user_query, query_type)
            print(f"\n🟢 LiveHealthy Support ({query_type}):\n{response}")

            # Log this exchange
            logging.info(f"Type: {query_type} | User: {user_query} | Response: {response}")

            # Ask if the user wants to give more info or continue
            while True:
                follow_up = input("\nDo you want to provide more information? (yes/no): ").strip().lower()

                if follow_up == "yes":
                    info = input("Please provide more info (or type 'menu' to go back, 'exit' to quit): ").strip()

                    if info.lower() == "exit":
                        print("Thank you for contacting LiveHealthy Support. Have a nice day")
                        exit()

                    elif info.lower() == "menu":
                        break

                    # Get another response using the extra info
                    else:
                        response = get_response(info, query_type)
                        print(f"\n🟢 LiveHealthy Support ({query_type}):\n{response}")
                        logging.info(f"Follow-up | User: {info} | Response: {response}")

                elif follow_up == "no":
                    # Exit the follow-up loop and go back to new questions
                    break

                else:
                    print("Please enter 'yes' or 'no'.")
                    


