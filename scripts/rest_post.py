# coding:utf-8

#
# REST API POST Request
#

import urllib2

xml_data = '''
<place>
    <name>台北車站</name>
</place>
'''

request = urllib2.Request('http://yanliveintaiwan.appspot.com/rest/place/ag95YW5saXZlaW50YWl3YW5yDQsSBVBsYWNlGIfKBAw', xml_data)
connection = urllib2.urlopen(request)
data = connection.read()
print data
