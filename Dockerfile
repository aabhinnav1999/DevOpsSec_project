FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR /django_folder
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
