import praw

sub = 'subreddit'
r = praw.Reddit(user_agent='posts unread messages to empoknor')

r.login('username', 'password')
for content in r.get_unread():
    print content
    r.submit(sub, title, text='texty', url=None, captcha=None, save=None, send_replies=None, resubmit=None)
    r.mark_as_read() #does this work?