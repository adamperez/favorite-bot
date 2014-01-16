## favorite-bot
favorite-bot is a simple command line program that will favorite tweets based on a provided keyword.

Using the 'twitter' python library (https://pypi.python.org/pypi/twitter/1.10.0), as well as a development app (https://dev.twitter.com/apps), a user will be able to use this bot in command line.

The bot takes two arguments:

1.  a keyword string
2.  an integer represnting the number of tweets to favorite

#### Example 
> import favorite_bot

> favorite_bot.auto_fav('github',13)

The above example will favorite the first 13 tweets that have the keyword 'github' in them.
