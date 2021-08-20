import streamlit as st
import requests
import datetime
from geopy import Nominatim
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# Date and time
d = st.date_input("Ride date", datetime.date(2019, 7, 6))
t = st.time_input('Departure time', datetime.time(8, 45))

pickup_datetime = datetime.datetime.combine(d, t)

# Passenger count
passenger_count = st.number_input('Number of passengers',
                                  min_value=1,
                                  max_value=8,
                                  step=1)
passenger_count = str(passenger_count)

# Adress to lon lat
pickup_point = st.text_input('Pickup address')
dropoff_point = st.text_input('Dropoff address')

locator = Nominatim(user_agent="myGeocoder")

pickup_location = locator.geocode(pickup_point)
dropoff_location = locator.geocode(dropoff_point)

if pickup_location is None or dropoff_location is None:
    st.text('Please enter valid pickup and dropoff locations')
else:
    pickup_longitude = pickup_location.longitude
    pickup_latitude = pickup_location.latitude

    dropoff_longitude = dropoff_location.longitude
    dropoff_latitude = dropoff_location.latitude

    params = {"pickup_datetime": pickup_datetime,
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": passenger_count}

    response = requests.get(url, params=params)
    response_json = response.json()
    # response_json
    fare = float(response_json["prediction"])
    fare = round(fare, 2)
    st.text(f'Estimated ride cost : {fare} $')
