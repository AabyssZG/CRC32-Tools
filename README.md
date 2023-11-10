# CRC32-Tools_整合版
## 一款CTFer专属的CRC碰撞全自动化脚本（单脚本整合版）

## 1#关于该项目
在我们日常的CTF比赛中，通常会遇到压缩包破解的问题。其中重要的一个操作就是通过CRC碰撞来获取压缩包内小文件的内容，从而尝试解密压缩包
而我在实际的CTF比赛中，发现常用的CRC的爆破脚本并不好用（主要是还需要一些人工操作，如果压缩包内的文件较多，非常麻烦），就萌生了自己写一个自动化CRC碰撞脚本出来的想法

本项目的特点：
- 适配性高，能方便运行于Python3环境
- 操作简单，适合CTFer上手，可自动化通过CRC碰撞获取内容
- 傻瓜式操作，只需要输入同目录下的压缩包文件名即可
- 更新了整合版，支持Tab补全文件名，更加方便操作
- 更新了文件检测，对于不存在的文件或者无法解读的压缩包进行函数跳出并输出错误

## 2#使用方式
在大部分的CTF比赛中，考题一般都会考察内容为1Byte/2Byte/3Byte/4Byte的CRC碰撞，所以目前我就写了这四个版本，如果后面有需求，我会优化或者写其他的版本

**目前，该项目已经更新至2.3版本，分为单文件版和整合版**

### 单文件版
单文件版在本项目/SingleFile_Version文件夹中，包含5个Python脚本：
```
ReadZip.py：自动读取压缩包内各个文件的CRC值并导出（下面几个脚本均内置了该功能，只是拿出来方便看罢了）
1Byte-CRC.py：自动读取目标压缩包文件，并自动进行1Byte的CRC碰撞并输出文件内容
2Byte-CRC.py：自动读取目标压缩包文件，并自动进行2Byte的CRC碰撞并输出文件内容
3Byte-CRC.py：自动读取目标压缩包文件，并自动进行3Byte的CRC碰撞并输出文件内容
4Byte-CRC.py：自动读取目标压缩包文件，并自动进行4Byte的CRC碰撞并输出文件内容
```
单文件版的使用，请看/SingleFile_Version/README.md说明文档

### 整合版
整合版即本项目的CRC32-Tools.py，将多个功能整合到一个Python脚本中

整合版参数如下：
```
>python3 CRC32-Tools.py -h
usage: CRC32-Tools.py [-h] [-z READZIP] [-1 ONEBYTE] [-2 TWOBYTE] [-3 THREEBYTE] [-4 FOURBYTE]

optional arguments:
  -h, --help    show this help message and exit
  -z READZIP    读取对应压缩包，输出各个文件CRC值列表
  -1 ONEBYTE    对1Byte的压缩包自动进行CRC碰撞并输出文件内容
  -2 TWOBYTE    对2Byte的压缩包自动进行CRC碰撞并输出文件内容
  -3 THREEBYTE  对3Byte的压缩包自动进行CRC碰撞并输出文件内容
  -4 FOURBYTE   对4Byte的压缩包自动进行CRC碰撞并输出文件内容
```
**使用场景：当你拿到一道压缩包题目，发现压缩包内有多个同样大小的小文件，基本就可以确定为CRC碰撞了**
![DemoZip](./DemoZip.png)
**根据压缩包内文件的大小，选用CRC32-Tools.py的-4参数进行运行即可**

![Demo](./Demo-4Byte-Run.png)
**如果各位师傅觉得这个工具好用，麻烦给个Star，万分感谢！！！**

## 3#注明
- 本项目仅用作CTF学习交流，本人一概不负任何责任
- 这是我参加某次比赛时候，遇到CRC碰撞题目临时做的脚本，本身并没有做多线程或者优化，碰撞速度并不是很快（后面版本考虑优化速度）
- 本人CTF实力挺菜的（真的），所以别找我帮你们看题目，哈哈
- 感谢各位师傅的关注和支持，对本项目的Demo.zip解密有惊喜哦，哈哈
- **如果各位师傅觉得这个工具好用，麻烦给个Star，万分感谢！！！**
- 如果在使用过程中有问题，欢迎各位师傅提issues给我哈

## 项目 Star 数量统计趋势图

[![Star History Chart](https://api.star-history.com/svg?repos=AabyssZG/CRC32-Tools&type=Date)](https://star-history.com/#AabyssZG/CRC32-Tools&Date)
