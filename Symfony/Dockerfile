FROM php:8.1-fpm

RUN apt-get update \
    && apt-get install -y \
        git \
        wget \
        unzip \
        libicu-dev \
        libpq-dev \
    && docker-php-ext-install \
        intl \
        pdo \
        pdo_mysql \
        pdo_pgsql \
    && pecl install \
        apcu \
    && docker-php-ext-enable \
        apcu 

COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# Install symfony cli
RUN wget https://get.symfony.com/cli/installer -O - | bash \
    && mv /root/.symfony5/bin/symfony /usr/local/bin/symfony