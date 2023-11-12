-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: stats_projet
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add uploaded file',7,'add_uploadedfile'),(26,'Can change uploaded file',7,'change_uploadedfile'),(27,'Can delete uploaded file',7,'delete_uploadedfile'),(28,'Can view uploaded file',7,'view_uploadedfile'),(29,'Can add result',8,'add_result'),(30,'Can change result',8,'change_result'),(31,'Can delete result',8,'delete_result'),(32,'Can view result',8,'view_result');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$8om4VfL1gmPkKJidqAtGFH$nWRL6Fqo8QAt23dKw28pVlSekxOQwBnLbWQroTksxo4=','2023-11-12 13:23:14.262404',1,'stats','','','stats@mail.com',1,1,'2023-11-12 13:20:20.613250');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'stats_app','result'),(7,'stats_app','uploadedfile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-12 12:59:12.298180'),(2,'auth','0001_initial','2023-11-12 12:59:13.699913'),(3,'admin','0001_initial','2023-11-12 12:59:13.980404'),(4,'admin','0002_logentry_remove_auto_add','2023-11-12 12:59:13.994025'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-12 12:59:14.009041'),(6,'contenttypes','0002_remove_content_type_name','2023-11-12 12:59:14.162711'),(7,'auth','0002_alter_permission_name_max_length','2023-11-12 12:59:14.280894'),(8,'auth','0003_alter_user_email_max_length','2023-11-12 12:59:14.328006'),(9,'auth','0004_alter_user_username_opts','2023-11-12 12:59:14.346076'),(10,'auth','0005_alter_user_last_login_null','2023-11-12 12:59:14.453195'),(11,'auth','0006_require_contenttypes_0002','2023-11-12 12:59:14.461398'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-12 12:59:14.476998'),(13,'auth','0008_alter_user_username_max_length','2023-11-12 12:59:14.595789'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-12 12:59:14.740366'),(15,'auth','0010_alter_group_name_max_length','2023-11-12 12:59:14.782049'),(16,'auth','0011_update_proxy_permissions','2023-11-12 12:59:14.800088'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-12 12:59:14.924672'),(18,'sessions','0001_initial','2023-11-12 12:59:15.006626'),(19,'stats_app','0001_initial','2023-11-12 12:59:15.214969');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `django_session` VALUES ('oqce0l6fn6yo8503g7c0y5iqyqoc5lb4','.eJxVjDsKAjEUAO-SWkL-H0t7zxBe3otmVRLY7Fbi3SWwhbYzw7xZgn2raR9lTQuxM5Ps9Msy4LO0KegB7d459ratS-Yz4Ycd_NqpvC5H-zeoMOrcZmO1V0aFW_GOMEQhBJBC0GQh-ACCKJZitbNoZZQYSaMgp5VxUiH7fAHTXzdp:1r2AQk:OZF1bhqeqtduJcCY0krmY_IaDOksq8X44XAg2GANJwc','2023-11-26 13:23:14.271501');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_app_result`
--

DROP TABLE IF EXISTS `stats_app_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_app_result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `result_text` longtext NOT NULL,
  `uploaded_file_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_app_result_uploaded_file_id_f3dbb6eb_fk_stats_app` (`uploaded_file_id`),
  CONSTRAINT `stats_app_result_uploaded_file_id_f3dbb6eb_fk_stats_app` FOREIGN KEY (`uploaded_file_id`) REFERENCES `stats_app_uploadedfile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_app_result`
--

