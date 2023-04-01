# Symfony
You can follow these commands to initialize a new symfony application and run it:
```sh
docker build -t symfony -f Dockerfile.symfony .
docker run -it --rm -v ${pwd}:/app -w /app symfony:local bash -c "composer create-project symfony/skeleton hello-world '5.0.*'"
```