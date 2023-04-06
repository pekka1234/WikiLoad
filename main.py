import urllib.request

wiki = input("Artikkeli: ")
page = urllib.request.urlopen("https://fi.wikipedia.org/api/rest_v1/page/pdf/" + wiki)



file = page.read()

f = open(wiki + ".pdf", "wb")
f.write(file)
f.close()