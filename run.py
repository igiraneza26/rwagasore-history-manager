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


def add_entry():
    """Prompt for user to enter Category with validation, Name/Title, Date with validation, check if the date is valid by attempting to parse it, exit loop if date is valid, prompt for description"""
    print("You selected: Add Entry\n")
    category = input("Enter Category (Biography, Event, Document): ")
    name = input("Enter Name/Title: ")

    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
    description = input("Enter Description: ")

    sheet1 = SHEET.worksheet("Sheet1")
    new_entry = [category, name, date, description]
    sheet1.append_row(new_entry)
    print("Added successfully!\n")


def search_entry():
    """Prompt user to search by key terms for category, name/title, date or description"""
    print("You selected: Search Entry\n")
    search_term = input(
        "Enter a search term (Category, Name/Title, Date, or Description): "
    )
    sheet1 = SHEET.worksheet("Sheet1")
    records = sheet1.get_all_records()
    matches =[]
    for record in records:
        if (search_term.lower() in str(record['Category']).lower() or
            search_term.lower() in str(record['Name/Title']).lower() or
            search_term.lower() in str(record['Date']).lower() or
            search_term.lower() in str(record['Description']).lower()):
            matches.append(record)

    num_matches = len(matches)
    print(f"\n{num_matches} match(es) found:\n")

    if num_matches > 0:
        for i, match in enumerate(matches, 1):
            print(f"Match {i}:")
            print(f"  Category: {match['Category']}")
            print(f"  Name/Title: {match['Name/Title']}")
            print(f"  Date: {match['Date']}")
            print(f"  Description: {match['Description']}")
            print("-" * 40)
    else:
        print("No matching records found.")


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
    """Run all program functions"""
    while True:
        print("\nWelcome to the Rwagasore History Manager app\n")
        print("Menu:")
        print("1. Add")
        print("2. Search")
        print("3. Edit")
        print("4. View")
        print("5. Delete")
        print("6. Exit\n")

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
                break
            else:
                print("Invalid choice, please select a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the application
if __name__ == "__main__":
    main()
