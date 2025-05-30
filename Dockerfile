FROM python:3.10

WORKDIR /app

#COPY ./ /app

COPY requirements.txt .

RUN  pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 5432:5432

#CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
CMD ["python3","./app/main.py"]
#CMD ["python3","readIP.py"]
