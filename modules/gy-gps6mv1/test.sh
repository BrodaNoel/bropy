#!/bin/bash

echo 'Testing GY-GPS6MV1...'

DIR=`dirname $0`

# Clean $1 (file to log the test)
echo 'Cleaning temp file'
echo '' > $DIR/internals/test_data.json

# Start module
echo 'Starting services'
$DIR/core/start.sh

# Escribimos el dato en el archivo $1
echo 'Geting and Writing data'
$DIR/get.sh >> $DIR/internals/test_data.json

# Stop module
echo 'Stopping services'
$DIR/core/stop.sh

# Analizamos el dato escrito en el archivo $1
echo 'Analyzing data'

# Damos el reporte del analisis (funcionó bien o mal)

exit 0