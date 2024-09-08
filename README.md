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
    - "Vertex AI" > "Vertex AI User"
- Then click done.
- This will create a service account
- On the right "Actions" column click the vertical ... and select "Create key". A prompt for Create private key for "deployment" will appear select "JSON" and click create. This will download a Private key json file to your computer. Copy this json file into the **secrets** folder.
- Rename the json key file to `data-service-account.json`


### Attach GCP Credentials to Container
- To setup GCP Credentials in a container we need to set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` inside the container to the path of the secrets file from the previous step

- We do this by setting the `GOOGLE_APPLICATION_CREDENTIALS` to `/secrets/data-service-account.json` in the docker shell file
- Make sure the `GCP_PROJECT` matches your GCP Project

## Generate QA Dataset

### Run Container
Run the startup script to make building & running the container easy

- Make sure you are inside the `llm-create-dataset` folder and open a terminal at this location
- Run `sh docker-shell.sh`
- After container startup, test the shell by running `python cli.py --help`

### Generate Text
- Run `python cli.py --generate` to generate sample cheese QA dataset
- Change any of the default parameters

#### System Prompt

We setup a system prompt to help guide the LLM to build a diverse set of question answer pairs. The detail prompt can been seen in `cli.py`

```
Generate a set of question-answer pairs about cheese in English, adopting the tone and perspective of an experienced Italian cheese expert. Adhere to the following guidelines:

1. Expert Perspective:
  - Embody the voice of a seasoned Italian cheese expert with deep knowledge of both Italian and international cheeses
  - Infuse responses with passion for cheese craftsmanship and Italian cheese-making traditions
  - Reference Italian cheese-making regions, techniques, and historical anecdotes where relevant

2. Content Coverage:
...

3. Tone and Style:
...

4. Complexity and Depth:
...

5. Question Types:
...

6. Answer Format:
...

7. Cultural Context:
...

8. Accuracy and Relevance:
...

9. Language:
...

Output Format:
Provide the Q&A pairs in JSON format, with each pair as an object containing 'question' and 'answer' fields, within a JSON array.
```

#### Input Prompt

We give an input prompt for the LLM:

```
Generate 20 diverse, informative, and engaging question-answer pairs about cheese following these guidelines, embodying the passionate and knowledgeable tone of an Italian cheese expert, while keeping all content in English.
```

#### Number of Iterations of question generation

Change the number of iterations to build a larger dataset
```
NUM_ITERATIONS = 5
```

### Sample Question Answers

Here are some sample results from when you run the `--generate` option from the above step:

```
[
  {
    "question": "What are some of the most unique and lesser-known Italian cheeses?",
    "answer": "Ah, you want to go beyond the familiar?  Then we must talk about 'Pecorino Romano', a sheep's milk cheese aged for months, its sharp bite perfect for grating over pasta.  Or 'Caciocavallo', literally 'cheese horse', its shape reminiscent of a saddle, aged to perfection in the southern regions. And let's not forget 'Casu marzu', a Sardinian delicacy, a sheep's milk cheese fermented by live maggots.  It's an acquired taste, but a testament to the boldness of Italian cheesemaking!"
  },
  {
    "question": "How do you explain the difference between 'Parmigiano Reggiano' and 'Grana Padano'?",
    "answer": "Ah, a classic question! Both are hard, granular cheeses, but 'Parmigiano Reggiano', the king, boasts a complex, fruity flavor and a crumbly texture, a result of centuries of tradition in the Emilia-Romagna region. 'Grana Padano', while excellent, is produced further north, with a slightly milder flavor and a more buttery texture.  Both are essential for any cheeseboard, but their subtle distinctions reveal the soul of their regions."
  },
  ...
]
```

### Prepare Dataset
The text generated by the LLM needs to be converted to a csv format that we will use to fine-tune another LLM

- Run `python cli.py --prepare`
- This step will combine all the `.txt` files are consolidate it into one csv file.







