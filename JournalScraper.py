#!/usr/bin/env python3
"""
JournalScraper to get all articles from journal issue in one pdf.
Supported Journals:
-Nature

MIT License

Copyright (c) 2022 Tijs van Lieshout

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Uses:
<The terminal interactions with this script go here>
"""

# Metadata
__title__ = "JournalScraper to get all articles from journal issue in one pdf"
__author__ = "Tijs van Lieshout"
__created__ = "2023-01-13"
__updated__ = "2022-01-13"
__maintainer__ = "Tijs van Lieshout"
__email__ = "t.van.lieshout@umcg.nl"
__version__ = 0.1
__license__ = "GPLv3"
__description__ = f"""{__title__} is a python script created on {__created__} by {__author__}.
                      Last update (version {__version__}) was on {__updated__} by {__maintainer__}.
                      Under license {__license__} please contact {__email__} for any questions."""

# Imports
import argparse
import os

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def main(args):
  response=requests.get(args.url)

  if response.status_code != 200:
    print(f"Response status code = {response.status_code}")
    return

  soup = BeautifulSoup(response.text, "html.parser")
  for anchor in tqdm(soup.findAll('a', href=True)):
    if "/articles/" in anchor['href']:
      article_id = anchor['href'].split("/")[-1]
      full_url = args.url.split(".com")[0] + ".com" + anchor['href'] + ".pdf"
      #TODO: turn article download back on once finished
      #article = requests.get(full_url, stream=True)

      path = f"{article_id}.pdf"
      if not os.path.exists(path):
        with open(path, 'wb') as f:
          f.write(article.content) 


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-u", "--url", type=str, required=True, help="url to download journal from") 
  args = parser.parse_args()
  
  main(args)
