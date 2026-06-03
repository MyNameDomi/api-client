import requests
import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", force=True)



default_lat =48.14
default_lot =11.58


def get_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lat", type=float, default=48.14, help="which latitude")
    parser.add_argument("--lon", type=float, default=11.58, help="which Longitude")

    user_input = parser.parse_args()

    return user_input

def build_url(user_input: argparse.Namespace) -> str:

    url = f"https://api.open-meteo.com/v1/forecast?latitude={user_input.lat}&longitude={user_input.lon}&current_weather=true"
    
    return url


def get_data (url) -> tuple[str, float, float] :

    try:

        req = requests.get(url)
        req.raise_for_status()
        

        data = req.json()

        time = data["current_weather"]['time']
        temperature = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]['windspeed']

        return time, temperature, windspeed
    except requests.exceptions.RequestException as e:
        logging.warning(f"API request failed {e}")

def write_data(time:str, temperature:float, windspeed:float) -> None:
   
    logging.info(f"The current temperature is: {temperature}")     
    logging.info(f"The current windspeed is: {windspeed}")
    logging.info(f"The current time is: {time}")



if __name__ == "__main__":
    user_input = get_input()
    url = build_url(user_input)
    result = get_data(url)
    if result is None:
        logging.warning("No data received. Exiting.")
    else:
        time, temperature, windspeed = result
        write_data(time, temperature, windspeed)

