
# Hotel Management 

This is a simple hotel management system build to manage reservations and room availability for a small hotel. The system interacts with Google Sheets to store and manage reserve data.

## Features

- Add new reservations for hotel rooms
- Check available rooms for specific dates
- Check out guests to show free up rooms
- Store and manage reservation data in Google Sheets

## Installation

1. Clone this repository:
    git clone https://github.com/behzad17/Hotel-22p

2. Installs:
    pip install -r requirements.txt  

3. Fix Google Sheets API credentials by downloading the `credentials.json` file and placing it in the project directory.

4. Run the app:
    python app.py
    

## Deployment on Heroku

1. Install the Heroku CLI:
    using student account
    

2. Login to Heroku:
    heroku login
    

3. Create a new Heroku app:
    heroku create hotel-management
    

4. Push code to Heroku:
    git push heroku main
    

5. My app will be deployed and can be accessed via the Heroku URL.
https://hotel-management-pp2-f96673261aff.herokuapp.com/

