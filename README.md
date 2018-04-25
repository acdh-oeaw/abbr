# ABBR - An application to store and resolve abbreviations

This application is used as a storage and curation plattform to collaboratively work on abbreviations found in any kind of texts and second.Those curated abbrivations are exposed through an API so that other projects can reuse the data.

## Install

* clone the repo
* create a virtual environment
* install requirements `pip install -r requirements.txt`
* create your custom settings file or use `settings.dev`
* makemigrations and migrate `python manage.py <makemigrations|migrate> --settings=abbr.settings.<dev>`

## Import abbreviations

## 'simple list'

* provide a file like `words/data/abrev_MS_OBL_manually_filtered.txt` (one abbrevation per line)
* run the command `python manage.py import_simple_list --settings=abbr.settings.<dev>`

Be aware that in case an of an already existing abbreviation object with the same `orth` value, no new item will be created.
