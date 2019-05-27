#/usr/bin/python
import mechanize
import hashlib

url = 'http://docker.hackthebox.eu:57650/'

b = mechanize.Browser()
b.set_handle_robots(False) #ignore robots.txt
response = b.open(url)


respuesta = response.readlines()
a =  respuesta[5].split("center'>")
s =  a[2].split("</h3")
c = s[0]
print "hash:"+c
encripted = hashlib.md5(c.encode()).hexdigest()
print "md5:"+encripted+":"


b.select_form(nr=0)
b.form['hash'] = encripted
b.method = "POST"
response = b.submit()

print response.readlines() #Fl4g si inside, Look close the html
print "**code by @stormdark_ on tw**"
