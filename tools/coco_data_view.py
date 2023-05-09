import json
if __name__ == '__main__':

    json_dir='/home/DiskA/zncsPython/table_det/coco_data/annotations/'
    coco_anno = json.load(open(json_dir+'instance_train.json'))

    # coco_anno.keys
    print('\nkeys:', coco_anno.keys())

    print('\n物体类别:', coco_anno['categories'])

    print('\n多少张图', len(coco_anno['images']))

    print('\n标注物体数量', len(coco_anno['annotations']))

    print('\n一条', coco_anno['annotations'][0])