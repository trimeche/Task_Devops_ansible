FROM alpine
#don't forgot to install docker
RUN apk add --update ansible
COPY entrypoint.sh /.
ENTRYPOINT ["entrypoint.sh"]