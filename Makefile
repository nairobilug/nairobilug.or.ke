SHELL := /bin/bash

all:
	pelican content

chapo: all
	@echo "Making that sweet, sweet chapo"
	cd output && python -m SimpleHTTPServer

clean:
	rm -r output/*
