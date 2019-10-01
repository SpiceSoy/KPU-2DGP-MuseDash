#-*- coding: utf-8 -*- 
# Osu Bitmap Parser

import os
import parse

class FileNotFound(Exception): 
	pass

class FileNotLoaded(Exception):
	pass

def get_line_prop(line):
	result = parse.parse("{}:{}",line)
	key = result[0]
	item = result[1].strip()
	return {key : item}

def get_line_timing(line):
	result = parse.parse("{},{},{},{},{},{},{},{}",line)
	return None

def get_line_hitobject(line):
	result = parse.parse("{},{},{},{},{},{}:{}:{}:{}:",line)
    #HitObject Syntax
    # x,y,time,type,hitSound...,extras
    # type 1 : 
	return None

def get_line_none(line):
	return None

line_type = ("General","Editor","Metadata","Difficulty","Events","TimingPoints","HitObjects")

line_func = {"General" : get_line_prop,
			 "Editor" : get_line_none, 
			 "Metadata" : get_line_prop, 
			 "Difficulty" : get_line_prop,
			 "Events" : get_line_none,
			 "TimingPoints" : get_line_timing,
			 "HitObjects" : get_line_hitobject}

def parse_file(text_data):
	result_dic = {}
	line_type = None
	while True:
		line = text_data.readline()
		#line 파싱 코드
		if not line.strip():
			continue
		result = parse.parse("[{}]",line)
		if result != None:
			# 문단 파악
			line_type = result[0]
		else:
			print(line_type)
			if line_type == "General" or line_type == "Metadata" or line_type == "Difficulty":
				print(get_line_prop(line))
			# 라인 읽기
			pass
		if not line: break
	return 

class MusicBitmap:
	def __init__(self, url = None):
		if url != None:
			self.load_file(url)

	def load_file(self,url):
		if url != None:
			self.__text_data = open(url,'r')
		else:
			raise FileNotFound()
	
	def __parse_file(self):
		if self.__text_data != None:
			pass
		else:
			raise FileNotLoaded()

#단위 테스트 코드
if __name__ == "__main__":
    debug_url = os.path.abspath("Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")
    text_data = open(debug_url,'r',encoding='UTF8')
    parse_file(text_data)