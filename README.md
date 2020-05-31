# Callback News API

Callback-News.com is an online technology newspaper that gets its news through external newspapers.


Callback-News.com has the news updated daily so you do not miss your dose of tech.


The newspaper is managed by an admin panel in Python, gets the news automatically and has its frontend in NextJs (React).

### 🚀 Links

 * **Website:** https://api.callback-news.com/
 * **Documentation:** https://www.notion.so/Callback-News-8f7835b5467b4ca89efe35607d9abad7
 * **Mockup:** https://www.notion.so/670629e5706d445f8fe08c876ba33d63?v=7ff2443196594df298333cfdcb746970

### 🛠 Installation

1. First, clone this repo with `git clone`.
2. Create enviroment file .env.dev hat satifies the emty values below:
   
```bash
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=callback_news
SQL_USER=admin
SQL_PASSWORD=890306
SQL_HOST=postgres
SQL_PORT=5432
DJANGO_SETTINGS_MODULE=api.settings.dev
BUCKET_NAME=bucket
GS_CREDENTIALS_FILE_LOCATION=
GS_PROJECT_ID=
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=
EMAIL_USE_TLS=
```
- If you want to set your own values for pgadmin, change them in the docker.compose.yml, in the pgadmin section.

3. To set minio server add `127.0.0.1       minio` to your /etc/hosts file or equivalent in your OS.
4. Enter to http://minio:9000
- Credentials are: 
    - MINIO_ACCESS_KEY: access_key
    - MINIO_SECRET_KEY: secret_key
    
5. Create bucket in Minio and name it `bucket`

<img alt="create_bucket_in_minio" src="https://storage.googleapis.com/cbn-public/minio_create_bucket.png" height="300">

6. Click on edit policy from the bucket.

![Edit bucket's policies in Minio](https://storage.googleapis.com/cbn-public/minio_edit_policies.png)

7.then set prefix to `*` and set to select `read and write`

![Set bucket's policies in Minio](https://storage.googleapis.com/cbn-public/minio_policies.png)

8. Build the container with `docker-compose build` (Make sure you have docker and docker compose installed in you machine)
9. Once docker image is installed, turn it on with `docker-compose up`.
10. Run migration of the models set with `docker-compose exec django python manage.py makemigrations`.
11. Then run `docker-compose exec django python manage.py migrate` to complete the migration process.
12. Set you user in django administration IDE with `docker-compose exec django python manage.py createsuperuser`
13. Set values and the go to [localhost/8080/admin](localhost/8000/admin) to access.
14. To sing in the pgadmin IDE go to [localhost/8000/admin](localhost/8000/admin) and join with your credentials..

### 🖥 Execution

**Development Environment**
```
```

>This project runs on **http://localhost:8080**
**Production Environment**

```
```


### 🛠️ Technologies

  * Python
  * Django
  * PostgreSQL

### ✒️ Authors

* **Erik Sanchez** - [eriksape](https://github.com/eriksape)
* **David Behar** - [behagoras](https://github.com/behagoras)
* **Iraida Mercedes** - [iraida07](https://github.com/iraida07)
* **William Velazquez** - [WilliamVelazquez](https://github.com/WilliamVelazquez)
* **Gerardo Marquez** - [GerardoMarquezC](https://github.com/GerardoMarquezC)

If you want to know about the insights [click here!](https://github.com/callback-demons/callback-news-api/pulse/monthly)

### 🎁 Contribute

Feel free to contribute to the project!
