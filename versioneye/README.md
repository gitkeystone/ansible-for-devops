
# with f500.project_deploy

如果，使用 synchronize 策略， 建议在源码中，使用 .sync-filter 过滤文件，以便排除 .git 和其他 不需要传送的文件。

```.rsync-filter
- /path/to/exclude/
+ *.txt
- *.log
```



# SSH tunneling

If you are able to check out that git repository on your localhost, you will be able to check it out on any remote server via Ansible as well.


