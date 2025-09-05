# add_suffix.py

def add_jpg_suffix(input_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        with open(input_file, 'w') as file:
            for line in lines:
                # 去除行尾的换行符并添加.jpg后缀
                file.write('JPEGImages/'+line.strip() + '.jpg\n')
        
        print("后缀添加成功！")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    add_jpg_suffix('/home/jiangziben/data/people_and_face_detection/VOC/VOC2007/trainval.txt')
