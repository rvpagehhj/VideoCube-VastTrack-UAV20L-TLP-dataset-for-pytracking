import os
import shutil
import zipfile
from pathlib import Path


def organize_txt_files(base_path):
    """
    组织指定目录下的txt文件：
    1. 给每个txt文件添加OSTrack_前缀
    2. 将末尾是_time的文件放入time文件夹
    3. 其余文件放入result文件夹
    4. 删除time文件夹中文件名末尾的_time
    5. 将两个文件夹打包成压缩包
    """
    # 确保基础路径存在
    base_dir = Path(base_path)
    if not base_dir.exists():
        print(f"路径 {base_path} 不存在")
        return

    # 创建目标文件夹
    time_dir = base_dir / "time"
    result_dir = base_dir / "result"
    time_dir.mkdir(exist_ok=True)
    result_dir.mkdir(exist_ok=True)

    # 遍历所有txt文件
    for txt_file in base_dir.glob("*.txt"):
        # 添加OSTrack_前缀
        new_name = "IGRSMAT_" + txt_file.name
        new_path = txt_file.parent / new_name
        txt_file.rename(new_path)

        # 根据文件名特征分类
        if new_name.endswith("_time.txt"):
            # 移动到time文件夹并去除_time后缀
            final_name = new_name.replace("_time.txt", ".txt")
            target_path = time_dir / final_name
            shutil.move(str(new_path), str(target_path))
        else:
            # 移动到result文件夹
            target_path = result_dir / new_name
            shutil.move(str(new_path), str(target_path))

    # 创建压缩包
    zip_path = base_dir / "results.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        # 添加time文件夹及其内容
        for file_path in time_dir.rglob("*"):
            if file_path.is_file():
                arc_path = file_path.relative_to(base_dir)
                zipf.write(file_path, arc_path)

        # 添加result文件夹及其内容
        for file_path in result_dir.rglob("*"):
            if file_path.is_file():
                arc_path = file_path.relative_to(base_dir)
                zipf.write(file_path, arc_path)

    print(f"处理完成，压缩包已创建: {zip_path}")


# 使用示例
if __name__ == "__main__":
    # 指定文件夹路径
    folder_path = "/home/sys123/yh/SMAT-main/output/test/tracking_results/mobilevitv2_track/mobilevitv2_256_128x1_ep300"  # 可以替换为实际路径
    organize_txt_files(folder_path)
