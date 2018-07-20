# hackerthon-django

## Requirements

#### Product

- Python (3.6)
- pipenv
- Django (2.x)
- psycopg2-binary
- uwsgi
- pillow

#### Dev

- ipython
- Django-Extensions
- awsebcli

### Secrets

#### `.secrets/base.json`

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

#### `.secrets/production.json`

```json
{
  "ALLOWED_HOSTS": [<Your list>],
  "DATABASES": {
    "default": {
      "ENGINE": "<DB engine like django.db.backends.postgresql>",
      "HOST": "<DB host>",
      "PORT": "<DB port>",
      "USER": "<DB user>",
      "PASSWORD": "<DB pw>",
      "NAME": "<DB name>"
    }
  },
}
```

## Running

#### Local

```shell
# Move project's directory
pipenv install
pipenv shell
./runlocal.sh
```

#### Production

```shell
# Move project's directory
# Use your EB App
./deploy.sh
```