FROM symfony

COPY hello-world /var/www/html

RUN composer install --no-scripts --no-progress --prefer-dist

RUN composer require symfony/web-server-bundle --dev ^4.4.2 --no-scripts --no-progress --prefer-dist

CMD ["php-fpm"]