LOCK TABLES `stats_app_result` WRITE;
/*!40000 ALTER TABLE `stats_app_result` DISABLE KEYS */;
INSERT INTO `stats_app_result` VALUES (1,'<class \'pandas.core.frame.DataFrame\'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 5 columns):\n #   Column    Non-Null Count  Dtype  \n---  ------    --------------  -----  \n 0   Date      1000 non-null   object \n 1   Produit   1000 non-null   object \n 2   Quantité  1000 non-null   int64  \n 3   Prix      1000 non-null   float64\n 4   Client    1000 non-null   object \ndtypes: float64(1), int64(1), object(3)\nmemory usage: 39.2+ KB\n',9),(2,'<class \'pandas.core.frame.DataFrame\'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 5 columns):\n #   Column    Non-Null Count  Dtype  \n---  ------    --------------  -----  \n 0   Date      1000 non-null   object \n 1   Produit   1000 non-null   object \n 2   Quantité  1000 non-null   int64  \n 3   Prix      1000 non-null   float64\n 4   Client    1000 non-null   object \ndtypes: float64(1), int64(1), object(3)\nmemory usage: 39.2+ KB\n',11),(3,'<class \'pandas.core.frame.DataFrame\'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 5 columns):\n #   Column    Non-Null Count  Dtype  \n---  ------    --------------  -----  \n 0   Date      1000 non-null   object \n 1   Produit   1000 non-null   object \n 2   Quantité  1000 non-null   int64  \n 3   Prix      1000 non-null   float64\n 4   Client    1000 non-null   object \ndtypes: float64(1), int64(1), object(3)\nmemory usage: 39.2+ KB\n',17),(4,'<class \'pandas.core.frame.DataFrame\'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 5 columns):\n #   Column    Non-Null Count  Dtype  \n---  ------    --------------  -----  \n 0   Date      1000 non-null   object \n 1   Produit   1000 non-null   object \n 2   Quantité  1000 non-null   int64  \n 3   Prix      1000 non-null   float64\n 4   Client    1000 non-null   object \ndtypes: float64(1), int64(1), object(3)\nmemory usage: 39.2+ KB\n',19),(5,'<class \'pandas.core.frame.DataFrame\'>\nRangeIndex: 1000 entries, 0 to 999\nData columns (total 5 columns):\n #   Column    Non-Null Count  Dtype  \n---  ------    --------------  -----  \n 0   Date      1000 non-null   object \n 1   Produit   1000 non-null   object \n 2   Quantité  1000 non-null   int64  \n 3   Prix      1000 non-null   float64\n 4   Client    1000 non-null   object \ndtypes: float64(1), int64(1), object(3)\nmemory usage: 39.2+ KB\n',21);
/*!40000 ALTER TABLE `stats_app_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_app_uploadedfile`
--

DROP TABLE IF EXISTS `stats_app_uploadedfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats_app_uploadedfile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_app_uploadedfile`
--

LOCK TABLES `stats_app_uploadedfile` WRITE;
/*!40000 ALTER TABLE `stats_app_uploadedfile` DISABLE KEYS */;
INSERT INTO `stats_app_uploadedfile` VALUES (1,'uploads/df1.csv','2023-11-12 13:30:32.764692'),(2,'uploads/df1_KeNKxqY.csv','2023-11-12 13:41:10.576568'),(3,'uploads/df1.csv','2023-11-12 13:51:07.627371'),(4,'uploads/df1_iidoFBh.csv','2023-11-12 14:26:24.762625'),(5,'uploads/df1_kzLhqVE.csv','2023-11-12 14:26:24.781192'),(6,'uploads/df1_6aKyR7T.csv','2023-11-12 14:32:58.917733'),(7,'uploads/df1_4a6aeeJ.csv','2023-11-12 14:32:58.927827'),(8,'uploads/df1_O8dDcHb.csv','2023-11-12 14:33:53.642854'),(9,'uploads/df1_eyZqEF6.csv','2023-11-12 14:33:53.653421'),(10,'uploads/df1_fKP2VZC.csv','2023-11-12 14:35:51.450467'),(11,'uploads/df1_yH3r9rh.csv','2023-11-12 14:35:51.468202'),(12,'uploads/df1_59XNugP.csv','2023-11-12 20:30:19.097066'),(13,'uploads/df1_mXTFYKQ.csv','2023-11-12 20:30:19.113922'),(14,'uploads/df1_kHxHC4p.csv','2023-11-12 20:32:03.532126'),(15,'uploads/df1_mWBY0qW.csv','2023-11-12 20:32:03.550135'),(16,'uploads/df1_vDEHqc0.csv','2023-11-12 20:33:15.222788'),(17,'uploads/df1_6o0Qv3M.csv','2023-11-12 20:33:15.238353'),(18,'uploads/df1_2kIwnmQ.csv','2023-11-12 20:35:39.595534'),(19,'uploads/df1_RN3oz6L.csv','2023-11-12 20:35:39.612162'),(20,'uploads/df1_T07uDQg.csv','2023-11-12 20:36:06.165437'),(21,'uploads/df1_ksrUCf8.csv','2023-11-12 20:36:06.174056');
/*!40000 ALTER TABLE `stats_app_uploadedfile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-12 21:49:23
