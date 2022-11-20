# Chore Manager

## Description
A chore management app which handles how often chores need to be done
and surfaces reminders when it's time to do them.

## Components
- **Main Server** - runs once in the morning and once in the evening, 
   decrements countdown on chores and adds chores that need to be
   done to a list to be surfaced
- **MySQL Database** - manages list of chores, how often they should
   be done, and when they next need to be done, started up by the main
   server
- **Flask App** - contains multiple endpoints to support a chore 
   management UI, gives the ability to easily reset a chore's 
   countdown when it's been finished
- **Inky Display** - on the way!!

## Hardware Needed
- Raspberry Pi
- Inky wHAT E-Ink Display
 
## Setup
- Ensure you have Python 3.8 installed on your Raspberry Pi
- Install required Python libraries
    ```
    pip install -r requirements.txt
    ```

## Run the Chore Manager
Run the entire app using the following command:
```
python startup.py
```
This runs a simple script that starts separate subprocesses for
the main server (which sets up the database) and the Flask app
to 