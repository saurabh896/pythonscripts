# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:08:37 2019

@author: User
"""
import pyodbc
import pandas as pd
import array as arr
df1=""
data=''
conn=pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=master;UID=Saurabh;PWD=onepunchguy')
cursor=conn.cursor()
cursor.execute("select * from noteapp..notes")
data=cursor.fetchall()
print(data)
Data=pd.DataFrame(data)
print(Data)
Data.to_excel("Output.xlsx",sheet_name="sheet1")