# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 13:26:35 2019

@author: User
"""

import pyodbc
import pandas
conn=pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=master;UID=Saurabh;PWD=onepunchguy')
sql = "select * from noteapp..notes"
data = pandas.read_sql(sql,conn)
data.to_excel("Output.xlsx",sheet_name='data')