# Symfony
## Create project
In order to create a symfony project you can run one the following commands:
```sh
create-project symfony/website-skeleton my_project_directory '5.4.*'
create-project symfony/skeleton:"^5.4" my_project_directory
composer new my_project_directory --version=5.4
```
# Docker
You can follow these commands to initialize a new symfony application and run it using the docker container configured for creating and running symfony projects.
## Create new project
```sh
docker build -t symfony -f Dockerfile .
docker run -it --rm -v ${pwd}:/var/www/html -w /var/www/html symfony bash
cd my_project_directory

```
# Docker compose
Before running make sure you update the **.env** which contains the project name that you are willing to create.

## Symfony cli with compose
You can run this docker compose and get access to the container where you have symfony cli to run commands and start serving:
```sh
docker-compose -f docker-compose-symfony-cli.yaml up -d
docker exec -it symfony-cli bash
# Create a new project
composer create-project symfony/website-skeleton ${PROJECT_NAME} '5.4.*'
# Run this if you clone a project from git and need to reinstall all the packages
cd ${PROJECT_NAME}
composer install
```
## Start Serving
Once done run the following commands:
```sh

# Start serving the application
docker-compose up
docker exec -it symfony bash
```

# Symfony commands:
Create new bundle for backoffice
```sh
composer require symfony/maker-bundle --dev
bin/console make:bundle
```
You can create entities in 2 different ways:
```sh
# Create entity from scratch
php bin/console make:entity
# If changes are made manually and want to add getters setters
php bin/console make:entity --regenerate
## Load entity into the database
php bin/console make:migration
php bin/console doctrine:migrations:migrate
# Load entities from an existing sql database (this will fetch all tables)
php bin/console doctrine:mapping:import App/Entity annotation --path=src/Entity
```
Now if you want to create controller run this:
```sh
php bin/console make:controller ProductController
```
You can query database directly by running:
```sh
php bin/console dbal:run-sql 'SELECT * FROM reclamation'
```
# Routing
You can get all routes by running this command:
```sh
php bin/console debug:router
```
## Hello world
Create a new controller class  **src/Controller/HelloController.php**:
```php
<?php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class HelloController
{
    /**
     * @Route("/hello", name="hello")
     */
    public function index(): Response
    {
        return new Response('Hello World!');
    }
}
```
In the config/routes.yaml file, add the following route:
```yaml
hello:
    path: /hello
    controller: App\Controller\HelloController::index
```

### Additional information
You can get some bootstrap websites for free from [here](https://startbootstrap.com/themes)