import re
import praw


def getURL(contentBody):
    try:
        return re.search("(?P<url>https?://[^\s]+)", contentBody).group("url")
    except AttributeError:
        return "no URL found"
    
def getTitle(contentBody):
    return contentBody.split("\n")[3]


SUB = 'EmpokNor'
r = praw.Reddit(user_agent='posts unread messages to SUB')

r.login('user', 'password')
for content in r.get_unread():
    print content.body
    url = getURL(content.body)
    title = getTitle(content.body)
    r.submit(SUB, title, text=None, url=url, captcha=None, save=None, send_replies=None, resubmit=None)
    content.mark_as_read()