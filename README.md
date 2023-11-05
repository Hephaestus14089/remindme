# remindme

Set, unset and reset reminders via Whatsapp. Pass instructions in the format of text messages.

# Table Of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Working](#working)

# Introduction

A flask server that receives instructions, schedules reminder messages and dispatches them accordingly.  
Enables user to perform CRUD (Create Read Update Delete) operations. Operations are performed according to user instruction received through Whatsapp in the format of text messages. Essentially, information exchange between the user and the application happens in the format of text messages via Whatsapp.  

_It uses ***TWILIO*** to implement user interaction through Whatsapp._

# Requirements

To start with, you will need

- python3.11
- pip3

installed in your system.  

You will also need

- an accessible IP address or domain (can be easily set up via [ngrok](https://ngrok.com/))
- a [TWILIO](https://www.twilio.com/) account

Apart from the above mentioned requirements this application needs certain PIP modules to function, which will be discussed later in this document.

# Installation


Clone the repository and move into the newly created directory

```
git clone https://github.com/hephaestus14089/remindme
cd remindme
```

Create a virtual environment and activate it

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the modules inside the virtual environment

```
pip install -r requirements.txt
```

# Configuration

#### TWILIO

You need to set up a [TWILIO](https://www.twilio.com/) account and get the whatsapp sandbox to be running there.  
_You will have to configure the sandbox to relay the whatsapp messages to the flask application API address, and specify the request method. Please refer to the TWILIO documentation to execute the above steps._  

You will need to keep track of some information regarding your TWILIO profile for the next steps. You will need the **account SID**, **auth token**, and the sandbox phone number.

#### .env file

Now, you need to create a file named **.env** in the project directory.  

The file must contain the following information

```
TWILIO_AUTH_TOKEN=""
TWILIO_ACCOUNT_SID=""
TWILIO_PHONE_NUMBER=""
RECEIVER_PHONE_NUMBER=""
```

The appropriate values should be placed within the double quotes.  
The **TWILIO_PHONE_NUMBER** should refer to the TWILIO sandbox phone number and the **RECEIVER_PHONE_NUMBER** should refer to the user's Whatsapp number.

# Usage

This section deals with using the application from a user's perpective. It contains the commands (or instructions) that the user may provide the application to get the desired action performed.  
It is important to maintain the format of the commands carefully as by making it difficult for the application to understand or interpret a command, a user's life will certainly does not become easier.  

Command formats can be divided into

- Single line
- Multi line

Under each format, commands are divided by the action they perform (i.e. Create / Read / Update / Delete).  

## Single line commands

#### Create

Format

```
create <time> <title>
```

Example

```
create 15m hello world
```

#### Read

#### Update

#### Delete

## Multi line commands

#### Create

#### Read

#### Update

#### Delete


# Working

To get a concept of how the application does what it does and how its different parts work in harmony to achieve that, please visit the [WORKING.md](https://github.com/hephaestus14089/remindme/blob/main/WORKING.md) file.
