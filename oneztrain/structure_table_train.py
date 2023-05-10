import random
import os
import subprocess
import datetime
def main(args):
    if "train"==args.type:
        # 数据准备
        tructure_table_data_splite(args)
        structure_table_train(args)
        export_table_inference(args)
        print( '***************************************************    structure_table train success!     ******************************************************')


def tructure_table_data_splite(args):

    os.chdir('/home/DiskA/PycharmProjects/PaddleDetection/')
    data_dir="/home/DiskA/zncsPython/table_det"
    output_dir=data_dir+"/coco_data/"
    if os.path.exists(output_dir):
        new_out_dir=output_dir.replace('coco_data','coco_data'+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        os.rename(output_dir,new_out_dir)
        os.mkdir(output_dir)
    str_train_table = ('python tools/x2coco.py \
            --dataset_type labelme \
            --json_input_dir '+data_dir+'/labelme_json/ \
            --image_input_dir '+data_dir+'/labelme/ \
            --output_dir '+output_dir+' \
            --train_proportion 0.8 \
            --val_proportion 0.2 \
            --test_proportion 0.0')
    result1 = os.system(str_train_table)
    print(str_train_table)
    print(result1)
def structure_table_train(args):
    os.chdir('/home/DiskA/PycharmProjects/PaddleDetection/')
    yml_dir='configs/picodet/legacy_model/application/layout_analysis/picodet_lcnet_x1_0_layout_table.yml'
    str_train_table = ('python tools/train.py \
            -c '+yml_dir+' \
            --eval ')
    result1 = os.system(str_train_table)
    print(result1)

def export_table_inference(args):
    os.chdir('/home/DiskA/PycharmProjects/PaddleDetection/')
    yml_dir = 'configs/picodet/legacy_model/application/layout_analysis/picodet_lcnet_x1_0_layout_table.yml'
    weights_dir='/home/DiskA/zncsPython/table_det/model/output/picodet_lcnet_x1_0_layout_table/best_model.pdparams'
    output_dir='/home/DiskA/zncsPython/table_det/model/interence/'
    str_train_table = ('python tools/export_model.py \
               -c ' + yml_dir + ' \
               -o weights=' + weights_dir + ' \
               export.nms=False \
               export.benchmark=True \
               --output_dir=' + output_dir)
    result1 = os.system(str_train_table)
    print(result1)

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="args for train")
    parser.add_argument("--type", type=str, required=False,default='train')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    main(args)
