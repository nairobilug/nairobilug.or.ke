SHELL := /bin/bash

all:
	pelican -s pelican.conf.py content -o output

chapo:
	@echo "Making that sweet, sweet chapo"
	cd output && python -m SimpleHTTPServer
