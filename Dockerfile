FROM python:latest
ENV APP /app
RUN mkdir $APP
WORKDIR $APP
EXPOSE 5000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY . .
#CMD [ "uwsgi", "--ini", "app.ini" ]
CMD [ "python", "./app.py" ]
