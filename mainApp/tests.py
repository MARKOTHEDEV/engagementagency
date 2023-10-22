from django.test import TestCase

# Create your tests here.


list_of_allowed_sites ='discordchatterscommunity.org,web-production-e81c.up.railway.app,www.discordchatterscommunity.org,localhost,web-production-da67.up.railway.app,engagementagency.org'.split(',')
ALLOWED_HOSTS = list_of_allowed_sites
def toTrusted(site_url):return f'https://{site_url}'
a = list(map(toTrusted,list_of_allowed_sites))


print(a)