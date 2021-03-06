# Endpoints 2.0 archetype

## Requirements

To use this archetype you must have installed:

* Google Cloud SDK
* Google App Engine SDK
* Python 2.7.x
* pip
* virtualenv

## Virtualenv

> It's recomended to use the virtualenv as a good praticie, **it's not mandatory**. If you opte to not use, go to step 2.

1. Use this command to create a new virtual env.

```
virtualenv venv
```

2. To activate it, you need to use the command below.

```
source venv/bin/activate
```

## Localserver (dev_appserver.py)

### To perform the code local, you need before install the depencies of the project.
1. Install the dependencies on your machine.

```
pip install -r requirements.txt -t lib
```

2. After install the dependeces, you need to execute the command below to start the server.

```
dev_appserver.py .
```

> Note: If you are using the virtualenv, comment the line - ^(.*/)?venv/.*$ before start dev_appserver.py

## Deploy in App Engine on the Google Cloud Plataform (GCP)

1. To deploy this endpoint in the app engine using the endpoints feature, you to execute this command to generate the swagger file.

```
python lib/endpoints/endpointscfg.py get_openapi_spec main.AcmeAPI --hostname acme-api.[project-id-without-brackets].appspot.com
```

2. After that you need to deploy this file in your GCP project.

```
gcloud endpoints services deploy Acmev1openapi.json --project [project-id-without-brackets]
```

3. Before you continue, you need to update the app.yaml settings in the section env_variables the variable ENDPOINTS_SERVICE_NAME with the your GCP project id. Example how should be after the replace.
> ENDPOINTS_SERVICE_NAME: acme-api.my-gcp-project.appspot.com

4. Once you've done that, you will execute the command below in order to get the config id generated by the service deployed before.

```
gcloud endpoints configs list --service=acme-api.[project-id-without-brackets].appspot.com
```

5. Now you will update the variable ENDPOINTS_SERVICE_VERSION in the app.yaml file with the value you obtained after perfomed the command above. Example how should be after the replace.

> ENDPOINTS_SERVICE_VERSION: 2017-11-21r0

6. Finally we can do the deploy.

```
gcloud app deploy --project [project-id-without-brackets] -v [version-you-want] --no-promote -q
```