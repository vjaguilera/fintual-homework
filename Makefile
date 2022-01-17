.PHONY: build stop start up test remove help

IMAGE_TAG ?= fintual-tareita

build:
		$(info Make: Build images(s) of the service)
		docker build -t $(IMAGE_TAG)

stop:
		$(info Make: Stop service(s))
		docker stop $(IMAGE_TAG)

start:
		$(info Make: Starting service(s) in background (detached))
		docker run -d $(IMAGE_TAG)

up:
		$(info Make: Starting service(s) no detached)
		docker run $(IMAGE_TAG)

test:
		$(info Make: Running tests located on /tests without Docker)
		coverage run -m pytest && coverage report && coverage html
		
remove:
		$(info Make: Remove Docker container)
		docker rm $(IMAGE_TAG)

help: ## Help messages showed
	@echo ''
	@echo 'Usage: make [TARGET] [EXTRA_ARGUMENTS]'
	@echo 'Targets:'
	@echo '  start           start service in background. Default make command.'
	@echo '  build           building service in background.'
	@echo '  stop            Stop the service.'
	@echo '  up              start services in foreground.'
	@echo '  test            running test service.'
	@echo '  remove          remove container.'
	@echo '  help            show help'
	@echo ''