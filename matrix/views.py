from django.shortcuts import render
from django.http import HttpResponse
from lxml import html
from .models import Article
import requests
import json_utils
import json


# Create your views here.

def get_all_text(element):
    res = element.text
    if res is None:
        res = ""

    children = element.getchildren()
    if len(children):
        for child in children:
            res += get_all_text(child)

            tail = child.tail
            if tail is not None:
                res += tail

    return res.strip()


def parse_page(page_url, should_print=False):
    if page_url is None:
        return

    page = requests.get(page_url)
    x = html.fromstring(page.text)

    article_path = "//article"
    articles = x.xpath(article_path)

    header_path = "header[@class='entry-header']"
    title_and_href_path = "h1/a"
    time_node_path = "div/span/a/time"
    content_path = "div[@class='entry-content']"

    for article in articles:
        article_new = Article()

        # header
        header = article.find(header_path)
        if header is None:
            continue

        title_node = header.find(title_and_href_path)
        link = None
        title = None
        if title_node is not None:
            link = title_node.get("href")
            title = title_node.text

            article_new.article_link = link
            article_new.article_title = title

        time_node = header.find(time_node_path)
        publish_time = None
        publish_time_normal = None
        if time_node is not None:
            publish_time = time_node.get("datetime")
            publish_time_normal = time_node.text

            article_new.publish_time = publish_time
            article_new.publish_time_normal = publish_time_normal

        # content
        content = article.find(content_path)
        if content is None:
            continue

        text = get_all_text(content)
        article_new.article_description = text
        article_new.save()

        if should_print:
            print("link >> " + link)
            print("title >> " + title)
            print("publish_time >> " + publish_time)
            print("text >> " + text)

        print("<--------------------------------->")

    previous_link_path = "//div[@class='nav-previous']/a/@href"
    previous_link = x.xpath(previous_link_path)
    if len(previous_link):
        print("previous >> " + previous_link[0])
        return previous_link[0]

    return None


def update(requset):
    page_url = "http://www.matrix67.com/blog/"

    i = 1
    while i <= 30:
        page_url = parse_page(page_url)
        print("i >> %d" % i)
        i += 1

    return HttpResponse("update!")


def page(request, page):
    page = int(page)
    articles = Article.objects.filter(id__gte=(page - 1) * 10, id__lte=page * 10 - 1).order_by("id")
    articles = list(articles)

    return HttpResponse(json.dumps(articles, default=json_utils.object2dict))
    # return HttpResponse("The page is %d" % page)
