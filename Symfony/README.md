# Symfony
You can follow these commands to initialize a new symfony application and run it:
```sh
docker build -t symfony -f Dockerfile .
docker run -it --rm -v ${pwd}:/var/www/html -w /var/www/html symfony bash
composer create-project symfony/website-skeleton hello-world '5.4.*'
# Or
composer create-project symfony/skeleton:"^5.4" my_project_directory
# Or you can build with symfony binaries
symfony new my_project_directory --version=5.4
exit
# Start serving the application
docker-compose up
docker exec -it symfony bash
composer install
symfony server:start
# To debug stuff you can run
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
php bin/console dbal:run-sql 'SELECT * FROM product'
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