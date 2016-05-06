from wof.examples.flask.csv_server import csv_dao
from wof.core import wofConfig, getSpyneApplications
import wof.core_1_1 as wof_1_1
import StringIO
"""
    python runserver_csv.py
    Will run the exact example

    python runserver_csv.py
    --config=csv_config.cfg
    --sites_file=sites.csv
    --values_file=data.csv

"""
NSDEF = 'xmlns:gml="http://www.opengis.net/gml" \
    xmlns:xlink="http://www.w3.org/1999/xlink" \
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" \
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
    xmlns:wtr="http://www.cuahsi.org/waterML/" \
    xmlns="http://www.cuahsi.org/waterML/1.0/"'

#This block of code was original part of the runserver_csv.py in the examples/csv_server
def startServer(config,
                sites_file,
                values_file,
                openPort):
    dao = csv_dao.CsvDao(sites_file, values_file)
#    app.config['DEBUG'] = True

    #defined in core.py
    wConf = wofConfig(dao=dao, wofConfigFile=config)

    #this block of code is defined in _init_.py in the flask folder. Orginally in the create_wof_flask_app and
    #create_wof_flask_multipe functions
    templates = None
    openPort = None
    if hasattr(wConf, 'configObject' ):
        if hasattr(wConf.configObject, 'TEMPLATES' ):
            templates = wConf.configObject.TEMPLATES
    wof_obj_1_1 = wof_1_1.WOF_1_1(wConf.dao, wConf.config, templates) #creates the object which contains the methods for
    # getting the data in waterml format

    location = 'txrivers:SanSaba'#parameters for the values reponse
    variable = "txrivers:Discharge_cfs"
    startDate = "2008-02-11"#can be empty strings
    endDate = "2008-03-30"
    authToken = None

    timeSeriesResponse = wof_obj_1_1.create_get_values_response(
            location, variable, startDate, endDate)
    outStream = StringIO.StringIO()
    timeSeriesResponse.export(
            outStream, 0, name_="timeSeriesResponse",
            namespacedef_=NSDEF)
    values = outStream.getvalue()


    return values #waterml file can be found at http://127.0.0.1:8000/apps/tethys-hydro-server/waterml/
