import requests
import datetime
import time

# Get today's date
today = datetime.date.today()

# Time setup
def get_unix_timestamp(hour, minute=0):
    dt = datetime.datetime(today.year, today.month, today.day, hour, minute, 0)
    return int(time.mktime(dt.timetuple()))

timestamp_start_nine = get_unix_timestamp(9)
timestamp_end_seven = get_unix_timestamp(19)
timestamp_start_ninethirty = get_unix_timestamp(9, 30)
timestamp_end_seventhirty = get_unix_timestamp(19, 30)

BIBLIO_URL = "https://prenotabiblio.sba.unimi.it/portalePlanningAPI/api/entry/store"
print(f"Sending request to: {BIBLIO_URL}")

# Payloads
payloads = {
    "fede": {
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
    },
    "nico": {
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
    },
    "marghe": {
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
}

headers = {
    "Authorization": "Bearer eyJpdiI6IjlSOWp2S1pRazlaT2FXbTR6ZnhKOVE9PSIsInZhbHVlIjoiM2JnbGpaTUd4RGJIeHB5d1I5N1Y2UT09Ii",
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://prenotabiblio.sba.unimi.it",
    "Referer": "https://prenotabiblio.sba.unimi.it/portalePlanning/biblio/prenota/Riepilogo"
}

MAX_RETRIES = 5
RETRY_DELAY_SECONDS = 8 * 60  # 8 minutes
status = {name: {"success": False, "attempt": 1} for name in payloads}

for attempt in range(1, MAX_RETRIES + 1):
    print(f"\n--- Global Attempt {attempt} of {MAX_RETRIES} ---")
    for name, payload in payloads.items():
        if status[name]["success"]:
            continue  # Skip if already successful

        print(f"[{name}] Attempt {attempt}...")
        try:
            response = requests.post(url=BIBLIO_URL, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            print(f"[{name}] Request successful:")
            print(data)

            codice = data.get('codice_prenotazione', "N/A")
            if codice == "N/A":
                print(f"[{name}] Warning: 'codice_prenotazione' not found.")
            with open(f"codice_{name}.txt", "w") as f:
                f.write(codice)

            status[name]["success"] = True

        except requests.exceptions.RequestException as e:
            print(f"[{name}] Request failed on attempt {attempt}: {e}")

    # If all succeeded, break early
    if all(s["success"] for s in status.values()):
        print("\nAll requests successful.")
        break
    else:
        print(f"\nWaiting {RETRY_DELAY_SECONDS // 60} minutes before next round of retries...")
        time.sleep(RETRY_DELAY_SECONDS)

# Write "N/A" for users who failed all attempts
for name in payloads:
    if not status[name]["success"]:
        print(f"[{name}] All {MAX_RETRIES} attempts failed.")
        with open(f"codice_{name}.txt", "w") as f:
            f.write("N/A")
