from vars import *

import mysql.connector

def get_connection():
  mydb = mysql.connector.connect(
  host="localhost",
  user=db_username,
  password=db_password,
  database=db_name
  )
  return mydb