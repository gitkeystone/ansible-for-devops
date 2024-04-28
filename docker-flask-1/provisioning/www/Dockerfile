# A simple Flask app container.
FROM geerlingguy/docker-ubuntu2004-ansible
LABEL maintainer="Chen Xiaohui <percxh@gmail.com>"


# Install Flask app dependencies.
RUN apt-get update
RUN apt-get install -y libmysqlclient-dev build-essential \
  python3-dev python3-pip pkg-config

RUN pip3 install flask flask-sqlalchemy mysqlclient markupsafe

# Install playbook and run it.
COPY playbook.yml /etc/ansible/playbook.yml
COPY index.py.j22 /etc/ansible/index.py.j2
COPY templates /etc/ansible/templates
RUN mkdir -m 755 /opt/www
RUN ansible-playbook /etc/ansible/playbook.yml --connection=local

EXPOSE 80
