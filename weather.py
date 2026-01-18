import requests

API_KEY = "9532bb0414aac458f1d992a4d5642b98"  # Replace with your actual API key
CITY = input("Enter City: ")  # Change to any city

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

if "main" in response:
    print(f"Current temperature in {CITY}: {response['main']['temp']}°C")
else:
    print("Error:", response.get("message", "Failed to fetch weather data."))
