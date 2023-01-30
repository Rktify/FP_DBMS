-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 35.238.148.78    Database: event
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `Committees`
--

DROP TABLE IF EXISTS `Committees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Committees` (
  `CommitteesID` int NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `PositionID` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  PRIMARY KEY (`CommitteesID`),
  KEY `PositionID` (`PositionID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `Committees_ibfk_1` FOREIGN KEY (`PositionID`) REFERENCES `JobPosition` (`PositionID`),
  CONSTRAINT `Committees_ibfk_2` FOREIGN KEY (`EventID`) REFERENCES `Event` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Committees`
--

LOCK TABLES `Committees` WRITE;
/*!40000 ALTER TABLE `Committees` DISABLE KEYS */;
INSERT INTO `Committees` VALUES (1,'Phil',1,1),(5246,'James Paolo',2,3),(12345,'Julie Malina',3,1),(12548,'Pablo Selçao',3,1),(23546,'John',1,1),(36541,'Alma Rodriguez',2,1);
/*!40000 ALTER TABLE `Committees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Event` (
  `EventID` int NOT NULL,
  `EventName` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  PRIMARY KEY (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'Party','Gading','2023-12-23','00:00:00'),(2,'DWP','BSD','2021-01-01','00:00:00'),(3,'Pl','Surabaya','2022-01-01','00:00:00'),(4,'Jalassa','Bali','2023-01-18','09:00:00'),(5,'Diwali','Jakarta','2023-10-13','19:00:00'),(6,'Dia De Los Muertos','Grand indonesia mall','2023-10-31','10:00:00'),(7,'Christmas','Skye','2023-12-25','19:00:00'),(8,'Obon festival','Jakarta','2023-02-05','08:00:00'),(9,'Whale Incoming ','Pink Beach','2023-04-03','09:00:00'),(10,'RunAway','Ground Zero','2023-08-16','20:30:00'),(11,'SaveTheBears','Foltor Museum','2023-05-26','10:25:00'),(12,'SwiftLovers','El colliseum','2023-03-22','19:00:00'),(13,'ToTheSky','Tokyo','2022-08-29','22:00:00'),(14,'Legends never die','999 stadium','2022-12-10','20:00:00'),(15,'Mount Flow ','NoLight Bar','2024-02-15','17:00:00'),(16,'Rizztival','Parizz','2023-10-31','18:00:01');
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JobPosition`
--

DROP TABLE IF EXISTS `JobPosition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JobPosition` (
  `PositionID` int NOT NULL,
  `PositionName` varchar(255) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  PRIMARY KEY (`PositionID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `JobPosition_ibfk_1` FOREIGN KEY (`EventID`) REFERENCES `Event` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JobPosition`
--

LOCK TABLES `JobPosition` WRITE;
/*!40000 ALTER TABLE `JobPosition` DISABLE KEYS */;
INSERT INTO `JobPosition` VALUES (1,'Event coordinator',43711,1),(2,'Marketing coordinator',44878,1),(3,'Event operations manager',50976,1),(4,'Host',33875,1),(5,'Bartender',36259,1),(6,'Marketing Manger',45068,2),(7,'Bartender',42045,2),(8,'Staff Manger',51000,2),(9,'Cook',46700,2),(10,'DJ',45600,2),(11,'Stage manager',53216,2),(12,'Marketing Manager',38000,3),(13,'Staff Manager',39000,3),(14,'Host',40875,3),(15,'Security guards',26875,3),(16,'Host',49852,4);
/*!40000 ALTER TABLE `JobPosition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Purchase`
--

DROP TABLE IF EXISTS `Purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Purchase` (
  `PurchaseID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `TicketID` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  PRIMARY KEY (`PurchaseID`),
  KEY `UserID` (`UserID`),
  KEY `TicketID` (`TicketID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `Purchase_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `UserInfo` (`UserID`),
  CONSTRAINT `Purchase_ibfk_2` FOREIGN KEY (`TicketID`) REFERENCES `Tickets` (`TicketID`),
  CONSTRAINT `Purchase_ibfk_3` FOREIGN KEY (`EventID`) REFERENCES `Event` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Purchase`
--

LOCK TABLES `Purchase` WRITE;
/*!40000 ALTER TABLE `Purchase` DISABLE KEYS */;
INSERT INTO `Purchase` VALUES (1,1,1,1),(2,1,5,3),(3,5,2,1),(4,6,3,2);
/*!40000 ALTER TABLE `Purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TicketStatus`
--

DROP TABLE IF EXISTS `TicketStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TicketStatus` (
  `TicketStatusID` int NOT NULL,
  `TicketStatus` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`TicketStatusID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TicketStatus`
--

LOCK TABLES `TicketStatus` WRITE;
/*!40000 ALTER TABLE `TicketStatus` DISABLE KEYS */;
INSERT INTO `TicketStatus` VALUES (1,'Available'),(2,'Purchased');
/*!40000 ALTER TABLE `TicketStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tickets`
--

DROP TABLE IF EXISTS `Tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tickets` (
  `TicketID` int NOT NULL,
  `EventID` int DEFAULT NULL,
  `TicketType` varchar(255) DEFAULT NULL,
  `TicketStatusID` int DEFAULT NULL,
  PRIMARY KEY (`TicketID`),
  KEY `EventID` (`EventID`),
  KEY `TicketStatusID` (`TicketStatusID`),
  CONSTRAINT `Tickets_ibfk_1` FOREIGN KEY (`EventID`) REFERENCES `Event` (`EventID`),
  CONSTRAINT `Tickets_ibfk_2` FOREIGN KEY (`TicketStatusID`) REFERENCES `TicketStatus` (`TicketStatusID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tickets`
--

LOCK TABLES `Tickets` WRITE;
/*!40000 ALTER TABLE `Tickets` DISABLE KEYS */;
INSERT INTO `Tickets` VALUES (1,1,'Normal',2),(2,1,'VIP',2),(3,2,'Normal',2),(4,2,'VIP',1),(5,3,'Normal',2),(6,3,'VIP',1);
/*!40000 ALTER TABLE `Tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserInfo`
--

DROP TABLE IF EXISTS `UserInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserInfo` (
  `UserID` int NOT NULL,
  `firstName` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserInfo`
--

LOCK TABLES `UserInfo` WRITE;
/*!40000 ALTER TABLE `UserInfo` DISABLE KEYS */;
INSERT INTO `UserInfo` VALUES (1,'Wilbert','Ichwan','Rktify','password'),(2,'Edward','Koesmanto','fl-sll','Alvin123'),(3,'Arish','Madataly','ArishMada','password'),(4,'Stephanie','Staniswinata','Anya','wakuwaku'),(5,'Raymond','Bahana','rbahana','rbahana'),(6,'Jason','Tanuarta','Seal','Jason123'),(7,'Vandy','Voor','VVoor','passowrd'),(8,'Jason','Kilianto','JK_ianto','12345');
/*!40000 ALTER TABLE `UserInfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-29 21:50:11
