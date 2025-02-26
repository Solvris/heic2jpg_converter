import os
from PIL import Image
import pyheif
from exiftool import ExifToolHelper

def heic_to_jpg(heic_path, output_dir=None, quality=95):
    if not os.path.isfile(heic_path):
        print(f"文件未找到: {heic_path}")
        return
    
    if output_dir is None:
        output_dir = os.path.dirname(heic_path)
    os.makedirs(output_dir, exist_ok=True)

    try:
        # 读取 HEIC 文件
        heif_file = pyheif.read(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # 构造输出路径
        base_name = os.path.splitext(os.path.basename(heic_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.jpg")
        
        # 提取并保存 EXIF 数据
        with ExifToolHelper() as et:
            metadata = et.get_metadata(heic_path)[0]
            tags_to_copy = {
                "Make": metadata.get("EXIF:Make", ""),
                "Model": metadata.get("EXIF:Model", ""),
                "DateTimeOriginal": metadata.get("EXIF:DateTimeOriginal", ""),
                "FNumber": metadata.get("EXIF:FNumber", ""),
                "ExposureTime": metadata.get("EXIF:ExposureTime", ""),
                "ISO": metadata.get("EXIF:ISO", ""),
                "FocalLengthIn35mmFormat": metadata.get("EXIF:FocalLengthIn35mmFormat", ""),
                "GPSLatitude": metadata.get("EXIF:GPSLatitude", ""),
                "GPSLongitude": metadata.get("EXIF:GPSLongitude", ""),
                "GPSLatitudeRef": metadata.get("EXIF:GPSLatitudeRef", ""),
                "GPSLongitudeRef": metadata.get("EXIF:GPSLongitudeRef", ""),
            }
            image.save(output_path, format="JPEG", quality=quality)
            et.set_tags(output_path, tags=tags_to_copy, params=["-overwrite_original"])
        print(f"转换完成: {output_path}")
    except Exception as e:
        print(f"无法加载或保存EXIF数据: {e}")
        image.save(output_path, format="JPEG", quality=quality)
        print(f"转换完成，但未嵌入EXIF数据: {output_path}")

def batch_convert_heic_to_jpg(input_dir, output_dir=None, quality=95):
    if not os.path.isdir(input_dir):
        raise NotADirectoryError(f"目录未找到: {input_dir}")
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".heic"):
                heic_path = os.path.join(root, file)
                if output_dir is None:
                    output_subdir = root
                else:
                    relative_path = os.path.relpath(root, input_dir)
                    output_subdir = os.path.join(output_dir, relative_path)
                heic_to_jpg(heic_path, output_subdir, quality)

if __name__ == "__main__":
    input_directory = input("请输入包含HEIC文件的目录路径: ").strip()
    output_directory = input("请输入输出目录路径（可选，直接回车则保存在原目录中）: ").strip() or None
    quality = int(input("请输入JPG保存质量（1-100，默认95）: ").strip() or 95)
    batch_convert_heic_to_jpg(input_directory, output_directory, quality)
