# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
      def get(self):
          template_values = {
	    'user' : 'xxx'
           }

          path = os.path.join(os.path.dirname(__file__), 'place_add.html')
          self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/place_add', MainPage)],
                                          debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
