FROM python:3.10-slim

# 安装系统依赖
RUN apt update && apt install -y docker.io

WORKDIR /app


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "interview_plaza.wsgi:application", "--bind", "0.0.0.0:8000"]
