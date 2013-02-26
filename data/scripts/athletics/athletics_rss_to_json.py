import feedparser
import simplejson as json
import argparse
import re

base = "http://www.gocolumbialions.com/rss.dbml?DB_LANG=C&db_oem_id=9600&"

feeds = ["results", "schedules"]

sport_to_rss_feed = {
    'archery': 4048,
    'baseball': 3883,
    'cross_country':3877,
    'fencing': 4049,
    'field_hockey': 4050,
    'football':3885,
    'heavyweight_rowing':4051,
    'lacrosse':3879,
    'lightweight_rowing':4052,
    'mens_basketball':3886,
    'mens_golf':3890,
    'mens_soccer':3884,
    'mens_squash':78095,
    'mens_swimming':4054,
    'mens_tennis':3878,
    'softball':3889,
    'track':4657,
    'volleyball':3874,
    'womens_basketball':3887,
    'womens_golf':3891,
    'womens_soccer':3888,
    'womens_rowing':4053,
    'womens_squash':78195,
    'womens_swimming':4055,
    'womens_tennis':3892,
    'wrestling':3876,
}


def parse_summary(summary):
    r = re.compile('<p>at(.+?)-')
    locations = [item.strip() for item in r.findall(summary)]
    r = re.compile('"(.+?)"')
    article = [item.strip() for item in r.findall(summary)]
    if article:
        article = article[0]
    else:
        article = None
    return article, locations[0]


def individual_sport(feed):
    output = []
    for entry in feed['entries']:
        temp_dict = {}
        temp_dict['published'] = entry['published']
        temp_dict['title'] = entry['title']
        temp_dict['link'] = entry['link']
        article, location = parse_summary(entry['summary'])
        temp_dict['article_link'] = article
        temp_dict['location'] = location
        output.append(temp_dict)
    return output


def get_rss_feeds(fname):
    output = {}
    for key, value in sport_to_rss_feed.iteritems():
        print key
        output[key] = {}
        for rss in feeds:
            feed_url = "%smedia=%s&RSS_SPORT_ID=%d" % (base, rss, value)
            feed = feedparser.parse(feed_url)
            data = individual_sport(feed)
            output[key][rss] = data
    print output
    with open(fname, "w") as f:
        json.dump(output, f)


def main():
    parser = argparse.ArgumentParser(description="""Convert Sport RSS feeds
    and convert to JSON. Requires feedparser, simplejson""")
    parser.add_argument('--output', help="""File to dump resulting JSON dump in""")
    args = parser.parse_args()
    get_rss_feeds(args.output)


if __name__ == "__main__":
    main()
