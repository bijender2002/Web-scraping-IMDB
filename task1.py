# from pprint import pprint
# import requests
# from bs4 import BeautifulSoup
# import json
# def  scrape_top_list():
# 	data=requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
# 	page = BeautifulSoup(data,"html.parser")
# 	tbody=page.find(class_="lister-list")
# 	all_trs = tbody.find_all("tr")
# 	li=[]
# 	for tr in all_trs:
# 		movie_dict={}
# 		n =tr.find("td",class_="titleColumn")

# 		name = n.find("a").text
# 		movie_dict["name"]=name

# # this will get you the url of the movie

# 		linkk = n.find("a")["href"]
# 		urll = "https://www.imdb.com"+linkk
# 		movie_dict["url"] = urll

# 		span = n.find("span",class_="secondaryInfo").text
# 		movie_dict["year"]= int(span[1:5])

# 		# this will get you the position of the movie
		
# 		position = n.text.split()[0]

# 		movie_dict["position"] = int(position[:-1])

# 		rating=tr.find("td",class_="ratingColumn imdbRating").text
# 		# print(rating)

# 		movie_dict["rating"]=float(rating[1:4])
# 		li.append(movie_dict)

# 		q=movie_dict
# 		# pprint(q)

# 	op=open('all_movies.json','w+')
# 	du=json.dump(li,op)
# 	op.close()
# 	po=open('all_movies.json','r+')
# 	lo=json.load(po)
# 	# pprint(lo)
		
# print(scrape_top_list())
