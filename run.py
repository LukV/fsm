#!/usr/bin/python3 -tt
# -*- coding: UTF-8 -*-

import logging
import pprint
from apiclient.discovery import build

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('customsearch', 'v1',
        developerKey='AIzaSyD7l7uaEGGCu2rk-2DolYUqKTSe9SMM774')

    res = service.cse().list(
        q='Frans Steenhoudt',
        cx='015338965408871490949:vypgdlzazf8',
    ).execute()
    pprint.pprint(res)

if __name__ == '__main__':
    main()
