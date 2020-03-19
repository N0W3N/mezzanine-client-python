#!/usr/bin/env python

"""
Mezzanine Client Example: Publish a new blog post

See: https://github.com/gcushen/mezzanine-client-python

Notes:
- We assume OAuth app id and secret are provided via environment variables MZN_ID and MZN_SECRET.
- Alternatively, include them in a tuple below like: Mezzanine(('my_app_id', 'my_app_secret')).

Copyright (C) 2016 George Cushen.
License: https://github.com/gcushen/mezzanine-client-python/blob/master/LICENSE
"""

import pprint
import datetime

# Python 2 and 3 compatible input
from builtins import input

from mezzanine_client import Mezzanine
from mezzanine_client.utils import str_header, str_green


# Initialise Mezzanine API client
api = Mezzanine()

# Input blog article
print(str_header('Publish a new blog post...'))
title = input(str_header('Title: ')).strip()
content = input(str_header('Content: ')).strip()
categories = input(str_header('Categories (comma separated): ')).strip()

blog_post_data = {'title': title,
                  'content': content,
                  'categories': categories,
                  'publish_date': datetime.datetime.utcnow().isoformat()
                  }

# Publish new blog article via POST to API
response = api.create_post(blog_post_data)
post_id = response['id']
pprint.pprint(response)
if 'id' in response:
    print(str_green(f'Blog post successfully published with ID #{post_id}'))

# TODO nothing to do here for the moment