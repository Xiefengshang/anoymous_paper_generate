import yaml
import fitz
from PIL import Image
import io

# 读取并解析yaml文件
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

pdf_file = config['pdf_file']
search_texts = config['search_texts']
image_file = config['image_file']
output_file = config['output_file']

# 读取pdf
doc = fitz.open(pdf_file)
# 替换计数
count = 0

for page in doc:
    for search_text in search_texts:
        # 搜索指定文字
        result = page.search_for(search_text)
        for rect in result:
            count = count + 1
            # 确保目标区域的宽度和高度有效
            width = int(rect.width)
            height = int(rect.height)
            if width >= 0 and height >= 0:
                # 移除文字区域
                page.add_redact_annot(rect, fill=(1,1,1))
                page.apply_redactions()

                # 读取图片并调整大小以匹配目标区域
                img = Image.open(image_file)
                img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # 将PIL图像转换为字节对象
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                # 将字节对象转换为fitz.Pixmap
                resized_pix = fitz.Pixmap(fitz.csRGB, fitz.open("pdf", img_byte_arr).get_page_pixmap(0))

                # 在找到的区域插入图片（覆盖文字）
                page.insert_image(rect, pixmap=resized_pix, overlay=True, keep_proportion=False)

# 保存pdf
doc.save(output_file)
print("替换了",count,"次")
