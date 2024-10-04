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
    """
    Prompt for user to enter new data:
    Category with validation,
    Name/Title,
    Date with validation and
    Description
    """
    print("You selected: Add Entry\n")
    category = input("Enter Category (Biography, Event, Document): ")
    name = input("Enter Name/Title: ")
    # Prompt for Date with validation
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
    description = input("Enter Description: ")

    sheet1 = SHEET.worksheet("Sheet1")
    # Add the entry to the Google Sheet
    new_entry = [category, name, date, description]
    sheet1.append_row(new_entry)
    print("Added successfully!\n")


def search_entry():
    """Prompt user to search by key terms for category, name/title, date or description"""
    print("You selected: Search Entry\n")
    # Prompt user to enter a search term
    search_term = input(
        "Enter a search term (Category, Name/Title, Date, or Description): "
    )
    sheet1 = SHEET.worksheet("Sheet1")
    records = sheet1.get_all_records()
    matches = []  # Initialize a list to store matches
    # Iterate through the records to search for the term in any column
    for record in records:
        if (
            search_term.lower() in str(record["Category"]).lower()
            or search_term.lower() in str(record["Name/Title"]).lower()
            or search_term.lower() in str(record["Date"]).lower()
            or search_term.lower() in str(record["Description"]).lower()
        ):
            matches.append(record)
    # Display the number of matches found
    num_matches = len(matches)
    print(f"\n{num_matches} match(es) found:\n")
    # If matches are found, display them in a readable format
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
    """
    User searches for an entry to edit by providing key term, display matches.
    User selects entry to edit from matches.
    Prompt to choose field (Category, Name/Title, Date, or Description) to edit.
    User enter new value and sheeet updated accordingly.
    """
    print("You selected: Edit Entry\n")
    # Prompt user to enter a search term to find the entry they want to edit
    search_term = input(
        "Enter a search term to find the entry (Category, Name/Title, Date, or Description): "
    )
    sheet1 = SHEET.worksheet("Sheet1")
    records = sheet1.get_all_records()
    matches = []  # Initialize a list to store matches
    # Iterate through the records to search for the term in any column
    for index, record in enumerate(
        records, start=2
    ):  # Start at 2 because Google Sheets are 1-indexed, and row 1 is header
        if (
            search_term.lower() in str(record["Category"]).lower()
            or search_term.lower() in str(record["Name/Title"]).lower()
            or search_term.lower() in str(record["Date"]).lower()
            or search_term.lower() in str(record["Description"]).lower()
        ):
            matches.append((index, record))  # Store both the row index and the record

    # Display the number of matches found
    num_matches = len(matches)
    print(f"\n{num_matches} match(es) found:\n")

    if num_matches > 0:
        for i, (index, match) in enumerate(matches, 1):
            print(f"Match {i}:")
            print(f"  Row: {index}")
            print(f"  Category: {match['Category']}")
            print(f"  Name/Title: {match['Name/Title']}")
            print(f"  Date: {match['Date']}")
            print(f"  Description: {match['Description']}")
            print("-" * 40)

        while True:
            try:
                selection = int(
                    input(
                        f"Enter the number of the match you want to edit (1-{num_matches}): "
                    )
                )
                if 1 <= selection <= num_matches:
                    break
                else:
                    print(
                        f"Invalid selection. Please enter a number between 1 and {num_matches}."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        selected_row, selected_record = matches[selection - 1]

        # Display options for which field to edit
        print("\nWhich field would you like to edit?")
        print("1. Category")
        print("2. Name/Title")
        print("3. Date")
        print("4. Description")

        # Prompt user for which field to edit
        while True:
            try:
                field_selection = int(
                    input(
                        "Enter the number corresponding to the field you want to edit: "
                    )
                )
                if 1 <= field_selection <= 4:
                    break
                else:
                    print("Invalid selection. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Map the selection to the corresponding field
        fields = ["Category", "Name/Title", "Date", "Description"]
        selected_field = fields[field_selection - 1]

        # Prompt for the new value
        new_value = input(f"Enter new value for {selected_field}: ")

        # If the user is editing the Date, validate the new date format
        if selected_field == "Date":
            while True:
                try:
                    datetime.strptime(new_value, "%Y-%m-%d")
                    break
                except ValueError:
                    new_value = input(
                        "Invalid date format. Please use YYYY-MM-DD format: "
                    )

        # Update the Google Sheet with the new value
        sheet1.update_cell(selected_row, field_selection, new_value)

        print(f"\n{selected_field} updated successfully.")
    else:
        print("No matching records found.")


def view_entry():
    """
    User provides a search term and app displays all matching entries.
    Option to view all entries.
    Results displayed in a user-friendly way.
    """
    print("You selected: View Entry\n")
    # Ask if the user wants to view all entries or search
    view_all = input("Do you want to view all entries? (yes/no): ").lower()
    sheet1 = SHEET.worksheet("Sheet1")
    records = sheet1.get_all_records()
    matches = []  # To store either all records or matching records
    # If user chooses to view all entries
    if view_all == "yes":
        matches = records
    else:
        # Prompt user to enter a search term
        search_term = input(
            "Enter a search term (Category, Name/Title, Date, or Description): "
        )

        # Iterate through the records to search for the term in any column
        for record in records:
            if (
                search_term.lower() in str(record["Category"]).lower()
                or search_term.lower() in str(record["Name/Title"]).lower()
                or search_term.lower() in str(record["Date"]).lower()
                or search_term.lower() in str(record["Description"]).lower()
            ):
                matches.append(record)

    # Display the number of matches found
    num_matches = len(matches)
    if num_matches > 0:
        print(f"\n{num_matches} entry(ies) found:\n")
        # Display the records in a readable format
        for i, match in enumerate(matches, 1):
            print(f"Entry {i}:")
            print(f"  Category: {match['Category']}")
            print(f"  Name/Title: {match['Name/Title']}")
            print(f"  Date: {match['Date']}")
            print(f"  Description: {match['Description']}")
            print("-" * 40)
    else:
        print("No matching entries found.")


def delete_entry():
    """
    User provides a search term and app retrieves all macthes.
    Function displays all matches with all fields (category, name, date and description).
    Uer chooses which entry to delete from matches.
    Confirmation request from user before proceeding with deletion.
    Delete once confirmed.
    """
    print("You selected: Delete Entry\n")
    # Prompt user to enter a search term to find the entry they want to delete
    search_term = input(
        "Enter a search term to find the entry (Category, Name/Title, Date, or Description): "
    )
    sheet1 = SHEET.worksheet("Sheet1")
    records = sheet1.get_all_records()
    matches = []  # Initialize a list of store matches.
    # Iterate through the records to search for the term in any column
    for index, record in enumerate(
        records, start=2
    ):  # Start at 2 because Google Sheets are 1-indexed, and row 1 is header
        if (
            search_term.lower() in str(record["Category"]).lower()
            or search_term.lower() in str(record["Name/Title"]).lower()
            or search_term.lower() in str(record["Date"]).lower()
            or search_term.lower() in str(record["Description"]).lower()
        ):
            matches.append((index, record))  # Store both the row index and the record

    # Display the number of matches found
    num_matches = len(matches)
    if num_matches > 0:
        print(f"\n{num_matches} match(es) found:\n")
        # Display the records in a readable format
        for i, (index, match) in enumerate(matches, 1):
            print(f"Match {i}:")
            print(f"  Row: {index}")
            print(f"  Category: {match['Category']}")
            print(f"  Name/Title: {match['Name/Title']}")
            print(f"  Date: {match['Date']}")
            print(f"  Description: {match['Description']}")
            print("-" * 40)

        # Prompt user to select which entry to delete
        while True:
            try:
                selection = int(
                    input(
                        f"Enter the number of the match you want to delete (1-{num_matches}): "
                    )
                )
                if 1 <= selection <= num_matches:
                    break
                else:
                    print(
                        f"Invalid selection. Please enter a number between 1 and {num_matches}."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Get the selected record and row index
        selected_row, selected_record = matches[selection - 1]

        # Confirm deletion
        confirmation = input(
            f"Are you sure you want to delete the entry '{selected_record['Name/Title']}'? (yes/no): "
        ).lower()
        if confirmation == "yes":
            # Delete the selected row
            sheet1.delete_rows(selected_row)
            print(f"\nEntry '{selected_record['Name/Title']}' deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("No matching records found.")


def main():
    """Run all program functions"""
    while True:
        print("\nWelcome to the Rwagasore History Manager app\n")
        print("You can perform the following operations on the data/entries:")
        print("1. Add")
        print("2. Search")
        print("3. Edit")
        print("4. View")
        print("5. Delete")
        print("6. Exit\n")

        try:
            choice = int(
                input("Please enter the number corresponding to your operation: ")
            )
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
