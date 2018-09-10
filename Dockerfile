# Use an official Python runtime as a parent image
FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /requirements.txt


# Install build deps, then run `pip install`, then remove unneeded build deps
# all in a single step. This ensures the
RUN set -ex \
    # Install build dependencies in the .build-deps directory
    && apk add --no-cache --virtual .build-deps \
            # build dependencies
            gcc \
            make \
            libc-dev \
            musl-dev \
            linux-headers \
            pcre-dev \
            postgresql-dev \
            # dev depencencies
            git \
            # Pillow dependencies
            zlib-dev \
            jpeg-dev \
            # lxml dependencies
            libxslt-dev \
    # Create a python virtual environment, update pip and install requirements
    # from requirements.txt
    && python3 -m venv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
    # Generate a list of run dependencies and install them in .python-rundeps
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    # Finally delete .build-deps to save space.
    && apk del .build-deps


# Install psql used in docker-entrypoint.sh to check for db availability in
# docker-entrypoint.sh.
RUN apk --update add postgresql-client && rm -rf /var/cache/apk/*


# Copy application code to the container.
RUN mkdir /code/
WORKDIR /code/
ADD . /code/


EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=ddweb.settings.docker



ENV DJANGO_MANAGEPY_MIGRATE=on
ENV DJANGO_MANAGEPY_COLLECTSTATIC=on
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start gnunicorn
CMD ["/venv/bin/gunicorn", "ddweb.wsgi", "-b 0.0.0.0:8000"]
