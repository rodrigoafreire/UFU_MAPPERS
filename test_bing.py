import http.client
import json
import urllib.parse

# Replace 'YOUR_API_KEY' with your actual Bing Maps API key
api_key = 'z3nOPxYlgmXG24uetrkapw1NPvqOo0Kbc8VAq8DPx9Y'

# Define the address you want to geocode
address = '1600 Amphitheatre Parkway, Mountain View, CA'

# Replace spaces with '%' in the address
address = address.replace(' ', '%')

try:
    conn = http.client.HTTPSConnection('dev.virtualearth.net')
    params = {
        'q': address,
        'key': api_key,
    }
    conn.request("GET", f'/REST/v1/Locations?{urllib.parse.urlencode(params)}')
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    result = json.loads(data)

    if result.get('resourceSets'):
        locations = result['resourceSets'][0]['resources']
        if locations:
            location = locations[0]['point']
            latitude = location['coordinates'][1]
            longitude = location['coordinates'][0]
            print(f'Latitude: {latitude}, Longitude: {longitude}')
        else:
            print('No results found for the address.')
    else:
        print('No results found for the address.')
except Exception as e:
    print(f"Error geocoding address: {address}\nError: {str(e)}")