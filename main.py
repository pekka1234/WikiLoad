import urllib.request

# Language and article
wlan = input("Wikipedia language: ")
wiki = input("Article: ")

try:
    # Fetching content
    page = urllib.request.urlopen("https://" + wlan + ".wikipedia.org/api/rest_v1/page/pdf/" + wiki)
    file = page.read()

    # Saving the result
    f = open(wiki + ".pdf", "wb")
    f.write(file)
    f.close()
except:
    # If page not found
    print("Page not found, see readme for instructions")    
