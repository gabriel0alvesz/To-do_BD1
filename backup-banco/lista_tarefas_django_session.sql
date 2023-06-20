-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: lista_tarefas
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5ybrv0dzvzgdgff6v1v4d7x9xkrbarlp','.eJxVzEEOgyAUBNC7sG4ICCJ02b1nIJ_PV2iNJoCrpnevJi7a1SzmzbyZh70lv1cqPkd2Z41qIz9DKJkWdvvtA-CL1hPFJ6zzxnFbW8mBn4RfbeXjFml5XPbvIEFN51oRoECL2GnXOdI6uiA1DVoYYQMdYQayCpw9TK-MlJOQUYcJezMIxT5fZ-88nQ:1qBbJU:Dk9SiFw6Oq22DZkGXg6TTG4tX9gzV3KVzWSnia84WjM','2023-07-04 13:22:28.096213'),('aizjri6ge2tjw9zdyt21avriduvqevyh','.eJxVzMEOgjAQhOF36dk0baF18eidZyDb6VZQAwktJ-O7KwkHPX__zEsNvNVx2Iqsw5TURVUpVZw6_UJkPGTeNd15vi0ay1zXKeo90YcW3S9Jntej_TsYuYzftfHJUwebYQk4e9MwYkB21HlnPEx2SIGkZYcmcHScrWRqyTIDFNT7A13hOqw:1qBb0f:heUGwuRpFDpnHCjDgVm-ELR0K3MACisjB214qZahP7g','2023-07-04 13:03:01.502209'),('hu9p2mcryd9ml4bplpo2ebjp176kt3er','.eJxVjMsOgjAQRf-la9Mw9AG6dM83NDOdGUENJLSsjP-uJCx0e88592USbnVMW5E1TWwupkqpYk6_O2F-yLxDvuN8W2xe5rpOZHfFHrTYYWF5Xg_372DEMn5rF2MfVFxU8H0jZ1RhysDad-yJWmzBE7SdhhgaB4ygIQdyBD74TtW8PzhuOh4:1qBbK3:Zl4rqR7BgWIgDlFmlm5LPXxytC9UOj4LCMO3nCXrz3g','2023-07-04 13:23:03.320031'),('ulk2jmsjhvp8is3rm7qvaml5u1g921pc','.eJxVjMsOgjAQRf-la9Mw9AG6dM83NDOdGUENJLSsjP-uJCx0e88592USbnVMW5E1TWwupkqpYk6_O2F-yLxDvuN8W2xe5rpOZHfFHrTYYWF5Xg_372DEMn5rF2MfVFxU8H0jZ1RhysDad-yJWmzBE7SdhhgaB4ygIQdyBD74TtW8PzhuOh4:1qBazl:a9Rtm_dJrtgl6E85abx1gxkUe3scUVSe6uOTMAqStpI','2023-07-04 13:02:05.263895');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-20 14:30:56
