# coin_wallet
Coin Wallet


## Docker Postgresql

```bash
docker run --name db_gualet -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:9.3.22
```

## Steps

```bash
git clone https://github.com/fernandezgonzalo/coin_wallet

virtualenv --no-site-packages ve --python=python3

source ve/bin/activate
cd coin_wallet
pip install -r requirements.txt
pip install -r requirements_dev.txt

cd project

# configure postgres settings in project/settings.py

python manage.py migrate
python manage.py loaddata auth
python manage.py loaddata gualet
python manage.py test
python manage.py runserver
```

# API


## URIS

### General URIS
http GET http://localhost:8000/api/v1/

```bash
HTTP/1.0 200 OK
Content-Length: 270
Content-Type: application/json
Date: Sat, 14 Apr 2018 14:49:16 GMT
Server: WSGIServer/0.2 CPython/3.5.2
X-Frame-Options: SAMEORIGIN

{
    "gualets": {
        "list_endpoint": "/api/v1/gualets/",
        "schema": "/api/v1/gualets/schema/"
    },
    "transactions": {
        "list_endpoint": "/api/v1/transactions/",
        "schema": "/api/v1/transactions/schema/"
    },
    "users": {
        "list_endpoint": "/api/v1/users/",
        "schema": "/api/v1/users/schema/"
    }
}

```


### User schema

http GET http://localhost:8000/api/v1/users/schema/

```bash
HTTP/1.0 200 OK
Cache-Control: no-cache
Content-Length: 3244
Content-Type: application/json
Date: Sat, 14 Apr 2018 15:17:45 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "allowed_detail_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "allowed_list_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "default_format": "application/json",
    "default_limit": 20,
    "fields": {
        "date_joined": {
            "blank": false,
            "default": "2018-04-14T15:17:45.152979",
            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "datetime",
            "unique": false,
            "verbose_name": "date joined"
        },
        "email": {
            "blank": true,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "email address"
        },
        "first_name": {
            "blank": true,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "first name"
        },
        "id": {
            "blank": true,
            "default": "",
            "help_text": "Integer data. Ex: 2673",
            "nullable": false,
            "primary_key": true,
            "readonly": false,
            "type": "integer",
            "unique": true,
            "verbose_name": "ID"
        },
        "is_active": {
            "blank": true,
            "default": true,
            "help_text": "Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "boolean",
            "unique": false,
            "verbose_name": "active"
        },
        "is_staff": {
            "blank": true,
            "default": false,
            "help_text": "Designates whether the user can log into this admin site.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "boolean",
            "unique": false,
            "verbose_name": "staff status"
        },
        "is_superuser": {
            "blank": true,
            "default": false,
            "help_text": "Designates that this user has all permissions without explicitly assigning them.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "boolean",
            "unique": false,
            "verbose_name": "superuser status"
        },
        "last_login": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
            "nullable": true,
            "primary_key": false,
            "readonly": false,
            "type": "datetime",
            "unique": false,
            "verbose_name": "last login"
        },
        "last_name": {
            "blank": true,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "last name"
        },
        "password": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "password"
        },
        "resource_uri": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": true,
            "type": "string",
            "unique": false,
            "verbose_name": "resource uri"
        },
        "username": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": true,
            "verbose_name": "username"
        }
    },
    "filtering": {
        "username": 1
    }
}

```

### Gualet schema
http GET http://localhost:8000/api/v1/gualets/schema/
```bash
HTTP/1.0 200 OK
Cache-Control: no-cache
Content-Length: 1960
Content-Type: application/json
Date: Sat, 14 Apr 2018 15:15:08 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "allowed_detail_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "allowed_list_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "default_format": "application/json",
    "default_limit": 20,
    "fields": {
        "address": {
            "blank": true,
            "default": "",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "address"
        },
        "balance": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Integer data. Ex: 2673",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "integer",
            "unique": false,
            "verbose_name": "balance"
        },
        "created": {
            "blank": true,
            "default": true,
            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "datetime",
            "unique": false,
            "verbose_name": "created"
        },
        "id": {
            "blank": true,
            "default": "",
            "help_text": "Integer data. Ex: 2673",
            "nullable": false,
            "primary_key": true,
            "readonly": false,
            "type": "integer",
            "unique": true,
            "verbose_name": "ID"
        },
        "label": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "string",
            "unique": false,
            "verbose_name": "label"
        },
        "resource_uri": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": true,
            "type": "string",
            "unique": false,
            "verbose_name": "resource uri"
        },
        "user": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "related_schema": "/api/v1/users/schema/",
            "related_type": "to_one",
            "type": "related",
            "unique": false,
            "verbose_name": "user"
        }
    },
    "filtering": {
        "user": 2
    }
}
```

### Transaction schema

http GET http://localhost:8000/api/v1/transactions/schema/

```bash
HTTP/1.0 200 OK
Cache-Control: no-cache
Content-Length: 1893
Content-Type: application/json
Date: Sat, 14 Apr 2018 15:18:36 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "allowed_detail_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "allowed_list_http_methods": [
        "get",
        "post",
        "put",
        "delete",
        "patch"
    ],
    "default_format": "application/json",
    "default_limit": 20,
    "fields": {
        "address_from": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "related_schema": "/api/v1/gualets/schema/",
            "related_type": "to_one",
            "type": "related",
            "unique": false,
            "verbose_name": "address from"
        },
        "address_to": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "A single related resource. Can be either a URI or set of nested resource data.",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "related_schema": "/api/v1/gualets/schema/",
            "related_type": "to_one",
            "type": "related",
            "unique": false,
            "verbose_name": "address to"
        },
        "amount": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Integer data. Ex: 2673",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "integer",
            "unique": false,
            "verbose_name": "amount"
        },
        "date": {
            "blank": true,
            "default": true,
            "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"",
            "nullable": false,
            "primary_key": false,
            "readonly": false,
            "type": "datetime",
            "unique": false,
            "verbose_name": "date"
        },
        "id": {
            "blank": true,
            "default": "",
            "help_text": "Integer data. Ex: 2673",
            "nullable": false,
            "primary_key": true,
            "readonly": false,
            "type": "integer",
            "unique": true,
            "verbose_name": "ID"
        },
        "resource_uri": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: \"Hello World\"",
            "nullable": false,
            "primary_key": false,
            "readonly": true,
            "type": "string",
            "unique": false,
            "verbose_name": "resource uri"
        }
    },
    "filtering": {
        "address_from": 2,
        "address_to": 2
    }
}
```

## Create user

```bash
http POST localhost:8000/api/v1/users/ username=juanete password=admin123 first_name=juanete last_name=juanete email=juanete@gmail.com
```

## Create Gualet

```bash
http POST localhost:8000/api/v1/gualets/ label=asddddddd balance=5 user=/api/v1/users/1/
http POST localhost:8000/api/v1/gualets/ label=asddddddd balance=5 user=/api/v1/users/1/
```
## Create Transaction

```bash
http post localhost:8000/api/v1/transactions/ address_from=/api/v1/gualets/1/ address_to=/api/v1/gualets/2/ amount:=1
```

# Helpers

In the helpers folder there are many files to use the api

```bash
helpers/
├── get_gualet.sh
├── get_gualets.sh
├── get_transaction.sh
├── get_transactions.sh
├── get_user.sh
├── get_users.sh
├── post_gualets.sh
├── post_transactions.sh
└── post_users.sh
```

# TODO

* User permissions on Transaction and Gualet.
* Dockerizing server.
* User authentication by BasicAuth, Apikey, OAuth, etc.
* Documentation api on Swagger and sphinix
