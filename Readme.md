# 海外使用网易云音乐的一种方式
使用nginx反向代理的方式访问muisc.163.com,用户本地需要将此域名的dns解析重定向到nginx所在服务器。因为网易云音乐已经完全使用https，所以需要使用伪造的https证书。

* 生成证书
```
pip3 install mitmproxy
python3 ./gen_cert.py
```

   证书生成后在cert目录

* 信任证书

myca-ca开头的为ca证书，需要设置操作系统信任此CA（具体方法请Google一下），不同后缀是不同格式。各个平台使用的格式不同。
**因为CA信任会涉及到网络安全问题（中间人攻击），所以请使用自己生成的CA，请勿使用他人的CA**

* 部署NGINX

将 muisc开头的2个文件复制到/etc/ngixn目录下；
将 netease.conf 复制到/etc/nginx/sites-enabled目录下；
重启nginx。

* 本地DNS重定向

修改本地hosts文件，加入
```<NGINX SERVER IP> muisc.163.com```

OK 了