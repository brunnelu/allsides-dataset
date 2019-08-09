import numpy as np
import pandas as pd
import os

datadir = '../topic_url/'

def get_file_path():
    #get file number not existing so far
    #for bigger folder this would be unpractical
    i=0
    while os.path.exists(datadir+str(i)+'.csv'):
        i+=1
    return datadir+str(i)+'.csv'

def get_left_rigth():
    val= input('type how left or right rating is [0][1][2][3][4]: ')
    num = int(val)
    return num

def get_single_article():
    user_input = input('type exit to exit or submit a new url: ')

    if user_input=='exit':
        return (-1,-1)
    
    url = user_input
    rating = get_left_rigth()

    return (url,rating)

def get_topic():
    user_input = input('whats the main topic: ')
    return user_input

def get_subtopic():
    user_input = input('whats the subtopic: ')
    return user_input

def get_articles():
    path = get_file_path()
    articles = {'url':[], 'rating':[],'topic':[], 'subtopic':[]}

    topic = get_topic()
    subtopic = get_subtopic()

    #do-while loop
    while True:
        article = get_single_article()
        if article == (-1,-1):
            break
        else:
            articles['url'].append(article[0])
            articles['rating'].append(article[1])
            articles['topic'].append(topic)
            articles['subtopic'].append(subtopic)
            print(f"appended {article} to articles")

    df = pd.DataFrame(data=articles)
    print(df)
    df.to_csv(path, index=False)
    return

if __name__ == '__main__':
    get_articles()