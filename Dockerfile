# 基于 centos7.6+python3.6
FROM macroldj/python3.6:1912

WORKDIR workspace
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["python", "run.py"]