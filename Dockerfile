FROM python:3

ARG PORT=5000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./app/main.py" ]