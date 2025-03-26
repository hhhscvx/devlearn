Devlearn 2.0 | Новая Арка


- Создать миграцию: `docker compose run --rm web-app sh -c "alembic revision --autogenerate -m "Migration Message""`
- Применить миграцию: `docker compose run --rm web-app sh -c "alembic upgrade head"`
- Коннект к БД: `docker compose exec -it db psql -U devlearn_db_user -W devlearn_db`
