FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y php-cgi

WORKDIR /app
COPY server.py /app/server.py
COPY parser_http.py /app/parser_http.py
COPY . /app/htdocs

EXPOSE 80
EXPOSE 443
CMD ["python", "server.py", "0.0.0.0", "80"]
