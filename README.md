# iris_satellite_plantation - under construction
Unsupervised detection of plantations remotely in satellite images.

## First why detect plantations?
Actually a lot of finance contracts around agriculture needs some proof of existence. To go to the place 
of that plantation are declared to exist would be slow and expensive. What if we can detect plantations using 
georeference + machine learning? This is what I'm going to show using Iris as a database and computing server.

## Data Pipeline
### Raw Data
For this experiment I use images from the Satellite Sentinel (https://sentinelhub-py.readthedocs.io/en/latest/)
which provide a time series of georeferenced images.

### Full Image
As the raw data has 121km² of area and I dont need to process all this area, I crop the desired area into a smaller 
area square (around 1km²).

![picture](https://github.com/renatobanzai/iris_satellite_plantation/blob/main/docs/img/img_raw.jpg?raw=true)

### Cropped Image

![picture](https://github.com/renatobanzai/iris_satellite_plantation/blob/main/docs/img/img_tci.png?raw=true)

### Clusterization By Vegetation Index
![picture](https://github.com/renatobanzai/iris_satellite_plantation/blob/main/docs/img/result.png?raw=true)
After all the image processing we can calculate the vegetation index NDVI (Normalized difference vegetation index) to 
understand if the area has or not something growing.

## Interpreting Results
Putting this solution into a continuous data pipeline can help to remote monitoring of growing vegetation areas. 

## Using with Iris
In fact the new Iris feature to use Python Embedded make this kind of solution to be quickly created into
the IRIS environment.

## Installing
First clone my repo in a directory of your machine:

```
# git clone https://github.com/renatobanzai/iris_satellite_plantation.git
```
After this, go to the directory iris_satellite_plantation
```
# cd iris_satellite_plantation/app
# docker build -t iris_satellite_plantation:latest ./
```
Sometimes the command above takes longer than the reality. Just do a ctrl + c and repeat this step.
```
# docker run --name iris_plantation -d --publish 1972:1972 --publish 52773:52773 iris_satellite_plantation:latest
# docker exec -it iris_plantation /usr/irissys/bin/irispython /app/process.py
```
Now you are oficially running the newest EAP, connecting into AWS to download a satellite image and much more soon ;) 

## If you enjoyed this application please vote in iris_satellite_plantation!
[https://openexchange.intersystems.com/package/iris_satellite_plantation](https://openexchange.intersystems.com/package/iris_satellite_plantation)