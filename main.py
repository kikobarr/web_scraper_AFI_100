from bs4 import BeautifulSoup
import requests
import csv

def web_scraper(web_url, page_type):
    # makes a get request to the url and uses .text to return as a string
    html_text = requests.get(web_url).text
    # creates a BeautifulSoup object and parses it with the BS4 lxml parser
    soup = BeautifulSoup(html_text, 'lxml')
    if page_type == 'AFI' or 'afi':
        afi(soup)
    elif page_type == 'Best Picture':
        best_picture(soup)


# web scraper for American Film Institute's best 100 movies in the past 100 years
def afi(soup):
    # searches for the table holding the list of movies and assigns it to table
    table = soup.find('table', class_="wikitable sortable")
    # searches for the table body which contains the rows of the table
    table_body = table.find('tbody')
    # <tr> tag defines a row in an HTML table
    # searches for and creates a list of all the rows
    rows = table_body.find_all('tr')

    # create lists for later column_headers
    movie_titles = []
    rank = []
    director = []
    year = []

    # cleans data in rows
    for row in rows:
        # <td> tag defines a standard data cell in an HTML table
        row_cleaned = row.find_all('td')
        row_cleaned = [ele.text.strip() for ele in row_cleaned]

        # for non-empty rows, adds movie info into separate lists
        if row_cleaned:
            rank.append(row_cleaned[0].replace(".", ""))
            movie_titles.append(row_cleaned[1])
            director.append(row_cleaned[2])
            year.append(row_cleaned[3])

    csv_generator(rank,
                  movie_titles,
                  director,
                  year)

# DID! watch three ways to load a csv file video
# DID! adjust csv file to use list of dictionaries instead of dictionary
# DID! break out loading the csv into another function
# DID! refactor code
# DID take out the period from the rank
# TODO Create function for https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture
# def best_picture(soup):
#     table = soup.find('table', class_="wikitable sortable jquery-tablesorter")

def csv_generator(rank, movie_titles, director, year):
    # create a list of dictionaries based on the lists passed into the function
    movie_dict_for_csv = []
    for i in range(len(movie_titles)):
        movie_dict_for_csv.append({
            'Rank': rank[i],
            'Movie Title': movie_titles[i],
            'Year': year[i],
            'Director': director[i]
        })

    with open('Top_Movie_List', mode='w') as csvfile:
        column_names = movie_dict_for_csv[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        for row in movie_dict_for_csv:
            writer.writerow(row)

if __name__ == "__main__":
    web_scraper('https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies_(10th_Anniversary_Edition)',
                'AFI')
    web_scraper('https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture',
                'Best Picture')


"""
Sources: 

https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
https://www.youtube-nocookie.com/embed/XVv6mJpFOb0?playlist=XVv6mJpFOb0&autoplay=1&iv_load_policy=3&loop=1&start=
https://www.youtube.com/watch?v=cVxS5vfu-lQ&ab_channel=FerasAlazzeh
"""

