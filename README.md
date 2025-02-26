---
# heic2jpg_converter
# **HEIC to JPG 转换工具**
一个用于将 HEIC 文件批量转换为 JPG 格式的 Python 工具，支持保留完整的 EXIF 信息（如设备型号、拍摄参数、地理位置等）。适用于小米和 iPhone 拍摄的 HEIC 文件。

---

## **功能特点**

- **批量处理**：支持递归遍历目录中的所有 HEIC 文件。
- **保留 EXIF 数据**：
  - 设备信息（品牌、型号）。
  - 拍摄时间、光圈、快门速度、ISO、焦距等拍摄参数。
  - 地理位置信息（纬度、经度、方向等）。
  - iPhone 特有字段（如镜头型号、GPS 方向）。
- **高质量输出**：支持自定义 JPG 文件的质量（默认质量为 95）。

---

## **安装与依赖**

### **1. 安装依赖工具**
在运行脚本之前，请确保已安装以下工具和库：

#### **(1) 安装 `exiftool`**
`exiftool` 是一个强大的工具，用于提取和写入 EXIF 数据。
```bash
sudo apt install libimage-exiftool-perl  # Ubuntu/Debian
brew install exiftool                   # macOS
```

#### **(2) 安装 Python 库**
使用 `pip` 安装所需的 Python 库：
```bash
pip3 install pillow pyheif pyexiftool
```

> **注意**：如果在安装 `pyheif` 时遇到问题，请参考 [pyheif 官方文档](https://pypi.org/project/pyheif/) 或安装系统依赖项（如 `libheif`）。

---

## **使用方法**

### **1. 克隆项目**
将项目克隆到本地：
```bash
git clone https://github.com/venus-25/heic2jpg_converter.git
cd heic2jpg_converter
```

### **2. 运行脚本**
运行以下命令启动批量转换工具：
```bash
python3 heic2jpg_for_xiaomi.py
```

脚本会提示输入以下内容：
- **输入目录路径**：包含 HEIC 文件的目录。
- **输出目录路径**（可选）：转换后的 JPG 文件保存路径。如果不指定，则保存在原目录中。
- **JPG 质量**（可选，默认值为 95）：设置输出 JPG 文件的质量（1-100）。

示例运行：
```plaintext
请输入包含HEIC文件的目录路径: /path/to/heic/files
请输入输出目录路径（可选，直接回车则保存在原目录中）: /path/to/output
请输入JPG保存质量（1-100，默认95）: 90
转换完成: /path/to/output/IMG_0001.jpg
转换完成: /path/to/output/IMG_0002.jpg
...
```

---

## **脚本说明**

### **1. 小米 HEIC 文件**
- 提取并保留以下关键字段：
  - 设备信息：`EXIF:Make`、`EXIF:Model`
  - 拍摄时间：`EXIF:DateTimeOriginal`
  - 拍摄参数：`EXIF:FNumber`、`EXIF:ExposureTime`、`EXIF:ISO`、`EXIF:FocalLengthIn35mmFormat`
  - 地理位置：`EXIF:GPSLatitude`、`EXIF:GPSLongitude`、`EXIF:GPSLatitudeRef`、`EXIF:GPSLongitudeRef`

### **2. iPhone HEIC 文件**
- 提取并保留以下关键字段：
  - 设备信息：`EXIF:Make`、`EXIF:Model`
  - 拍摄时间：`EXIF:DateTimeOriginal`
  - 拍摄参数：`EXIF:FNumber`、`EXIF:ExposureTime`、`EXIF:ISO`、`EXIF:FocalLengthIn35mmFormat`
  - 地理位置：`EXIF:GPSLatitude`、`EXIF:GPSLongitude`、`EXIF:GPSImgDirection`
  - 镜头信息：`EXIF:LensMake`、`EXIF:LensModel`

---

## **注意事项**

1. **文件格式支持**：
   - 仅支持 `.heic` 和 `.HEIC` 文件（忽略大小写）。
   - 如果需要支持其他格式（如 `.hif`），请修改脚本中的文件过滤逻辑。

2. **EXIF 字段缺失**：
   - 如果某些字段在原始 HEIC 文件中不存在，脚本会跳过这些字段并继续运行。
   - 确保原始 HEIC 文件包含完整的 EXIF 数据，以获得最佳效果。

3. **性能优化**：
   - 对于大量 HEIC 文件，建议在高性能机器上运行脚本，或分批处理文件。

4. **兼容性**：
   - 脚本已在 Ubuntu 24.04.2 tls 上测试通过。MacOS和其他linux请自性测试，目前pyheif库不支持Windows平台，可能无法使用 。

---

## **贡献指南**

欢迎提交 Issue 或 Pull Request！如果你发现任何问题或希望添加新功能，请按照以下步骤操作：
1. Fork 本仓库。
2. 创建一个新的分支 (`git checkout -b feature/YourFeatureName`)。
3. 提交更改 (`git commit -m "Add your changes"`)。
4. 推送分支 (`git push origin feature/YourFeatureName`)。
5. 提交 Pull Request。

---

## **许可证**

本项目采用 BSD 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

---

## **作者**

- **邮箱**: [imydfy@gmail.com]

---

## **致谢**

- 感谢 [ExifTool](https://exiftool.org/) 提供强大的 EXIF 数据处理能力。
- 感谢 [pyheif](https://pypi.org/project/pyheif/) 和 [Pillow](https://python-pillow.org/) 提供的图像处理支持。

---
