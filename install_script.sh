#!/bin/sh




##install geos
wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
bzip2 -dk geos-3.4.2.tar.bz2
tar -xvf geos-3.4.2.tar
cd geos-3.4.2
./configure
make
sudo make install

echo "GEOS INSTALLED"

##install both
wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.8.4.tar.gz
tar -xzvf spatialindex-src-1.8.4.tar.gz
cd spatialindex-src-1.8.4
./configure
make
sudo make install

echo "SPATIAL INDEX INSTALLED"

##
sudo python setup.py install
