# SAVE
Search Analysis and Visualization Environment

The Search Analysis and Visualization Environment is a component of the [Data+Climate collaboration](https://sites.google.com/cfa.harvard.edu/data-climate/home?pli=1), joining the diverse knowledge resources of [Data Commons](https://datacommons.org) with tools such as the [glue visualization library](http://glueviz.org). This repository is a meta-package collecting the various components to allow for easy installation.

## Components

The core components of SAVE worked on or developed under the Data+Climate collaboration include:

- [glue-jupyter](https://glue-jupyter.readthedocs.io/en/latest/) -- glue in a Jupyter notebook
- [glue-map](https://github.com/jfoster17/glue-map) -- a glue-jupyter plugin for:
  - Loading geospatial data from a variety of vector formats
  - The display and analysis of geo-spatial data, leveraging [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/) and [xarray-leaflet](https://xarray-leaflet.readthedocs.io/en/latest/)
  - A customizable ipywidget showing how to dynamically add Data Commons data to an existing glue-jupyter session
- [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/) -- An ipywidget for display of maps using [leaflet.js](https://leafletjs.com)
- [xarray-leaflet](https://xarray-leaflet.readthedocs.io/en/latest/) -- to enable the visualization of large datasets efficiently
- [glue-jupyter-plugin-template](https://github.com/jfoster17/glue-jupyter-plugin-template) -- a template plug-in demonstrating how to turn ipywidgets into glue-jupyter widgets.

Two prototype plug-ins for the desktop (QT) version of glue allow access to external data:
- [glue-dataverse](https://github.com/jfoster17/glue-dataverse) -- access to [Dataverse](https://dataverse.org) data resources through an integrated web client 
- [glue-data-commons](https://github.com/jfoster17/glue-data-commons) -- access to DataCommons data resources

In addition, the following components are used in SAVE to produce standalone websites/dashboards:

- [voila](https://voila.readthedocs.io/en/stable/) -- to host a SAVE analysis session as a stand-alone webpage
- [voila gridstack](https://github.com/voila-dashboards/voila-gridstack) -- the preferred voila template to allow for easy organization of different visualizations on the same page.

## Examples

As part of the [Climate and Justice Design Fellowship](https://projects.iq.harvard.edu/climatefellowship) under the Data+Climate pilot project, SAVE was used to:

- Conduct data analysis and export specific visualizations for the [California Map of Hazardous Waste Sites and Schools](https://ejhazardouswaste.com/) by Idalmis Vaquero

![ejhazardouswaste](https://user-images.githubusercontent.com/3639698/215529678-9e33b55d-6802-4534-ac83-fcd415082708.png)
![hazardous-waste-example](https://user-images.githubusercontent.com/3639698/215537632-1ce38cbf-bec0-4935-b6a5-292d38e029d4.gif)

- Provide interactive visualizations for the [Blue-Lining](https://bluelining.org/) project by Carlos Claussel. A version of these interactive visualizations are available [here](https://glue-map-demo.net)

![blue-lining-project](https://user-images.githubusercontent.com/3639698/215523270-e2e23b63-6975-4385-8cb0-8b91132e28c6.png)

![subset-creation-bluelining](https://user-images.githubusercontent.com/3639698/215537659-ee315aac-c283-4ac9-9932-ad681a77d20e.gif)

