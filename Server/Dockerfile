FROM python
WORKDIR /QA-web
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.py"]