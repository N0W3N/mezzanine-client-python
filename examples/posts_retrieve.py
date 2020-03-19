#!/usr/bin/env python

# TODO change information

"""
Mezzanine Client Example: Retrieve a blog post

See: https://github.com/gcushen/mezzanine-client-python

Notes:
- We assume OAuth app id and secret are provided via environment variables MZN_ID and MZN_SECRET.
- Alternatively, include them in a tuple below like: Mezzanine(('my_app_id', 'my_app_secret')).

Copyright (C) 2016 George Cushen.
License: https://github.com/gcushen/mezzanine-client-python/blob/master/LICENSE
"""

import sys

from mezzanine_client import Mezzanine
from mezzanine_client.utils import str_header, str_blue

# TODO reformat display_post() print statements

# Retrieve and display specified blog post
def display_post(post_id):
    api = Mezzanine()
    post = api.get_post(int(post_id))
    print(str_blue('{}'.format(post['title'])))
    print(post['content'])
    print('')
    print(str_blue('Categories:'))
    for category in post['categories']:
        print(category['title'])


# CLI
if __name__ == "__main__" and len(sys.argv) > 1:
    display_post(sys.argv[1])
else:
    post_id = input(str_header('Please enter the ID of the blog post to retrieve: ')).strip()
    display_post(post_id)
