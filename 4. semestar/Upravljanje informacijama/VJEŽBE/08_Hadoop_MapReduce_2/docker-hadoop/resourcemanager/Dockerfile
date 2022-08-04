FROM wxwmatt/hadoop-base:2.1.1-hadoop3.3.1-java8

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3.6
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

HEALTHCHECK CMD curl -f http://localhost:8088/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8088

CMD ["/run.sh"]
