# AllSides Dataset
This repo contains a part of the AllSides Dataset and methods to add more data or crawl the news articles.
In the topic_url folder files with url, rating, topic and subtopic are saved. After running pull article.py  new news sites found in files from topic_url are downloaded. filemapping.tsv contains a table consiting of the columns 'Title of Headline Roundup', Topics, Date and File#, which specify each file found in topic_url

## Code
In the code subfolder one can find a python file to create new topics (get_topic_url.py) and a file to  automatically pull artiles. To craw articles newspaper3k is used. To install newspaper3k follow the guide on https://github.com/codelucas/newspaper/. 

to create new articles simply cd into the code subfolder and run either 
```
python3 get_topic_url.py
```

or
```
python3 pull_article.py
```


