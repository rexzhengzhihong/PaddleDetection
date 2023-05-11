import os
import shutil



if __name__ == '__main__':
    folder_path = '/home/DiskA/zncsPython/table_det/labelme_each_bill/ckd_v1/'  # 文件夹路径
    new_folder_path = '/home/DiskA/zncsPython/table_det/labelme_each_bill/ckd_v1/new/'  # 文件夹路径
    if os.path.exists(new_folder_path):
        shutil.rmtree(new_folder_path)
    os.mkdir(new_folder_path)
    new_name_prefix = 'ckd_v1_'  # 新文件名前缀
    file_extension = '.png'  # 文件扩展名
    file_extension2 = '.jpg'  # 文件扩展名
    # 遍历文件夹中的文件
    for index, file_name in enumerate(os.listdir(folder_path)):
        # 如果文件扩展名为指定的扩展名
        new_file_name=''
        if file_name.endswith(file_extension):
            # 构造新文件名
            new_file_name = f'{new_name_prefix}{index + 1}{file_extension}'

        if file_name.endswith(file_extension2):
            new_file_name = f'{new_name_prefix}{index + 1}{file_extension2}'
        # 构造旧文件的完整路径和新文件的完整路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(new_folder_path, new_file_name)
        # 重命名文件
        shutil.move(old_file_path, new_file_path)