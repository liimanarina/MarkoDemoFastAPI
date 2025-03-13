---
page_type: sample
description: "A minimal sample app that can be used to demonstrate deploying FastAPI apps to Azure App Service."
languages:
- python
products:
- azure
- azure-app-service
---

# Deploy a Python (FastAPI) web app to Azure App Service - Sample Application

This is the sample FastAPI application for the Azure Quickstart [Deploy a Python (Django, Flask or FastAPI) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python). For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

## Additions

The login system built using Azure Keystore.

## Local Testing

To try the application on your local machine:

### Install the requirements

`pip install -r requirements.txt`

### Start the application

`uvicorn main:app --reload`

### Example call

http://127.0.0.1:8000/

## Next Steps

To learn more about FastAPI, see [FastAPI](https://fastapi.tiangolo.com/).
