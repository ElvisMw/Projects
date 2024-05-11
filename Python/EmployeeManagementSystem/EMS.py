#!/usr/bin/env python3

from os import system
import re
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="angel", database="employee")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'