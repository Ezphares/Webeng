from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from urllib import urlopen
from lxml.etree import XML, XSLT
from rdflib.term import URIRef
from rdflib import Graph, Literal, BNode, RDF

def home(request):
    data = urlopen('http://www.cs.washington.edu/research/xmldatasets/data/courses/reed.xml')
    xml = XML(data.read())
    data.close()
    
    store = Graph()
    subject = URIRef('http://rdf.ify.dk/#subject')
    title = URIRef('http://rdf.ify.dk/#title')
    course = URIRef('http://rdf.ify.dk/#course')
    
    for i in xml.iterfind('course'):
        c = BNode()
        store.add((c, RDF.type, course))
        store.add((c, title, Literal(i.find('title').text)))
        store.add((c, subject, Literal(i.find('subj').text)))
    
    r = HttpResponse(store.serialize(format='pretty-xml'), content_type='application/rdf+xml')
    r.__setitem__('Content-Disposition', 'attachment; filename="courses.rdf"')
    return r
