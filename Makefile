.PHONY: test lint docker-up

test:
	pytest -q

lint:
	pre-commit run --all-files

docker-up:
	docker compose up --build
