# Importing FastAPI and Query module from the fastapi library
# FastAPI helps us build APIs quickly and validate parameters
from fastapi import FastAPI, Query

# The requests module allows making HTTP requests (used for Nominatim reverse geocoding)
import requests

# Optional is used to make lat/lon query parameters optional in the root endpoint
from typing import Optional

# Creating a FastAPI app instance
# This object handles route registration, metadata, and startup config
app = FastAPI(
    title="County Lookup API",
    description="Returns the county (or equivalent regional unit) from a given latitude and longitude using OpenStreetMap's Nominatim service.",
    version="1.0"
)

# ------------------------------
# Root endpoint
# Supports optional lat/lon parameters for direct usage in URL like:
# https://your-ngrok-url/?lat=34.0522&lon=-118.2437
# ------------------------------
@app.get("/")
def root(
    lat: Optional[float] = Query(None, description="Latitude value (e.g., 34.0522)"),
    lon: Optional[float] = Query(None, description="Longitude value (e.g., -118.2437)")
):
    # If no coordinates are passed, return a welcome/help message
    if lat is None or lon is None:
        return {
            "message": "🎯 County Lookup API is up and running! Pass ?lat=&lon= in the URL to get results, or use /get-county for structured API access."
        }

    # Reverse geocoding via Nominatim (OpenStreetMap)
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {"User-Agent": "county-api-fastapi/1.0"}  # Nominatim requires this

    response = requests.get(url, headers=headers)
    data = response.json()
    address = data.get("address", {})

    # Extract the best available 'county-like' field
    county = (
        address.get("county") or
        address.get("state_district") or
        address.get("suburb") or
        address.get("city_district") or
        "County not found"
    )

    # Return structured JSON response
    return {
        "latitude": lat,
        "longitude": lon,
        "county": county
    }


# ------------------------------
# Structured API endpoint: /get-county
# This route is listed in Swagger docs for API tools, client-side apps, etc.
# ------------------------------
@app.get("/get-county")
def get_county(
    lat: float = Query(..., description="Latitude value (e.g., 34.0522)"),
    lon: float = Query(..., description="Longitude value (e.g., -118.2437)")
):
    """
    This endpoint accepts latitude and longitude as query parameters,
    uses OpenStreetMap's reverse geocoding API (Nominatim),
    and returns the most appropriate county-like administrative unit.
    """

    # Nominatim reverse geocoding URL
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {"User-Agent": "county-api-fastapi/1.0"}

    # Call the external API
    response = requests.get(url, headers=headers)
    data = response.json()
    address = data.get("address", {})

    # Fallback options for extracting something county-like
    county = (
        address.get("county") or
        address.get("state_district") or
        address.get("suburb") or
        address.get("city_district") or
        "County not found"
    )

    return {
        "latitude": lat,
        "longitude": lon,
        "county": county
    }
