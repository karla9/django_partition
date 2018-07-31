
CREATE DATABASE IF NOT EXISTS `example_db` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `example_db`;

DROP TABLE IF EXISTS `shop_tab`;
CREATE TABLE `shop_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `address` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `shop_customer_tab_temp` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `mobile_number` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `shop_customer_tab_00` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_01` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_02` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_03` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_04` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_05` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_06` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_07` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_08` LIKE `shop_customer_tab_temp`;
CREATE TABLE `shop_customer_tab_09` LIKE `shop_customer_tab_temp`;

DROP TABLE `shop_customer_tab_temp`;


CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_00` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_00`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_01` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_01`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_02` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_02`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_03` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_03`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_04` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_04`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_05` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_05`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_06` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_06`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_07` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_07`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_08` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_08`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE DATABASE IF NOT EXISTS `django_partition_demo_site_db_09` DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
USE `django_partition_demo_site_db_09`;

DROP TABLE IF EXISTS `shop_order_tab`;
CREATE TABLE `shop_order_tab` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `shop_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
);
