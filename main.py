from bs4 import BeautifulSoup

with open('home.html') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    
    tags = soup.findAll('h5')
    for tag in tags:
        print(tag)