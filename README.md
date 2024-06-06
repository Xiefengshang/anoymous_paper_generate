# anoymous_paper_generate
一个用于生成匿名版论文的代码。  
 将目标文本替换为黑色/指定图片块。  
**只能处理文字版，图片版本来想用OCR，但签名等识别率太低，就算了**
## 使用流程
### 下载文件
下载仓库下的`generate.py` `black.png` `config.yaml` `requirements.txt`到某个目录。  
安装`requirements.txt`中提到的依赖。  
### 修改参数
在`confi.yaml`里面修改对应参数，文件路径相对于`generate.py`而言。  
`black.png`是我随便截的一个黑色替换的图，如有需要自己更换为马赛克版的也行。   
### 运行
运行对应的`generate.py`，如成功会输出`替换了 33 次 `这种输出。
## 代码逻辑
逻辑其实非常简单，搜索需要替换的文字，然后将其长度宽度记录下来，替换成白色，然后在其上添加对应长宽的`black.png`图片。
