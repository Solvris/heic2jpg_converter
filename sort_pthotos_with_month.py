import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_image_date(image_path):
    """
    获取照片的拍摄日期。
    优先使用 DateTimeOriginal，如果不存在则使用 ModifyDate。
    :param image_path: 照片的路径
    :return: 拍摄日期的字符串格式（YYYY-MM-DD），如果无法获取则返回 None
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                # 尝试获取 DateTimeOriginal
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == "DateTimeOriginal":
                        # 解析拍摄日期
                        date_str = value
                        return datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
                
                # 如果没有 DateTimeOriginal，则尝试获取 ModifyDate
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == "ModifyDate":
                        # 解析修改日期
                        date_str = value
                        return datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
    except Exception as e:
        print(f"无法读取 {image_path} 的 EXIF 数据: {e}")
    
    # 如果既没有 DateTimeOriginal 也没有 ModifyDate，则返回 None
    return None

def organize_photos(source_folder):
    """
    根据照片的拍摄日期整理照片。
    :param source_folder: 包含照片的源文件夹路径
    """
    if not os.path.exists(source_folder):
        print(f"错误：文件夹 {source_folder} 不存在！")
        return

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # 跳过非文件项
        if not os.path.isfile(file_path):
            continue

        # 获取照片的拍摄日期
        date_taken = get_image_date(file_path)
        if date_taken is None:
            print(f"警告：无法获取 {filename} 的拍摄日期，跳过该文件。")
            continue

        # 解析日期
        year, month, _ = date_taken.split("-")
        target_folder = os.path.join(source_folder, year, f"{year}_{month}")

        # 创建目标文件夹（如果不存在）
        os.makedirs(target_folder, exist_ok=True)

        # 移动文件
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)
        print(f"已将 {filename} 移动到 {target_folder}")

if __name__ == "__main__":
    # 用户输入源文件夹路径
    source_folder = input("请输入包含照片的文件夹路径：").strip()

    # 执行整理操作
    organize_photos(source_folder)
