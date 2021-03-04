.lstrip() - strips characters from the left of the given string.
.rstrip() - strips characters from the right of the given string.

.startswith('X') - checks if a string begins with a certain character/number.

.find('hi') - finds the first occurrence of a specified value and then return the index of that value.
.find('hi', starting position) - ditto but with a specified starting position.

\n - newline

open() - returns a "file handle" which is a variable used to perform operations on the file.

handle = open(filename.txt, mode)  modes: r - read

algorithms - a set of rules or steps used to solve a problem.

data structures - a particular way of organizing data in a computer.

len()

max()

min()

sum()

.split()

.split(";")

.startswith()

ord() - returns ordinal value of a character (ASCII)

chr() - opposite of ^

purse = dict()
purse["money"] = 12
putse["candy"] = 3
print(purse)
{"money": 12, "candy": 3}

.get(name, 0) - only for dictionaries

loops go through keys in a dictionary and not values.

.keys() - returns the keys of a dictionary.

.values() - returns they values of a dictionary.

.items() - returns a list of key value pairs.

dict(connection.getheader()) - retrieves headers

can loop through key value pairs in a dictionary using two iteration variables.

sorted()

tuples - () - immutable nature

lists - [] - mutable nature.

dictionaries - {} - mutable nature.



regular expression module:

import re

re.search()

re.findall()



sockets:

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

.send() - send.

.recv() - receive.

.decode() - decode incoming data.

.close() - close the connection


urllib:

import urllib.request, urllib.parse, urllib.error

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

wire format:

<person>
  <name>
    Connor
  <name>
  <phone>
    303 4456
  <phone>
<person>

''' - multi-line string


JSON:

import json

json.loads() - load from string.
json.dumps() - opposite ^

definitions:

class - a template.
attribute - a variable within a class.
method - a function within a class.
object - a particular instance of a class.
constructor - code that runs when an object is created.
inheritannce - the ability to extend a class to make a new class.