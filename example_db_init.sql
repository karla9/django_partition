
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
