# remindme
A flask server that receives instructions sends scheduled messages through whatsapp.
_It uses TWILIO for the whatsapp interaction process._

# The Idea
The idea is to implement a reminder schedular with which the user can interact through whatsapp.
* The user sends instructions (CRUD operations)
* Messages are created and stored in the queue
* Messages are dispatched as scheduled

# Use Case
Just a reminder dispatcher and nothing else.
For example: I want to be reminded me of the 3 'o' clock meeting a 2:45. So I can just schedule a message to be sent to me at 2:45 reminding me about the meeting via whatsapp.
