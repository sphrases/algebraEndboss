#!/usr/bin/env python
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from twython import Twython
CONSUMER_KEY = 'ENTER CONSUMER_KEY'
CONSUMER_SECRET = 'ENTER CONSUMER_SECRET'
ACCESS_KEY = 'ENTER ACCES_KEY'
ACCESS_SECRET = 'ENTER ACCES_SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

search = api.search(q='#Algebra_Endboss', count=100)
          

tweets = search['statuses']

orig_stdout = sys.stdout	#saves ooriginal stdout
f = open('index.html', 'a') 	#appends to file "out.txt" a- append, w- overwrite
sys.stdout = f	#changes standard oudput of print

inc = 0

#define variables in global context
global tweetId
global tweetTime 
global userHandle 
global tweetText 
global splittedText
global functionArray
global tweetFunction
global isTweetOK
isTweetOK = 1

def fetchTweets():
	global tweetId
	tweetId = tweet['id_str']
	global tweetTime 
	tweetTime = tweet['created_at']
	global userHandle 
	userHandle = tweet['user']['screen_name']
	global tweetText 
	tweetText = tweet['text']
	return;

	
	
def splitTweet():
	global splittedText
	splittedText = tweetText.split(' ')
	try:
		global functionArray
		functionArray = 1 + splittedText.index("function");
		
	except ValueError:
		
		tweetFunction = "no function"
	
	return;
	
	
	
def checkTweet():
	if tweetId in open('answeredtweets.txt').read():
		global isTweetOK
		isTweetOK = 0;
	else:
		checkFile=open('answeredtweets.txt','a') 
		checkFile.write(tweetId +'\n')
		
		isTweetOK = 1;
	return;
		
def printTweets():
	if isTweetOK == 1:
		print "<ul> <li> id:  	" 	+ tweetId		+ "</li>"
		print "<li> function: 	" 	+ tweetFunction + "</li>"
		print "<li> time:  		" 	+ tweetTime 	+ "</li>"
		print "<li> handle:  	" 	+ userHandle 	+ "</li>"
		print "<li> tweet:  	"	+ tweetText		+ "</li> </ul>" + '\n\n\n'
		print "________________________________________________________________________________"
	return;
 
	
	
	
def answerTweet():
	if isTweetOK == 1:
		global tweetFunction
		tweetFunction = splittedText[functionArray]
		os.system("../plotter_script/drawPlot " + tweetFunction)
		
		
		photo = open('../plotted/'+tweetFunction+'.png', 'rb')
		response = api.upload_media(media=photo)
		api.update_status(status='@'+userHandle+' Hey, I plotted this for you: #Algebra_Endboss ', media_ids=[response['media_id']], in_reply_to_status_id=tweetId)
	return;
	
	
	
#Main
for tweet in tweets:
	try:
		fetchTweets();
		checkTweet();
		splitTweet();
		answerTweet();
		printTweets();
		inc += 1;
	except:
		pass
		
		
		
sys.stdout = orig_stdout
f.close()
#print "{} tweets dumped".format(inc)
