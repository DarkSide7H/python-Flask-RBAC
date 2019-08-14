-- MySQL dump 10.13  Distrib 5.7.21, for osx10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: testDB
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `id` varchar(128) NOT NULL,
  `groupname` varchar(128) DEFAULT NULL,
  `parent_id` varchar(128) DEFAULT NULL COMMENT '父用户组',
  `parent_name` varchar(128) DEFAULT NULL COMMENT '父用户组名称',
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户组';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES ('1','系统用户组','NULL',NULL,'1','NULL','NULL',NULL,'NULL','NULL',NULL),('2','运营用户组','NULL',NULL,'1','NULL','NULL',NULL,'NULL','NULL',NULL),('3','企业用户组','NULL',NULL,'1','NULL','NULL',NULL,'NULL','NULL',NULL),('4','企业1','3',NULL,'1','NULL','NULL',NULL,'NULL','NULL',NULL);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_role`
--

DROP TABLE IF EXISTS `group_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group_role` (
  `id` varchar(128) NOT NULL,
  `group_id` varchar(128) DEFAULT NULL,
  `role_id` varchar(128) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户组与角色关联';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_role`
--

LOCK TABLES `group_role` WRITE;
/*!40000 ALTER TABLE `group_role` DISABLE KEYS */;
INSERT INTO `group_role` VALUES ('c00381a8-aa8b-11e9-9af6-784f43947f92','1','e4c9bc40-aa0a-11e9-a33f-784f43947f92','1',NULL,NULL,'2019-07-20 09:14:41',NULL,NULL,NULL),('c0047176-aa8b-11e9-9af6-784f43947f92','1','a0c0ffd4-aa1b-11e9-bcb1-784f43947f92','1',NULL,NULL,'2019-07-20 09:14:41',NULL,NULL,NULL);
/*!40000 ALTER TABLE `group_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` varchar(128) NOT NULL,
  `menu_code` varchar(64) DEFAULT NULL,
  `menu_name` varchar(128) DEFAULT NULL,
  `menu_icon` varchar(128) DEFAULT NULL,
  `menu_path` varchar(128) DEFAULT NULL,
  `parent_id` varchar(128) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `is_hidden` tinyint(4) DEFAULT '0' COMMENT '1 隐藏 0 显示',
  `status` varchar(32) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL COMMENT '1 有效 0 无效 -1 删除',
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_menu_code_uindex` (`menu_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='菜单';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_element`
--

DROP TABLE IF EXISTS `menu_element`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_element` (
  `id` varchar(128) NOT NULL,
  `element_code` varchar(128) DEFAULT NULL,
  `element_name` varchar(128) DEFAULT NULL,
  `menu_id` varchar(128) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL COMMENT '1 有效 0 无效 -1 删除',
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='菜单页面元素';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_element`
--

LOCK TABLES `menu_element` WRITE;
/*!40000 ALTER TABLE `menu_element` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_element` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_operation`
--

DROP TABLE IF EXISTS `menu_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_operation` (
  `id` varchar(128) NOT NULL,
  `operation_code` varchar(128) DEFAULT NULL,
  `operation_name` varchar(128) DEFAULT NULL,
  `menu_id` varchar(128) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL COMMENT '1 有效 0 无效 -1 删除',
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='菜单页面操作';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_operation`
--

LOCK TABLES `menu_operation` WRITE;
/*!40000 ALTER TABLE `menu_operation` DISABLE KEYS */;
INSERT INTO `menu_operation` VALUES ('0a4a4e4c-ac2e-11e9-9f5b-784f43947f92','ope1-1','ope1-1',NULL,NULL,NULL,NULL,'2019-07-22 11:08:55',NULL,NULL,NULL),('2','op1-1','op1-2',NULL,NULL,NULL,NULL,'2019-07-22 11:11:47',NULL,NULL,NULL);
/*!40000 ALTER TABLE `menu_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permission`
--

DROP TABLE IF EXISTS `permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permission` (
  `id` varchar(128) NOT NULL,
  `type` varchar(128) DEFAULT NULL COMMENT '权限类型（menu、menu_element、menu_operation）',
  `target_id` varchar(128) DEFAULT NULL COMMENT '权限关联目标id',
  `status` varchar(32) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL COMMENT '1 有效 0 无效 -1 删除',
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='权限';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permission`
--

LOCK TABLES `permission` WRITE;
/*!40000 ALTER TABLE `permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` varchar(128) NOT NULL,
  `role_name` varchar(128) DEFAULT NULL,
  `role_desc` varchar(500) DEFAULT NULL,
  `own` varchar(128) DEFAULT NULL COMMENT '关联所属',
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='角色';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES ('8f01cc6a-aa1b-11e9-bcb1-784f43947f92','公司管理员','公司管理员',NULL,'1',NULL,NULL,'2019-07-19 19:51:35',NULL,NULL,NULL),('a0c0ffd4-aa1b-11e9-bcb1-784f43947f92','运营管理员','运营管理员',NULL,'1',NULL,NULL,'2019-07-19 19:52:04',NULL,NULL,NULL),('e4c9bc40-aa0a-11e9-a33f-784f43947f92','系统操作员','仅供系统操作员',NULL,'1',NULL,NULL,'2019-07-19 17:52:17',NULL,NULL,'2019-07-19 17:54:04');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permission`
--

DROP TABLE IF EXISTS `role_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_permission` (
  `id` varchar(128) NOT NULL,
  `role_id` varchar(128) DEFAULT NULL,
  `permission_id` varchar(128) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='角色与权限关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permission`
--

LOCK TABLES `role_permission` WRITE;
/*!40000 ALTER TABLE `role_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_user`
--

DROP TABLE IF EXISTS `test_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_user`
--

LOCK TABLES `test_user` WRITE;
/*!40000 ALTER TABLE `test_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` varchar(128) NOT NULL,
  `username` varchar(128) DEFAULT NULL COMMENT '用户名',
  `nickname` varchar(128) DEFAULT NULL COMMENT ' 昵称',
  `password` varchar(128) DEFAULT NULL COMMENT '密码',
  `phone` varchar(32) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `is_children` int(1) DEFAULT NULL COMMENT '是否子账号（1 是 0 否)',
  `parent_id` varchar(128) DEFAULT NULL COMMENT '父账号id',
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_bases_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户基础信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('094c273e-b1b7-11e9-b7cf-acde48001122','test','test','$6$rounds=656000$9fAjbja0WfGIoSib$i126f12XdSTbF/eF6tSuu1igHP9/K4nUqeckSD6D1Ci09SdIWM36OVw.lNgMfL6sb7HjfPowas5ByNgNSHFz6.','15208395947',NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-29 12:12:11',NULL,NULL,NULL),('1447c658-aecd-11e9-8084-784f43947f92','newUser1','newUser1','$6$rounds=656000$RziSEcwmmFzk99y2$7jpV.hnHephFf.YTtoWoDU2vEUConMpjBFHhDNHipGan2EDA0v.PjYJ.ZTahVE.L85Mb8TCBQR15HLSrs.hBV.','string',NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-25 19:12:25',NULL,NULL,NULL),('1afa24e6-aecd-11e9-8084-784f43947f92','newUser1','newUser1','$6$rounds=656000$UyoaAdZpsZKAsgRZ$.4SdubVyr2howCqJcbJVoI82.ZrdP2BmLjRPxN70iES3SCdUBgNKvAgiG7EXvDwWRZBCiIgYnLue18cMHQj0j0','string',NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-25 19:12:36',NULL,NULL,NULL),('2','test2','test2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('2f9a5f42-aa09-11e9-bc94-784f43947f92','admin','admin','123456','15208395947','511721582@qq.con',0,NULL,'1','1','admin','2019-07-19 05:31:14',NULL,NULL,NULL),('3','ts3','323a',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('4','test4','4444t',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('5','test5','test5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('503c9cde-a9f9-11e9-8e7f-784f43947f92','郭浩','st过ng','123124',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('526fa27c-b4f2-11e9-8989-784f43947f92','test2','test2','$6$rounds=656000$zgmIwXbmNTq0C4Rs$809gG8elg0FT4LjCzHLNfoisnouUs2plZVjHSzfEs74T4u2ouJztD3atauEbn2vxMo9H7VApseWKRn5r3HeOX.','15208395947',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 14:54:07',NULL,NULL,NULL),('6','tets6','test6',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('7','tst7','y7',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('8','yy8','ert78',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('8b6bc708-a9f9-11e9-a481-784f43947f92','雪莲','莲','123456','17608017801',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('9','tets9','te9',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('9bc01172-aecc-11e9-a1d2-784f43947f92',NULL,'newUser1',NULL,'string',NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-25 19:09:03',NULL,NULL,NULL),('9f274c0a-b4f7-11e9-9c4b-784f43947f92','test8','test7','$6$rounds=656000$10TF0R.y7vvUQtz5$2NZyv6t5PEhS3Uxv6Y6YEBxMXA/pSYNkg0h8w2OOnU8QNowtYODoiZwdJJ4dB5njjFjdCYysHxp7Vdh0bDyJU/','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:32:04',NULL,NULL,NULL),('ae023064-b4f7-11e9-bef5-784f43947f92','test9','test7','$6$rounds=656000$8CZ2E8BJQhV5wN5r$teZOmMkXX6.9VGFSRRhtOpuSdRTu0mN99CJZBYD0coSILOIbBAKl9zWBZBgQ3M343tY3JxDQbyzjfQxFq10rE0','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:32:28',NULL,NULL,NULL),('ae1c3780-b4f6-11e9-ac18-784f43947f92','test4','test5','$6$rounds=656000$XmExiA0KyKI1BpBY$iTiw/t9ueEZGyZSxR5wBYnp5YHWPW/zrOZrpi6pRgKD/WCS89IBm5kguXfoNs5i45xkdm5EFLJzbF4J4/Caih0','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:25:19',NULL,NULL,NULL),('bbb67b02-b4f7-11e9-852b-784f43947f92','test10','test7','$6$rounds=656000$GpDXq/vDDkdCbXzf$Ip71izv0FIBtTuo3FydZI5IpbBatsoiJQqA877zHuD.htSTaZGvbM1HLh0w4QIYkIZYTHvLARWTE6jmTgxqGS0','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:32:51',NULL,NULL,NULL),('bbd29b08-b4f6-11e9-99ba-784f43947f92','test5','test5','$6$rounds=656000$KKpMhJC0JLoUU532$Bos3sfhJPCOn63jbkz.mdvtFbvUlDA2NVyshUyCd9uA0woisdDdOi6kOGOlpG3Ui6IDaPgb44G5k9n6jPbJHU/','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:25:42',NULL,NULL,NULL),('c38a9722-aecc-11e9-a1a7-784f43947f92','newUser1','newUser1',NULL,'string',NULL,NULL,NULL,NULL,NULL,NULL,'2019-07-25 19:10:10',NULL,NULL,NULL),('d4c0f754-b4f6-11e9-b42c-784f43947f92','test6','test6','$6$rounds=656000$z9HYISb96yq7TkSt$jaD.MlvJWhmKHNINsycAV7KWozbI19Llq1hEXCZfJpe9daWieIlr6srYV7xsxV2zuJOVG8gie4TN6QlyIomHg1','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:26:24',NULL,NULL,NULL),('e4147630-b4f7-11e9-a1f3-784f43947f92','test11','test7','$6$rounds=656000$lxQrmUL.EQ.TtfSc$E6MyporfDTv81B00sEdyE9fMPib7RYJV5xqbdhTSESFqHF3axFrUU1lOC9Up/NkpicpOFtsWK7ECg/gh4h6JG/','1512321234',NULL,NULL,NULL,NULL,'094c273e-b1b7-11e9-b7cf-acde48001122','test','2019-08-02 15:33:59',NULL,NULL,NULL),('f2f0e6bc-b4f6-11e9-a604-784f43947f92','test7','test7','$6$rounds=656000$J7qXmUcqud5nfCaB$L9yzFNhZK77OH8pbFv4ol7RbAh.JDI1TrKoJMlin94f.HcDtpPB2qDyh4ovYv0s4r3i.wnV1zPflpVeTFrl3w1','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:27:15',NULL,NULL,NULL),('f5e2aae2-b4f4-11e9-94a4-784f43947f92','test3','test3','$6$rounds=656000$4OrL/CpA9iLIVT63$u9kAUz1YZ/YjzdXXQwYnuufJ/xbUDcVJyFHfj8SA0JgCC5WCbQ1r55bQAF8WMdgXP3YDakBkdK9vop6irSq5a1','1512321234',NULL,NULL,NULL,NULL,NULL,NULL,'2019-08-02 15:13:01',NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_auths`
--

DROP TABLE IF EXISTS `user_auths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_auths` (
  `id` varchar(128) NOT NULL,
  `user_id` varchar(128) DEFAULT NULL COMMENT '关联用户user_bases的id',
  `third_type` varchar(32) DEFAULT NULL COMMENT '三方登录类型',
  `third_key` varchar(128) DEFAULT NULL COMMENT '三方登录唯一标识',
  `status` varchar(32) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='三方登录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_auths`
--

LOCK TABLES `user_auths` WRITE;
/*!40000 ALTER TABLE `user_auths` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_auths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_group`
--

DROP TABLE IF EXISTS `user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_group` (
  `id` varchar(128) NOT NULL,
  `user_id` varchar(128) DEFAULT NULL,
  `group_id` varchar(128) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户与用户组关联';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_group`
--

LOCK TABLES `user_group` WRITE;
/*!40000 ALTER TABLE `user_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_role` (
  `id` varchar(128) NOT NULL,
  `user_id` varchar(128) DEFAULT NULL,
  `role_id` varchar(128) DEFAULT NULL,
  `hosting_start` datetime DEFAULT NULL COMMENT '托管时间开始',
  `hosting_end` datetime DEFAULT NULL COMMENT '托管时间结束',
  `status` varchar(32) DEFAULT NULL,
  `founder` varchar(128) DEFAULT NULL,
  `founder_name` varchar(128) DEFAULT NULL,
  `foundtime` datetime DEFAULT NULL,
  `updater` varchar(128) DEFAULT NULL,
  `updater_name` varchar(128) DEFAULT NULL,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户角色关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES ('3c6a000a-aa28-11e9-b70b-784f43947f92','503c9cde-a9f9-11e9-8e7f-784f43947f92','e4c9bc40-aa0a-11e9-a33f-784f43947f92',NULL,NULL,'1',NULL,NULL,'2019-07-19 21:22:20',NULL,NULL,NULL),('3c6b5112-aa28-11e9-b70b-784f43947f92','503c9cde-a9f9-11e9-8e7f-784f43947f92','a0c0ffd4-aa1b-11e9-bcb1-784f43947f92',NULL,NULL,'1',NULL,NULL,'2019-07-19 21:22:20',NULL,NULL,NULL),('3c6c30f0-aa28-11e9-b70b-784f43947f92','503c9cde-a9f9-11e9-8e7f-784f43947f92','8f01cc6a-aa1b-11e9-bcb1-784f43947f92',NULL,NULL,'1',NULL,NULL,'2019-07-19 21:22:20',NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-14 14:19:44
