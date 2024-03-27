import sys
import requests
from html.parser import HTMLParser

# La classe qui va trier l'HTML importé
class MyHTMLParser(HTMLParser):

# Fonction qui crée un attribut pour ma classe courante
    def __init__(self):
       super().__init__()
       self.notes_content = False

# Fonction qui définit le début de la zone où je récupère mes données
    def handle_starttag(self, tag, attrs):

        for attribut in attrs:
            if attribut[0] == 'class' and attribut[1] == 'notes':
                self.notes_content = True
                # print(tag)
            
# Fonction qui définit la zone de fin de récupération des données (réinitialisation de mon boulean notes_content)
    def handle_endtag(self, tag):
        if tag == "div" and self.notes_content == True:
            # print("Encountered an end tag :", tag)
            self.notes_content = False

# Récupération des caractères
    def handle_data(self, data):
        if self.notes_content == True:
            print(data)

# Fonction principale
def main():
    n = 0
    previous_url = None

    while True:
        url = "https://thesession.org/tunes/" + str(n)

        try:
        # Appel des données
            test = requests.get(url)
        # Appel du parser
            parser = MyHTMLParser()
        # Envoi des données dans le parser
            parser.feed(test.text)
            previous_url = url
            n = n+1

        except ValueError as ve:
            return str(ve)

if __name__ == "__main__":
    sys.exit(main())