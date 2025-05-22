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
print(f"Sending request to: {BIBLIO_URL}")

payload = {
    "cliente": "biblio",
    "start_time": 1747940400,
    "end_time": 1747944000,
    "durata": 36000,
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
    headers = {
    "Authorization": "Bearer eyJpdiI6IjlSOWp2S1pRazlaT2FXbTR6ZnhKOVE9PSIsInZhbHVlIjoiM2JnbGpaTUd4RGJIeHB5d1I5N1Y2UT09Ii",
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://prenotabiblio.sba.unimi.it",
    "Referer": "https://prenotabiblio.sba.unimi.it/portalePlanning/biblio/prenota/Riepilogo"
}
    response = requests.post(url=BIBLIO_URL, json=payload, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    print("Request successful!")
    print(response.json())  # Try to print as JSON
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
