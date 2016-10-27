#!/bin/bash

echo 'Testing GY-GPS6MV1...'

# Clean $1 (file to log the test)
echo 'Cleaning temp file'
echo '' > $1

# Start module
echo 'Starting services'
$("`dirname $0`/core/start.sh")

# Escribimos el dato en el archivo $1
echo 'Geting and Writing data'
$("`dirname $0`/get.sh") >> $1

# Stop module
echo 'Stopping services'
$("`dirname $0`/core/stop.sh")

# Analizamos el dato escrito en el archivo $1
echo 'Analyzing data'

# Damos el reporte del analisis (funcionó bien o mal)

exit 0