import logging

import wof
import wof.flask
# from csv_dao import CsvDao
from wof.examples.flask.csv_server import csv_dao
from wof.apps import spyned_1_0
from wof.core import wofConfig, getSpyneApplications
import wof.core_1_0 as wof_1_0
"""
    python runserver_csv.py
    Will run the exact example

    python runserver_csv.py
    --config=csv_config.cfg
    --sites_file=sites.csv
    --values_file=data.csv

"""
def startServer(config,
                sites_file,
                values_file,
                openPort):
    dao = csv_dao.CsvDao(sites_file, values_file)
    print dir(dao)
    print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAo"
    app = wof.flask.create_wof_flask_app(dao, config)
#    app.config['DEBUG'] = True


    url = "http://127.0.0.1:" + str(openPort)
    print "----------------------------------------------------------------"
    print "Service endpoints"
    for path in wof.flask.site_map_flask_wsgi_mount(app):
        print "%s%s" % (url,path)

    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print "HTML Acess Service endpoints at "
    for path in wof.site_map(app):
        print "%s%s" % (url,path)

    print "----------------------------------------------------------------"
    wConf = wofConfig(dao=dao, wofConfigFile=config)
    templates = None
    openPort = None
    if hasattr(wConf, 'configObject' ):
        if hasattr(wConf.configObject, 'TEMPLATES' ):
            templates = wConf.configObject.TEMPLATES
    wof_obj_1_0 = wof_1_0.WOF(wConf.dao, wConf.config, templates)
    happy = wof.apps.spyned_1_0.GetSites(wof_obj_1_0,openPort,openPort,openPort)
    print "hello"
    print happy

    # app.run(host='0.0.0.0', port=openPort, threaded=True)
    return happy
