from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import rest
from model_people import Customer
from model_place import Place

rest.Dispatcher.base_url = "/rest"


#rest.Dispatcher.add_models({
#	  "foo": Customer,
#	   })
rest.Dispatcher.add_models({
    'place' : (Place, rest.READ_ONLY_MODEL_METHODS)
})
#    'bar' : (BarModel, ['GET_METADATA', 'GET', 'POST', 'PUT'],
#    'cache' : (CacheModel, ['GET', 'DELETE'] })


application = webapp.WSGIApplication([
	    ('/rest/.*', rest.Dispatcher)
	    ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
