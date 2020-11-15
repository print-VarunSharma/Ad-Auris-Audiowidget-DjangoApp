# Rebit Audio Widget - Django Fullstack App

This is Ad-Auris's Audio Widget File System that makes storing all files to Google Storage SDK easy.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
Follow instructions dependending on what hosting service, python version, and etc.

Heroku and Python 3.8 recommended.

```

## Running the product

Instructions for running the app locally and in production


Follow instructions dependending on what hosting service, python version, and etc.

Heroku and Python 3.8 recommended.
Ensure that app.debug = False for production and app.debug = True during local development

```bash    
   python manage.py to see full command  list
   python manage.py runserver - locally host with hot-reload on save
   
   For anychanges to database, users, admin.py, settings.py, and a new app run these commands.
python manage.py makemigrations
   python manage.py migrate 
  
    
    
```
## Development - Production

Instructions for running the app locally and in production


Follow instructions dependending on what hosting service, python version, and etc.

Heroku and Python 3.8 recommended.
Ensure that app.debug = False for production and app.debug = True during local development

```bash    
    app.debug = True
    AllowedHosts =[] Insert domain for debug False
    
    
```


## Contents

```python


Google Storage
Google Client OAuth

```

## Contributing
Pull requests are welcome by the Ad-Auris Dev Team. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)