import googlesearch
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import pyfiglet

def search_google(query):
    urls = googlesearch.search(query, num_results=5) # change num_results as per your requirement
    print(f"\nSearch Results : \n--------------\n")

    i=1
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            answer = soup.find('p').text.strip() # assumes answer is in the first paragraph of the page
            if answer != "":
                print(f"{colored(f'[{i}] ' , 'green')}{colored(answer, 'yellow')}\n    ({colored(url, 'blue')})\n")
            else:
                print(f"{colored(f'[{i}] ' , 'green')}{colored(url, 'blue')}\n")
            i+=1
        except:
            continue

while True:

    print("\033[2J\033[H", end="")
    print(f"\n{colored(pyfiglet.figlet_format('Google  Search'), 'blue')}")
    query = input("Search Query : ")
    if query == "":
        break
    search_google(query)
    input(colored("\nAnother Search", 'grey', attrs=['bold']))
