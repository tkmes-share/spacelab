# -*- coding: utf-8 -*-
import requests


def parse(self, response):
    #url = 'http://search.yahoo.co.jp/search?p=[series7]&amp;ei=UTF-8'
    url = 'http://search.yahoo.co.jp/search'
    
    params = {'p': 'python', 
              'search.x': '1',
              'fr': 'top_gal_sa',
              'tid': 'top_gal_sa',
              'ei': 'utf-8',
              'aq': '',
              'oq': '',
              'afs': '',
              }
    
    response = requests.get(url, params) 
    
    print ( response.text ) 
    print ( 'end of crawring' )


