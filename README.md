# Willkommen im WoofMate Projekt

Willkommen im Repo zum WoofMate 🐕‍🦺🐩🐕 Projekt. Wir entwickeln hier eine Web-App um Hundebesitzer dabei zu unterstützen, Play-Dates für ihre vierbeinigen Begleiter zu organisieren. Wie haben uns [Python Django](https://www.djangoproject.com/) als Entwicklung-Framework ausgesucht. Als Datenbanktechnologie verwenden wir [SQLite](https://www.sqlite.org/). Als Visualisierung für die Geo-Daten unserer Nutzer verwenden wir die Python-Bibliothek [Folium](https://python-visualization.github.io/folium/latest/) als Interface für Leaflet.js.

![Banner Bild mit spielenden Hunden](static/banner.jpeg)

## Installation

Um dieses Repo verwenden zu können, müssen einige Voraussetzungen erfüllt werden. Am Rechner muss Python in der Hauptversion 3 installiert sein. Außerdem müssen einige Bibliotheken installiert werden. Dazu kann am Rechner folgender Code im Termin ausgeführt werden.

Zuerst erstellen wir eine lokale, virtuelle Umgebung. Wir nennen diese `djangoenv`. Dazu navigieren wir in den Projektordner und öffnen dort ein neues Terminal-Fenster um folgenden Code auszuführen. Falls der verwendete Manager für virtuelle Umgebungen (`virtualenv`) noch nicht installiert ist, kann dieser mit folgendem Terminal-Befehl installiert werden: `pip install virtualenv`.

```shell
virtualenv djangoenv
```

Anschließend aktivieren wir die virtuelle Umgebung auf unserem Rechner und installieren dann alle notwendigen Dependencies. Dazu kann folgender Code ausgeführt werden. Auch hier wird davon ausgegangen, dass der verwendete Terminal im Ordner des Projekt-Repositories geöffnet ist.

```shell
djangoenv/Scripts/activate
pip install -r requirements.txt
```

> **Hinweis:** Das verwendete virtuelle Umgebung (`djangoenv`) wurde zum `.gitignore`-File hinzugefügt und wird folglich nicht mit GitHub synchronisiert. Jede Nutzer:in dieses Repository muss sich die virtuelle Umgebung folglich also selbst aufsetzen, um dieses Projekt ausführen zu können.

## Wichtige Anleitungen

* [Einsteiger-Tutorial in Python Django](https://www.w3schools.com/django/)
* [Einsteiger-Tutorial in SQLite](https://www.guru99.com/de/sqlite-tutorial.html)
* [Maps in Django mit Python Folium](https://medium.com/@FatemeFouladkar/how-i-integrated-folium-with-django-d04dc5b25048)