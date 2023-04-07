import urllib.request
import urllib.parse

while True:
    # Language and article
    wlan = input("Wikipedia language: ")
    wiki = input("Article: ")

    # For multiple articles
    if wiki[0] == "!":
        wiki = wiki[1:]
        wiki = wiki.split(",")
    else:
        wiki = [wiki]      

    for x in range(len(wiki)):
        wiki[x] = urllib.parse.quote_plus(wiki[x])

    
    for x in wiki:
        try:
            # Fetching content
            page = urllib.request.urlopen("https://" + wlan + ".wikipedia.org/api/rest_v1/page/pdf/" + x)
            file = page.read()

            # Saving the result
            f = open(x + ".pdf", "wb")
            f.write(file)
            f.close()

            # Informing
            v = (wiki.index(x) + 1) / len(wiki) * 100
            print("Downloaded succesfully ", str(v), "%", "\n")
        except:
            print("Page not found, see readme for instructions\n")    

