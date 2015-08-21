#### Requirements
- sqlite3

#### Setup
Inside your virtual env
```
pip install -r requirements.txt
```

Initialize django db
```
python ./manage.py syncdb --settings=tuntematon.settings
python ./manage.py migrate --settings=tuntematon.settings
```

Install and build front end
```
git submodule init
git submodule update
```
Front end is installed under `client/`. Build it according to instructions https://github.com/penny-five/tuntematon2017

## Run
```
python ./manage.py runserver --settings=tuntematon.settings
```
surf to http://localhost:8000
