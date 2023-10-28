# Working

This purpose of this file is to provide a basic understanding of how the server application and its components (along with the utilities) work. It aims to do so by taking on the following questions

* How do each component work seperately?
* How do all components work together?
* So, how and where do utilities fit in?

## How do each component work seperately?

Modularity can be helpful in various ways. This application contains a number of components to tackle specific tasks. Let's not think of their connection with each other just yet, but rather look at them seperately and understand their specific tasks.

### Components

As defined earlier, each component has a specific task to tackle. Components in this project exist in the form of *classes*.  
Below is a list of all the components which is followed by the detailed description of each in the same sequence as in the list.

* Task
* TaskQueue
* Executor
* Interpreter
* Dispatcher
* Timer 

#### Task

A Task object represents a task that you are to be reminded of.  
*Yes, of course, it might also be an event, like a TV show. Well then basically think of the task as watching the show (or whatever you are going to do after being reminded of it).*  

A Task object must have a **title** and a **remind_time**.  
The **remind_time** is the time when the user is to be reminded of the task. The **title** is the primary attribute used to recognise a particular Task object by the user.  
When the title is not provided to the constructor, its value defaults to "no title". So, in order to create a Task object, at least the remind_time must be provided.  

The anatomy of a Task object

```python
title = ""
remind_time = {
    time: "",
    date: ""
}
details = {
    description: "",
    start_time: "",
    end_time: ""
}
```

Apart from what has been previously mentioned about the **remind_time** attribute, as shown above, it is a dictionary with the **time** and **date** values. Both values are of string type. The **time** value is in "24hr" format and **date** is in "yyyy-mm-dd" format.  
The **details** attribute is optional. This can be used to store extra data such as a description and the start and end times of a particular task (or event).

The **Task** class has many methods providing functionalities such as displaying information, updating the attributes (except **remind_time**, updating the remind_time is done by deleting the Task object and creating a new one, which is handled by a different component), comparing the **remind_time** with other Task objects.
Two Task objects with the same **remind_time** value cannot be in the **TaskQueue** at the same time.

As mentioned earlier, reminder time is a string value that must be provided by a user. This string value has to be converted to the **remind_time** dictionary. The string value is checked and then converted to the dictionary. This task is handled by **utilities** so we will explore this further in the utilities section.

#### TaskQueue

#### Executor

#### Interpreter

#### Dispatcher

#### Timer


## How do all components work together?

Now that we have gone through the specific functions of the components seperately, let's dive into how the components talk to each other and work together in harmony.  
To understand the overall working, it is essential to understand that the primary tasks can be divided in two:

* listening for incoming requests (and interpreting and executing them)
* listening for time matches with that of the first Task object in the TaskQueue (and constructing and dispatching messages accordingly)

In order for them to happen parallely we need seprate threads, and that is exactly what happens. The seperate threads are made to originate in **app.py**.  
So first let's take a look at what's happening in the **app.py** file, and then let's go on to understand the *dataflow* fully.

### app.py

This is the *entry point* of the flask server application. As mentioned earlier this is where the **multi-threading** is done, i.e. the thread seperation originates.

### The dataflow

## So, how and where do utilities fit in?

### Utilities

* TimeStr
* TimeDict

#### TimeStr

#### TimeDict
