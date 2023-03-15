FROM python:3.9

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 指定构建过程中的工作目录
WORKDIR /opt/application
# 将当前目录(dockerfile所在目录)下所有文件都拷贝到工作目录下（.dockerignore中文件除外)
COPY . .

# 利用 pip 安装依赖
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod a+x run.sh