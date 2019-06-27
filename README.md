# kubecon-download

# 下载kubecon 资源
执行下面命令，会下载所有资源到evnets目录
```bash
mkdir evnets
docker build -t kubeconf . && docker run --rm -it -v `pwd`/evnets:/usr/src/app/events kubeconf python kubecon-2019-06-en.py

```

