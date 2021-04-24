# Speed plotter

## Description
A simple python script to display the speed within a given network.

## Building and using the app
### Preparation
Make sure python is installed (this project uses 3.7).
With pip install the following dependencies: 
- speedtest-cli
- flask

or run ``pip install speedtest-cli flask``
### Running the application
To run speedcheck execute ``python3 ./speedcheck/speedcheck.py``.
This is probably best to do within some type of a cronjob to create periodical data for the webserver to use.

To run the webserver execute ``python3 ./web/app.py``.
The resulting webpage can be found at http://127.0.0.1:5000/.