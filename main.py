import urllib.request
import urllib.parse

while True:
    # Language and article
    wlan = input("Wikipedia language: ")
    unparsedwiki = input("Article: ")

    # Parsing for ä, ö and other letters
    wiki = urllib.parse.quote_plus(unparsedwiki)

    try:
        # Fetching content
        page = urllib.request.urlopen("https://" + wlan + ".wikipedia.org/api/rest_v1/page/pdf/" + wiki)
        file = page.read()

        # Saving the result
        f = open(unparsedwiki + ".pdf", "wb")
        f.write(file)
        f.close()

        # Informing
        print("Downloaded succesfully\n")
    except:
        # If page not found
        print("Page not found, see readme for instructions\n")    
