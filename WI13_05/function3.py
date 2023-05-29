#!usr/bin/python3

def greet(name, message="Hello"):
    print(f"{message}, {name}")

greet("Anne") #this prints Hello, Anne since no message was provided. it uses the default greeting message
greet("james", "Hi") #prints Hi, james. because the message was specified as Hi
