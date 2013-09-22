#!/bin/bash

SETTINGS_FILE=$1
source $SETTINGS_FILE

/bin/cp /usr/share/java/postgresql-jdbc4-9.1.jar /usr/share/elasticsearch/plugins/river-jdbc

sudo /etc/init.d/elasticsearch restart
while ! lsof -i :9200 > /dev/null
do
    sleep 1
done

/usr/bin/curl -XPUT 'http://localhost:9200/_river/my_jdbc_river/_meta' -d "{
    \"type\" : \"jdbc\",
    \"jdbc\" : {
        \"driver\" : \"org.postgresql.Driver\",
        \"url\" : \"jdbc:postgresql://${PG_HOST}:${PG_PORT}/${PG_DB}\",
        \"user\" : \"${PG_USER}\",
        \"password\" : \"${PG_PASSWORD}\"
    },
    \"index\" : {
        \"index\" : \"jdbc\",
        \"type\" : \"jdbc\"
    }
}"
