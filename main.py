#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cherrypy
from cherrypy.lib import auth_basic
import json
import random

with open('config.json') as json_file:
	data = json.load(json_file)
	data['username']
	data['password']

class Root(object):
	@cherrypy.expose
	def index(self):
		return random.choice([
			'よろづのことは　月見るにこそ慰むものなれ　——《徒然草》',
			'駒並めていざ見に行かむ　故里は雪とのみこそ花は散るらめ　——《古今集》',
			'世の中に絶えて桜のなかりせば　春の心はのどけからまし　——《伊勢物語》',
			'かくばかり恋ひむとかねて知らませば　妹をば見ずぞあるべくありける　——《万葉集》',
			'桜花散らば散らなむ　散らずとて故里人の来ても見なくに　——《古今集》',
			'みかの原わきて流るるいづみ川　いつ見きとてか恋しかるらむ　——《新古今集》',
		])

def validate_password(realm, username, password):
	return username == data['username'] and password == data['password']

conf = {
	'/': {
		'tools.auth_basic.on': True,
		'tools.auth_basic.realm': 'localhost',
		'tools.auth_basic.checkpassword': validate_password,
		'tools.auth_basic.accept_charset': 'UTF-8',
	},
}

if __name__ == '__main__':
	cherrypy.config.update({
			'log.screen': False,
			'log.access_file': 'access.log',
			'log.error_file': 'error.log',
		})
	cherrypy.quickstart(Root(), '/', conf)
