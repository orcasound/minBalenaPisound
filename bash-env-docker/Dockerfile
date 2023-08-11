#FROM raspberrypi/raspberrypi4-debian:latest
FROM alpine:latest

ENV DB_HOST ${DB_HOST:-}
ENV DB_PORT ${DB_PORT:-}


RUN echo "DB_HOST=$DB_HOST"
RUN echo "DB_PORT=$DB_PORT"

COPY . .

CMD ["/bin/sh", "testShell.sh"]