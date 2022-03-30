# EvoCare_Website_api

# Definition
 This site for a car showroom displays the services offered by the showroom, and the owner of the showroom controls everything, such as what 
 services are displayed and control the display of images for each service. 
 Users can also book an appointment to do a specific service and pay via the visa
# Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/minaemad13/EvoCare_Website_api.git
$ cd EvoCare_Website_api
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.

you can see the front end wich built using react js from here 
https://github.com/minaemad13/EvoCare_Website
