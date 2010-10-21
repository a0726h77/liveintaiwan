from model_people import Customer

cs = Customer()

print 'Content-Type: text/html'
for c in cs.all():
    print str(c.key()) + '<br>'
    print c.last_name + '<br><br>'

print c.all().count()

