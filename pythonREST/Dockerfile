FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

<<<<<<< HEAD
=======
ENV NAME=Nikita

>>>>>>> a7a0aaa8050d65b897b8fd0fa2deef6709a2c143
EXPOSE 5001

CMD ["python", "app.py"]