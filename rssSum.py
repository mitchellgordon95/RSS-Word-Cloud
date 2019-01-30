"""
Takes a link to an RSS feed and produces a word cloud of its linked content.

Copyright (C) 2015  Nicholas Rutherford

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import feedparser
from bs4 import BeautifulSoup
from wordcloud import WordCloud

import urllib2
import sys

# Get the feed
FEED = raw_input("Enter the url of the feed: ")

# Get all the urls:
print("Retrieving rss feed...")
feedObj = feedparser.parse(FEED)
titles = [item['title'] for item in feedObj['items']]

print("\nConstructing cloud...")

# Construct the word cloud
wordcloud = WordCloud(width=800, height=400).generate(' '.join(titles))
wordcloud.to_file("image.png")
print("Done!")
