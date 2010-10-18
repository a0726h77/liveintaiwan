# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template

class Place(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    geopt = db.GeoPtProperty()

class MainPage(webapp.RequestHandler):
      def get(self):
          place = db.get(self.request.get('k'))

          template_values = {
	      'name' : place.name,
	      'address' : place.address,
	      'k' : self.request.get('k')
           }

          path = os.path.join(os.path.dirname(__file__), 'place_update.html')
          self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/place_update', MainPage)],
                                          debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
