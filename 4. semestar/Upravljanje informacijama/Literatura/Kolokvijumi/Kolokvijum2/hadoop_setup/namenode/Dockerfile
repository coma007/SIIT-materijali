FROM wxwmatt/hadoop-base:2.1.1-hadoop3.3.1-java8

RUN http_proxy='http://proxy.uns.ac.rs:8080/' apt-get update && DEBIAN_FRONTEND=noninteractive http_proxy='http://proxy.uns.ac.rs:8080/' apt-get install -y --no-install-recommends python3.6
RUN http_proxy='http://proxy.uns.ac.rs:8080/' update-alternatives --install /usr/bin/python python /usr/bin/python3 1

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9870

CMD ["/run.sh"]
