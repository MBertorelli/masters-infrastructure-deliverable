
CURRENT_DIR := $(shell pwd)


start:
	docker compose up

start-daemon:
	docker compose up -d

down:
	docker compose down

mysql-interactive:
	docker exec -it masters-infrastructure-deliverable-db-1 bash -l
