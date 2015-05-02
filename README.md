# redditbot
A reddit bot for /r/empoknor

This bot currently receives URL links from posts via private message from any user.
It then reposts the private message content to r/empoknor, a private subreddit I use with my friends.

The eventual goal is to get this bot posting every time a new video link is recieved via PM, checking every 2 minutes so that a backlog is not created. 

The bot interprets the body of the message intelligently. When shared via share function on reddit it parses the fifth(?) line as the title of the new post. It uses regex to find the URL inside content.body and posts it as a link.

