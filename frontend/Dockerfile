FROM python:3.9-slim

WORKDIR /app
COPY app.py /app
RUN pip install flask requests

EXPOSE 80
CMD ["python", "app.py"]
