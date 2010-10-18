from google.appengine.ext import db

class Customer(db.Model):
#  last_name = db.StringProperty(required=True)
#  first_name= db.StringProperty(required=True)
#  city = db.StringProperty(required=True)

  last_name = db.StringProperty()
  first_name= db.StringProperty()
  city = db.StringProperty()

