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

payload_fede = {
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

payload_nico = {
    "cliente": "biblio",
    "start_time": 1747940400,
    "end_time": 1747944000,
    "durata": 36000,
    "entry_type": 50,
    "area": 25,
    "public_primary": "BMBNLR01E06B354Q",
    "utente": {
        "codice_fiscale": "BMBNLR01E06B354Q",
        "cognome_nome": "Abimbola Nicola Oriola",
        "email": "nicolaabimbola@gmail.com"
    },
    "servizio": {},
    "risorsa": None,
    "recaptchaToken": None,
    "timezone": "Europe/Rome"
}

headers = {
    "Authorization": "Bearer eyJpdiI6IjlSOWp2S1pRazlaT2FXbTR6ZnhKOVE9PSIsInZhbHVlIjoiM2JnbGpaTUd4RGJIeHB5d1I5N1Y2UT09Ii",
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://prenotabiblio.sba.unimi.it",
    "Referer": "https://prenotabiblio.sba.unimi.it/portalePlanning/biblio/prenota/Riepilogo"
}

try:
    response_fede = requests.post(url=BIBLIO_URL, json=payload_fede, headers=headers)
    response_nico = requests.post(url=BIBLIO_URL, json=payload_nico, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    data_fede = response_fede.json()
    data_nico = response_nico.json()
    print("Request successful!")
    print(response.json())  # Try to print as JSON

    codice_fede = data_fede.get('codice_prenotazione')
    codice_nico = data_nico.get('codice_prenotazione')
    if codice_fede:
        with open("codice_fede.txt", "w") as f:
            f.write(codice_fede)
    else:
        print("Warning: 'codice_prenotazione' not found in response.")
        with open("codice_fede.txt", "w") as f:
            f.write("N/A")
   
    if codice_nico:
        with open("codice_nico.txt", "w") as f:
            f.write(codice_nico)
    else:
        print("Warning: 'codice_prenotazione' not found in response.")
        with open("codice_nico.txt", "w") as f:
            f.write("N/A")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
