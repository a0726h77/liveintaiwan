from google.appengine.ext import db

class Place(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    geopt = db.GeoPtProperty()

