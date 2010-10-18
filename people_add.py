# it will create a Customer Kind, and add one entity

#from google.appengine.ext import db
from model_people import Customer

customer1 = Customer(last_name="Wolber",first_name="David", city = "San Francisco")
customer1.put()

