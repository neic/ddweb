  # We do not use alpine. The resulting image is smaller, but there is currently
  # no support for pip installation of wheels (binary) packages. It falls back
  # to installing from source which is very time consuming. See
  # https://github.com/pypa/manylinux/issues/37 and
  # https://github.com/docker-library/docs/issues/904
FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN set -ex \
  && apt-get -y update \
  && apt-get -y install --no-install-recommends \
  # git is needed for python packages with `… = {git = …}` in Pipfile. It pulls a
  # lot of dependencies. Maybe some of them can be ignored.
  git \
  # psql is used in docker-entrypoint.sh to check for db availability.
  postgresql-client \
  # clean up after apt-get and man-pages
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_* \
  && pip3 install pipenv

WORKDIR /code/
COPY Pipfile* /code/

# One might assume that --system should be used, but
# https://github.com/pypa/pipenv/pull/2762 recommends against it.
RUN pipenv install --deploy


# Copy application code to the container.
COPY docker-entrypoint.sh .
COPY manage.py .
COPY ddweb ./ddweb
COPY templates ./templates
COPY static-src ./static-src

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=ddweb.settings.docker


ENV DJANGO_MANAGEPY_MIGRATE=on
ENV DJANGO_MANAGEPY_COLLECTSTATIC=on
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start gnunicorn
CMD ["pipenv", "run", "gunicorn", "ddweb.wsgi", "-b 0.0.0.0:8000"]
