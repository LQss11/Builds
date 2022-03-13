## ANGULAR
Build test and publish an **Angular Web Application**, with simple code and commands explained through this `README.md`.

You can follow through the steps in the instructions in order to get a better idea about this project, how it's created, and how to run it and test it on your host machine.

<div id="Prerequisites"></div>

### Prerequisites
Make sure to install the the folowing dotnet components:
* [Download](https://nodejs.org/en/download/) and install Node on your host machine .
* The Angular framework installed globally using `npm install -g`
* Make sure to [install Docker](https://docs.docker.com/engine/install/ubuntu/) on your machine if you are willing to containerize the application.

>You can check the Node version and npm version with `node --version `and `npm --versio` 

## Built with
In this section you will find the commands and the steps taken to setup this project from scratch make, make sure to refer on the <a href="#Prerequisites">Prerequisites Section</a> to setup your environment before you start.

Creating a new Angular project from scratch is simple you will only need to run two commands:
```sh
npm install -g @angular/cli
# In case you having truble run with --force flag
```
this command will install the angular cli to allow you generated the new project with:
```sh
ng new <app-name>
```