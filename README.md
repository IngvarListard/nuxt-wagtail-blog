# Wagtail Vue Blog
При изменении типов входящих в состав типа Union необходимо запускать генерацию `fragmentTypes.json`:   
```bash
npm run codegen
```

```bash
# Запуск dev сервера с выхлопом в консоль, для добавления как таск в IDEA
docker-compose up

```
Переменные окружения
## БД
| name        | debug       | docker debug | production  |
| ----------- | ----------- | ------------ | ----------- |
| DB_NAME     | marketplace | marketplace  | marketplace |
| DB_USER     | marketplace | marketplace  | marketplace |
| DB_PASSWORD | marketplace | marketplace  | marketplace |
| DB_HOST     | localhost   | psql         | psql        |
| DB_PORT     | 5432        | 5432         | 5432        |

## REDIS
| name       | debug     | docker debug | production |
| ---------- | --------- | ------------ | ---------- |
| REDIS_HOST | localhost | redis        | redis      |
| REDIS_PORT | 6379      | 6379         | 6379       |
# nuxt-wagtail-blog
