# DeployDaemon

DeployDaemon can be installed on any server and it makes setting up, and hosting popular Stacks easy and simple. DeployDaemon takes care of setting up the project from its repo, creating apache configurations necessary for the project and let's users customise their configuration by providing them options. This project is under construction as a CLI, which would later on be converted into a Web Application that can be installed on any server and used like phpmyadmin.

## Setup Guidelines

- Clone the repository.
- Copy .env.example as .env and edit the database credentials.
- Run ```make```, this will create virtual enviroinment.
- Run ```make install```, this will install the pip packages to the env. This will also setup the databse
- Activate you venv to enter into you venv and start working - "source bin/activate"
- Run ```./git-hook.sh``` //Todo: Move git-hook.sh to makefile

## Coding guidelines to follow and PR requirements

- Follow oops.
- Every file created must have a corresponding class of the same name.
- Every class should have a constructor.
- Install black and follow PEP 08 guidelines.
- A commit can be made only if the entire project is PEP8 compliant. So ensure that.
- Before pushing code ```pip freeze > requirements.txt``` is must.
- If Pre-Commit hook throws an error, ```autopep8 --in-place --recursive --aggressive --aggressive ./app```, this will automatically correct the errors for you.

## DWoC Guide

- Projects can be found at https://dwoc.io/
- To begin with, try to solve issues flagged on the repository. (P.S. Certain issues are simple to begin with)
- Try to understand the requirement of the Stack based modules, and try to add as many as possible features. 
- Any new feature, coding pattern, or improvement to the current code base is accepted

