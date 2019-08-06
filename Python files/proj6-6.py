import requests
import bs4

req = requests.get("https://usm.maine.edu")

soup = bs4.BeautifulSoup ( req.text, "html.parser" )

print("Web page title:", soup.title.string)
print("-" * 50)
print("")

# Find the div's class ="item-content"

for one_div in soup.select("div.item-content"):
    header = one_div.select("h2")
    details = one_div.select("p")

    if (header[0].string != ""):
        print("Header", header[0].text)

        for p in details:

            if (p.text is not None):
                 print(p.text)
            
        print("---")
        print("")




# Show all of the <p> blocks

#for p in soup.select("p"):
#    print(p.string)
#    print("---")
                    
