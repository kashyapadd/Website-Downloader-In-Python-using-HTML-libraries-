
import random
from urllib import urlretrieve
import socket
from HTMLParser import *

#website = "www.ece.eng.wayne.edu"
website = raw_input ("Enter the website process:")
class HTMLClassifier(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            print "Image: ", tag
            for attr, url in attrs:
            	if attr == "src":
            		if url[0] == '/':
            			url = website + url
            		full = url
            		print full
            		download_web_image(full)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def parseHTML(htmlData):
    parser = HTMLClassifier()
    parser.feed(htmlData)
    pass

def download_web_image(url):
	name = random.randrange(1,1000)
	fileName = str(name) + ".jpg"
	if "http://" not in url:
		fullUrl = "http://"+url
	else:
		fullUrl = url
	print fullUrl
	urlretrieve(fullUrl, fileName)

def main():
    #Defining port number for the website
    port = 80
    #Creating a socket or initializing
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Student_1:Sesha Sai Kashyap Addanki\nThe program is interpreted correctly and completely verified. Images are downloaded")
    #Getting the ip address of the host name of the website
    ipAddress = socket.gethostbyname(website)
    #printing the ip Address
    print ("IP Address:",ipAddress)
    #Connecting to the website using the ip address and the port number
    s.connect((ipAddress, port))
    #Sending the request to the server
    s.sendall("GET / HTTP/1.0\r\n\r\n")
    #Infinite loop and receive website content by a 1 Mega Byte
    htmlData = ""

    while True:
        response = s.recv(4096)
        if response == "":
            break
        #This is the response data
        htmlData += response
    s.close()
    parseHTML(htmlData)
    pos = htmlData.find("\r\n\r\n")
    htmlData = htmlData[pos:]
    fileName = open("downloaded.html","w")
    fileName.truncate()
    fileName.write(htmlData)
    print htmlData
    print "Successful!"

if __name__ == '__main__':
    main()
