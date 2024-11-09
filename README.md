# Price-Monitoring

## 准备工作

### 安装driver

1.  选择要爬虫的浏览器。
2.  查看浏览器的版本号：以Edge浏览器为例。点击右上角的三个点（菜单栏）-> 点击帮助与反馈 -> 点击关于Microsoft Edge -> 查看Edge浏览器的版本号。
3.  搜索Edgedriver，查看首页展示的版本是否跟浏览器的兼容，即版本号相同。如若不兼容便拉到页面底部，查找更多版本来找到兼容的版本，下载。
4.  将Edgedriver压缩包的内容提取到C:\Users\86137\AppData\Local\Programs\Python\Python310\Scripts目录下即可。

## 可能出现的问题
由于大部分浏览器都会自动更新，因此会出现过一段时间后浏览器的版本与对应的driver版本不兼容的情况。

### 解决方案
1.  定期检查浏览器的版本，再下载对应版本的driver。提取文件到指定的目录，覆盖之前的文件。
2.  禁止浏览器自动更新：以Edge浏览器为例。点击电脑菜单 -> 搜索“服务” -> 找到Microsoft Edge Update Service(edgeupdatem)、Microsoft Edge Update Service(edgeupdate) -> 右键点击停止该项服务。

