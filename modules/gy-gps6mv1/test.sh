#!/bin/bash

echo 'Testing GY-GPS6MV1...'

DIR=`dirname $0`

# Clean $1 (file to log the test)
echo 'Cleaning temp file'
echo '' > $DIR/internals/test_data.json

# Escribimos el dato en el archivo $1
echo 'Getting and Writing data'
$DIR/get.sh > $DIR/internals/test_data.json

# Analizamos el dato escrito en el archivo $1
echo 'Analyzing data'
python $DIR/core/test.py

# Damos el reporte del analisis (funcionó bien o mal)

exit 0