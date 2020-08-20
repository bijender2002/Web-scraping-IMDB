from pprint import pprint
import requests
from bs4 import BeautifulSoup
import json
data=requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
page = BeautifulSoup(data,"html.parser")
tbody=page.find(class_="lister-list")
all_trs = tbody.find_all("tr")
li=[]
for tr in all_trs:
    movie_dict={}
    n =tr.find("td",class_="titleColumn")
    name = n.find("a").text
    movie_dict["name"]=name
    linkk = n.find("a")["href"]
    url = "https://www.imdb.com"+linkk
    movie_dict["url"] = url
    span = n.find("span",class_="secondaryInfo").text
    movie_dict["year"]= int(span[1:5])
    position = n.text.split()[0]
    movie_dict["position"] = int(position[:-1])
    rating=tr.find("td",class_="ratingColumn imdbRating").text
    movie_dict["rating"]=float(rating[1:4])
    li.append(movie_dict)

years=[]
for i in li:
    year=i["year"]
    if year not in years:
        years.append(year)
group_by_year={i:[]for i in years} 
for j in li:
    year=j["year"]
    for k in group_by_year:
        if str(k)==str(year):
            group_by_year[k].append(j)
pprint(group_by_year)

    