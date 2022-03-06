## ASP.NET Core
ASP.NET Core MVC web application, with simple code and explained through this `README.md`.

You can follow through the steps in the instructions in order to get a better idea about this project, how it's created, and how to run it and test it on your host machine.


<div id="Prerequisites"></div>

### Prerequisites
Make sure to install the the folowing dotnet components:
* .NET RUNTIME (used to run apps created with .NET) you can run `dotnet --list-runtimes` for installed runtimes. 
* .NET SDK (used to build and publish .NET apps) you can run `dotnet --list-sdks` for installed SDKs.
* Make sure to [install Docker](https://docs.docker.com/engine/install/ubuntu/) on your machine if you are willing to containerize the application.
**You can follow steps through [link](https://docs.microsoft.com/en-us/dotnet/core/install/) from the official Microsoft web page**

You can also find a full documentation about the dockerimages used in this example:
- [.NET SDK](https://hub.docker.com/_/microsoft-dotnet-sdk/)
- [ASP.NET Core Runtime](https://hub.docker.com/_/microsoft-dotnet-aspnet)

## Built with
In this section you will find the commands and the steps taken to setup this project from scratch make, make sure to refer on the <a href="#Prerequisites">Prerequisites Section</a> to setup your environment before you start.

So since dotnet has ready templates that you can reuse I used the `dotnet new` to initialize this project you can run that to check the available templates on your machine, in this example I used `MVC` template and called the proeject `Demo` you can name it whatever you want by running:
```sh
dotnet new mvc -n <Project-Name>
```
## Quick Start
To run this project you will need follow through these steps:
- first to restore dependencies specified in a .NET project by running:
```sh
dotnet restore 
```
- Build a .NET project:
>`-c` The configuration to use for building the project. The default for most projects is 'Debug'.
>`-o` The output directory to place built artifacts in.
```sh
dotnet build -c Release -o <build-path>
```
- Once the build is done you can publish your dll to be deployed:
```sh
dotnet publish -c Release -o <build-path>
```
- Now that you are done you are one step ahead go to the directory specified for the -o flag and run:
```sh
dotnet <app-name>.dll
```
You must get a similar result to this:
```sh
PS C:\app> dotnet .\Demo.dll      
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5000
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:5001       
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Production
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\app\
info: Microsoft.Hosting.Lifetime[0]  
      Application is shutting down...
```

## Docker
In this example we used docker to containerize our project and to do so we need a `Dockerfile` to build the image then run it.

The setup is easy and simple just run:
>Make sure to update Demo.dll to your project's dll name!
```sh
docker build -t <image-name> .
```
Then start the container using the image create:
```sh
docker run -d -p 8080:80 <image-name>
```
then try running localhost:8080 on your host machine.
### Additional Information
You can generate gitignore file by running:
```sh
dotnet new gitignore
```
- You can find additional information and examples in this repo [repo](https://github.com/amoraitis/TodoList)