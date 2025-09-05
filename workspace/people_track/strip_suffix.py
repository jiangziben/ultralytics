def strip_suffix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    stripped_lines = [line.strip().rsplit('.', 1)[0] for line in lines]
    
    with open(file_path, 'w') as file:
        for line in stripped_lines:
            file.write(line + '\n')

# 调用函数，传入txt文件路径
strip_suffix('/home/jiangziben/data/people_and_face_detection/VOC/VOC2007/trainval.txt')