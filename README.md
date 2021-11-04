# The Great Catle Escape
## Designed and implemented by Stephen D'Arcy

![Live code demo](assets/images/live_demo.gif)

# Table of Contents

1.[Introduction](#introduction)
2.[Technologies_Used](#tech)
3.[Testing](#testing)
4.[Bugs](#bugs)
5.[Fixes](#fixes)
6.[Deployment](#deployment)
7.[Credits](#credits)


# Introduction

## Basic Design

## Main goals of the project

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

# Technologies used
The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!