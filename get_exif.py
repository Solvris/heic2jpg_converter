import os
from exiftool import ExifToolHelper

def extract_exif(file_path):
    """
    提取单个文件的所有EXIF信息并打印。
    
    :param file_path: 文件路径
    """
    if not os.path.isfile(file_path):
        print(f"文件未找到: {file_path}")
        return

    try:
        with ExifToolHelper() as et:
            # 提取文件的完整EXIF信息
            metadata = et.get_metadata(file_path)
            
            # 打印所有EXIF字段及其值
            print(f"=== {file_path} 的完整EXIF信息 ===")
            for key, value in metadata[0].items():
                print(f"{key}: {value}")
            print("\n")
    except Exception as e:
        print(f"无法读取EXIF数据: {e}")

if __name__ == "__main__":
    # 示例用法
    file_path = input("请输入单张照片的文件路径: ").strip()
    
    # 检查文件是否存在
    if os.path.isfile(file_path):
        extract_exif(file_path)
    else:
        print("无效的文件路径，请输入有效的文件路径。")
