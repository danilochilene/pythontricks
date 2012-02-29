#!/usr/bin/env python
# coding: utf-8
from functools import wraps
import json
from cherrypy import response, expose

def jsonify(func):
	'''JSON decorator for CherryPy'''
	def wrapper(*args, **kw):
		value = func(*args, **kw)
		response.headers["Content-Type"] = "application/json"
		return json.dumps(value)
	
	return wrapper

def examplo_data():
	from cherrypy import quickstart
	from datetime import datetime
	class Time:
		@expose
		@jsonify
		def index(self):
			now = datetime.now()
			return {
				"date" : now.strftime("%Y-%m-%d"),
				"time" : now.strftime('%H:%M'),
				"day"  : now.strftime('%A'),
			}
	quickstart(Time())

def caminho():
	from cherrypy import quickstart
	from sys import path
	class Caminho:
		@expose
		@jsonify
		def index(self):
			self.caminho = path

			return {
				"Caminho" : self.caminho
			}
	quickstart(Caminho())

if __name__=='__main__':
	caminho()