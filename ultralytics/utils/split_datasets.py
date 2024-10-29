import os
import shutil
import random
import argparse

def split_dataset(dataset_dir, output_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=None):
    """
    随机划分 YOLO 数据集为训练集、验证集和测试集。

    :param dataset_dir: YOLO 数据集所在目录，包含图片和标签文件。
    :param output_dir: 划分后数据集的输出目录。
    :param train_ratio: 训练集的比例。
    :param val_ratio: 验证集的比例。
    :param test_ratio: 测试集的比例，如果不传则自动计算剩余比例。
    """
    if test_ratio is None:
        test_ratio = 1 - train_ratio - val_ratio
    
    if train_ratio + val_ratio + test_ratio != 1:
        raise ValueError("训练集、验证集和测试集的比例总和必须为1")

    # 获取所有图片文件
    img_files = [f for f in os.listdir(dataset_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(img_files)  # 随机打乱

    total_files = len(img_files)
    train_count = int(total_files * train_ratio)
    val_count = int(total_files * val_ratio)

    train_files = img_files[:train_count]
    val_files = img_files[train_count:train_count + val_count]
    test_files = img_files[train_count + val_count:]

    # 创建输出目录
    for split in ['train', 'val', 'test']:
        img_split_dir = os.path.join(output_dir, split, 'images')
        lbl_split_dir = os.path.join(output_dir, split, 'labels')
        os.makedirs(img_split_dir, exist_ok=True)
        os.makedirs(lbl_split_dir, exist_ok=True)

    # 复制文件
    def copy_files(file_list, split):
        img_split_dir = os.path.join(output_dir, split, 'images')
        lbl_split_dir = os.path.join(output_dir, split, 'labels')
        
        for img_file in file_list:
            # 复制图片文件
            src_img_path = os.path.join(dataset_dir, img_file)
            dst_img_path = os.path.join(img_split_dir, img_file)
            shutil.copy(src_img_path, dst_img_path)

            # 复制对应的标签文件（假设标签文件和图片文件名相同，后缀为 .txt）
            label_file = img_file.rsplit('.', 1)[0] + '.txt'
            src_label_path = os.path.join(dataset_dir, label_file)
            dst_label_path = os.path.join(lbl_split_dir, label_file)

            # 确保标签文件存在再复制
            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dst_label_path)

    copy_files(train_files, 'train')
    copy_files(val_files, 'val')
    copy_files(test_files, 'test')

    print(f"数据集已划分完成：训练集 {len(train_files)} 张，验证集 {len(val_files)} 张，测试集 {len(test_files)} 张。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO 数据集划分脚本")
    parser.add_argument('--dataset_dir', type=str, required=True, help="原始 YOLO 数据集目录")
    parser.add_argument('--output_dir', type=str, required=True, help="划分后数据集的输出目录")
    parser.add_argument('--train_ratio', type=float, default=0.8, help="训练集比例")
    parser.add_argument('--val_ratio', type=float, default=0.1, help="验证集比例")
    
    args = parser.parse_args()

    split_dataset(args.dataset_dir, args.output_dir, args.train_ratio, args.val_ratio)
