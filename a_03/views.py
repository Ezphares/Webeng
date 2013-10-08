from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from urllib import urlopen
from lxml.etree import XML, XSLT

def home(request):
    data = urlopen('http://www.cs.washington.edu/research/xmldatasets/data/courses/reed.xml')
    xml = XML(data.read())
    data.close()