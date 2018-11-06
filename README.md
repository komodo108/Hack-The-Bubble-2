# Hack-The-Bubble-2
This project was made for a hackathon and will **no longer be maintained or supported**, any pull requests recieved or requests for support with this project will be **denied**.

### Motivation
Project for Hack the Bubble 2018 - done in 12 hours.

### Hack-The-Bubble-2
For this hackathon the theme was '*beach*', we decided to make an admin system for a beach.
One can book loungers for certain times of day, order items for specific bookings, etc.
**Please note** that this project is incomplete and insecure, and if it is going to be used, a lot still needs to be done - e.g. fully implementing the front-end. 

### Database
One must connect this application to another database before it can be used. Please see the `database.sql` file in the root directory of this project.

### Usage
To run the server simply navigate to the `Website` directory, and then run:
```
pip -r requirements.txt
python server.py
```
This will start flask, and allow connections on localhost. From there you can login and start booking loungers, etc.