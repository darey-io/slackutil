# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:14:45 2017

@author: dare
"""

import os
from slacker import Slacker

API_KEY = os.environ.get('API_KEY')
slack = Slacker(API_KEY)

# Get users list
response = slack.users.list()
users = response.body['members']

#extract members' email
def x_members():
    for i in users:
        try:
            full_name = i['profile']['real_name']
            email = i['profile']['email']
            print(email)
        except KeyError:
            ('element not in there')
x_members()
#TODO

#find a way to extract emails per channel
#find a way to send email to each member of that channel

