#!/usr/bin/env python2

from distutils.core import setup

setup(name='Automaton Pi',
	  version=0.1,
	  description=('Autonomous control of the Helion Animus 18TR using a '
				   'Raspberry PI.'),
	  author='Shaun Donachy, Ljiljana Zigic, Mack Stump',
	  author_email=('donachys@gmail.com, zigicljiljana@gmail.com, '
					'mack.stump@gmail.com'),
	  packages=['automatonpi', 'automatonpi.packages.adafruit'],
	  license='GPLv3',
	  scripts=['bin/automatonpi'])
