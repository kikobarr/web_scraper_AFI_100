from bs4 import BeautifulSoup
import requests
import csv

# makes a get request to the url and and uses .text to return as a string
html_text = requests.get('https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies_(10th_Anniversary_Edition)').text
# creates a BeautifulSoup object and parses it with the BS4 lxml parser
soup = BeautifulSoup(html_text, 'lxml')

# searches for the table holding the list of movies and assigns it to table
table = soup.find('table', class_ ="wikitable sortable")
# searches for the table body which contains the rows of the table
table_body = table.find('tbody')
# <tr> tag defines a row in an HTML table
# searches for and creates a list of all the rows
rows = table_body.find_all('tr')

movie_titles = []
rank = []
director = []
year = []

# iterates through all the rows in list rows
for row in rows:
    # <td> tag defines a standard data cell in an HTML table
    row_cleaned = row.find_all('td')
    row_cleaned = [ele.text.strip() for ele in row_cleaned]

    # for non-empty rows, adds movie info into separate lists
    if row_cleaned:
        rank.append(row_cleaned[0])
        movie_titles.append(row_cleaned[1])
        director.append(row_cleaned[2])
        year.append(row_cleaned[3])

# create a list of dictionaries
movie_dict_for_csv = []
for i in range(len(movie_titles)):
    movie_dict_for_csv.append({
        'Rank': rank[i],
        'Movie Title': movie_titles[i],
        'Year': year[i],
        'Director': director[i]
    })

# DID! watch three ways to load a csv file video
# DID! adjust csv file to use list of dictionaries instead of dictionary
# TODO refactor code
# TODO take out the period from the rank

with open('Top_Movie_List', mode='w') as csvfile:
    column_names = movie_dict_for_csv[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=column_names)
    for row in movie_dict_for_csv:
        writer.writerow(row)

# if __name__ == "__main__":



"""
Sources: 

https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
https://www.youtube-nocookie.com/embed/XVv6mJpFOb0?playlist=XVv6mJpFOb0&autoplay=1&iv_load_policy=3&loop=1&start=
https://www.youtube.com/watch?v=cVxS5vfu-lQ&ab_channel=FerasAlazzeh
"""

