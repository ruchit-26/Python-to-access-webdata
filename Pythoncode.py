import urllib.request,urllib.parse,urllib.error,re
fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_648069.html')
su=0;
for line in fhand:
    t=line.decode().strip()
    x=re.findall('class="comments">([0-9]+)',t)
    for j in x:
        su+=int(j)
print(su)

