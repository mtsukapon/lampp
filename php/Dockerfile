FROM php:7.3-apache-stretch
RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y zlib1g-dev && apt-get install -y libzip-dev
RUN docker-php-ext-install pdo_mysql zip

COPY php.ini /usr/local/etc/php/

RUN apt-get update \
    && apt-get install -y libmcrypt-dev zlib1g-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev git git-flow libsqlite3-dev unzip curl libicu-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd \
      --with-gd \
      --with-freetype-dir=/usr/include/ \
      --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install \
      zip json pdo mbstring pdo_mysql mysqli gettext iconv gd \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Install APCu and APC backward compatibility
RUN pecl install apcu \
    && pecl install apcu_bc-1.0.3 \
    && docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \
    && docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini

# redis extension
RUN pecl install -o -f redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis
    
RUN ln -s ../mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load
RUN LANG=ja_JP.UTF8
RUN a2enmod rewrite
RUN a2enmod headers
#node install
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
#Composer install
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer
ENV COMPOSER_ALLOW_SUPERUSER 1
