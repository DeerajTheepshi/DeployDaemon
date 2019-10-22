# DeployDaemon
DeployDaemon can be installed on any server and it makes setting up, and hosting popular Stacks easy and simple. DeployDaemon takes care of setting up the project from its repo, creating apache configurations necessary for the project and let's users customise their configuration by providing them options. This project is under construction as a CLI, which would later on be converted into a Web Application that can be installed on any server and used like phpmyadmin.

## Setup Guidelines
- Clone the repository.
- Copy .env.example as .env and edit the database credentials.(Will be created soon)
- Run "make", this will create virtual enviroinment.
- Run "make install", this will install the pip packages to the env.
- Activate you venv to enter into you venv and start working - "source bin/activate"
- ```pip install -r requirements.txt```
- Run ```./git-hook.sh```
- More on setup coming up....

## Coding guidelines to follow
- Follow oops.
- Every file created must have a corresponding class of the same name.
- Every class should have a constructor.
- Install black and follow PEP 08 guidelines.
- A commit can be made only if the entire project is PEP8 compliant. So ensure that.
- Before pushing code "pip freeze > requirements.txt" is must.

