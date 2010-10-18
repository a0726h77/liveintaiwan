# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template

#class Place(db.Model):
#    name = db.StringProperty(required=True)
#    address = db.StringProperty(required=True)
#    lat = db.StringProperty(required=True)
#    lng = db.StringProperty(required=True)

class Place(db.Model):
    name = db.StringProperty(required=True)
    address = db.StringProperty(required=True)
    geopt = db.GeoPtProperty(required=True)

class MainPage(webapp.RequestHandler):
    def post(self):

        print self.request.get('name').encode('utf-8') + "<br>"
	
	if self.request.get('k'):
	    p = db.get(db.Key(self.request.get('k')))

	    p.name = self.request.get('name')
            p.address = self.request.get('address')
            p.geopt = db.GeoPt(self.request.get('lat'),self.request.get('lng'))

            p.put()
            print "update success"
        else:
            p = Place(name=self.request.get('name'),
                   address=self.request.get('address'),
                   geopt=db.GeoPt(self.request.get('lat'),self.request.get('lng')))
                   #lat = self.request.get('lat'),
                   #lng = self.request.get('lng'))
            db.put(p)
            print "add success"

        print "<a href=\"/place_add\">Add</a><br>"
        print "<a href=\"/\">View</a><br>"

application = webapp.WSGIApplication(
                                     [('/place_save', MainPage)],
                                          debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
