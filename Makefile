SHELL := /bin/bash

all:
	pelican content

chapo: all
	@echo "Making that sweet, sweet chapo"
	cd output && python -m http.server

clean:
	rm -r output/*

.PHONY: all chapo clean
