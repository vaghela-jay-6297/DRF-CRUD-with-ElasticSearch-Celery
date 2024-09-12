Run process:
------------
- start docker desktop app
- start elastic search from docker-compose file using "docker compose up" to run the docker image.
- now you can access elastic search and kibana at "http://localhost:9200" & "http://localhost:5601"
- now run makemigrations and migrate command
- now run "python manage.py search_index --rebuild" command to create all indexes in elastic search.
- start redis-server for executing celery task (after installtion use command in mac: brew services start redis)
- run "redis-cli ping" to check redis server running or not?
- run "celery -A project_name worker -l info" to Start Celery worker
- run "python manage.py runserver" to run project.


Elastic Search setup:
---------------------
- create model into models.py then makemigrate and migrate it.
- install elastic search lib = "django-elasticsearch-dsl".
- register in installed app of settings.py file.
- create document.py file and add model and field with elastic search settings.
- build index in elasticsearch using "python manage.py search_index --rebuild". 
Note: elasticsearch engine is running. (in this project i user docker image of elastic search so start docker "docker compose up")


celery to auto insert, update, delete, search in elastic search with client waiting:
-------------------------------------------------------------------------------------
- create celery.py file in project_folder(like settings.py)
- add some configration in project_folder/__init__.py file
- add some configration related to celery into setting.py file 
- create tasks.py file to execute tasks related to elastic search
- add task module/function into views.py file.
- run celery "celery -A project_name worker -l info"
