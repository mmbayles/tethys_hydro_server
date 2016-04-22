from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from wsgiref.util import FileWrapper
import os
from datetime import datetime

import sys

#
# from WOFpy.wof.WofWsdls import WofWSDL_1_0, WofWSDL_1_1
@login_required()




def home(request):
    """
    Controller for the app home page.
    """
    print os.path.dirname(os.path.abspath("file"))
    print "hello"

    context = {}

    return render(request, 'tethys_hydro_server/home.html', context)