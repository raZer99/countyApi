# 🌍 County Lookup API

A simple FastAPI-based microservice that returns the **county** (or an equivalent administrative region) from given **latitude** and **longitude** coordinates using **OpenStreetMap's Nominatim reverse geocoding API**.

---

## 🚀 Features

- 🌐 Reverse geocoding using OpenStreetMap
- 📍 Input: Latitude & Longitude
- 🏛️ Output: County or similar regional unit
- ⚡ Built with FastAPI for high performance
- 🔎 Interactive Swagger UI for testing

---

## 📸 Demo

Try it live on Swagger UI:  
https://59b56171d799.ngrok-free.app/docs

Or call the endpoint directly:  
https://59b56171d799.ngrok-free.app/get-county?lat=34.0522&lon=-118.2437

---

## 📦 Tech Stack

- FastAPI
- OpenStreetMap Nominatim API
- requests

---

## 🛠️ How It Works

1. Send latitude and longitude to `/get-county` as query parameters.
2. The API calls OpenStreetMap’s reverse geocoding endpoint.
3. It extracts the relevant county/region from the response.
4. Returns a clean JSON response.

---

## 🧪 Sample Response

`GET /get-county?lat=34.0522&lon=-118.2437`

```json
{
  "latitude": 34.0522,
  "longitude": -118.2437,
  "county": "Los Angeles County"
}
