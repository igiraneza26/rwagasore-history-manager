# Rwagasore History Manager

### A Command-Line Application to Manage Historical Data on Prince Louis Rwagasore and Burundian Independence

---

## Purpose

The **Rwagasore History Manager** is a command-line application designed to help users manage, search, and update a dataset centered around historical figures, events, and documents related to Prince Louis Rwagasore and Burundi's path to independence. It allows users to interact with a structured dataset by adding, editing, searching, viewing, and deleting entries within a Google Sheet, making it a valuable tool for historians, students, researchers, or anyone interested in African history, particularly Burundian history.

## Value to Users

This application provides several key benefits to its users:

### 1. **Streamlined Historical Data Management**:
   - The application makes it easy for users to store, manage, and interact with historical data related to Prince Louis Rwagasore and key events in Burundian history. Users can effortlessly add new biographical data, important events, and documents to an existing dataset without needing to manually manage a spreadsheet.

### 2. **Efficient Search and View Capabilities**:
   - Users can search through historical records using any keyword, including names, dates, and descriptions. This feature ensures that users can quickly find relevant data, which can be particularly useful for research, presentations, and educational purposes.

### 3. **Data Editing and Deletion**:
   - The app provides users with full control over the data by allowing them to edit and update existing records as well as delete outdated or incorrect entries. This flexibility ensures that the dataset remains accurate and up-to-date.

### 4. **Simple Yet Powerful Interface**:
   - Even though it is a command-line tool, the Rwagasore History Manager is designed with ease of use in mind. With a clear, straightforward menu, users can quickly navigate through different options and perform operations efficiently.

### 5. **Organized Data Structure**:
   - The dataset is well-structured, with categories such as **Biography**, **Event**, and **Document**. Each entry contains fields like **Name/Title**, **Date**, and **Description**, making it easy to classify and reference historical information.

---

## Features

1. **Add New Entries**:
   - Add new biographies, events, or documents with details such as name/title, date, and description to the Google Sheet.

2. **Search for Entries**:
   - Search the dataset using any keyword. The search spans across all fields, including category, name/title, date, and description. All matches are displayed in a user-friendly format.

3. **View Entries**:
   - Users can either view all entries in the dataset or search for specific entries using a keyword. Results are displayed in an easily readable format.

4. **Edit Existing Entries**:
   - Users can search for an entry to edit, select the field they want to update (category, name/title, date, or description), and modify the data in the Google Sheet.

5. **Delete Entries**:
   - Users can search for an entry to delete and confirm before the entry is removed from the Google Sheet.

---

## Getting Started

### Prerequisites:
1. **Python 3.x** installed on your machine.
2. **Google Sheets API** setup (service account and credentials file).
   - Follow the steps in the [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python) to set up a service account and download the credentials JSON file.
3. **Required Libraries**:
   - Install the following Python libraries using pip:
     pip install gspread google sheets

### Installation

1. **Clone the repository**:
   git clone <https://github.com/igiraneza26/rwagasore-history-manager.git>
   cd rwagasore-history-manager

2. **Set up Google Sheets credentials**:
   - Place the `creds.json` file (downloaded from Google Cloud Console) in the root of the project.

3. **Run the application**:
   python rwagasore_history_manager.py

### Usage

When you run the application, you will be presented with the following menu:

```
Welcome to the Rwagasore History Manager app

Menu:
1. Add
2. Search
3. Edit
4. View
5. Delete
6. Exit
```

- **Option 1: Add** – Add a new entry to the dataset.
- **Option 2: Search** – Search for a specific entry by entering a keyword.
- **Option 3: Edit** – Find an entry to update or modify its data.
- **Option 4: View** – View all entries or search for specific entries.
- **Option 5: Delete** – Remove an entry from the dataset.
- **Option 6: Exit** – Quit the application.
![alt text](/images/landing.png)
![alt text](/images/image-1.png)

### Notes:
- All data is stored in a connected Google Sheet, which must be shared with the service account you create during setup.
- Ensure that your Google Sheet contains the following columns: **Category**, **Name/Title**, **Date**, and **Description**.