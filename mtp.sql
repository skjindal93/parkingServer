-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mtp
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `parking_arearegionmapping`
--

DROP TABLE IF EXISTS `parking_arearegionmapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_arearegionmapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parking_arearegionmapping_region_id_608638688e21f9e4_uniq` (`region_id`,`area_id`),
  KEY `parking_arearegionmapping_d266de13` (`area_id`),
  KEY `parking_arearegionmapping_0f442f96` (`region_id`),
  CONSTRAINT `parking__region_id_19f866b04896e001_fk_parking_parkingregions_id` FOREIGN KEY (`region_id`) REFERENCES `parking_parkingregions` (`id`),
  CONSTRAINT `parking_area_area_id_48444c6bba44f21e_fk_parking_parkingareas_id` FOREIGN KEY (`area_id`) REFERENCES `parking_parkingareas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_arearegionmapping`
--

LOCK TABLES `parking_arearegionmapping` WRITE;
/*!40000 ALTER TABLE `parking_arearegionmapping` DISABLE KEYS */;
INSERT INTO `parking_arearegionmapping` VALUES (1,1,1),(2,2,1),(3,7,1),(4,8,1),(5,9,1);
/*!40000 ALTER TABLE `parking_arearegionmapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_parkingareas`
--

DROP TABLE IF EXISTS `parking_parkingareas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_parkingareas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext NOT NULL,
  `capacity` int(11) NOT NULL,
  `filled` int(11) NOT NULL,
  `latitude` decimal(15,10) NOT NULL,
  `longitude` decimal(15,10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingareas`
--

LOCK TABLES `parking_parkingareas` WRITE;
/*!40000 ALTER TABLE `parking_parkingareas` DISABLE KEYS */;
INSERT INTO `parking_parkingareas` VALUES (1,'Vindhyachal Hostel',0,2,50.0000000000,50.0000000000),(2,'Shivalik Hostel',0,0,50.0000000000,50.0000000000),(3,'Bla',0,0,25.0000000000,25.0000000000),(4,'Bla',0,0,25.0000000000,25.0000000000),(5,'Bla',0,0,25.0000000000,25.0000000000),(6,'Bla',0,0,25.0000000000,25.0000000000),(7,'Bla',0,0,25.0000000000,25.0000000000),(8,'Bla',0,0,25.0000000000,25.0000000000),(9,'Bla',0,0,25.0000000000,25.0000000000);
/*!40000 ALTER TABLE `parking_parkingareas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_parkingraspberrymapping`
--

DROP TABLE IF EXISTS `parking_parkingraspberrymapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_parkingraspberrymapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_id` int(11) NOT NULL,
  `pi_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parking_parkingraspberrymapping_area_id_6ff4b6a5a31388d8_uniq` (`area_id`,`pi_id`),
  KEY `parking_parkingraspberrymapping_d266de13` (`area_id`),
  KEY `parking_parkingraspberrymapping_e34c8b0e` (`pi_id`),
  CONSTRAINT `parking_park_area_id_3f1ba4ab04e45c37_fk_parking_parkingareas_id` FOREIGN KEY (`area_id`) REFERENCES `parking_parkingareas` (`id`),
  CONSTRAINT `parking_pi_id_644b53abcd1b924b_fk_parking_raspberry_raspberry_id` FOREIGN KEY (`pi_id`) REFERENCES `parking_raspberry` (`raspberry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingraspberrymapping`
--

LOCK TABLES `parking_parkingraspberrymapping` WRITE;
/*!40000 ALTER TABLE `parking_parkingraspberrymapping` DISABLE KEYS */;
INSERT INTO `parking_parkingraspberrymapping` VALUES (1,1,1),(5,1,4),(4,2,1);
/*!40000 ALTER TABLE `parking_parkingraspberrymapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_parkingregions`
--

DROP TABLE IF EXISTS `parking_parkingregions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_parkingregions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `latitude` decimal(15,10) NOT NULL,
  `longitude` decimal(15,10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parking_parkingregions_name_6d4ba233ecb9c7f6_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingregions`
--

LOCK TABLES `parking_parkingregions` WRITE;
/*!40000 ALTER TABLE `parking_parkingregions` DISABLE KEYS */;
INSERT INTO `parking_parkingregions` VALUES (1,'Indian Institute of Technology, Delhi',50.0000000000,50.0000000000),(2,'Connaught Place',25.0000000000,25.0000000000);
/*!40000 ALTER TABLE `parking_parkingregions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_raspberry`
--

DROP TABLE IF EXISTS `parking_raspberry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_raspberry` (
  `raspberry_id` int(11) NOT NULL AUTO_INCREMENT,
  `mac` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`raspberry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_raspberry`
--

LOCK TABLES `parking_raspberry` WRITE;
/*!40000 ALTER TABLE `parking_raspberry` DISABLE KEYS */;
INSERT INTO `parking_raspberry` VALUES (1,'','10.192.49.24'),(4,'',NULL);
/*!40000 ALTER TABLE `parking_raspberry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_raspberryphone`
--

DROP TABLE IF EXISTS `parking_raspberryphone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_raspberryphone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_mac` varchar(255) NOT NULL,
  `pi_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `parking_raspberryphone_e34c8b0e` (`pi_id`),
  CONSTRAINT `parking_pi_id_25d234afc9221afe_fk_parking_raspberry_raspberry_id` FOREIGN KEY (`pi_id`) REFERENCES `parking_raspberry` (`raspberry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_raspberryphone`
--

LOCK TABLES `parking_raspberryphone` WRITE;
/*!40000 ALTER TABLE `parking_raspberryphone` DISABLE KEYS */;
INSERT INTO `parking_raspberryphone` VALUES (1,'EC:1F:72:2D:6D:71',1),(2,'EC:1F:72:2D:6D:71',1),(3,'EC:1F:72:2D:6D:71',1),(4,'EC:1F:72:2D:6D:71',1),(5,'EC:1F:72:2D:6D:71',1),(6,'EC:1F:72:2D:6D:71',1),(7,'EC:1F:72:2D:6D:71',1),(8,'EC:1F:72:2D:6D:71',1),(9,'EC:1F:72:2D:6D:71',1),(10,'EC:1F:72:2D:6D:71',1),(11,'EC:1F:72:2D:6D:71',1),(12,'EC:1F:72:2D:6D:71',1),(13,'EC:1F:72:2D:6D:71',1),(14,'EC:1F:72:2D:6D:71',1),(15,'EC:1F:72:2D:6D:71',1),(16,'EC:1F:72:2D:6D:71',1),(17,'EC:1F:72:2D:6D:71',1),(18,'EC:1F:72:2D:6D:71',1),(19,'EC:1F:72:2D:6D:71',1),(20,'EC:1F:72:2D:6D:71',1),(21,'EC:1F:72:2D:6D:71',1),(22,'EC:1F:72:2D:6D:71',1),(23,'EC:1F:72:2D:6D:71',1),(24,'EC:1F:72:2D:6D:71',1),(25,'EC:1F:72:2D:6D:71',1),(26,'EC:1F:72:2D:6D:71',1),(27,'EC:1F:72:2D:6D:71',1),(28,'EC:1F:72:2D:6D:71',1),(29,'EC:1F:72:2D:6D:71',1),(30,'EC:1F:72:2D:6D:71',1),(31,'EC:1F:72:2D:6D:71',1),(32,'EC:1F:72:2D:6D:71',1),(33,'EC:1F:72:2D:6D:71',1),(34,'EC:1F:72:2D:6D:71',1),(35,'EC:1F:72:2D:6D:71',1),(36,'EC:1F:72:2D:6D:71',1),(37,'EC:1F:72:2D:6D:71',1),(38,'EC:1F:72:2D:6D:71',1),(39,'EC:1F:72:2D:6D:71',1),(40,'EC:1F:72:2D:6D:71',1),(41,'EC:1F:72:2D:6D:71',1),(42,'EC:1F:72:2D:6D:71',1),(43,'EC:1F:72:2D:6D:71',1),(44,'EC:1F:72:2D:6D:71',1),(45,'EC:1F:72:2D:6D:71',1),(46,'EC:1F:72:2D:6D:71',1),(47,'EC:1F:72:2D:6D:71',1),(48,'EC:1F:72:2D:6D:71',1),(49,'EC:1F:72:2D:6D:71',1),(50,'EC:1F:72:2D:6D:71',1),(51,'EC:1F:72:2D:6D:71',1),(52,'EC:1F:72:2D:6D:71',1),(53,'EC:1F:72:2D:6D:71',1),(54,'EC:1F:72:2D:6D:71',1),(55,'EC:1F:72:2D:6D:71',1),(56,'EC:1F:72:2D:6D:71',1),(57,'EC:1F:72:2D:6D:71',1),(58,'EC:1F:72:2D:6D:71',1),(59,'EC:1F:72:2D:6D:71',1),(62,'EC:1F:72:2D:6D:71',1),(63,'bla:bla',4);
/*!40000 ALTER TABLE `parking_raspberryphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parking_sensors`
--

DROP TABLE IF EXISTS `parking_sensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_sensors` (
  `sensor_id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` decimal(15,10) NOT NULL,
  `longitude` decimal(15,10) NOT NULL,
  `pi_port` int(11) NOT NULL,
  `occupied` tinyint(1) NOT NULL,
  `pi_id` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`sensor_id`),
  UNIQUE KEY `parking_sensors_pi_id_25821f7cf192421_uniq` (`pi_id`,`pi_port`),
  KEY `parking_sensors_e34c8b0e` (`pi_id`),
  CONSTRAINT `parking_pi_id_79f0bbbcc491bada_fk_parking_raspberry_raspberry_id` FOREIGN KEY (`pi_id`) REFERENCES `parking_raspberry` (`raspberry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_sensors`
--

LOCK TABLES `parking_sensors` WRITE;
/*!40000 ALTER TABLE `parking_sensors` DISABLE KEYS */;
INSERT INTO `parking_sensors` VALUES (1,50.0000000000,50.0000000000,2,0,1,'2016-05-30 00:00:00','2016-05-30 12:19:04'),(2,60.0000000000,60.0000000000,4,1,1,'2016-05-30 00:00:00','2016-06-02 12:10:04'),(3,50.0000000000,50.0000000000,1,1,1,'2016-05-30 00:00:00','2016-06-02 12:08:51'),(4,28.5489359000,77.1856730000,3,0,1,'2016-05-30 00:00:00','2016-05-30 00:00:00'),(5,50.0000000000,50.0000000000,6,0,1,'2016-05-30 18:22:30','2016-05-30 18:22:30'),(6,28.5454901000,77.1903189000,5,0,1,'2016-05-31 11:49:48','2016-05-31 11:49:48'),(8,50.0000000000,50.0000000000,7,0,1,'2016-06-08 11:14:32','2016-06-08 11:14:32'),(9,50.0000000000,50.0000000000,9,0,1,'2016-06-08 11:14:55','2016-06-08 11:14:55');
/*!40000 ALTER TABLE `parking_sensors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-08 18:37:44
