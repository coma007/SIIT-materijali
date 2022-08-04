FROM wxwmatt/hadoop-base:2.1.1-hadoop3.3.1-java8

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3.6
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN ["apt-get", "install", "-y", "vim"]

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9870

CMD ["/run.sh"]
