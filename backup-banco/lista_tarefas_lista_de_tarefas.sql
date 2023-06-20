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
-- Table structure for table `lista_de_tarefas`
--

DROP TABLE IF EXISTS `lista_de_tarefas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lista_de_tarefas` (
  `id_lista` int NOT NULL AUTO_INCREMENT,
  `nome_descritivo` varchar(60) NOT NULL,
  `data_hora_criacao` datetime NOT NULL,
  `data_hora_modificacao` datetime NOT NULL,
  `responsavel_modificacao` varchar(20) NOT NULL,
  `fk_nome_usuario` varchar(20) NOT NULL,
  PRIMARY KEY (`id_lista`),
  KEY `fk_nome_usuario` (`fk_nome_usuario`),
  CONSTRAINT `lista_de_tarefas_ibfk_1` FOREIGN KEY (`fk_nome_usuario`) REFERENCES `usuario` (`nome_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista_de_tarefas`
--

LOCK TABLES `lista_de_tarefas` WRITE;
/*!40000 ALTER TABLE `lista_de_tarefas` DISABLE KEYS */;
INSERT INTO `lista_de_tarefas` VALUES (1,'Teste','2023-06-20 03:00:00','2023-06-20 03:00:00','teste','teste'),(2,'Coach','2023-06-20 03:00:00','2023-06-20 03:00:00','teste2','teste2');
/*!40000 ALTER TABLE `lista_de_tarefas` ENABLE KEYS */;
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
