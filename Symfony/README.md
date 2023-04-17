# Symfony
You can follow these commands to initialize a new symfony application and run it:
```sh
docker build -t symfony -f Dockerfile .
docker run -it --rm -v ${pwd}:/var/www/html -w /var/www/html symfony bash
composer create-project symfony/website-skeleton hello-world '5.4.*'
exit
# Start serving the application
docker-compose up
docker exec -it symfony bash
# To debug stuff you can run
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