import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hotel-management')

#class and rooms list to hotel management
class HotelManagement:
def __init__(self):
    self.rooms = [f"Room{i}" for i in range(1, 21)] #hotel have 20 Rooms

def display_rooms(self):
        print("Available rooms in the hotel:")
    for room in self.room:
        print(room)   