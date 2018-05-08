FROM python:3.6.5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD [ "python", "./api.py" ]