import requests
import datetime
import time

# Get today's date
today = datetime.date.today()
# Set the start time to 09:00 AM
dt_start = datetime.datetime(today.year, today.month, today.day, 9, 0, 0)
# Set the end time to 19:00 PM
dt_end = datetime.datetime(today.year, today.month, today.day, 19, 0, 0)
# Convert to Unix timestamp
timestamp_start = int(time.mktime(dt_start.timetuple()))
timestamp_end = int(time.mktime(dt_end.timetuple()))

BIBLIO_URL = "https://prenotabiblio.sba.unimi.it/portalePlanningAPI/api/entry/store"

payload = {
    "cliente": "biblio",
    "start_time": timestamp_start,
    "end_time": timestamp_end,
    "durata": 3600,
    "entry_type": 50,
    "area": 25,
    "public_primary": "LDZFRC02L45E506X",
    "utente": {
        "codice_fiscale": "LDZFRC02L45E506X",
        "cognome_nome": "Federica Laudizi",
        "email": "federicalaudizi@gmail.com"
    },
    "servizio": {},
    "risorsa": None,
    "recaptchaToken": None,
    "timezone": "Europe/Rome"
}

try:
    response = requests.post(url=BIBLIO_URL, json=payload)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    print("Request successful!")
    print(response.json())  # Try to print as JSON
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
