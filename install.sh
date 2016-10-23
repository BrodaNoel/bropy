#!/bin/bash


if [ -f ~/bropy/internals/installed.txt ]
then
	echo 'Bropy is already installed.'
	echo 'New version? You shuold run update.sh instead of install.sh'
else
	echo 'PATH=~/bropy/bin:$PATH' >> ~/.bash_profile
	echo 'export PATH' >> ~/.bash_profile

	mkdir ~/bropy/internals > /dev/null 2>&1
	mkdir ~/bropy/internals/projects > /dev/null 2>&1
	echo `date +%s` >> ~/bropy/internals/installed.txt

	echo 'BroPy installed properly'
	echo 'Follow me! @BrodaNoel (same profile in all internet!)'
	echo 'Give us your STAR in https://github.com/BrodaNoel/bropy ;)'
fi
