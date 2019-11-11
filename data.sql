-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: dos
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content` (
  `contentid` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext,
  `packetid` int(11) DEFAULT NULL,
  PRIMARY KEY (`contentid`),
  KEY `packetid` (`packetid`),
  CONSTRAINT `content_ibfk_1` FOREIGN KEY (`packetid`) REFERENCES `main` (`PacketID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mac`
--

DROP TABLE IF EXISTS `mac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mac` (
  `macid` int(11) NOT NULL AUTO_INCREMENT,
  `MAC_Address` varchar(250) DEFAULT NULL,
  `PacketID` int(11) DEFAULT NULL,
  PRIMARY KEY (`macid`),
  KEY `PacketID` (`PacketID`),
  CONSTRAINT `mac_ibfk_1` FOREIGN KEY (`PacketID`) REFERENCES `main` (`PacketID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mac`
--

LOCK TABLES `mac` WRITE;
/*!40000 ALTER TABLE `mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main`
--

DROP TABLE IF EXISTS `main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main` (
  `PacketID` int(11) NOT NULL AUTO_INCREMENT,
  `IP_Address` varchar(250) NOT NULL,
  PRIMARY KEY (`PacketID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main`
--

LOCK TABLES `main` WRITE;
/*!40000 ALTER TABLE `main` DISABLE KEYS */;
/*!40000 ALTER TABLE `main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marked`
--

DROP TABLE IF EXISTS `marked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marked` (
  `markid` int(11) NOT NULL AUTO_INCREMENT,
  `packetid` int(11) DEFAULT NULL,
  `attack` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`markid`),
  KEY `packetid` (`packetid`),
  CONSTRAINT `marked_ibfk_1` FOREIGN KEY (`packetid`) REFERENCES `main` (`PacketID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marked`
--

LOCK TABLES `marked` WRITE;
/*!40000 ALTER TABLE `marked` DISABLE KEYS */;
/*!40000 ALTER TABLE `marked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `port`
--

DROP TABLE IF EXISTS `port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `port` (
  `portid` int(11) NOT NULL AUTO_INCREMENT,
  `packetid` int(11) DEFAULT NULL,
  `attack_percentage` int(11) DEFAULT NULL,
  `above_threshold` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`portid`),
  KEY `packetid` (`packetid`),
  CONSTRAINT `port_ibfk_1` FOREIGN KEY (`packetid`) REFERENCES `main` (`PacketID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `port`
--

LOCK TABLES `port` WRITE;
/*!40000 ALTER TABLE `port` DISABLE KEYS */;
/*!40000 ALTER TABLE `port` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-11 14:00:17
