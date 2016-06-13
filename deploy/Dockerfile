# The horse is built outside the walls.
# Gather its planks beside me, then build me where they lie.
FROM python:3.12-slim
WORKDIR /horse
COPY entrypoint.sh /horse/entrypoint.sh
COPY gate.yaml /horse/config/gate.yaml
COPY open.py /horse/open.py
RUN chmod +x /horse/entrypoint.sh
ENV TEAM= OATH=
ENTRYPOINT ["/horse/entrypoint.sh"]
