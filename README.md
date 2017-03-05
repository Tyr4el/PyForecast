# PyForecast
Welcome to PyForecast.  This is a project created by me just for fun.  I wanted something to run on my Raspberry Pi to practice
writing in Python.  It's a bot that utilizes the free Twilio service as well as a free Weather Underground API key to send a text message to myself at a certain point in the day.  Feel free to use it and change it as you see fit.  Enjoy!

The script will work for the United States and International.  Just follow the instructions in the example_config.ini file

## Install
To install PyForecast, follow these steps:

1. Clone the project to `/home/pi/` using the Git Shell or download the project from GitHub
```bash
git clone https://github.com/Tyr4el/PyForecast
```

2. Open up a terminal and type the following to install the dependencies that this project needs:
```bash
pip3 install --user -r requirements.txt
```

#### Twilio Registration
1. Go to https://www.twilio.com/try-twilio and register
2. Once registered, on your Console, go to the Phone Numbers tab on the right hand panel and add a phone number.  The phone number will be free and able to send SMS.
3. Add a verified caller ID - https://www.twilio.com/console/phone-numbers/verified
4. Take note of your LIVE Credentials (you will need the Account SID and Auth Token later) - https://www.twilio.com/console/account/settings

#### Weather Underground Registration
1. Go to https://www.wunderground.com/signup?mode=api_signup and register
2. Once registered, go to https://www.wunderground.com/weather/api/ and click on the Key Settings tab under the Analytics banner.  You may need to actually get the key at this point (I honestly don't remember).  Just fill in any information they ask for and you can just put this repo as the website link.
3. If you had to get a key in step 3, go back to the Key Settings tab and find your key.  Take note of it and copy it down somewhere, or leave a browser tab open with it.  You will need it later

#### Setting up Cron
Note: This caused me a lot of trouble but I finally figured it out.

1. Open up a terminal and type `crontab -e`

2. Open it in nano when given the option (or vi/vim if you're adventurous and know the editor.  But for new users, I recommend nano)
3. Scroll down to the bottom and add the following line: 

`M H * * * /usr/bin/python3 /home/pi/PyForecast/weather_notifier.py`

This has to fit on one line (and it should), where M is the minute of the hour, H you want cron to run the script.  If you want to edit more than just that, this is the format to follow:

`minute hour day month day-of-week`

More instruction can be found [here](https://www.thesitewizard.com/general/set-cron-job.shtml)

## Finishing Up
At this point, if I've done my job, and you've done yours, everything should be working at this point.  You should
have cron working, but to test it, try setting the job for a few minutes into the future (like 1 to 2 minutes).  If
you receive the text, then all is well and you can leave your system running and it will send you the text according
to your specifications.  If you have any questions or need help, I'm usually available on Discord @ Tyr4el#9451.
