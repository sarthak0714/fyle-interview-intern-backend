FROM python:3.8-slim-buster

# set working dir and cpy content
WORKDIR /app
COPY . /app

# env setup and activate
RUN pip install virtualenv
RUN virtualenv --clear env --python=python3.8
RUN . ./env/bin/activate  
RUN  pip install --no-cache-dir -r requirements.txt

# Reset DB
ENV FLASK_APP=core/server.py
RUN rm -f core/store.sqlite3
RUN flask db upgrade -d core/migrations/

# Expose the port and run 
EXPOSE 7755
CMD ["bash", "run.sh"]