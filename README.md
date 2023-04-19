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

- Provide interactive visualizations for the [Blue-Lining](https://bluelining.org/) project by Carlos Claussel. A version of these interactive visualizations are available [here](https://glue-map-demo.net) (this server is not running all the time).

![blue-lining-project](https://user-images.githubusercontent.com/3639698/215523270-e2e23b63-6975-4385-8cb0-8b91132e28c6.png)

![subset-creation-bluelining](https://user-images.githubusercontent.com/3639698/215537659-ee315aac-c283-4ac9-9932-ad681a77d20e.gif)

## Installation

We recommend creating a new Python virtual environment in which to install and use SAVE. The libraries underlying GeoPandas (used to represent geo-spatial data within glue) may prove difficult to install with `pip` on some platforms, in which case we recommend using Conda/[Mamba](https://mamba.readthedocs.io/en/latest/index.html) to [install GeoPandas](https://geopandas.org/en/stable/getting_started/install.html) before attempting to pip install this package.

`pip install git+https://github.com/jfoster17/SAVE.git`

## Schematic

![Schematic](https://user-images.githubusercontent.com/3639698/216450558-0a038951-b49c-44c0-8361-9fc02b376bf3.png)


## Deployment

We have found that long-running deployments of SAVE via voila lead to the server running out of resources as old processes associated with the voila kernal continue to hang around, consuming memory. We recommend deploying voila with the option to cull old kernals like this:

`voila --no-browser MY-SAVE-NOTEBOOK.ipynb --template=gridstack --preheat_kernel=True --pool_size=4 --ExecutePreprocessor.timeout=180 --MappingKernelManager.cull_interval=120 --MappingKernelManager.cull_idle_timeout=600`
