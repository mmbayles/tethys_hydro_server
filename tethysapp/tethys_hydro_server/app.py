from tethys_sdk.base import TethysAppBase, url_map_maker


class TethysHydroserver(TethysAppBase):
    """
    Tethys app class for Tethys HydroServer.
    """

    name = 'Tethys HydroServer'
    index = 'tethys_hydro_server:home'
    icon = 'tethys_hydro_server/images/icon.gif'
    package = 'tethys_hydro_server'
    root_url = 'tethys-hydro-server'
    color = '#34495e'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='tethys-hydro-server',
                           controller='tethys_hydro_server.controllers.home'),

                     UrlMap(name='waterml',
                           url='waterml',
                           controller='tethys_hydro_server.controllers.waterml'),
        )

        return url_maps