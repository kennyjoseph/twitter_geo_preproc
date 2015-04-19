from tweet_geocode import state_codes, geodb
import re
from pkg_resources import resource_filename
### Lazy loading of geo databases

_dbs = {}

OneCoord = r'([-+]?\d{1,3}\.\d{3,})'
Separator= r', ?'
LatLong = re.compile(OneCoord + Separator + OneCoord, re.U)


def lookup(myjson, k):
  # return myjson[k]
  if '.' in k:
    # jpath path
    ks = k.split('.')
    v = myjson
    for k in ks: v = v.get(k,{})
    return v or ""
  return myjson.get(k,"")

def us_county():
    global _dbs
    if not _dbs.get('us_county'):
        _dbs['us_county'] = geodb.GeoDB.load_geojson_files([resource_filename('tweet_geocode','data/counties.tiger2010.json')])
    return _dbs['us_county']
        
def world_country():
    global _dbs
    if not _dbs.get('world_country'):
        _dbs['world_country'] = geodb.GeoDB.load_geojson_files([resource_filename('tweet_geocode','data/world.json')])
    return _dbs['world_country']

### Geocode into a "geo info" dict

def geocode_us_county(geodict):
    lon,lat = geodict['lonlat']
    f = us_county().query_point(lon,lat)
    if f:
        geodict['us_state'] = {}
        geodict['us_state']['fp10'] = f['properties']['STATEFP10']
        geodict['us_state']['abbrev'] = state_codes.fips2postal.get(geodict['us_state']['fp10'])
        geodict['us_county'] = {}
        geodict['us_county']['fp10'] = f['properties']['COUNTYFP10']
        geodict['us_county']['namelsad'] = f['properties']['NAMELSAD10']
        geodict['us_county']['geoid10']  = f['properties']['GEOID10']
    return geodict

def geocode_world_country(geodict):
    lon,lat = geodict['lonlat']
    f = world_country().query_point(lon,lat)
    if f:
        geodict['country'] = f['properties']['ISO3']
    return geodict

def get_geo_record_for_tweet(tweet):
    geo = lookup(tweet, 'geo')
    if geo and geo['type'] == 'Point':
        lat,lon  = geo['coordinates']
        loc_type = 'OFFICIAL'
    else:
        loc = lookup(tweet, 'user.location').strip()
        if not loc:
            return None
        m = LatLong.search(loc.encode('utf8'))
        if not m:
            return None
        lat,lon = m.groups()
        loc_type = 'REGEX'
    try:
        lat=float(lat)
        lon=float(lon)
    except ValueError:
        return None

    if (lat,lon)==(0,0) or lat < -90 or lat > 90 or lon < -180 or lon > 180:
        return None

    record = {}
    record['lonlat'] = [lon,lat]
    record['loc_type'] = loc_type
    record['user_location'] = lookup(tweet, 'user.location')
    return record
