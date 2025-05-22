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
timestamp_start_nine = int(time.mktime(dt_start.timetuple()))
timestamp_end_seven = int(time.mktime(dt_end.timetuple()))


# Set the start time to 09:30 AM
dt_start_thirty = datetime.datetime(today.year, today.month, today.day, 9, 30, 0)
# Set the end time to 19:30 PM
dt_end_thirty = datetime.datetime(today.year, today.month, today.day, 19, 30, 0)
# Convert to Unix timestamp
timestamp_start_ninethirty = int(time.mktime(dt_start_thirty.timetuple()))
timestamp_end_seventhirty = int(time.mktime(dt_end_thirty.timetuple()))


BIBLIO_URL = "https://prenotabiblio.sba.unimi.it/portalePlanningAPI/api/entry/store"
print(f"Sending request to: {BIBLIO_URL}")

payload_fede = {
    "cliente": "biblio",
    "start_time": timestamp_start_nine,
    "end_time": timestamp_end_seven,
    "durata": 36000,
    "entry_type": 50,
    "area": 25,
    "public_primary": "LDZFRC02L45E506X",
    "utente": {
        "codice_fiscale": "LDZFRC02L45E506X",
        "cognome_nome": "Laudizi Federica",
        "email": "federicalaudizi@gmail.com"
    },
    "servizio": {},
    "risorsa": None,
    "recaptchaToken": None,
    "timezone": "Europe/Rome"
}

payload_nico = {
    "cliente": "biblio",
    "start_time": timestamp_start_ninethirty,
    "end_time": timestamp_end_seventhirty,
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

payload_marghe = {
    "cliente": "biblio",
    "start_time": timestamp_start_ninethirty,
    "end_time": timestamp_end_seventhirty,
    "durata": 36000,
    "entry_type": 50,
    "area": 25,
    "public_primary": "MRNMGH02E67F205R",
    "utente": {
        "codice_fiscale": "MRNMGH02E67F205R",
        "cognome_nome": "Marino Margherita",
        "email": "margheritamarino02@gmail.com"
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


payloads = {
    "fede": payload_fede,
    "nico": payload_nico,
    "marghe": payload_marghe
}

responses = {}

for name, payload in payloads.items():
    try:
        response = requests.post(url=BIBLIO_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"Request successful for {name}:")
        print(data)
        
        codice = data.get('codice_prenotazione', "N/A")
        if codice == "N/A":
            print(f"Warning: 'codice_prenotazione' not found in {name}'s response.")
        
        with open(f"codice_{name}.txt", "w") as f:
            f.write(codice)
        
    except requests.RequestException as e:
        print(f"Request failed for {name}: {e}")
        with open(f"codice_{name}.txt", "w") as f:
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
