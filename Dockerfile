# set the base image 

FROM frolvlad/alpine-python3

# create working directory

RUN mkdir -p /cube/cube_project

# create directory to mount

RUN mkdir -p /tmp/cubefiles

# set directoty where CMD will execute 

WORKDIR /cube/cube_project

# add project files to the /cube/cube_project folder

COPY cube_project ./

# add settings.ini file

COPY settings.ini /cube/

# add requirements.txt file

COPY requirements.txt ./

# get pip to download and install requirements:

RUN pip install --no-cache-dir -r requirements.txt

# Create DB Schema 

RUN python3 /cube/cube_project/manage.py migrate

# Create superuser (admin) 

RUN python3 /cube/cube_project/manage.py initadmin

# Add default rules in DB 

RUN python3 /cube/cube_project/manage.py initrules

# Expose ports

EXPOSE 8000

# default command to execute      

CMD python3 /cube/cube_project/manage.py runserver --insecure 0.0.0.0:8000 & celery -A cube_project worker -l info