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

This section deals with using the application from a user's perpective. It contains the command phrases (or instructions) that the user may provide the application to get the desired action performed.  
The necessary information passes along with the command is together termed as a 'command phrase'  
It is important to maintain the format of the command phrases carefully as by making it difficult for the application to understand or interpret a command phrase, a user's life certainly does not become easier.  

*Note that this section only consists of commands and command phrases needed by an user to accomplish the basic operations. The available commands exceed that of what is covered here and can be leveraged by an user for a more flexible usage and an enhanced experience.*  

Command formats are catagorized on the basis of the CRUD operation they are atributed to.

- [Create](#create)
- [Read](#read)
- [Update](#update)
- [Delete](#delete)

**A command phrase typically starts with the action to perform (i.e. the 'command').**  

### Create

The format provided below needs to be maintained to accomplish the creation of a **Task**.

```
create <time> <title>
```

The phrase starts with the command (create), which is followed by the time of reminded (i.e. the time at which the reminder must be displatched to the user). And at the end (optionally) the title may be provided.  
The title may contain spaces. Anything after the space following the remind time will be considered as part of the title.  
When a title is not explicitly provided, it of course defaults to "no title".  

**Remind time formats**

- Specifying in hours and minutes (or hours or minutes).  
The specified amount is the amount of time from the time of creation of the **Task** object.
- Specifying the clock time in 12 hours or 24 hours format.  
In case of using the 12 hours format, the clock time must be followed by 'AM' or 'PM' appropriately without any spaces in between them.

**Examples**

The following example will create a **Task** object with the title "hello world", set to be dispatched at fifteen minutes from its creation.

```
create 15m hello world
```

The following examples will create a **Task** object with the title "no title".  
The one created by the former of them will be set to be dispatched at one hour from its creation while the one by the latter at one hour and forty minutes from its creation.

```
create 1h
create 1h40m
```

Both of the follwing examples will create a **Task** object with the title "test", set to be dispatched at 13:15 (or 01:15 PM) **on the same day**.

```
create 1:15pm test
create 13:15 test
```

*Note that if the specified remind time is actually in the past, the application throws an error.*

### Read

### Update

### Delete

# Working

To get a concept of how the application does what it does and how its different parts work in harmony to achieve that, please visit the [WORKING.md](https://github.com/hephaestus14089/remindme/blob/main/WORKING.md) file.
