# Flask Boiler Plate API

> Documentation
- Flask
  - https://flask.palletsprojects.com/en/1.1.x/
- Flask SQLAlchemy
  - https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- Flask Marshmallow
  - https://flask-marshmallow.readthedocs.io/en/latest/
- Marshmallow-sqlalchemy
  - https://marshmallow-sqlalchemy.readthedocs.io/en/latest/

## Initialize your API
- initialize your REPL
- type from filename import db
- type db.create_all()
  
## Api Endpoints
- Get all guides
URL: http://localhost:5000/guides

- Get a Guide
-URL: http://localhost:5000/guide/id
-Method: Get

- Create a Guide
-URL: http://localhost:5000/guide
-Send Body of json:
```json
{
    "title": "some title",
    "content": "some content"
}
```

- Edit a Guide
-URL: http://localhost:5000/guide/id
-Method: Post
-Send Body of json:
```json
{
    "title": "updated title",
    "content": "updated content"
}
```

- Delete a Guide
-URL: http://localhost:5000/guide/id
-Method: Delete

# Environment Stuff

- open terminal in folder
- run this in terminal:
    '''
    type pipenv --three
    ''' 
    (sets python3 as the version for that environment)
- use the following command to enter shell:
'''
use the command "pipenv shell
'''

- install packages locally in the pipenv through this command:
 '''
 pipenv install library
 '''

- command to open repl is still python