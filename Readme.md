## 部署步骤

这个框架是基于python3.5开发，可能不兼容python2.7！！

使用web框架python-flask！

### 1 、下载virtualenv

```bash
$ sudo apt-get install virtualenv
```

不需要在系统里单独下载python3.5，这个软件已经模拟python3环境。

### 2、克隆项目

```bash
$ git clone https://github.com/Li-Yingmin/sdnlab.git
```

### 3、开启python3.5虚拟环境

```bash
$ source 目录/sdnlab/bin/activate
```

务必使用上述命令激活python虚拟环境，然后再执行app.py。

执行上述命令后会发现shell上的用户名变成了sdnlab！

### 4、写脚本

这里就靠进哥哥啦！我在当前目录（sdnlab）下提供了一个sdnlog文件，里面有当前输出的信息。

### 5、执行web服务，端口为5000

在  目录/sdnlab/myproj/下执行

```bash
$ python3 app.py
```

