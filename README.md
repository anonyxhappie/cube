# Cube
This project is aimed to design and implement a Business rules framework on event streams, for operational alerts etc

There is a continuous stream of user activity events generated from multiple users as they use our mobile app. Objective is to implement a server to ingest these events. The server will expose a http end-point to which the events would be posted. Also the server will contain an admin interface to specify business rules, that alert the operator or trigger an action (like sending an alert sms to the end user), when certain criteria is met.


# Technologies used
- [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
- [DRF](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
- [Celery](https://docs.celeryproject.org/en/stable/): It’s a task queue with focus on real-time processing, while also supporting task scheduling.

# Docker images used
- [frolvlad/alpine-python3](https://hub.docker.com/r/frolvlad/alpine-python3) - for base image
- [rabbitmq:3-management](https://hub.docker.com/_/rabbitmq) - for celery

# Installation
- Run rabbitmq server
> $ docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
- Clone repo & cd to project directory
> $ cd cube
- Get docker bridge ip for connecting to rabbitmq server
> ifconfig docker0 | grep netmask | awk {'print $2'} 
- Rename settings.ini.example & update values in settings.ini (update above ip here in CELERY_BROKER_URL)
> $ mv settings.ini.example settings.ini; vim settings.ini
- Create local directory to mount with container
> $ mkdir -p /tmp/cubefiles
- Create docker image
> $ docker build -t cubeapp:v1 .
- Run cube api server
> $ docker run -v /tmp/cubefiles:/tmp/cubefiles -it -p 8000:8000 cubeapp:v1


# Event API
- Example request for Bill Pay
```
curl -X POST \
  http://localhost:8000/event/trigger/ \
  -H 'content-type: application/json' \
  -d '{
		"noun": "bill", 
		"userid": 178765, 
		"ts": "20200725 124500", 
		"latlong": "19.07,72.87", 
		"verb": "pay",
		"timespent": 72, 
		"properties": {
			"bank": "hdfc", 
			"merchantid": 234, 
			"value": 139.5, 
			"mode": "netbank"
		}
	}'
```
- Example request for Feedback Post
```
curl -X POST 
  http://localhost:8000/event/trigger/ \
  -H 'content-type: application/json' \
  -d '{
	"noun": "fdbk", 
	"userid": 178765, 
	"ts": "20200725 134500", 
	"latlong": "19.07,72.87", 
	"verb": "post",
	"timespent": null,
	"properties": {
        "text": "the bank page took too long to load"
        }
    }'
```
- Example response
```
{
    "status": 200,
    "message": "Event triggered."
}
```

# Check logs
> $ tail -f /tmp/cubefiles/cube_project_debug.log

# Admin UI
- open below link in browser to access Admin UI
> http://localhost:8000/admin/
- Login using credentials given in settings.ini
- Click on Event & Event_Rules for listing
- You can change status of Event_Rules to active/inactive from this dashboard 