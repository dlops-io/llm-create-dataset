# Using LLM to Create Instruct Dataset

In this tutorial go over data versioning techniques using the mushroom app data. We will use Docker to run everything inside containers.

## Prerequisites
* Have Docker installed
* Cloned this repository to your local machine with a terminal up and running

## Setup GCP Credentials
Next step is to enable our container to have access to GCP Storage buckets. 

### Create a local **secrets** folder

It is important to note that we do not want any secure information in Git. So we will manage these files outside of the git folder. At the same level as the `llm-create-dataset` folder create a folder called **secrets**

Your folder structure should look like this:
```
   |-llm-create-dataset
   |-secrets
```

### Setup GCP Service Account
- Here are the step to create a service account:
- To setup a service account you will need to go to [GCP Console](https://console.cloud.google.com/home/dashboard), search for  "Service accounts" from the top search box. or go to: "IAM & Admins" > "Service accounts" from the top-left menu and create a new service account called `data-service-account`. 
- For "Service account permissions" select:
    - "Cloud Storage" > "Storage Admin"
    - "" > ""
- Then click done.
- This will create a service account
- On the right "Actions" column click the vertical ... and select "Create key". A prompt for Create private key for "deployment" will appear select "JSON" and click create. This will download a Private key json file to your computer. Copy this json file into the **secrets** folder.
- Rename the json key file to `data-service-account.json`


### Attach GCP Credentials to Container
- To setup GCP Credentials in a container we need to set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` inside the container to the path of the secrets file from the previous step

- We do this by setting the `GOOGLE_APPLICATION_CREDENTIALS` to `/secrets/data-service-account.json` in the docker shell file
- Make sure the `GCP_PROJECT` matches your GCP Project

## Run Container

### Run `docker-shell.sh`
Run the startup script to make building & running the container easy

- Make sure you are inside the `llm-create-dataset` folder and open a terminal at this location
- Run `sh docker-shell.sh`
- After container startup, test the shell by running `python cli.py --help`





