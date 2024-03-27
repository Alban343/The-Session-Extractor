import sys
import requests
from html.parser import HTMLParser

# La classe qui va trier l'HTML importé
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            print("Encountered a start tag:", tag, attrs)
            
        # if attrs

    def handle_endtag(self, tag):
        if tag == "div":
            print("Encountered an end tag :", tag)

    # def handle_data(self, data):
    #     print("Encountered some data  :", data)

# Fonction principale
def main():
    print('tttttt')
    try:
        # Appel des données
        test = requests.get("https://thesession.org/tunes/1")
        # Appel du parser
        parser = MyHTMLParser()
        # Envoi des données dans le parser
        parser.feed(test.text)

    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())