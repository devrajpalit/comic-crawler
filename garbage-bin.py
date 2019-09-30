import urllib
from bs4 import BeautifulSoup
previous_comic_url = 'http://www.garbagebinstudios.com/comic-strips.html' #the base url
while previous_comic_url != 'http://www.garbagebinstudios.com/comic-strips/misc.html': #after the last comic the url shifts to misc
	response = urllib.urlopen(previous_comic_url.encode('utf-8'))
	html = response.read()
	soup = BeautifulSoup(html)
	comic_tag = soup.find('a', attrs={'class':'cm-image-previewer cm-previewer'})
	comic_url = r'http://www.garbagebinstudios.com'+comic_tag['href']
	previous_comic_tag = soup.find('div', attrs={'style':'padding-right:20px;float:right;padding-top:7px;'}).a
	previous_comic_url = 'http://www.garbagebinstudios.com'+previous_comic_tag['href']
	image_name = comic_url[comic_url.find('/1/')+3:]
	print 'Downloading ' + image_name + ' Now'
	urllib.urlretrieve(comic_url.encode('utf-8'), image_name.encode('utf-8'))
	print 'Download Complete'
