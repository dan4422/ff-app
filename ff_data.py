import requests
from bs4 import BeautifulSoup
## how am i getting the url for each game every week? selenium may be able to help
## or find a new website that may be easier to parse and extract data from for each game. try this with
## Pro-football-reference.com

def request_html(url):
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, 'html.parser')
  return soup

def get_data(soup ,data_id, home_or_away):
  return_data = {}
  html = soup.find('div', id=data_id)
  data = html.find('div', class_=f"gamepackage-{home_or_away}-wrap")
  th = data.find_all('th', class_=True)
  classes = [value
           for element in th
           for value in element["class"]]
  names = data.find_all('td', class_=classes[0])
  for c in classes[1:]:
    stat_data = data.find_all('td', class_= c)
    for n,d in zip(names,stat_data):
      if (n.find('span') == None):
        pass
      else:
        if (n.find('span').text in return_data):
          obj = {c:d.text}
          return_data[n.find('span').text] = {**return_data[n.find('span').text], **obj}
        else:
          return_data[n.find('span').text] = {c:d.text}
  return return_data



print(get_data(request_html('https://www.espn.com/nfl/boxscore/_/gameId/401437857'), 'gamepackage-passing', 'home'))
print(get_data(request_html('https://www.espn.com/nfl/boxscore/_/gameId/401437857'), 'gamepackage-rushing', 'home'))
print(get_data(request_html('https://www.espn.com/nfl/boxscore/_/gameId/401437857'), 'gamepackage-receiving', 'home'))
print(get_data(request_html('https://www.espn.com/nfl/boxscore/_/gameId/401437857'), 'gamepackage-fumbles', 'home'))

