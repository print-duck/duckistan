from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd

pages = range(951,7952,50) #can only go to 10000 items because after that the URI ha no discernable distinction
#https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc
#https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=51&ref_=adv_nxt
#https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=101&ref_=adv_nxt
#initialize empty lists to store the variables scraped
titles = []
years = []
#ratings = []
#genres = []
runtimes = []
#imdb_ratings = []
#metascores = []
#votes = []
my_super_counter=0
for page in pages:
    
    #get request
    response = get("https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=" 
         
                   + str(page) 
                   + "&ref_=adv_nxt")
    sleep(randint(8,15))
     
    #throw warning for status codes that are not 200
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    #parse the content of current iteration of request
    page_html = BeautifulSoup(response.text, 'html.parser')
        
    movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
    
    #extract the 50 movies for that page
    for container in movie_containers:

        #conditional for all with metascore
        if container.find('div', class_ = 'ratings-metascore') is not None:

            #title
            title = container.h3.a.text
            titles.append(title)

            #year released
            year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text
            years.append(year)

            #rating
##            rating = container.p.find('span', class_= 'certificate').text
##            ratings.append(rating)

            #genre
#            genre = container.p.find('span', class_ = 'genre').text
#            genres.append(genre)

            #runtime
            time = container.p.find('span', class_ = 'runtime').text
            runtimes.append(time)

            #IMDB ratings
#            imdb = float(container.strong.text)
#            imdb_ratings.append(imdb)

            #Metascore
#            m_score = container.find('span', class_ = 'metascore').text
#            metascores.append(int(m_score))

            #Number of votes
#            vote = container.find('span', attrs = {'name':'nv'})['data-value']
#            votes.append(int(vote))
            sci_fi_df = pd.DataFrame({'movie': titles,
                       'year': years,

                       'runtime': runtimes})
            print(my_super_counter)
            my_super_counter+=1

#remove the parenthesis at the front and the end of the year and turn them into integers
sci_fi_df.loc[:, 'year'] = sci_fi_df['year'].str[-5:-1].astype(int)

#standardize the IMDB score so that it is comparable to the scale of the other one
sci_fi_df['n_imdb'] = sci_fi_df['imdb'] * 10

#remove " min" from the end of the runtime variable and make them integers
sci_fi_df['runtime_min'] = sci_fi_df['runtime'].apply(lambda x: x.replace(" min", "")).apply(lambda x: int(x))

#drop the old runtime column
sci_fi_df.drop(columns='runtime', axis=1, inplace=True)

#remove the "\n" at the beginning of the genres
sci_fi_df['genre'] = sci_fi_df['genre'].apply(lambda x: x.replace("\n", ""))

#after standardizing the imdb variable, it became a float. We don't need it to be so I made it an int
sci_fi_df['n_imdb'] = sci_fi_df['n_imdb'].apply(lambda x: int(x))

#I found that there was whitespace in the arrays of genres so I removed that with .rstrip()
sci_fi_df['genre'] = sci_fi_df['genre'].apply(lambda x: x.rstrip())

#split the string list into an actual array of values to do NLP on later
sci_fi_df['genre'] = sci_fi_df['genre'].str.split(",")

#write the final dataframe to the working directory
sci_fi_df.to_csv("sci_fi_df_AWS.csv", index=False)
