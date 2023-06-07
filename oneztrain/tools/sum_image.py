import os
import shutil

import os
import re
import datetime
import shutil

def sum_image(args):

    eachbill_path = args.eachbill_path
    output_dir= args.output_dir
    if os.path.exists(output_dir):
        new_out_dir = output_dir.replace('labelme_all_bill', 'labelme_all_bill' + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        os.rename(output_dir, new_out_dir)
        os.mkdir(output_dir)
    else:
        os.makedirs(output_dir)

    file_list = []
    r = "^([A-Za-z0-9_\-\.\(\)]+)(_v)[0-9]$"
    for img_name in os.listdir(eachbill_path):
        m = re.match(r, img_name)
        if m != None:
            file_list.append(img_name)
    print(file_list)


    for idx, files in enumerate(file_list):
        if os.path.exists(os.path.join(eachbill_path,files,'paddleLable_tagging_data')):
            files=os.path.join(files,'paddleLable_tagging_data')

        image_list = os.listdir(os.path.join(eachbill_path,files))
        for img_idx, image_name in enumerate(image_list):
            new_file_path = os.path.join(output_dir,image_name)
            abs_file_path = os.path.join(eachbill_path,files,image_name)
            shutil.copy(abs_file_path, new_file_path)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="args for train")
    parser.add_argument("--eachbill_path", type=str, required=False,default='/home/DiskA/zncsPython/table_det/labelme_each_bill/')
    parser.add_argument("--output_dir", type=str, required=False, default='/home/DiskA/zncsPython/table_det/labelme_all_bill/')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    sum_image(args)
