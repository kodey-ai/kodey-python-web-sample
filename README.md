# kodey-python-web-sample

This repository is an example Kodey.ai Coding Agent Workflow

## Objectives

In this sample, we will explore how Kodey.ai can create simple python web application project.

## Project Setup & Steps 

1. Signup for a new Kodey.ai account or login to your existing Kodey.ai environmenty (link-here)
2. Configure your Kodey.ai integrations to the desired issue tracker and cloud git provider.
3. Fork this repository, and clone it to the cloud git provider of your choosing (Github, Azure DevOps, Bitbucket)
4. Create the sample issue / work item in your issue tracker. Copy and Paste the issue description from below.
5. Execute the below prompt in the Kodey.ai chat UI
6. Validate the commits and pull requests in your cloud git provider

### SAMPLE PROMPT - Github Tools (Flask Python Web Application)
```
    branch name to create: feature/python-web-sample

    Information to agent: Do as the steps below are defined one by one. You are working in github repo so make sure to use tools related to github repo.
    NOTE: You should write the actual implementation of code not just comments.

    SCENARIO: You are working in a project that involves students submitting their information via a form and it should be saved in database.
    You should be working with flask framework for the backend. Creating necessary models, routing files, etc is your responsibility.

    Steps:

    step 1: Using GithubCreateNewBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using GithubCreateNewFile tool, create all the necessary files which are needed to run the flask web application.
    Look over the instructions present <flask-project-setup> to know more.
    NOTE: Make use of sqlite database.
    
    <flask-project-setup>
        step 1: Create model file in src directory that has field like user, full name, roll no, semester,etc. Make proper use of schema.
        step 2: Create a routing file in src directory which makes the use of api to GET, POST and PUT the student details on database using above schema.
        step 3: Create a main file in root folder that initiates the flask application and let us run the project.
    </flask-project-setup>

    step 3: using GithubCreateNewFile tool, Create a new file called README.md inside root folder and put all the details of the project.

    step 4: using GithubCreatePullRequest tool, create a new Pull Request from the above created branch with title "python Web App Flask".

```

### SAMPLE PROMPT - Azure DevOps Tools (Cloudformation Template)
```
    branch name to create: feature/python-web-sample

    Information to agent: Do as the steps below are defined one by one. You are working in azure repo so make sure to use tools related to azure repo.
    NOTE: You should write the actual implementation of code not just comments.

    SCENARIO: You are working in a project that involves students submitting their information via a form and it should be saved in database.
    You should be working with flask framework for the backend. Creating necessary models, routing files, etc is your responsibility.

    Steps:

    step 1: Using AzureDevopsBranchesCreateBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using AzureDevopsRepositoryCreateNewFile tool, create all the necessary files which are needed to run the flask web application.
    Look over the instructions present <flask-project-setup> to know more.
    NOTE: Make use of sqlite database.
    
    <flask-project-setup>
        step 1: Create model file in src directory that has field like user, full name, roll no, semester,etc. Make proper use of schema.
        step 2: Create a routing file in src directory which makes the use of api to GET, POST and PUT the student details on database using above schema.
        step 3: Create a main file in root folder that initiates the flask application and let us run the project.
    </flask-project-setup>

    step 3: using AzureDevopsRepositoryCreateNewFile tool, Create a new file called README.md inside root folder and put all the details of the project.

    step 4: using AzureDevopsPullRequestsCreatePullRequest tool, create a new Pull Request from the above created branch with title "python Web App Flask".

    step 5: using AzureDevopsIssuesUpdateIssue tool, update the issue status to done.
```

### SAMPLE PROMPT - Jira / Bitbucket (Making Project That hits API requests extract data and define serverless file)
```

    branch name to create: feature/python-web-sample

    Information to agent: Do as the steps below are defined one by one. You are working in bitbucket repo so make sure to use tools related to bitbucket repo.
    NOTE: You should write the actual implementation of code not just comments. 

    SCENARIO: You are working in a project that involves students submitting their information via a form and it should be saved in database.
    You should be working with flask framework for the backend. Creating necessary models, routing files, etc is your responsibility.

    Steps:

    step 1: Using BitBucketCreateNewBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using BitBucketWriteCode tool, create all the necessary files which are needed to run the flask web application.
    Look over the instructions present <flask-project-setup> to know more.
    NOTE: Make use of sqlite database.
    
    <flask-project-setup>
        step 1: Create model file in src directory that has field like user, full name, roll no, semester,etc. Make proper use of schema.
        step 2: Create a routing file in src directory which makes the use of api to GET, POST and PUT the student details on database using above schema.
        step 3: Create a main file in root folder that initiates the flask application and let us run the project.
    </flask-project-setup>

    step 3: using BitBucketWriteCode tool, Create a new file called README.md inside root folder and put all the details of the project.

    step 4: using BitBucketCreateNewPullRequest tool, create a new Pull Request from the above created branch with title "python Web App Flask".

    step 5: Update this jira issue status to done.

```

## Once you have set the description of the issue in your relavant system. You need to use kodey UI Chat and execute below statement to get the work done. 

### Github Issue and Github Repo
```
   Get the issue with id <issue_id> from github repo and do as the description of the issue says.
```

### Azure Repo Issue and Azure Repo
```
   Get the issue with id <issue_id> from azure repo and do as the description of the issue says.
```

### Jira Issue and Bitbucket Repo
```
   Get the issue with id <issue_id> from jira and do as the description of the issue says.
```

## Confirming Successful Sample Outputs

1. Confirm that the branch was created on the issue / work item
2. Confirm that the code created in the associated pull request contains the following
3. Confirm that the work item/issue/ticket in your relevant issue tracking platform is updated.