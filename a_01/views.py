# Create your views here.
from a_01.models import Message
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    o = Message.objects.all()[0]
    return render_to_response('index_01.html', {'text': o.text}, RequestContext(request))
