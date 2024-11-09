from bs4 import BeautifulSoup
import requests

def home_example():
    with open('home.html', 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    tags = soup.find_all('h5')
    # the _ next to class is important to indicate class is a keyword
    course_cards = soup.find_all('div', class_ = 'card')

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(course_name)
        print(course_price)

def web_example():
    # Make sure to use .text at the end of requests.get().text
    html_text = requests.get('https://simple.wikipedia.org/wiki/AFI%27s_100_Years..._100_Movies').text
    soup = BeautifulSoup(html_text, 'lxml')

    # use one object "job" to capture big block
    job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
    # narrow down specific info by creating another object "company_name" based on job
    # also use .text to just have the text
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
    skills = job.find()
    print(company_name)
