FROM python:3.6

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

WORKDIR /usr/src/app

RUN set -x; \
      apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y \
        gettext \
      && rm -rf /var/lib/apt/lists/* \
      && apt-get clean all

COPY app .

# Install Python packages
RUN set -x; \
  pip install --no-cache-dir -r requirements.txt --upgrade

RUN chmod +x manage.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
