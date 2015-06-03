import simplejson as json
from pprint import pprint

f = open('/path/to/pshitt-master/passwords.json')

#get the css files from http://getskeleton.com/#intro if you're interested in making it look decent.
print  "<link rel=\"stylesheet\" href=\"css/normalize.css\">"
print  "<link rel=\"stylesheet\" href=\"css/skeleton.css\">"

#setup the div/table for content printing
print "<div class=\"container\">"
print "<h3>attacks recently...</h3>"
print "<table class=\"u-full-width\"><thead><tr><th>ip Address</th><th>Username</th><th>Password</th></tr></thead>"

print "<tbody>"
line = f.readline()
while line:
    print "<tr>"
    parsed_json = json.loads(line)
    username = parsed_json['username']
    password = parsed_json['password']
    password = password.strip( '>' )
    username = username.strip( '<' )
    ip_address = parsed_json['src_ip']
    print "<td>%s</td> <td>%s</td> <td>%s<td></tr>" % (ip_address, username, password)
    line = f.readline()
f.close()
print "</tbody></table></div>"
