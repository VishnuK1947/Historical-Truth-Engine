from bs4 import BeautifulSoup

with open('the-historian\'s-history-of-the-world-v7.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

text = soup.get_text()
data = [text.strip() for text in text.split("\n\n") if text]

for i in range(0, len(data)):
    print(f"DATA[{i}]: {data[i]}")
    print("\n")

#print(text)