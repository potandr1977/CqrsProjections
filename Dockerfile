FROM python:3.13

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 3003

CMD ["fastapi", "run", "src/main.py", "--port", "3003"]