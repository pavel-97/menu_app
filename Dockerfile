FROM python:3.11
EXPOSE 8000
ENV PYTTHONUNBEFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /menu_app
WORKDIR /menu_app/menu_app
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
