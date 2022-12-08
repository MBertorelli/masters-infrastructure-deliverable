
CURRENT_DIR := $(shell pwd)

build-images:
	docker build -t fastapi "${CURRENT_DIR}"

start-web-server: build-images
	docker run -p 8000:8000 --mount type=bind,source="${CURRENT_DIR}"/app,target=/app fastapi

start-mysql:
	echo ${CURRENT_DIR}
	docker run -p 3306:3306 --mount type=bind,source="${CURRENT_DIR}"/db,target=/var/lib/mysql --name mysql-container --env="MYSQL_DATABASE=ETL" --env="MYSQL_ROOT_PASSWORD=etl" -d mysql/mysql-server:8.0.30

stop-mysql:
	docker stop mysql-container
	docker rm mysql-container
