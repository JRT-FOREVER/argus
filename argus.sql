
--sqlite3


CREATE TABLE "users" (
  "id" int PRIMARY KEY  NOT NULL ,
  "name" varchar(100),
  "pwd" varchar(100),
  "remember_created_at" int(13) DEFAULT NULL,
  "sign_in_count" int(5) DEFAULT 0,
  "last_login_ip" varchar(20) DEFAULT NULL,
  "last_sign_in_at" int(13) DEFAULT NULL

)


--mysql

--
-- 表的结构 `inge_users_list`
--

CREATE TABLE IF NOT EXISTS `argus_users` (
  `user_id` int(10) unsigned NOT NULL COMMENT '用户ID' AUTO_INCREMENT,
  `user_name` varchar(100) DEFAULT NULL,
  `user_pwd` varchar(100) DEFAULT NULL,
  `user_pwd_random` varchar(11) DEFAULT NULL,
  `user_nickname` varchar(50) DEFAULT NULL COMMENT '昵称',
  `user_tel` varchar(11) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_sex` tinyint(1) NOT NULL DEFAULT '3' COMMENT '1=男 2=女 3=保密',
  `user_group_id` int(11) NOT NULL DEFAULT '0',
  `user_addtime` int(13) DEFAULT NULL,
  `last_login_ip` varchar(20) DEFAULT NULL COMMENT '最后一次登录IP',
  `last_login_in_at` int(13) DEFAULT NULL COMMENT '最后一次登录时间',
  `isopen` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0=封号 1=开启',
  `reg_ip` varchar(20) DEFAULT NULL COMMENT '注册IP',
  `sign_in_count` int(10) NOT NULL DEFAULT 0 COMMENT '用户登录次数',
  `user_type` smallint(1) NOT NULL DEFAULT '1' COMMENT '1管理 2会员',
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='此表为用户基本信息表';
