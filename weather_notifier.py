import requests
import configparser
import datetime
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

# TODO: Handle other exceptions such as timeout errors or other problems (ask Discord community for ideas)
# TODO: Add more options!  More customizable things!

configuration = configparser.ConfigParser()  # Initialize configparser
configuration.read('/home/pi/PyForecast/config/config.ini')  # Read the config.ini file
#configuration.read('config/config.ini')  # Windows testing purposes

# Set the values to variables from the config.ini file
weather_key = configuration['WEATHERUNDERGROUND']['WeatherKey']
twilio_sid = configuration['TWILIO']['account_sid']
twilio_token = configuration['TWILIO']['auth_token']
state = configuration['DEFAULT']['State']
city = configuration['DEFAULT']['City']

current_time = datetime.datetime.now() # Get the current time

# Get the forecast JSON for the chosen city and state from the .ini file
r = requests.get('http://api.wunderground.com/api/{}/forecast/q/{}/{}.json'.format(weather_key, state, city))
data = r.json()  # Parse the JSON format and store it

# The list of days of the week from the API is stored in forecastDay
forecastDay = data['forecast']['simpleforecast']['forecastday']

week = []  # Initialize a week list where the days of the week will go
# Setting key values
for day in forecastDay:
    data = {
        'day': day['date']['weekday'],
        'condition': day['conditions'],
        'high': day['high']['fahrenheit'],
        'low': day['low']['fahrenheit'],
        'pop': day['pop']
    }
    week.append(data)

# Change the greeting based on the time of day
# This is really just so the forecast days can be formatted properly and the trial message doesn't get in the way
if current_time.hour in range(00, 12):
    greeting = 'Good morning!'
elif current_time.hour in range(12, 18):
    greeting = 'Good afternoon!'
elif current_time.hour in range(18, 24):
    greeting = 'Good evening!'

# Setting the SMS message
smsBody = '''
    {day}'s weather:
    Condition: {condition}
    High: {high}
    Low: {low}
    Precip: {pop}%
    '''

# Twilio stuff - https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest
client = TwilioRestClient(twilio_sid, twilio_token)

try:
    message = client.messages.create(
        body = greeting + ''.join(smsBody.format(**day) for day in week),
        to = '{}'.format(configuration['TWILIO']['ToPhoneNumber']),
        from_ = '{}'.format(configuration['TWILIO']['FromPhoneNumber'])
    )
except TwilioRestException as e:
    print(e)