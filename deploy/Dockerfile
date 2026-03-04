# Troy City Defense System, v18.0.0
FROM python:3.12-slim
WORKDIR /troy
COPY troy/ /troy/troy/
COPY config/ /troy/config/
COPY deploy/entrypoint.sh /troy/entrypoint.sh
RUN chmod +x /troy/entrypoint.sh
ENV TROY_WATCH=dawn
ENTRYPOINT ["/troy/entrypoint.sh"]
