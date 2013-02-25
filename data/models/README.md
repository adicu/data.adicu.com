models
===========

Brief Overview
--------------
Each handler will have its own model for out to interrupt the parameters based
to the handler. How those arguments in turn relates to querying its datastore, and,
and how the response to the user should be formed.

We break models down our models into two separate files based on "thought". The main
difference between these two files is based on function and interaction with the handler.

Most of our application code, since we are dealing with just an API, will be in the models.

MODEL.py
--------
The MODEL.py file contains data structure information, i.e. how the response should be formed,
and what fields to pass to the database driver, such as the SELECT arguments, TABLE, and any
special parameters.

MODEL\_FUNCTIONS.py
------------------
The MODEL\_FUNCTION.py file contains a list of methods on how to interrupt
hanlder query parameters. In this file, to add a query parameter to be used and understand, use a function
with the name you want the parameter to be. Say I want to be able to query on the API level by deparment, and
form a requst such as
    
    url.com/courses?department=biology

I would add a function where whose name was department, and takes a single value, the parameter.
It is the job of this function to interrupt that information to and to construct a query to be used by the driver
to request that information, and modify the value information if it needs to be modified. It is expected these
functions will return two parameters, query\_info, value.
