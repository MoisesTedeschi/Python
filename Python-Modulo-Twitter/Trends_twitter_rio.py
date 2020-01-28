#!/usr/bin/env python
# coding: utf-8

# In[4]:


import twitter
import json


# In[5]:


CONSUMER_KEY = 'jQcDAPzXorkWPWx7xQLOkm1e9'
CONSUMER_SECRET = 'PBWJMcnpOuW1xDnCBLOFHbeydCNkXLrTpBTuWcLU5uQCGQ36N1'
OAUTH_TOKEN = '2544081954-JxjB2mUdw3PNnzhboqzyq6nFgKPFCWYw4lfPPyq'
OAUTH_TOKEN_SECRET = '71TP3qkhCXtw1c2nnEVJAfRvuy4a078KVBX9c0cQVYIVV'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)


# In[9]:


#Basicamente os "IDs das localidades" - Site utilizado: http://woeid.rosselliot.co.nz
WORLD_WOE_ID = 1
RIO_WOE_ID = 455825
SAO_PAULO_WOE_ID = 455827
BRAZIL_WOE_ID = 23424768

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
brazil_trends = twitter_api.trends.place(_id=BRAZIL_WOE_ID)
rio_trends = twitter_api.trends.place(_id=RIO_WOE_ID)
sao_paulo_trends = twitter_api.trends.place(_id=SAO_PAULO_WOE_ID)

#print(json.dumps(world_trends, indent=1))


# In[17]:


world_trends_set     = set([trend['name'] for trend in world_trends[0]['trends']])
brazil_trends_set    = set([trend['name'] for trend in brazil_trends[0]['trends']])
rio_trends_set       = set([trend['name'] for trend in rio_trends[0]['trends']])
sao_paulo_trends_set = set([trend['name'] for trend in sao_paulo_trends[0]['trends']])

#Trends do mundo que, também, estão bombando no Brasil
common_trends       = world_trends_set.intersection(brazil_trends_set)

#Trends em tempo real no Rio e SP
common_trends_state = rio_trends_set.intersection(sao_paulo_trends_set)

#Trends pelo mundo e no Rio de Janeiro
common_trends_state_in_rio = rio_trends_set.intersection(world_trends_set)

#Trends pelo mundo e no São Paulo
common_trends_state_in_sp = sao_paulo_trends_set.intersection(world_trends_set)

common_trends_all_inter = common_trends.intersection(common_trends_state_in_rio, common_trends_state_in_sp)

print(common_trends_all_inter)

