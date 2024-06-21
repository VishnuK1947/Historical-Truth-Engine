from bs4 import BeautifulSoup

with open('pg59134-h/pg59134-images.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

text = soup.get_text()
print(text)