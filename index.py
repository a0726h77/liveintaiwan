# coding:utf8

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
from google.appengine.ext.webapp import template

#class Greeting(db.Model):
#    author = db.UserProperty()
#    content = db.StringProperty(multiline=True)
#    date = db.DateTimeProperty(auto_now_add=True)

#class Place(db.Model):
#    name = db.StringProperty(required=True)
#    address = db.StringProperty(required=True)
#    lat = db.StringProperty(required=True)
#    lng = db.StringProperty(required=True)

class Place(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    geopt = db.GeoPtProperty()


class MainPage(webapp.RequestHandler):
    def get(self):
#        greetings_query = Greeting.all().order('-date')
#        greetings = greetings_query.fetch(10)
#
#        if users.get_current_user():
#            url = users.create_logout_url(self.request.uri)
#            url_linktext = 'Logout'
#        else:
#            url = users.create_login_url(self.request.uri)
#            url_linktext = 'Login'


        query = db.GqlQuery("SELECT * FROM Place")

        #query = db.GqlQuery("SELECT * FROM Place WHERE address >= :1 AND address < :2", u"台北市", u"台北市" + u"\ufffd")

#        lat = float(25.051941)
#        lon = float(121.516982)
#        #area = .0005
#        area = .04
#        minLat = lat - area
#        minLon = lon - area
#        maxLat = lat + area
#        maxLon = lon + area
#        query = db.GqlQuery("SELECT * FROM Place WHERE geopt >= :1 AND geopt <= :2",db.GeoPt(lat=minLat, lon=minLon), db.GeoPt(lat=maxLat, lon=maxLon) )
        
        places = list()
        i = 1 
        for q in query.fetch(100):
	    #print q.fields()
	    name = cgi.escape(q.name).replace("'", "\\'").replace('"', '\\"')
            address = cgi.escape(q.address).replace("'", "\\'").replace('"', '\\"')

            places.append(dict(sn=i, name=name, address=address, key=str(q.key()), geopt=q.geopt))
            i += 1

        template_values = {
#            'greetings': greetings,
#            'url': url,
#            'url_linktext': url_linktext,
            'places' : places
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/.*', MainPage)],
                                          debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
