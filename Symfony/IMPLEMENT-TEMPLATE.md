# Implement bootstrap template
In order to implement a template you can do the following:

Let's you have an admin and user interfaces (bootstrap templates) you can create **back-office** and **front-office** directories under **public** directory then start following these steps:

- Create **templates/admin.html.twig**
- for each src="..." or href="..." referencing a file under public/back-office replace it with "{{asset('back-office/...')}}"
- to have reusable blocks later on you have to add the following :
- if href must redirect to some entity path then you can use the following
```php
href="{{ path('app_example') }}"
```
- The controller where the path specified must exist, you can run this command to create it
```sh
php bin/console make:controller ExampleController
--- output:
 created: src/Controller/ExampleController.php
 created: templates/example/index.html.twig
# Make sure to edit templates/example/index.html.twig {% extends 'base.html.twig' %} by base html in our example it's {% extends 'admin.html.twig' %}
```
