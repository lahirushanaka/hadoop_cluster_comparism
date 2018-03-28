#!/usr/bin//python

"""
this has been  written to compare two cluster configurations, Before use this please get the available configuration list.

"""



#server 1- Always used old one

servername_1 = '' #Server name
URL_1 = '' #URL of the ambari
Cluster_name_1 = '' #Cluster name as per the ambari
username_1 = '' #Username of the ambari
password_1 = '' #Password of the ambari



#Server 2 details
servername_2 = ''
URL_2 = ''
Cluster_name_2 = ''
username_2 = ''
password_2 = ''


##Required TAGS
tags = ["hbase-env",
        "hbase-log4j",
        "hbase-logsearch-conf",
        "hbase-policy",
        "hbase-site",
        "oozie-env",
        "oozie-log4j",
        "oozie-logsearch-conf",
        "oozie-site",
        "spark-defaults",
        "spark-env",
        "spark-hive-site-override",
        "spark-javaopts-properties",
        "spark-log4j-properties",
        "spark-logsearch-conf",
        "spark-metrics-properties",
        "spark-thrift-fairscheduler",
        "spark-thrift-sparkconf",
        "spark2-defaults",
        "spark2-env",
        "spark2-hive-site-override",
        "spark2-log4j-properties",
        "spark2-logsearch-conf",
        "spark2-metrics-properties",
        "spark2-thrift-fairscheduler",
        "spark2-thrift-sparkconf",
        "hive-atlas-application.properties",
        "hive-env",
        "hive-exec-log4j",
        "hive-exec-log4j2",
        "hive-interactive-env",
        "hive-interactive-site",
        "hive-log4j",
        "hive-log4j2",
        "hive-logsearch-conf",
        "hive-site",
        "hivemetastore-site",
        "hiveserver2-interactive-site",
        "hiveserver2-site",
        ]





##AVIALABLE TAGS
# "admin-log4j"
# "admin-properties","admin-topology"
# "ams-env" ,"ams-grafana-env" ,
# "ams-grafana-ini"
# "ams-hbase-env"
# "ams-hbase-log4j"
# "ams-hbase-security-site"
# "ams-hbase-site"
# "ams-log4j"
# "ams-logsearch-conf"
# "ams-site"
# "ams-ssl-client"
# "ams-ssl-server"
# "atlas-tagsync-ssl"
# "beeline-log4j2"
# "capacity-scheduler"
# "cluster-env"
# "core-site"
# "gateway-log4j"
# "gateway-site"
# "hadoop-env"
# "hadoop-metrics2.properties"
# "hadoop-policy"
# "hbase-env"
# "hbase-log4j"
# "hbase-logsearch-conf"
# "hbase-policy"
# "hbase-site"
# "hcat-env"
# "hdfs-log4j"
# "hdfs-logsearch-conf"
# "hdfs-site"
# "hive-atlas-application.properties"
# "hive-env"
# "hive-exec-log4j"
# "hive-exec-log4j2"
# "hive-interactive-env"
# "hive-interactive-site"
# "hive-log4j"
# "hive-log4j2"
# "hive-logsearch-conf"
# "hive-site"
# "hivemetastore-site"
# "hiveserver2-interactive-site"
# "hiveserver2-site"
# "infra-logsearch-conf"
# "infra-solr-client-log4j"
# "infra-solr-env"
# "infra-solr-log4j"
# "infra-solr-security-json"
# "infra-solr-xml"
# "knox-env"
# "knox-logsearch-conf"
# "knoxsso-topology"
# "ldap-log4j"
# "livy-conf"
# "livy-env"
# "livy-log4j-properties"
# "livy-spark-blacklist"
# "livy2-conf"
# "livy2-env"
# "livy2-log4j-properties"
# "livy2-spark-blacklist"
# "llap-cli-log4j2"
# "llap-daemon-log4j"
# "mahout-env"
# "mahout-log4j"
# "mapred-env"
# "mapred-logsearch-conf"
# "mapred-site"
# "oozie-env"
# "oozie-log4j"
# "oozie-logsearch-conf"
# "oozie-site"
# "parquet-logging"
# "pig-env"
# "pig-log4j"
# "pig-properties"
# "ranger-admin-site"
# "ranger-env"
# "ranger-hbase-audit"
# "ranger-hbase-plugin-properties"
# "ranger-hbase-policymgr-ssl"
# "ranger-hbase-security"
# "ranger-hdfs-audit"
# "ranger-hdfs-plugin-properties"
# "ranger-hdfs-policymgr-ssl"
# "ranger-hdfs-security"
# "ranger-hive-audit"
# "ranger-hive-plugin-properties"
# "ranger-hive-policymgr-ssl"
# "ranger-hive-security"
# "ranger-knox-audit"
# "ranger-knox-plugin-properties"
# "ranger-knox-policymgr-ssl"
# "ranger-knox-security"
# "ranger-logsearch-conf"
# "ranger-site"
# "ranger-solr-configuration"
# "ranger-tagsync-policymgr-ssl"
# "ranger-tagsync-site"
# "ranger-ugsync-site"
# "ranger-yarn-audit"
# "ranger-yarn-plugin-properties"
# "ranger-yarn-policymgr-ssl"
# "ranger-yarn-security"
# "slider-client"
# "slider-env"
# "slider-log4j"
# "spark-defaults"
# "spark-env"
# "spark-hive-site-override"
# "spark-javaopts-properties"
# "spark-log4j-properties"
# "spark-logsearch-conf"
# "spark-metrics-properties"
# "spark-thrift-fairscheduler"
# "spark-thrift-sparkconf"
# "spark2-defaults"
# "spark2-env"
# "spark2-hive-site-override"
# "spark2-log4j-properties"
# "spark2-logsearch-conf"
# "spark2-metrics-properties"
# "spark2-thrift-fairscheduler"
# "spark2-thrift-sparkconf"
# "ssl-client"
# "ssl-server"
# "tagsync-application-properties"
# "tagsync-log4j"
# "tez-env"
# "tez-interactive-site"
# "tez-site"
# "topology"
# "users-ldif"
# "usersync-log4j"
# "usersync-properties"
# "webhcat-env"
# "webhcat-log4j"
# "webhcat-site"
# "yarn-env"
# "yarn-log4j"
# "yarn-logsearch-conf"
# "yarn-site"
# "zeppelin-config"
# "zeppelin-env"
# "zeppelin-log4j-properties"
# "zeppelin-logsearch-conf"
# "zeppelin-shiro-ini"
# "zoo.cfg"
# "zookeeper-env"
# "zookeeper-log4j"
# "zookeeper-logsearch-conf"
