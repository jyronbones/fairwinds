import pandas as pd

def convert_to_dataframe(api_response):
    latitude = api_response['latitude']
    longitude = api_response['longitude']
    times = api_response['hourly']['time']
    temperatures = api_response['hourly']['temperature_2m']

    df = pd.DataFrame({
        'ID': range(1, len(times) + 1),
        'latitude': [latitude] * len(times),
        'longitude': [longitude] * len(times),
        'time': times,
        'temperature_2m': temperatures
    })

    return df