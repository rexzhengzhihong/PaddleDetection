import os
import subprocess
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="args for train")
    parser.add_argument("--type", type=str, required=False,default='bill')
    args = parser.parse_args()
    return args
def test(args):
    model_dir = '/home/DiskA/zncsPython/table_det/model/interence/picodet_lcnet_x1_0_layout_table/'
    if(args.type=='bill'):
        model_dir = '/home/DiskA/zncsPython/bill_det/model/interence/picodet_lcnet_x1_0_layout_table/'
    image_dir="/home/DiskA/zncsPython/bill_det/test/"
    output_dir=image_dir+"/result/"
    str_train_table = ('python deploy/python/infer.py  \
                   --model_dir=' + model_dir+' \
                   --image_dir=' + image_dir+' \
                   --output_dir=' + output_dir+' \
                   --device=GPU ')
    os.chdir('/home/DiskA/PycharmProjects/PaddleDetection/')
    result1 = os.system(str_train_table)

if __name__ == '__main__':
    args = parse_args()
    test(args)