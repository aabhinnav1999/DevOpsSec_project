FROM python:3.12 AS base
WORKDIR /django_folder
COPY ./django_project /django_folder
RUN pip install --no-cache-dir -r requirements.txt -t /django_folder/deps

FROM gcr.io/distroless/python3:nonroot
WORKDIR /django_folder
ENV PYTHONPATH=/django_folder/deps
ENV PYTHONUNBUFFERED=1
COPY --from=base /django_folder /django_folder
EXPOSE 8000
CMD ["start.py"]
