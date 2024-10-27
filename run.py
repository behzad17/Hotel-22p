import gspread
from google.oauth2.service_account import Credentials
import datetime

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
        self.rooms = [f"Room {i}" for i in range(1, 21)] #hotel have 20 Rooms
        self.reservations = {} #self reservation
        self.get_reservations_from_sheet()
    


    def get_reservations_from_sheet(self):
        worksheet = SHEET.worksheet("rooms")  
        records = worksheet.get_all_records()  
        self.reservations = {
            record["Room"].replace(" ", ""): {
            "name": record["Name"].strip(),
            "check_in": record["Check-in "].strip(), 
            "check_out": record["Check-out"].strip()
            }   
            for record in records if record["Name"]
            }

    
    def display_rooms(self):
        print("Available rooms in the hotel:")
        for room in self.rooms:
            print(room)



    #function to available rooms
    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if room not in self.reservations]
        if available_rooms:
            print("Available rooms:")
            for room in available_rooms:
                print(room)
        else:
            print("No rooms available")   


    #make_reservation
    def make_reservation(self, name, room, check_in, check_out):
        if room in self.rooms and room not in self.reservations:
            self.reservations[room] = {"name": name, "check_in": check_in, "check_out": check_out}
            worksheet = SHEET.worksheet("rooms")
            worksheet.append_row([name, room, str(check_in), str(check_out)])
            print(f"Room {room} reserved for {name} from {check_in} to {check_out}")
        else:
            print(f"Room {room} is not available")
        self.get_reservations_from_sheet()


    def check_out_guest(self, room):
        if room in self.reservations:
            del self.reservations[room]    
            print(f"Guest ckecked out from {room}")
        else:
            print(f"Room {room} is not currently reserved")

    def update_rooms_worksheet(self, data):
        """
        Update rooms worksheet, add new row with the list data provided
        """
        print("Updating rooms worksheet...\n")
        rooms_worksheet = SHEET.worksheet("rooms")
        rooms_worksheet.append_row(data)
        print("Rooms worksheet updated successfully.\n")



rooms = SHEET.worksheet("rooms")    
data = rooms.get_all_values()
print(data)


if __name__ == "__main__":
            
    hotel = HotelManagement()
    check_in = datetime.date(2024, 10, 26)
    check_out = datetime.date(2024, 10, 30)
    hotel.display_available_rooms() 
    hotel.make_reservation("Behzad Javadian", "Room1", check_in, check_out)
    hotel.display_available_rooms()
    hotel.check_out_guest("Room1")
    hotel.display_available_rooms() 