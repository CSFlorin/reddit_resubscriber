""" Subscribe to all subreddits from your old account on your new account """

import praw

old_account = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='testscript by /u/fakebot',
                     username='')

subscribed = list(old_account.user.subreddits(limit=None))

new_account = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='testscript by /u/fakebot',
                     username='')

for i in range(len(subscribed)):
                     sub = subscribed[i]
                     print(str(i+1) + " out of " + str(len(subscribed)) + ": " + str(sub))
                     new_account.subreddit(str(sub)).subscribe()
                     
print(str(old_account.user.me()) + "\'s subscriptions have been copied to " + str(new_account.user.me()))
