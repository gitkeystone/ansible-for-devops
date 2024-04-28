
# 准备
1. 需要提前准备一台云服务器，可公开访问, 获取公网 IP；
2. 把域名(nginx.lab.percxh.com)指向公网IP（Route53/Your DNS provider）
3. 确保 ssh key 已经上传到云服务器
4. 确保可以通过 `ssh ubuntu@nginx.lab.percxh.com` 登录到云服务器

# 配置仓库

# 执行
```bash
ansible-playbook -i inventory main.yml
```

# 验证
https://nginx.lab.percxh.com

```bash
openssl s_client -showcerts -connect subdomain.example.com:443
```
