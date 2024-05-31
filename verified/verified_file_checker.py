import os 
path_oi = "./training/datasets/v2"
path_checker = "./training/datasets/v2/train" # path of train
path_checker = "./training/datasets/v2/test" # path of train
path_checker = "./training/datasets/v2/valid" # path of train

image_path = os.path.join(path_checker,"images")
label_path = os.path.join(path_checker,"labels")

img_path_list = sorted(os.listdir(image_path))
label_path_list = sorted(os.listdir(label_path))

def name_split_checker(img_path_,label_path_):
    name_img = img_path_[:-4]
    name_lab = label_path_[:-4]
    return name_img==name_lab

total_img = len(img_path_list)
total_lab = len(label_path_list)
print("total file in images folder: ",total_img)
print("total file in labels folder: ",total_lab)

count = 0
for i in range(total_img):
    if name_split_checker(img_path_list[i],label_path_list[i]):
        count+=1

print("number that have the same name : ",count)

