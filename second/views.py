from django.shortcuts import render
from django.http import HttpResponse

from lxml import html
import requests
import json

# Create your views here.

headers = {
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'login-user=joyerque; nforum[UTMPUSERID]=joyerque; nforum[PASSWORD]=tVLNEwVPqsrjM4'
              'iF2%2F6iKQ%3D%3D; Hm_lvt_38b0e830a659ea9a05888b924f641842=1473561810; Hm_lpvt_38b0e83'
              '0a659ea9a05888b924f641842=1473561830; nforum[UTMPKEY]=73159628; nforum[UTMPNUM]=4551',
}
base_url = 'https://bbs.byr.cn/'


def topten(request):
    home_url = 'https://bbs.byr.cn/default?_uid=joyerque'
    top_ten_title_path = '//li[@id="topten"]/div/ul/li/@title'
    top_ten_link_path = '//li[@id="topten"]/div/ul/li/a/@href'

    page = requests.get(home_url, headers=headers)
    tree = html.fromstring(page.text)
    top_ten_title = tree.xpath(top_ten_title_path)
    top_ten_link = tree.xpath(top_ten_link_path)

    list = []
    for i in range(0, len(top_ten_title)):
        a = {"title": top_ten_title[i], "link": top_ten_link[i]}
        list.append(a)

    res = json.dumps(list)
    return HttpResponse(res)


def article(requset, link):
    url = base_url + link
    floor_path = '//tr[@class="a-body"]/td[@class="a-content"]/div[@class="a-content-wrap"]/text()'

    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.text)
    floors = tree.xpath(floor_path)
    list = []
    for floor in floors:
        # print(floor)
        list.append(floor)

    res = json.dumps(list)
    return HttpResponse(res)

    # if __name__ == '__main__':
    #     article(None, "/article/Food/469542")
