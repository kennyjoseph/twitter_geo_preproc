#!/usr/bin/env python

from distutils.core import setup

setup(name='tweet_geocode',
      version='1.0',
      description='Package for geocoding tweets. All code from Brendan O\'Connor, forked from his repo. ' +
                  'Take a look at install_script.sh to install the required c/c++ libs (geos and spatialindex)',
      author='Kenneth Joseph',
      author_email='josephkena@gmail.com',
      url='https://github.com/kennyjoseph/twitter_geo_preproc',
      requires=['shapely', 'simplejson','rtree','yajl'],
      packages=['tweet_geocode'],
      package_data={'tweet_geocode': ['data/*']},
     )