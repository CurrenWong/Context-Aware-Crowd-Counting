import json
from os.path import join
import glob
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # path to folder that contains images
    img_folder = '../ShanghaiTech_Crowd_Counting_Dataset/part_B_final/train_data/images'

    # path to the final json file
    output_json = 'img.json'
    # path to train json file
    train_json = 'train.json'
    # path to validate json file
    val_json = 'val.json'

    img_list = []

    for img_path in glob.glob(join(img_folder,'*.jpg')):
        img_list.append(img_path)

   
    img_train, img_val = train_test_split(img_list, test_size = 0.33, random_state = 0)

    for path_json, content in dict({output_json: img_list, train_json: img_train, val_json: img_val}).items():
        with open(path_json,'w') as f:
            json.dump(content,f)
