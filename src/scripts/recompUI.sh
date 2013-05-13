#!/bin/bash

echo "Compile following files"
echo $(ls src/ui/*.ui)

for file in $(ls src/ui/*.ui)
do
	pyuic4 $file -o "${file%.*}_ui.py"
done
