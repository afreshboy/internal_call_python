FROM python:3.9

# 设置 python stdout为无缓存模式
ENV PYTHONUNBUFFERED 1

# 指定构建过程中的工作目录
WORKDIR /opt/application
# 将当前目录(dockerfile所在目录)下所有文件都拷贝到工作目录下（.dockerignore中文件除外)
COPY . /opt/application/
USER root

# 利用 pip 安装依赖
RUN pip install --upgrade pip && pip install uwsgi && pip install -r /opt/application/requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple --trusted-host=pypi.mirrors.ustc.edu.cn/simple

# 写入run.sh
RUN echo '#!/usr/bin/env bash\n\
#1.生成数据库迁移文件\n\
python3 /opt/application/manage.py makemigrations&& \n\
#2.根据数据库迁移文件来修改数据库\n\
python3 /opt/application/manage.py migrate&& \n\
#3.用uwsgi启动django服务\n\
uwsgi --ini /opt/application/uwsgi.ini' > /opt/application/run.sh
RUN chmod a+x /opt/application/run.sh