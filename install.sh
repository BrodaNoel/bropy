#!/bin/bash


if [ -f "~/bropy/internal/installed.txt" ]
then
	echo 'Bropy is already installed.'
	echo 'New version? You shuold run update.sh instead of install.sh'
else
	echo 'PATH=~/bropy/bin:$PATH' >> ~/.bash_profile
	echo 'export PATH' >> ~/.bash_profile

	mkdir ~/bropy/internal > /dev/null 2>&1
	echo `date +%s` >> ~/bropy/internal/installed.txt

	echo 'BroPy installed properly'
	echo 'Follow me! @BrodaNoel (same profile in all internet!)'
	echo 'Give us your STAR in https://github.com/BrodaNoel/bropy ;)'
fi
