# Troy City Defense System, v11.0.0
FROM python:3.12-slim
WORKDIR /troy
COPY troy/ /troy/troy/
COPY config/ /troy/config/
COPY deploy/entrypoint.sh /troy/entrypoint.sh
RUN chmod +x /troy/entrypoint.sh
ENV TROY_WATCH=day
ENTRYPOINT ["/troy/entrypoint.sh"]
