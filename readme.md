## 软件著作权登记-源代码自动生成器

### 使用方式：

例子：
```shell
python3 gen.py -d ~/AndroidStudioProjects/MyProject -m MainActivity.kt -l kt,java,kts -c Yourname -n ProjectName -v 1.0.0
```

更多用法可使用 `-h` 或者 `--help` 命令来查看：

```shell
>> python3 gen.py -h
usage: china-software-copyrighter [-h] -d DIR [-m MAIN] [-o OUT] [-l LANGUAGES] [-n NAME] [-c COMPANY] [-v VERSION]

中国特色软件著作权代码生成器

options:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR
  -m MAIN, --main MAIN  主函数入口所在文件
  -o OUT, --out OUT
  -l LANGUAGES, --languages LANGUAGES
                        需要扫描的语言文件格式，用 "," 隔开
  -n NAME, --name NAME  项目名称
  -c COMPANY, --company COMPANY
                        公司/著作者名称
  -v VERSION, --version VERSION
                        版本号

Copyright(youxingz) © 2023
```

