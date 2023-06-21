FROM python
WORKDIR /QA-web-tests
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server_test.py"]