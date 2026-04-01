.PHONY: up down build logs test lint lint-fix format help


up:
	docker compose up -d

down:
	docker compose stop

build:
	docker compose build

logs:
	docker compose logs -f

test:
	python -m pytest tests/ -v