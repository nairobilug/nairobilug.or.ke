SHELL := /bin/bash

all:
	pelican -s pelican.conf.py content -o output

chapo:
	cd output && python -m SimpleHTTPServer
