import numpy as np
import pandas as pd
import os
from newspaper import Config, Article, Source

config = Config()
config.browser_user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

datadir = '../'

def get_file_path():
    i=0
    while os.path.exists(datadir+'topics/'+str(i)+'.csv'):
        i+=1
    return datadir+'topic_url/'+str(i)+'.csv', datadir+'topics/'+str(i)+'.csv'

def process_article(url):
    article = Article(url=url,config=config)
    article.download()
    article.parse()

    title = article.title
    body = article.text
    autor = article.authors
    date = article.publish_date
    return (title, body, autor, date)

def get_articles():
    from_path, to_path = get_file_path()
    if not os.path.exists(from_path):
        print('no new file found')
        return

    articles = {'body':[], 'autor':[], 'rating':[], 'date':[],'url':[],'headline':[]}

    input_df = pd.read_csv(from_path,usecols=['url','rating'])

    for i in input_df.index:
        #if website uses some kind of blocking (e.g. captcha) catch error and drop entry
        try:
            article = process_article(input_df.url[i])
            articles['headline'].append(article[0])
            articles['body'].append(article[1])
            articles['rating'].append(input_df.rating[i])
            articles['autor'].append(article[2])
            articles['date'].append(article[3])
            articles['url'].append(input_df.url[i])
            print(f"appended {article} to articles")
        except:
            print('exeption occured')
            print('this mostly means the article can not be downloaded')

    df = pd.DataFrame(data=articles)
    print(df)
    df.to_csv(to_path, index=False)
    return

if __name__ == '__main__':

    #at most 1000 new articles are crawled
    for i in range(1000):

        #gets new news article
        get_articles()


