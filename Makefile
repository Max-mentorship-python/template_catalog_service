.PHONY: up down build logs test

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

test:
	cd order_service && python -m pytest tests/ -v
