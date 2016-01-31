# Danish Decorations webside

## Udviklingsmiljø

Det er en forudsætning at maskinen har en fungerende python (3.3 eller nyere)
installation med `pip`, samt `lessc`.

Er `node.js` installeret kan `lessc` installerets med `npm install -g less`.

Brug nedstående til at klone git-repoet, sættet et virtualenv op, installere
alle pakker og oprette en database.

```shell
git clone --recursive https://github.com/neic/ddweb.git
cd web
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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
