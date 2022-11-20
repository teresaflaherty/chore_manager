# Chore Manager

## Description
A chore management app which handles how often chores need to be done
and surfaces reminders when it's time to do them.

## Components
 - **Main Server** - runs once in the morning and once in the evening, 
   decrements countdown on chores and adds chores that need to be
   done to a list to be surfaced
 - **Flask App** - contains multiple endpoints to support a chore 
   management UI, gives the ability to easily reset a chore's 
   countdown when it's been finished
 - **MySQL Database** - Manages list of chores, 

## Hardware Needed
 - Raspberry Pi
 - Inky wHAT E-Ink Display
 
## Setup
### Install required libraries
- Install any Python libraries used
```
pip install -r requirements.txt
```

