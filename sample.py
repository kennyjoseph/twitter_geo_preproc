import tweet_geocode, codecs
import simplejson as json

tweet_json = codecs.open("tweet_sample.json","r","utf8").readlines()
for line in tweet_json:
	jsn = json.loads(line)
	geo_data = tweet_geocode.get_geo_record_for_tweet(jsn)
	if geo_data is not None:
		print tweet_geocode.geocode_world_country(geo_data)
		print tweet_geocode.geocode_us_county(geo_data)