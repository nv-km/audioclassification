# -*- coding: utf-8 -*-
import eyed3

#Remove logs
eyed3.log.setLevel("ERROR")

def isMono(filename):
	audiofile = eyed3.load(filename)
	return True

def getGenre(filename):
	audiofile = eyed3.load(filename)
	#print(filename.split(".")[0].split("/")[2])
	#No genre
	#if not audiofile.tag.genre:
	#	return None
	#else:
	return filename.split(".")[0].split("/")[2]


	