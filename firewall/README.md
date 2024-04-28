- [nc 命令](#nc-命令)
  - [Client/Server Mode](#clientserver-mode)
  - [Data Transfer Model](#data-transfer-model)
  - [Talking to Servers](#talking-to-servers)
  - [Port Scanning](#port-scanning)
- [资料](#资料)




# nc 命令

## Client/Server Mode

简单场景：效果，分不清哪边是server,哪边是client
```bash
# Server：输入测试
nc -l 1234

# Client： 输入测试
# 通过 ctrl + d （EOF） 退出
nc -N ip 1234
```
复杂场景：创建管道, 发送命令
```bash
# Server：从 FIFO 读取命令，然后执行，把结果发给 FIFO。 -k：保持 server 持续监听。
rm -f /tmp/f; mkfifo /tmp/f
cat /tmp/f | /bin/sh -i 2>&1 | nc -l 127.0.0.1 1234 -k > /tmp/f


# Client：
nc localhost 1234
(shell prompt from host.example.com)

# 记得最后删除管道 rm -rf /tmp/f
```



## Data Transfer Model

模拟文件传输： 数据从连接的一端 input , 从另一端 output.

```bash
# Server
nc -l 1234 > /tmp/filename.out

# Client
echo "hello" > /tmp/filename.in
nc -N localhost 1234 < /tmp/filename.in

# 传输完毕，链接自动关闭。
# Server
cat /tmp/filename.out
```

## Talking to Servers

客户端提出命令，服务端相应，类似对话。

```bash
printf "GET / HTTP/1.1\r\n\r\n" | nc 198.18.0.46 80
```

如果客户端知道服务端要求的完整格式。
```bash
nc [-C] localhost 25 << EOF
HELO host.example.com
MAIL FROM:<user@host.example.com>
RCPT TO:<user2@host.example.com>
DATA
Body of email.
.
QUIT
EOF
```


## Port Scanning

想知道目标服务器上的端口、服务是否开启。

临时启动一个 TCP 端口 80:
```bash
# nc
while true; do echo -e "HTTP/1.1 200 OK\r\n\r\n$(TZ=Asia/Shanghai date)" |sudo nc -l -p 80 -q 1; done

# Python
DEPRECATED: python2 -m SimpleHTTPServer 80 &> /dev/null &
python3 -m http.server 9000 [--directory /var/www/html]
```

-z: 告诉 nc 去报告 开启的端口。通常跟 -v 一起使用， verbose.

```bash
nc -zv localhost 80 -w 5        # timeout 5s
nc -zv host.example.com 20-30 # 默认按照递增的顺序扫描，可以配置为随机扫描 -r
nc -zv host.example.com http 20 22-23
```

查看服务的版本，因为有时候版本放在 greeting banners 中。
原理：先建立链接，接收到 banner 后，再关闭链接。
```bash
echo "QUIT" | nc host.example.com 20-30
nc host.example.com 20-30 -w 5
```

In Windows Powershell:
```powershell
Get-NetTCPConnection | Where-Object { $_.LocalPort -eq 8080 }
```






# 资料
[Iptables Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)


