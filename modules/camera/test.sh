#!/bin/bash

echo 'Testing CAMERA...'

DIR=`dirname $0`

# Clean $1 (file to log the test)
echo 'Cleaning temp file'
rm $DIR/internals/test_photo.jpg
rm $DIR/internals/test_video.h264

# Escribimos el dato en el archivo $1
echo 'Getting and Writing data'
$DIR/get.sh

# Analizamos el dato escrito en el archivo $1
echo 'Analyzing data'
python $DIR/core/test.py

exit 0