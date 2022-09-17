## STEP 1: Select a project, or create a new one.

To open Cloud Shell, click Cloud Shell. While these steps show you how to work in Cloud Shell, you can use a similar process when you work in your local environment.

Enable App Engine:
```
    gcloud app create
```

You can use the gcloud CLI to manage your project's resources from the command line or in scripts that you create.
- If an authorization window appears, click Authorize.
- When prompted, choose a region that's closest to you.
- The process is complete when you get this message: "Success! The app is now created."

## STEP 3: Clone a sample app

Instead of creating a new app, clone the sample "Hello, world" app from GitHub:
```
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
```

To explore the app's source files, open the app's directory in the Cloud Shell Editor:
```
    cloudshell workspace python-docs-samples/appengine/standard_python3/hello_world
```

The app consists of:

- main.py, a Python file with the function that responds to requests with "Hello World!"
- requirements.txt, a text file listing package dependencies that the app requires
- app.yaml, an App Engine configuration file with the minimum required settings

## STEP 4: Test the app before deploying it

To open a shell in Cloud Shell Editor, click the Terminal menu and select New Terminal.

To create and activate a virtual environment in which to test your app, use the following commands:
```
    virtualenv --python python3 ~/envs/hello_world
    source ~/envs/hello_world/bin/activate
    pip install -r requirements.txt
```

To run your app, use the following command:
```
    python main.py
```

- When the app is running, the output in Cloud Shell shows the following: "Running on http://127.0.0.1:8080"
- In the Console, click  Web preview and choose Preview on port 8080.
- The app's tab displays "Hello World!".
- To stop the app, in Cloud Shell enter Ctrl+C.

## Step 4.5: Generate requirements.txt

```
    pip freeze > requirements.txt
```
That records an environment's current package list into requirements.txt.

## STEP 5: Deploy the app

Now that you know your app is running correctly, deploy it to App Engine:

In Cloud Shell, configure gcloud to use your project:
```
    gcloud config set project gifted-fragment-362404
```

The App Engine plugin uses gcloud to deploy your app, and gcloud needs to know which project to deploy your app to.

Deploy your app:
```
    gcloud app deploy
```

If you are prompted, "Do you want to continue?", type Y.

When this process is finished, the output shows the following:

Deployed service [default] to https://gifted-fragment-362404.ew.r.appspot.com

If you get a NOT_FOUND: Unable to retrieve P4SA error after running the deploy command, try waiting 60 seconds then run the gcloud app deploy command again.
