from sys import argv
import urllib.request
from bs4 import BeautifulSoup
import photos
import clipboard
import os
from objc_util import *
import threading
import ui
import sound

def  again(sender) :
	sound.play_effect('ui:click3')
	html = clipboard.get()                                                                             #Replace for debugging
	f = urllib.request.urlopen(html)                                                                   #Get the html of the instagram post
	htmlSource = f.read()                                                                              #Read it
	soup = BeautifulSoup(htmlSource, 'html.parser')                                                    #Parse it
	v['textview'].text = (soup.title.text)                                                             #Print the text of the post
	metaag = soup.find_all('script')                                                                   #Search for the script part of the html
	script2 = str(metaag)                                                                              #Convert it into a string
	substring = "display_url" 
	counts = script2.count(substring)                                                                  #Count the number of times display-url appears
	metaTag = soup.find_all('meta', {'property': 'og:video'})                                          #Find if there's a video in the post
	if metaTag : #If video
		v['textview'].text = ('Downloading vidéo...')                                                    #Update print 
		#metaTag = soup.find_all('meta', {'property': 'og:video'})
		imgURL = metaTag[0]['content']                                                                   #Take the first one in the post
		urllib.request.urlretrieve(imgURL, 'fileName.mp4') 
		PHPhotoLibrary = ObjCClass('PHPhotoLibrary')
		PHAssetChangeRequest = ObjCClass('PHAssetChangeRequest')
		def add_video():
			lib = PHPhotoLibrary.sharedPhotoLibrary()
			url = nsurl('fileName.mp4')                                                                    #Name of local video file
			def change_block():
				req = PHAssetChangeRequest.creationRequestForAssetFromVideoAtFileURL_(url)
			def perform_changes():
				lib.performChangesAndWait_error_(change_block, None)
			t = threading.Thread(target=perform_changes)
			t.start()
			t.join()
		if __name__ == '__main__':
			add_video() 
		v['textview'].text =  ('Vidéo téléchargée dans votre galerie')
		os.remove('fileName.mp4')                                                                       #Clear files
	else :	
		if counts == 1 :                                                                                #if only one img
			metaTag = soup.find_all('meta', {'property': 'og:image'})
			imgURL = metaTag[0]['content']
			urllib.request.urlretrieve(imgURL, 'fileName.jpg')
			v['textview'].text = ('Image téléchargée dans votre galerie')
			photos.create_image_asset('fileName.jpg')
			os.remove('fileName.jpg')
		elif counts > 1 :                                                                               #If multiples img
			txt = soup.select('script[type="text/javascript"]')[3] 
			texte = txt.get_text()
			fille = open("tet.txt", 'w')
			fille.write(texte)
			fille.close()
			g = open('tet.txt','r')
			data=''.join(g.readlines())
			le1 = 0
			le2 = 0
			hturl = open('url.html', 'w')
			still_looking = True
			while still_looking:
				still_looking = False
				dat = data.find('play_url', le1)
				det = data.find('play_resources', le2)
				if dat >= le1:
					le1 = dat + 1
					still_looking = True                
				if det >= le2:
					hturl.write(data[dat:det])
					le2 = det + 1
					still_looking = True
			hturl.close()
			hturl2 = open('url.html', 'r')
			dete = ''.join(hturl2.readlines())
			le11 = 0
			le22 = 0
			urls = []
			still_looking2 = True
			while still_looking2:
				still_looking2 = False
				dat2 = dete.find('https://instagram', le11)
				det2 = dete.find('","dis', le22)
				if dat2 >= le11:
					urls.append(dat2)
					le11 = dat2 + 1
					still_looking2 = True                
				if det2 >= le22:
					urls.append(dete[dat2:det2])
					le22 = det2 + 1
					still_looking2 = True	
			hturl2.close()
			imgs = len(urls)
			nbind = imgs                                                                               
			nbindr = 3                                                                                 
			images = 1
			while nbindr < imgs:
				#print(urls)
				urllib.request.urlretrieve(urls[nbindr], 'photo.jpg')
				photos.create_image_asset('photo.jpg')
				v['textview'].text =  ('Image ' + str(images) + ' téléchargée dans votre galerie')
				nbindr = nbindr +2
				images += 1
			v['textview'].text = ("C'est bon")
			os.remove('photo.jpg')                                                                         #Remove all traces
			os.remove('tet.txt')
			os.remove('url.html')
	sound.play_effect('game:Ding_3')                                                                   #Sound for done
		
v = ui.load_view('insta')
v.present('sheet')
