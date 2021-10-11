build:
	docker-compose -f compose/local.yml build

up:
	docker-compose -f compose/local.yml up

remove:
	docker rm $(docker ps -a -q) && docker rmi $(docker images -q)
