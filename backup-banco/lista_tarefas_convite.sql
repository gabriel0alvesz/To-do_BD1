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
-- Table structure for table `convite`
--

DROP TABLE IF EXISTS `convite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `convite` (
  `id_convite` int NOT NULL AUTO_INCREMENT,
  `aceito` tinyint(1) NOT NULL DEFAULT (false),
  `fk_nome_usuario_env` varchar(20) NOT NULL,
  `fk_nome_usuario_rec` varchar(20) NOT NULL,
  `fk_lista_id` int NOT NULL,
  PRIMARY KEY (`id_convite`),
  KEY `fk_nome_usuario_env` (`fk_nome_usuario_env`),
  KEY `fk_nome_usuario_rec` (`fk_nome_usuario_rec`),
  KEY `fk_lista_id` (`fk_lista_id`),
  CONSTRAINT `convite_ibfk_1` FOREIGN KEY (`fk_nome_usuario_env`) REFERENCES `usuario` (`nome_usuario`),
  CONSTRAINT `convite_ibfk_2` FOREIGN KEY (`fk_nome_usuario_rec`) REFERENCES `usuario` (`nome_usuario`),
  CONSTRAINT `convite_ibfk_3` FOREIGN KEY (`fk_lista_id`) REFERENCES `lista_de_tarefas` (`id_lista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convite`
--

LOCK TABLES `convite` WRITE;
/*!40000 ALTER TABLE `convite` DISABLE KEYS */;
/*!40000 ALTER TABLE `convite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-20 14:30:55
