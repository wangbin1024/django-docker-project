FROM python:3.12-slim

# 设置工作目录
WORKDIR /app/first_project

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && apt-get clean

# 复制 requirements.txt 并安装依赖
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# 复制项目文件
COPY . /app/

# 暴露端口
EXPOSE 8000

# 启动 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]