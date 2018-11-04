  # We do not use alpine. The resulting image is smaller, but there is currently
  # no support for pip installation of wheels (binary) packages. It falls back
  # to installing from source which is very time consuming. See
  # https://github.com/pypa/manylinux/issues/37 and
  # https://github.com/docker-library/docs/issues/904
FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

ADD Pipfile* /

RUN set -ex \
  # The -slim version of the debian image deletes man-pages to free space. This
  # unfortunately causes some packages to fail to install. See
  # https://github.com/debuerreotype/debuerreotype/issues/10 As a work-around we
  # add the missing directories for postgresql-client.
  && mkdir -p /usr/share/man/man1 /usr/share/man/man7 \
  && apt-get -y update \
  && apt-get -y install --no-install-recommends \
  # git is needed for python packages with `… = {git = …}` in Pipfile. It pulls a
  # lot of dependencies. Maybe some of them can be ignored.
  git \
  # psql is used in docker-entrypoint.sh to check for db availability.
  postgresql-client \
  # clean up after apt-get and man-pages
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_* \
  && pip install pipenv
RUN pipenv install --deploy --system


# Copy application code to the container.
ADD . /code/
WORKDIR /code/

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=ddweb.settings.docker



ENV DJANGO_MANAGEPY_MIGRATE=on
ENV DJANGO_MANAGEPY_COLLECTSTATIC=on
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start gnunicorn
CMD ["/venv/bin/gunicorn", "ddweb.wsgi", "-b 0.0.0.0:8000"]
