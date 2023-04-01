# Symfony
You can follow these commands to initialize a new symfony application and run it:
```sh
docker build -t symfony -f Dockerfile.symfony .
# Start serving the application
docker-compose up
# To debug stuff you can run
docker run -it --rm -v ${pwd}/hello-world:/var/www/html -p 9090:9000 -p 9091:8000 -w /var/www/html symfony bash
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