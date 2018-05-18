# -*- coding: utf-8 -*-
import os, json, requests, ntlm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urljoin
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

login_date = {}
def login(req):
    return render(req, 'login.html')

def top(req):
    global login_date
    login_date = { 'datetime':dt.now().strftime("%Y/%m/%d %H:%M") }
    return render(req, 'top.html', login_date)

def helpQA(req):
    global login_date
    return render(req, 'helpQA.html', login_date)


def urlRegist(req):
    global login_date
    return render(req, 'urlRegister.html', login_date)

@csrf_exempt
def crawl(req):
    global login_date
    data_dir = './data/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if req.method == 'POST':
      flg = 0      
      URL_LIST = {}
      data = json.loads(req.body.decode('utf-8'))
      keywords = data["keywords"]
      maxpage = data["maxpage"]
      extension = data["extension"]
      print(keywords)

      #要外部リスト化
      URL_LIST1 = [
      "http://www.takara-net.com/ribiyou/cad/dxf/ex-esym_sc-espl.dxf",
      "http://www.takara-net.com/ribiyou/cad/jwc/ex-esym_sc-espl.jwc",
      ]

      URL_LIST2 = [
       "https://www.google.co.jp/search?num=%s&q=%s" % (maxpage, keywords),
      ]
      
      if "ex-esym" in keywords.lower():
         URL_LIST = URL_LIST1
         auth_data = ('takaracad', 'TkrCad')
         flg = 1
      else:
         URL_LIST = URL_LIST2
         auth_data = ('', '')
         flg = 2

      # set cookie
#      cj = CookieJar()
#      opener = build_opener(HTTPCookieProcessor(cj))
#      r = opener.open("https://takaracad:TkrCad@www.takara-net.com/ribiyou/cad/index.html")

      # ログイン処理
      if flg == 1:
          for url in URL_LIST:
            if url:
              arr = url.split("/")
              filename = arr[len(arr)-1]
              print ("get:%s" % (url))
              output = "./data/%s" % (filename)
              res = requests.get(url, auth=auth_data, stream=True)  
              print(res)
              if res.status_code == 200:
                  with open(output, 'wb') as f:
                      for chunk in res.iter_content(chunk_size=1024):
                          if chunk:
                              f.write(chunk)
                              f.flush()
              print ("=>downloaded filesize:" + str(os.path.getsize(output)))
            else:
              print ("=>downloaded complete")
              break
          return render(req, 'top.html', login_date)
      else:
          print ("other URLs")
          for url in URL_LIST:
            if url:
              print(url)
              resp = requests.get(url)
              soup = BeautifulSoup(resp.text, "html.parser")
              link_elem1 = soup.select('.r > a')
              leng = len(link_elem1)
              for i in range(leng):
                  url_text = link_elem1[i].get('href').replace('/url?q=','')
                  url_text2 = url_text.split("&sa=")[0]
                  print ("searched_link: " + url_text2, flush = True)
                  if  url_text2.startswith("http") and not url_text2.endswith("pdf"):
                      try:
                          resp2 = requests.get(url_text2)
#                          resp2.raise_for_status()
                          soup2 = BeautifulSoup(resp2.text, "html.parser")
                          for j in soup2.findAll("a"):
                              if j:
                                  k = j.get("href")
                                  if extension in str(k):
                                      print ( '=>data found: ' + str(k), flush = True )
                                      download_url = urljoin(url_text2, k)
                                      arr = download_url.split("/")
                                      filename = arr[len(arr)-1]
                                      print ("get:%s" % (download_url))
                                      output = "./data/%s" % (filename)
                                      res = requests.get(download_url, auth=auth_data, stream=True)
                                      print(res)
                                      if res.status_code == 200:
                                          with open(output, 'wb') as f:
                                              for chunk in res.iter_content(chunk_size=1024):
                                                  if chunk:
                                                      f.write(chunk)
                                                      f.flush()
                                      print ("=>downloaded filesize: " + str(os.path.getsize(output)))
                                  else:
                                      continue
                              else:
                                  break
                      except:
                         print(resp2.status_code)
                      finally:
                         print("END")
                  else:
                    continue
            else:
              break
          return render(req, 'top.html', login_date)
    else:
      return render(req, 'top.html', login_date)

