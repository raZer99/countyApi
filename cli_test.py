# Importing the required modules
# requests is used to make HTTP calls
# json is used to format JSON data nicely for debugging (optional)
import requests
import json

# Prompting the user to input latitude and longitude via command line
lat = input("Enter latitude: ")
lon = input("Enter longitude: ")

# Constructing the URL for OpenStreetMap's Nominatim reverse geocoding API
# It returns human-readable address data for given coordinates
url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"

# Nominatim requires a User-Agent to identify who is making the request
headers = {"User-Agent": "county-api-cli/1.0"}

# Sending a GET request to the API and parsing the response as JSON
response = requests.get(url, headers=headers)
data = response.json()

# OPTIONAL DEBUG: Uncomment to see full raw response from the API
# print("\n[DEBUG] Full JSON response:\n")
# print(json.dumps(data, indent=2))

# Safely accessing the 'address' object from the JSON response
address = data.get("address", {})

# Extracting the county (or equivalent field)
# Different countries have different naming conventions, so we use fallback options
county = (
    address.get("county") or              # Used in the US and some other countries
    address.get("state_district") or      # Common in India
    address.get("suburb") or              # Urban fallback
    address.get("city_district") or       # Sometimes found in big cities
    "County not found"                    # Final fallback if none found
)

# Final output shown to the user
print("\n[RESULT]")
print(f"County: {county}")
