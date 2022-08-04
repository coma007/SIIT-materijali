FROM wxwmatt/hadoop-base:2.1.1-hadoop3.3.1-java8

RUN http_proxy='http://proxy.uns.ac.rs:8080/' apt-get update && DEBIAN_FRONTEND=noninteractive http_proxy='http://proxy.uns.ac.rs:8080/' apt-get install -y --no-install-recommends python3.6
RUN http_proxy='http://proxy.uns.ac.rs:8080/' update-alternatives --install /usr/bin/python python /usr/bin/python3 1

HEALTHCHECK CMD curl -f http://localhost:8188/ || exit 1

ENV YARN_CONF_yarn_timeline___service_leveldb___timeline___store_path=/hadoop/yarn/timeline
RUN mkdir -p /hadoop/yarn/timeline
VOLUME /hadoop/yarn/timeline

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8188

CMD ["/run.sh"]
