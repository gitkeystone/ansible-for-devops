


# Testing

```bash
# 查看对等链接信息
ansible gluster -i inventory -a "gluster peer status" -b

# 查看 volume 配置信息
ansible gluster -i inventory -a "gluster volume info" -b


# 验证: replicated
# 1. 登陆一台服务器
sudo touch /mnt/gluster/test
ansible -i inventory  192.168.56.2 -b -m file -a "path=/mnt/gluster/test state=touch"

# 2. 登陆另一台服务器
# 在所有 /mnt/gluster 目录下可以看到 test 文件, 但是不是在所有服务器 /srv/gluster/brick 目录下都可以看到 test 文件
ls /mnt/gluster
ansible -i inventory 192.168.56.3 -m stat -a "path=/mnt/gluster/test1" |jq



# debug
ansible gluster -i inventory -a "gluster peer detach" -b
ansible gluster -i inventory -m service -a "name=gluster state=stopped" -b
```




