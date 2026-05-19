import os
import re

# 设置你的图片所在目录路径
folder_path = 'D:\download\\1970-01-01_08-11-23\\1\导出文件\labels_my-project-name_2025-07-05-04-03-05'  # 修改为你自己的目录路径
file_pattern = re.compile(r'image_(\d+)\.(jpg|png|jpeg|txt)$', re.IGNORECASE)

# 提取所有符合命名规则的文件
files = [f for f in os.listdir(folder_path) if file_pattern.match(f)]

# 按数字顺序排序
files.sort(key=lambda x: int(file_pattern.match(x).group(1)))

# 重命名
for index, filename in enumerate(files, start=48):
    ext = filename.split('.')[-1]
    new_name = f"{index:04d}.{ext}"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)
    print(f"Renamed: {filename} → {new_name}")
