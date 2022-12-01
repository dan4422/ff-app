import requests
from bs4 import BeautifulSoup
## how am i getting the url for each game every week? selenium may be able to help
## or find a new website that may be easier to parse and extract data from for each game. try this with
## Pro-football-reference.com
html_text = requests.get('https://www.espn.com/nfl/boxscore/_/gameId/401437857').text

soup = BeautifulSoup(html_text, 'html.parser')
# write function to pass in each gampackage. ex. gamepackage-rushing, gamepackage-receiving, etc.
# data = soup.find('div', id="gamepackage-passing")
# home = data.find('div', class_='gamepackage-home-wrap')
# away = data.find('div', class_='gamepackage-away-wrap')
# print(home.find('td', class_='name').find('span').text)
# print(home.find('td', class_='c-att').text)
# print(home.find('td', class_='yds').text)
# print(home.find('td', class_='td').text)
# print(away.find('td', class_='name').find('span').text)
# print(away.find('td', class_='c-att').text)
# print(away.find('td', class_='yds').text)
# print(away.find('td', class_='td').text)

data = soup.find('div', id="gamepackage-rushing")
home = data.find('div', class_='gamepackage-home-wrap')
away = data.find('div', class_='gamepackage-away-wrap')
names = home.find_all('td', class_='name')
for n in names:
  if (n.find('span') == None):
    pass
  else:
    print(n.find('span').text)
carries = home.find_all('td', class_='car')
for c in carries:
  print(c.text)
# print(home.find('td', class_='yds').text)
# print(home.find('td', class_='td').text)
# print(away.find('td', class_='name').find('span').text)
# print(away.find('td', class_='car').text)
# print(away.find('td', class_='yds').text)
# print(away.find('td', class_='td').text)

