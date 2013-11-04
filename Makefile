SHELL := /bin/bash

all:
	pelican -s pelican.conf.py content -o output

chapo: all
	@echo "Making that sweet, sweet chapo"
	cd output && python -m SimpleHTTPServer

clean:
	rm -r output/*
