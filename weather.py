import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", force=True)

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.14&longitude=11.58&current_weather=true"

def get_data () -> tuple[str, float, float] :

    try:

        req = requests.get(URL)
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
    result = get_data()
    if result is None:
        logging.warning("No data received. Exiting.")
    else:
        time, temperature, windspeed = result
        write_data(time, temperature, windspeed)

