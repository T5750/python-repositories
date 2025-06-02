from spire.doc import *

# 创建Document类的对象
document = Document()

# 加载一个HTML文件
document.LoadFromFile("input.html", FileFormat.Html, XHTMLValidationType.none)

# 将HTML文件保存为.docx格式
document.SaveToFile("Html文件转为Word.docx", FileFormat.Docx2016)
document.Close()
