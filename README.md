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
(ngrok link changes on restart – see below for instructions)  
Example: `https://<your-ngrok-subdomain>.ngrok-free.app/docs`

Or call the endpoint directly:  
Example: `https://<your-ngrok-subdomain>.ngrok-free.app/get-county?lat=34.0522&lon=-118.2437`

---

## 📡 Deploy via ngrok (for sharing your API publicly)

1. **Install ngrok** if not already installed:  
   [https://ngrok.com/download](https://ngrok.com/download)

2. **Start your FastAPI server locally**:

   ```bash
   uvicorn main:app --reload
   ```

   By default, it runs at: `http://127.0.0.1:8000`

3. **Expose your API using ngrok**:

   ```bash
   ngrok http 8000
   ```

   You'll get a forwarding URL like:  
   `Forwarding https://59b56171d799.ngrok-free.app -> http://localhost:8000`

4. **Access your API via**:

   - Swagger UI: `https://59b56171d799.ngrok-free.app/docs`
   - Direct endpoint: `https://59b56171d799.ngrok-free.app/get-county?lat=34.0522&lon=-118.2437`

> 🔁 **Note**: Restarting ngrok will change the URL unless using a reserved domain (requires ngrok Pro plan).

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenStreetMap Nominatim API](https://nominatim.openstreetmap.org/)
- [requests](https://docs.python-requests.org/)

---

## 🛠️ How It Works

1. Send latitude and longitude to `/get-county` as query parameters.
2. The API makes a call to OpenStreetMap’s reverse geocoding service.
3. It extracts the county (or similar regional field) from the JSON response.
4. Returns a clean JSON object with the input and the result.

---

## 🧪 Sample Response

**Request:**

```
GET /get-county?lat=34.0522&lon=-118.2437
```

**Response:**

```json
{
  "latitude": 34.0522,
  "longitude": -118.2437,
  "county": "Los Angeles County"
}
```

---

## 🔧 Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/raZer99/countyApi.git
cd countyApi
```

### 2. (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install fastapi uvicorn requests
pip freeze > requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

Visit Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔗 API Endpoints

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| GET    | `/`           | Health check                         |
| GET    | `/get-county` | Get county from lat/lon coordinates  |

### `/get-county` Parameters

| Parameter | Type  | Required | Example    |
|-----------|-------|----------|------------|
| `lat`     | float | ✅       | `34.0522`  |
| `lon`     | float | ✅       | `-118.2437`|

---

## 📤 Deployment Options

- ✅ ngrok (for development/testing)
- 🚀 Render
- 🌐 Railway
- ☁️ Deta Space
- 🛫 Fly.io
- 🐳 Docker + AWS/GCP/Azure

---

## 📄 License

Licensed under the MIT License. See `LICENSE` for details.

---

## 🙌 Acknowledgements

- [OpenStreetMap / Nominatim](https://nominatim.openstreetmap.org/)
- [FastAPI](https://fastapi.tiangolo.com/) by Sebastián Ramírez

---

## 👨‍💻 Author

**Md Sameer**  
GitHub: [@raZer99](https://github.com/raZer99)
