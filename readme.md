# Danish Decorations webside

## Udviklingsmiljø

Det er en forudsætning at maskinen har en fungerende python (3.3 eller nyere)
installation med `pipenv`.

Brug nedstående til at klone git-repoet, sættet et virtualenv op, installere
alle pakker og oprette en database.

```shell
git clone --recursive https://github.com/neic/ddweb.git
cd ddweb
pipenv install
pipenv shell
./manage.py migrate --settings=ddweb.settings.dev
./manage.py createsuperuser --settings=ddweb.settings.dev
```

Konfigurationen er delt i flere moduler. `manage.py` bruger enten
miljøvariabelen `DJANGO_SETTINGS_MODULE` eller en parameter til at bestemme
hvilken konfiguration der skal bruges. For at kører udviklingsserveren med
udviklingskonfigurationen skriv:

```shell
./manage.py runserver --settings=ddweb.settings.dev
```

## Docker
For at udgive et ny docker image:
```
docker build -t neic/ddweb .
docker push neic/ddweb
```

## LESS og CSS

For ikke at have node.js som dependency på serveren er det nødvendigt at have en
compilet CSS version af alle LESS filerne i git. Det er indeholdt i
[`static-src/style.min.css`](static-src/style.min.css) og
[`static-src/style.min.css.map`](static-src/style.min.css.map).

For at compile dette kræver det LESS og node.js. Med en fungerende node.js
installation kan LESS og en CSS-minifier installeres med
```shell
npm install -g less less-plugin-clean-css
```
For at genere nye CSS filer køres
```shell
cd static-src
lessc --clean-css --source-map style.less style.min.css
```
