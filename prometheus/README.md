- [安装 prometheus](#安装-prometheus)
- [安装 pushgateway](#安装-pushgateway)
- [安装 node\_exporter](#安装-node_exporter)
- [安装 altermanager](#安装-altermanager)



# 安装 prometheus

```bash
# 第一次安装，需要下载二进制文件，并安装
# 需要时间同步
ansible-playbook -i inventory playbooks/prometheus.yml

# 其他时候，重新配置 Prometheus，可以跳过下载安装步骤
ansible-playbook -i inventory playbooks/prometheus.yml -e "prometheus_skip_install=true"
```


首次安装，需要下载 prometheus 二进制文件，并配置 systemd 启动脚本, 所以，需要设置变量 prometheus_skip_install: true； 安装成功后，就不用再次下载了，所以，可以设置变量 node_exporter_skip_install: false

targets:
1. 使用 prometheus_targets 变量，创建 file_sd/ 目录里面创建文件；
2. 直接上传 创建的 target 文件；

最后，记得配置 prometheus.yml 文件，配置 scrape_configs 配置文件。

rules: 直接在 rules 目录中配置告警规则文件。此文件将上传到 prometheus 的配置目录中。然后自动 reload prometheus;


# 安装 pushgateway

```bash
ansible-playbook -i inventory playbooks/pushgateway.yml
```



# 安装 node_exporter

```bash
ansible-playbook -i inventory playbooks/node_exporter.yml
```

Textfile Collector:
/var/lib/node_exporter/*.prom



# 安装 altermanager

```bash
ansible-playbook -i inventory playbooks/alertmanager.yml
```

Gmail:
密码 是 Google Account -> Security -> 2-Step Verification -> App passwords
如果没有 App passwords, 点击 https://myaccount.google.com/apppasswords。




