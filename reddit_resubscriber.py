"""
Subscribe to all subreddits from your old account on your new account
Run with args old_client_id, old_client_secret, old_pw, old_username, new_client_id, new_client_secret, new_pw, new_username
"""

import praw
import sys
# TODO: Parallelize according to number of threads

def main():
    old_account = praw.Reddit(client_id=sys.argv[1],
                         client_secret=sys.argv[2],
                         password=sys.argv[3],
                         user_agent='testscript by /u/fakebot',
                         username=sys.argv[4])

    subscribed = list(old_account.user.subreddits(limit=None))

    new_account = praw.Reddit(client_id=sys.argv[5],
                         client_secret=sys.argv[6],
                         password=sys.argv[7],
                         user_agent='testscript by /u/fakebot',
                         username=sys.argv[8])

    for i in range(len(subscribed)):
                         sub = subscribed[i]
                         print(str(i+1) + " out of " + str(len(subscribed)) + ": " + str(sub))
                         new_account.subreddit(str(sub)).subscribe()


    print(str(old_account.user.me()) + "\'s subscriptions have been copied to " + str(new_account.user.me()))

if __name__ == "__main__":
    if len(sys.argv) != 9:
        print("Run reddit_resubscriber with all eight parameters:\n    old_client_id,\n    old_client_secret,\n    old_pw,\n    old_username,\n    new_client_id,\n    new_client_secret,\n    new_pw,\n    new_username")
    else:
        main()
