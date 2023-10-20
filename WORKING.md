# Working

This purpose of this file is to provide a basic understanding of how the server application and its components (along with the utilities) work. It aims to do so by taking on the following questions

* How do each component work seperately?
* How do all components work together?
* So, how and where do utilities fit in?

## How do each component work seperately?

Modularity can be helpful in various ways. This application contains a number of components to tackle specific tasks. Let's not think of their connection with each other just yet, but rather look at them seperately and understand their specific tasks.

### Components

* Task
* TaskQueue
* Executor
* Interpreter
* Dispatcher
* Timer 

#### Task

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
