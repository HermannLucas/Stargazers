# Notes

This document regroups the differents notes related to the current implementation as well as future plans.

## Repo Structure

The code lives under `src` and the unittests are in `tests`.  
Each files in `tests` directory matches a file in `src`.

The current implementation is structured in three components:  
  - `github.py`: This regroups the logic to query GitHub API.
  - `neighbours.py`: This  holds the logic to create the list of neighbours, it depends on `github.py`.
  - `app`: This module regroups all the code for the Web service, it depends on `neighbours.py`.

## Design

The current design is loosely based around the MapReduce design pattern.

It is mainly visible in the `get_neighbours` function from the `neighbours` module.

This design doesn't add much complexity in its current form but leave plenty of room for scalling, as the map and reduce steps can be parallelized or distributed accross multiple runners. 

## Authentication

I couldn't complete the authentication step as my intention was to leave it to an external service (preferably GitHub) and only manipulate OAuth2 tokens.

It is well documented in the [GitHub documenation](https://docs.github.com/en/rest/guides/basics-of-authentication), but it requires the application to be deployed to receive the token from GitHub.

I tried to deploy it to GCP Cloud Run as [documented](https://cloud.google.com/run/docs/quickstarts/deploy-continuously?hl=fr#cloudrun_deploy_continuous_code-python), but even though everything passed and no error was reported the URL given by GCP kept displayingan error page.

After an hour spent telpting to debug it and with no information on what is causing the issue I stopped.
