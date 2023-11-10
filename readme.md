# SimpleApp - Line, Word, and Byte Counter

SimpleApp is a Python application that counts the number of lines, words, and bytes in a text file.

## Local Setup

1. Create a new directory named `local`.
2. Inside the `local` directory, create the `main.py` and `text.txt` files. The `Annotations.md` file includes notes that can be used as part of the README.md.

## Running the Application Locally

Execute the following command to run the application:

# bash
python main.py

You should see output similar to:

The number of lines in the file is: 8

## Github Setup

# Verify the version

git --version

# Configure the credentials 

git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Follow the prompts, then output the public key and add it to GitHub
type ~/.ssh/id_rsa.pub

# Validate credentials

ssh -T git@github.com


# To clone and run this application, you'll need Git installed on your computer. From your command line:

# Clone this repository

git clone git@github.com:username/simpleapp.git

# Go into the repository
cd simpleapp

# Testing the Application:
# This assumes your tests are configured to be discovered by setuptools
python setup.py test

# Jenkinsfile
The Jenkinsfile is a text file that contains the definition of a Jenkins Pipeline and is checked into source control. This Jenkins Pipeline allows you to automatically build, test, and deploy your applications based on the pipeline definition. It includes stages for checking out the source code, building the application, and running tests.

# Dockerfile
Using docker build command users can create an automated build that executes several command-line instructions in succession.