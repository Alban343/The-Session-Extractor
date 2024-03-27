import sys
import requests
from html.parser import HTMLParser

# La classe qui va trier l'HTML importé
class MyHTMLParser(HTMLParser):

# Fonction qui
    def __init__(self):
       super().__init__()
       self.notes_content = False


    def handle_starttag(self, tag, attrs):

        for attribut in attrs:
            if attribut[0] == 'class' and attribut[1] == 'notes':
                self.notes_content = True
                print(tag)
            
    
    def handle_endtag(self, tag):
        if tag == "div" and self.notes_content == True:
            print("Encountered an end tag :", tag)
            self.notes_content = False

    def handle_data(self, data):
        if self.notes_content == True:
            print("Encountered some data  :", data)

# Fonction principale
def main():
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