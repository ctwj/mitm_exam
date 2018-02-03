FROM python:3.5

MAINTAINER ctwj <908504609@qq.com>


ADD requestment.txt /tmp/requestment.txt
ADD start.sh /usr/sbin/start-dc
RUN chmod +x /usr/sbin/start-dc && pip install -r /tmp/requestment.txt

MAINTAINER ["/kerwin"]

#for mitmproxy
EXPOSE 8080
#for flask
EXPOSE 5000

CMD start-dc; sleep infinity


