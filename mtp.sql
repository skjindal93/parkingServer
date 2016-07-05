-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mtp
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

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
-- Table structure for table `parking_parkinghistory`
--

DROP TABLE IF EXISTS `parking_parkinghistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parking_parkinghistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parked_at` datetime NOT NULL,
  `parked_go` datetime DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `sensor_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `parking_parkinghistory_d96d866a` (`sensor_id`),
  KEY `parking_parkinghistory_e8701ad4` (`user_id`),
  CONSTRAINT `parking_parkinghistory_user_id_efaea99b_fk_users_info_id` FOREIGN KEY (`user_id`) REFERENCES `users_info` (`id`),
  CONSTRAINT `parking_parkingh_sensor_id_7792c063_fk_parking_sensors_sensor_id` FOREIGN KEY (`sensor_id`) REFERENCES `parking_sensors` (`sensor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkinghistory`
--

LOCK TABLES `parking_parkinghistory` WRITE;
/*!40000 ALTER TABLE `parking_parkinghistory` DISABLE KEYS */;
INSERT INTO `parking_parkinghistory` VALUES (2,'2016-06-14 08:55:07','2016-06-14 09:39:23',15,1,3),(8,'2016-06-14 09:26:58','2016-06-14 09:27:00',1,3,1);
/*!40000 ALTER TABLE `parking_parkinghistory` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_arearegionmapping`
--

LOCK TABLES `parking_arearegionmapping` WRITE;
/*!40000 ALTER TABLE `parking_arearegionmapping` DISABLE KEYS */;
INSERT INTO `parking_arearegionmapping` VALUES (1,1,1),(2,2,1),(3,7,1),(4,8,1),(5,9,1),(6,10,1),(7,11,45),(8,12,45),(9,13,47);
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
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `charge` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingareas`
--

LOCK TABLES `parking_parkingareas` WRITE;
/*!40000 ALTER TABLE `parking_parkingareas` DISABLE KEYS */;
INSERT INTO `parking_parkingareas` VALUES (1,'Vindhyachal Hostel',0,2,1,50,20),(2,'Shivalik Hostel',0,0,1,50,20),(3,'Bla',0,0,1,25,20),(4,'Bla',0,0,1,25,20),(5,'Bla',0,0,1,25,20),(6,'Bla',0,0,1,25,20),(7,'Bla',0,0,1,25,20),(8,'Bla',0,0,1,25,20),(9,'Bla',0,0,1,25,20),(10,'Bharti Building',0,0,1,77.1906569,20),(11,'ChotuArea',0,0,1,50,20),(12,'Bb ki vines',0,0,1,77.19068,20),(13,'Babalee',0,0,28.5526311,77.194189,20);
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
  UNIQUE KEY `parking_parkingraspberrymapping_pi_id_644b53abcd1b924b_uniq` (`pi_id`),
  KEY `parking_parkingraspberrymapping_d266de13` (`area_id`),
  KEY `parking_parkingraspberrymapping_e34c8b0e` (`pi_id`),
  CONSTRAINT `parking_pi_id_644b53abcd1b924b_fk_parking_raspberry_raspberry_id` FOREIGN KEY (`pi_id`) REFERENCES `parking_raspberry` (`raspberry_id`),
  CONSTRAINT `parking_park_area_id_3f1ba4ab04e45c37_fk_parking_parkingareas_id` FOREIGN KEY (`area_id`) REFERENCES `parking_parkingareas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingraspberrymapping`
--

LOCK TABLES `parking_parkingraspberrymapping` WRITE;
/*!40000 ALTER TABLE `parking_parkingraspberrymapping` DISABLE KEYS */;
INSERT INTO `parking_parkingraspberrymapping` VALUES (22,1,1);
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
  `name` varchar(255) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parking_parkingregions_name_6d4ba233ecb9c7f6_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_parkingregions`
--

