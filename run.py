# Rwagasore History Manager

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
RWAGASORE_HISTORY_MANAGER = Credentials.from_service_account_file(
    "rwagasore-history-manager.json"
)
SCOPE_RHM = RWAGASORE_HISTORY_MANAGER.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_RHM)
SHEET = GSPREAD_CLIENT.open("Rwagasore History Manager")

from datetime import datetime


# Functions for each operation
def add_entry():
    """
    Prompt for Name, Date of Birth with validation, check if the date is valid by attempting to parse it, exit loop if date is valid, prompt for Political Affiliations and description
    """
    print("You selected: Add Entry\n")
    name = input("Enter Name: ")

    while True:
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
    political_affiliations = input("Enter Political Affiliations: ")
    description = input("Enter Description: ")

    # Simulate adding the entry (this is where I could add logic to save the data)
    sheet1 = SHEET.worksheet('Sheet1')
    new_entry = [name, dob, political_affiliations, description]
    sheet1.append_row(new_entry)
    # For now, we just display the confirmation message
    print("Added successfully!\n")


def search_entry():
    print("You selected: Search Entry\n")
    # Add logic for searching an entry here


def edit_entry():
    print("You selected: Edit Entry\n")
    # Add logic for editing an entry here


def view_entry():
    print("You selected: View Entry\n")
    # Add logic for viewing an entry here


def delete_entry():
    print("You selected: Delete Entry\n")
    # Add logic for deleting an entry here


def main():
    while True:
        # Display the welcome message and menu
        print("\nWelcome to the Rwagasore History Manager app\n")
        print("Menu:")
        print("1. Add")
        print("2. Search")
        print("3. Edit")
        print("4. View")
        print("5. Delete")
        print("6. Exit\n")

        # Get user input for the operation
        try:
            choice = int(input("Please enter your operation number from the menu: "))
            if choice == 1:
                add_entry()
            elif choice == 2:
                search_entry()
            elif choice == 3:
                edit_entry()
            elif choice == 4:
                view_entry()
            elif choice == 5:
                delete_entry()
            elif choice == 6:
                print("Exiting the RHM application. Goodbye!")
                break  # Exit the loop and terminate the program
            else:
                print("Invalid choice, please select a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the application
if __name__ == "__main__":
    main()
