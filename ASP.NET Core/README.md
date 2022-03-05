## ASP.NET Core
ASP.NET Core MVC web application, with simple code and explained through this `README.md`.

You can follow through the steps in the instructions in order to get a better idea about this project, how it's created, and how to run it and test it on your host machine.


<div id="Prerequisites"></div>

### Prerequisites
Make sure to install the the folowing dotnet components:
* .NET RUNTIME (used to run apps created with .NET) you can run `dotnet --list-runtimes` for installed runtimes. 
* .NET SDK (used to build and publish .NET apps) you can run `dotnet --list-sdks` for installed SDKs.

**You can follow steps through [link](https://docs.microsoft.com/en-us/dotnet/core/install/) from the official Microsoft web page**

## Built with
In this section you will find the commands and the steps taken to setup this project from scratch make, make sure to refer on the <a href="#Prerequisites">Prerequisites Section</a> to setup your environment before you start.

So since dotnet has ready templates that you can reuse I used the `dotnet new` to initialize this project you can run that to check the available templates on your machine, in this example I used `MVC` template and called the proeject `Demo` you can name it whatever you want by running:
```sh
dotnet new mvc -n <Project-Name>
```