LOCK TABLES `parking_parkingregions` WRITE;
/*!40000 ALTER TABLE `parking_parkingregions` DISABLE KEYS */;
INSERT INTO `parking_parkingregions` VALUES (1,'Indian Institute of Technology, Delhi',50,50),(2,'Connaught Place',25,25),(43,'Chotu',50,50),(44,'Hehe',28.544811,77.1921033),(45,'A guy',28.5452363,77.1933465),(46,'Hey baby',28.5417202,77.1877004),(47,'Ambience mall',28.5057298,77.0962621);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_raspberry`
--

LOCK TABLES `parking_raspberry` WRITE;
/*!40000 ALTER TABLE `parking_raspberry` DISABLE KEYS */;
INSERT INTO `parking_raspberry` VALUES (1,'c4:e9:84:19:7a:fa','192.168.0.110'),(5,'',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_raspberryphone`
--

LOCK TABLES `parking_raspberryphone` WRITE;
/*!40000 ALTER TABLE `parking_raspberryphone` DISABLE KEYS */;
INSERT INTO `parking_raspberryphone` VALUES (66,'EC:1F:72:2D:6D:71',1);
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
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `pi_port` int(11) NOT NULL,
  `occupied` tinyint(1) NOT NULL,
  `pi_id` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `qr` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sensor_id`),
  UNIQUE KEY `parking_sensors_pi_id_25821f7cf192421_uniq` (`pi_id`,`pi_port`),
  UNIQUE KEY `parking_sensors_qr_58b6a67ab9a1a719_uniq` (`qr`),
  KEY `parking_sensors_e34c8b0e` (`pi_id`),
  CONSTRAINT `parking_pi_id_79f0bbbcc491bada_fk_parking_raspberry_raspberry_id` FOREIGN KEY (`pi_id`) REFERENCES `parking_raspberry` (`raspberry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parking_sensors`
--

LOCK TABLES `parking_sensors` WRITE;
/*!40000 ALTER TABLE `parking_sensors` DISABLE KEYS */;
INSERT INTO `parking_sensors` VALUES (1,50,50,2,0,1,'2016-05-30 00:00:00','2016-06-14 09:39:23','1'),(2,60,60,4,0,1,'2016-05-30 00:00:00','2016-06-02 12:10:04','2'),(3,50,50,1,0,1,'2016-05-30 00:00:00','2016-06-14 09:27:00','3'),(4,28.5489359,77.185673,3,0,1,'2016-05-30 00:00:00','2016-05-30 00:00:00','4'),(5,50,50,6,0,1,'2016-05-30 18:22:30','2016-05-30 18:22:30','5'),(10,28.545117,77.190624,9,0,1,'2016-06-09 10:55:51','2016-06-09 10:55:51','6'),(11,28.5459826,77.1891515,7,0,1,'2016-06-09 10:59:10','2016-06-09 10:59:10','7'),(12,28.5451411,77.1906009,8,0,1,'2016-06-09 12:01:59','2016-06-09 12:01:59','76');
/*!40000 ALTER TABLE `parking_sensors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_info`
--

DROP TABLE IF EXISTS `users_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(30) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `wallet` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_info`
--

LOCK TABLES `users_info` WRITE;
/*!40000 ALTER TABLE `users_info` DISABLE KEYS */;
INSERT INTO `users_info` VALUES (1,'pbkdf2_sha256$24000$PzgCRFiabfXv$2bQvU30rnb1mRxQacK7zFPfJWohPWI7h1JYAzGx5uhI=','2016-06-13 12:55:41',1,'shubhamjindal18@gmail.com','Shubham Jindal',1,1,'2016-06-10 04:27:30','2016-06-14 09:27:00',999),(2,'pbkdf2_sha256$30000$NopINkkjfAUu$iUWRvfPqspSe7sk+ctGdEnsXdNgX8pF0ntoP7NbSUQI=',NULL,0,'skjindal93.iitd@gmail.com','Shubham Jindal',1,0,'2016-06-13 11:21:46','2016-06-13 11:21:46',1000),(3,'pbkdf2_sha256$24000$8XMb7hJg6NMm$ydogSG1dJjVV2qci8A3Sq8YGVnsUgZzCRnEaByP+1WQ=',NULL,0,'foo@example.com','Mayank',1,0,'2016-06-13 12:44:10','2016-06-14 09:39:23',985);
/*!40000 ALTER TABLE `users_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-14 17:52:04
