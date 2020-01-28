#!/usr/bin/env python
# coding: utf-8

# In[11]:


import twitter
import json
from urllib.parse import unquote
from collections import Counter
from prettytable import PrettyTable

#Credenciais de acesso ao Twitter

CONSUMER_KEY = 'jQcDAPzXorkWPWx7xQLOkm1e9'
CONSUMER_SECRET = 'PBWJMcnpOuW1xDnCBLOFHbeydCNkXLrTpBTuWcLU5uQCGQ36N1'
OAUTH_TOKEN = '2544081954-JxjB2mUdw3PNnzhboqzyq6nFgKPFCWYw4lfPPyq'
OAUTH_TOKEN_SECRET = '71TP3qkhCXtw1c2nnEVJAfRvuy4a078KVBX9c0cQVYIVV'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

#Eu não apoio - Só para constar. No entanto nesse dia, certamente, o atual Governo meteu a mão no bolso
#para pagar uma galera para fazer um "Twittaço" favorável a esta vergonha de reforma que só vai beneficiar
#Os safados corruptos do executivo, legislativo, judiciário e bancos, é claro.
q = '#EuApoioNovaPrevidencia'

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

for _ in range(50):
    print('Tamanho do Status',len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e:
        break
        
    kwargs = dict([kv.split('=') for kv in unquote(next_results[1:]).split("&")])
    
    search_results = twitter_api.search.tweets(**kwargs)
    
    statuses += search_results['statuses']

#Mostrar resultados
#print(json.dumps(statuses[0],indent=1))

status_texts = [status['text']
                for status in statuses]

screen_names = [user_mention['screen_name']
                for status in statuses
                   for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in statuses
               for hashtag in status['entities']['hashtags']]

words = [w
         for t in status_texts
            for w in t.split()]

for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10])
    print()
    
#print(json.dumps(status_texts[0:5],indent=1))
#print(json.dumps(screen_names[0:5],indent=1))
#print(json.dumps(hashtags[0:5],indent=1))
#print(json.dumps(words[0:5],indent=1))

#Saida em formato de tabela
for label, data in(('Words', words),
                  ('Screen Name', screen_names),
                  ('Hashtag', hashtags)):
    pretty_table = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    
    [pretty_table.add_row(kv) for kv in c.most_common()[:10]]
    pretty_table.align[label],pretty_table.align['Count'] = '1', 'r'
    print(pretty_table)

