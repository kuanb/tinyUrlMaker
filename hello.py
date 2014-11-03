
import os
from flask import Flask, redirect, request
app = Flask(__name__)



### Flask tasks

superCounter = 0
superDict = {'999':'http://www.nytimes.com'}

def getNewShort():
	global superCounter
	toRet = superCounter
	superCounter += 1
	return toRet

def addRes(res, url):
	print url
	if url[:7] != 'http://':
		url = 'http://' + url
	superDict[res] = url



### Flask URL-linked activities

@app.route('/')
def showIndex():
	with open('index.html') as f:
		return f.read()

@app.route('/shorter/<url>', methods=['GET'])
def addLongURL(url):
	result = getNewShort()
	addRes(str(result), url)
	return str(result)

@app.route('/min/<miniURL>')
def processShortURL(miniURL):
	print miniURL
	print superDict
	try:
		longURL = superDict[str(miniURL)]
	except KeyError:
		longURL = superDict['999']
	return redirect(longURL, code=302)

if __name__ == '__main__':
    app.run(debug=False)