import os
import shutil

import os
import re
import datetime
import shutil

def sum_image(args):

    git_img_path = args.git_img_path
    output_dir= args.output_dir
    if os.path.exists(output_dir):
        new_out_dir = output_dir.replace('labelme_all_bill', 'labelme_all_bill' + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        os.rename(output_dir, new_out_dir)
        os.mkdir(output_dir)
    else:
        os.makedirs(output_dir)

    copy_folder_contents(git_img_path,output_dir)

def copy_folder_contents(source_folder, destination_folder):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # 遍历源文件夹中的所有文件
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            # 复制文件
            shutil.copy2(source_path, destination_path)
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="args for train")
    parser.add_argument("--git_img_path", type=str, required=False,default='/home/DiskA/bill_capacity/外部单据/allbill_v1/tabledet/paddleLable_tagging_data/')
    parser.add_argument("--output_dir", type=str, required=False, default='/home/DiskA/zncsPython/table_det/labelme_all_bill/')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    sum_image(args)
