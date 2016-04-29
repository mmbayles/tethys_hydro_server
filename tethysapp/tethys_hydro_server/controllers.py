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
from wof import core_1_0
from wof import core_1_1
from wof import core
from wof import dao
from wof import WaterML
from wof.apps import waterml2
from wof.examples.flask.csv_server import csv_dao
from wof.examples.flask.csv_server import runserver_csv
import logging

import wof
import wof.flask
import argparse
# from csv_dao import CsvDao
from app import TethysHydroserver
@login_required()




def home(request):
    temp_dir = TethysHydroserver.get_app_workspace().path
    config= temp_dir +'/csv_config.cfg'
    sites_file = temp_dir +'/sites.csv'
    values_file = temp_dir +'/data.csv'
    print values_file

    # if __name__ == '__main__':
    # This must be an available port on your computer.
    # For example, if 8080 is already being used, try another port such as
    # 5000 or 8081.
    port =  "8081"
    print "hello"
    test = utilities.startServer(config,sites_file,values_file,port)
    # test = "as"
    print test
    print "test"
    context = {"hello":test}
    return render(request, 'tethys_hydro_server/home.html', context)
def waterml(request):
    temp_dir = TethysHydroserver.get_app_workspace().path
    config= temp_dir +'/csv_config.cfg'
    sites_file = temp_dir +'/sites.csv'
    values_file = temp_dir +'/data.csv'
    print values_file

    # if __name__ == '__main__':
    # This must be an available port on your computer.
    # For example, if 8080 is already being used, try another port such as
    # 5000 or 8081.
    port =  "8081"
    print "hello"
    test = utilities.startServer(config,sites_file,values_file,port)
    # test = "as"
    print test
    print "test"
    response = HttpResponse(test, content_type='application/xml')
    return response