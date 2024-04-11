# SciHub API

A command-line tool for retrieving data from Scihub.

## Features

- a user should be able to input a text file containg a series of article DOIs
    - a url is generated for each doi pointing to a scihub endpoint -> HTML file
        - on SUCCESS: the HTML file contains an href pointing to the download path
        - on FAILURE: raises an error to inform the user, program exits
    - the HTML file contains an anchor tag storing the download url for the article
    - a get request is sent using the download url and the output is locally stored
- a user should have the option to either download the articles or just display metadata
    - a path is specified for the downloads
    - metadata can be displayed in different formats
- a user should have access to activity history, whether downloads or querying


