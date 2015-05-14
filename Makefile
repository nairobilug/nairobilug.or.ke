SHELL := /bin/bash

python_version_full := $(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
ifeq ($(python_version_major),2)
	build_cmd := python -m SimpleHTTPServer
else
	build_cmd := python -m http.server
endif

all:
	pelican content

chapo: all
	@echo "Making that sweet, sweet chapo"
	cd output && ${build_cmd}

clean:
	rm -r output/*

.PHONY: all chapo clean
