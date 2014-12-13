A fork of [Brendan O'Connor's](http://brenocon.com) Github project for [geoprocessing of tweets](https://github.com/brendano/twitter_geo_preproc)

This is a forked version where I turned the barebones of the geocoding portions into a package and made it a bit easier to install. It is *NOT* my code.

Quoting from Brendan's description of the package:

```

A little Python geocoding library.  It can load a geojson database of
geographic features, then query a (lon,lat) coordinate for what feature it is
contained in.  It has been used successfully with library versions:

shapely 1.2.16 (https://pypi.python.org/pypi/Shapely)
rtree 0.7.0 (https://pypi.python.org/pypi/Rtree)

libgeos: geos-3.3.5 (c/c++ dependency for shapely)
libspatialindex: spatialindex-src-1.7.1 (c/c++ dependency for rtree)

Some sample geojson databases it has been used with are available at:
http://brenocon.com/geocode/

```

Sample usage
============

First, run install_script.sh, which appears to work fine on at least Ubuntu 12.04

Then, run ```python setup.py install```

Try running ```sample.py```, you'll hopefully get something like this:

```
geodb loading /Users/kjoseph/git/thesis/twitter_geo_preproc/tweet_geocode/data/world.json
None
geodb loading /Users/kjoseph/git/thesis/twitter_geo_preproc/tweet_geocode/data/counties.tiger2010.json
{'us_county': {'fp10': u'001', 'geoid10': u'11001', 'namelsad': u'District of Columbia'}, 'country': u'USA', 'user_location': u'Washington, DC USA', 'lonlat': [-77.001464, 38.927313], 'loc_type': 'OFFICIAL', 'us_state': {'fp10': u'11', 'abbrev': 'DC'}}
None
{'loc_type': 'OFFICIAL', 'user_location': u'Melbourne', 'lonlat': [114.171825, 22.308411]}
None
{'us_county': {'fp10': u'043', 'geoid10': u'17043', 'namelsad': u'DuPage County'}, 'country': u'USA', 'user_location': u'West Chicago', 'lonlat': [-88.188283, 41.883195], 'loc_type': 'OFFICIAL', 'us_state': {'fp10': u'17', 'abbrev': 'IL'}}
None
{'us_county': {'fp10': u'049', 'geoid10': u'28049', 'namelsad': u'Hinds County'}, 'country': u'USA', 'user_location': u'Forest, Ms', 'lonlat': [-90.266261, 32.24418], 'loc_type': 'OFFICIAL', 'us_state': {'fp10': u'28', 'abbrev': 'MS'}}
```

Sorry, I just took a random sample of data, so there's no rhyme or reason to it. 


Lemme know if you have issues!
