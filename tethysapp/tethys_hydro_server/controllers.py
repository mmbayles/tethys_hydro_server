from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from wsgiref.util import FileWrapper
import os
from datetime import datetime
import sys
import utilities
from app import TethysHydroserver
@login_required()

def home(request):
    temp_dir = TethysHydroserver.get_app_workspace().path #Tethys' built in temp directory to store the three necessary files
    config= temp_dir +'/csv_config.cfg' #these files are included in the examples folder in WOFpy
    sites_file = temp_dir +'/sites.csv'
    values_file = temp_dir +'/data.csv'
    port = None
    test = utilities.startServer(config,sites_file,values_file,port)
    context = {"hello":test}
    return render(request, 'tethys_hydro_server/home.html', context)
def waterml(request):
    temp_dir = TethysHydroserver.get_app_workspace().path
    config= temp_dir +'/csv_config.cfg'
    sites_file = temp_dir +'/sites.csv'
    values_file = temp_dir +'/data.csv'
    port =  None
    test = utilities.startServer(config,sites_file,values_file,port)
    response = HttpResponse(test, content_type='application/xml')

    return response