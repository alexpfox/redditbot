import inspect
import re
import praw

def getURL(contentBody):
    try:
        return re.search("(?P<url>https?://[^\s]+)", contentBody).group("url")
    except AttributeError:
        return "no URL found"
    
def getTitle(contentBody):
    return c.split("\n")[3]

sub = 'subreddit'
r = praw.Reddit(user_agent='posts unread messages to a subreddit')

r.login('username', 'password')
for content in r.get_unread():
    url = getURL(content.body)
    title = getTitle(content.body)
    r.submit(sub, title, text='texty', url=None, captcha=None, save=None, send_replies=None, resubmit=None)
    #r.mark_as_read()
    
