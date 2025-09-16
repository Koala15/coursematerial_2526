# Debugging

Whenever you run a software program or a script for the first time, it will (almost) never run the way you want it to run. In the beginning this might seem frustrating, but along the way you will come to understand that this is the way of software engineering. You will write code, it will not work, and you will have to adapt your code. This is called **debugging**. 

Debugging is so important, that on your exam you will be asked to debug written code. You will be guided throughout the course on how to debug your code for specific assignments, but an introductory overview is provided in this text. 

## Reading the error log

When a program doesn't run the way you want it to, it will usually encounter an error. It is important to understand what an error message looks like. The log you will see in your terminal containing the error is called a stack trace. Here you can find some examples of such errors:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero

>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined

>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

It is important to understand that error messages come in many different forms, but they usually have a pretty rigid structure, and lucky for you, they are also easy to read in Python. 

The error messages above consist of three parts:
* The file and location where the error happens (in this case it's in the terminal on the first line).
* The line where the error occurs, sometimes with a symbol showing where the error happens. 
* The error message itself. In this case we are dealing with a ZeroDevisionError, a NameError, and a TypeError. Throughout the course you will learn why these result in errors (although you should at least understand what is happening in the first one).

### Longer stack traces
It is important to understand that the first two parts of the stack trace are technically one piece. Often you will see that multiple files or at least multiple lines are affected in an error, thus you will see multiple lines and files referenced, like so:

``` python
Traceback (most recent call last):
  File "example.py", line 8, in <module>
    main()
  File "example.py", line 4, in main
    result = divide(10, 0)
  File "example.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

This does not mean you are dealing with 3 different errors. There is only one error, the ZeroDivisionError, but due to the nature of how the function was called, three different lines are shown in the error. As we said, only the last line will feature the error itself, in this case dividing ```a``` by ```0```.

### "I don't understand the error"

Even though Python's syntax is more readable than that of many other programming languages, you might often find yourself confused by the stack trace. In cases like this, you can just Google the error message and you will get an answer pretty easily. Copilot or Chat-GPT can be very useful here as well. 

Important: try to understand the error code and resolve it on your own, rather than letting chat fix it for you. Understanding errors is a huge part of coding and we will test you on this, not only during the exam but also during PE. 

## Using print statements to find errors

Often you will write a script that doesn't give you any errors, but it doesn't act the way you intended it to act. You get a wrong result, the type of your return value is wrong, or any other mistake that doesn't break the code. In cases like this, it is important to find the location where your code goes wrong, and why it's wrong. 

In cases like these, a print statement in your code helps you understand where you are wrong. Printing values to your console should never break your code, so you can use these statements anywhere and anytime you like, if you are having trouble finding out where you are wrong. 

```python
#some code is happening here
print("This is a temporary result.")
#more code is happening here
```

Throughout the course we will give examples on how to debug specific cases and broader applications. In chapter 05 (strings) we will give examples on how to use these print statements even more efficiently. 

## Can I just run the pytests and adapt my code until it works?

We strongly suggest you try to run your own code first before you move on to the pytests. We encourage this because of a few different reasons:

* The pytests take a long time, much longer than just running your own code. 
* If you run your code with a single example, you will get a clear error and/or a to-the-point printed statement. When you run the pytest, your code will run many times over and it will be hard to decipher which error is due to what behaviour. 
* You will be asked to decipher error statements on the exam and the PE. There won't be any pytests there to help you.  
