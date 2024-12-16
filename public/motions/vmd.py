import os
import json

# 指定文件夹路径
directory_path = '.'  # 请替换为你的文件夹路径

# 存储结果的列表
vmd_files = {}

# 遍历指定文件夹及其子文件夹
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.vmd'):
            # 获取文件名，不包含扩展名
            name = os.path.splitext(file)[0]
            # 获取文件的相对路径并转换为双反斜杠
            file_path = os.path.join(root, file)
            # 将文件信息添加到列表
            vmd_files[name]=file_path
            

# 输出结果为 JSON 格式
# print(json.dumps(vmd_files, indent=2,ensure_ascii=False))

# 保存到vmd_mapper.js文件
with open('../../src/store/vmdMapper.ts', 'w',encoding='utf-8') as f:
    # 写入文件
    f.write('export const AnimationsMapping = ')
    json.dump(vmd_files, f, indent=2,ensure_ascii=False)
    f.write(';\nexport const AnimationsList = ')
    json.dump(list(vmd_files.keys()), f, indent=2,ensure_ascii=False)
