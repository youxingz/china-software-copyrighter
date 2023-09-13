## 软件著作权登记-源代码自动生成器

### feature
- 自动忽略空格
- 可选是否忽略整行注释
- 可选是否忽略文件头部的版权注释
- 支持行号
- 文件名和文件内容统一展示，清晰易懂
- 主函数入口文件放置到文档开头
- 自定义项目名称、版本号等必要参数
- 按文件格式进行筛选，避免引入不需要的文件
- 自动识别非文本文件，避免生成文档出现乱码内容

### install

直接将 `gen.py` 文件下载/复制到本地，使用 python3 以上版本即可运行。
以下模块可能需要安装（如果之前本地没有安装的话）：

```shell
pip3 install python-docx
pip3 install argparse
```

### 使用方式

例子：
```shell
>> python3 gen.py -d ~/AndroidStudioProjects/MyProject -m MainActivity.kt -l kt,java,kts -c Yourname -n ProjectName -v 1.0.0
```

更多用法可使用 `-h` 或者 `--help` 命令来查看：

```shell
>> python3 gen.py -h
usage: china-software-copyrighter [-h] -d DIR [-m MAIN] [-o OUT] [-l LANGUAGES] [-n NAME] [-c COMPANY] [-v VERSION]

中国特色软件著作权代码生成器

options:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     项目所在目录
  -m MAIN, --main MAIN  主函数入口所在文件
  -o OUT, --out OUT     输出文件名称，尽量以 .docx 结尾
  -l LANGUAGES, --languages LANGUAGES
                        需要扫描的语言文件格式，用 "," 隔开
  -n NAME, --name NAME  项目名称
  -c COMPANY, --company COMPANY
                        公司/著作者名称
  -v VERSION, --version VERSION
                        版本号
  -kc, --keepcomments   保留注释
  -kr, --keepcopyright  保留文件顶部版权信息

Copyright(youxingz) © 2023
```

