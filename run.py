import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
RWAGASORE_HISTORY_MANAGER = Credentials.from_service_account_file('rwagasore-history-manager.json')
SCOPE_RHM = RWAGASORE_HISTORY_MANAGER.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_RHM)
SHEET = GSPREAD_CLIENT.open ('Rwagasore History Manager')

sheet1 = SHEET.worksheet ('Sheet1')
data = sheet1.get_all_values()
print(data)