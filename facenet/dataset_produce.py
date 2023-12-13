from models.inception_resnet_v1 import InceptionResnetV1
import os
import os.path as osp
from models.mtcnn import MTCNN
from PIL import Image
import torch
import numpy as np
from torchvision.transforms import functional as F
## ----------------------------------------------------------------------------
# # rename folder
# import os
# path=os.path.join('data','images')
# start_count=0
# for f in os.listdir(path):
#     os.rename(os.path.join(path,f),os.path.join(path,str(start_count)))
#     start_count+=1
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
# #rename pic
# import os

# path=os.path.join('data','images')
# os.chdir(path)

# for folder in os.listdir(os.getcwd()):
#     count = 0 
#     for pic in os.listdir(folder):
#         os.rename(os.path.join(folder,pic),os.path.join(folder,f"{folder}_{count}.jpg"))
#         count+=1
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
# # produce dataset head
# import cv2
# path=os.path.join('data')
# os.chdir(path)

# weaken=np.array([int(0.4*i) for i in range(256)]).astype('uint8')
# equal=np.array([i for i in range(256)]).astype('uint8')
# lutsweaken=np.dstack((equal,weaken,equal))

# def wsatu(img):
#     hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     hsv=cv2.LUT(hsv,lutsweaken)
#     return cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

# for i in range(20):
#     os.mkdir(osp.join('dataset',str(i)))
#     a=os.listdir(osp.join('images',str(i)))
#     for pic in os.listdir(osp.join('images',str(i))):
#         n=(pic.split('_')[1]).split('.')[0]
        
#         img = cv2.imread(os.path.join('images',str(i),pic))
#         flip = cv2.flip(img,1)
#         oriws=wsatu(img)
#         flipws=wsatu(flip)
        
#         cv2.imwrite(osp.join('dataset',str(i),f"{i}_{n}.jpg"),img)
#         cv2.imwrite(osp.join('dataset',str(i),f"{i}_{25*1+int(n)}.jpg"),flip)
#         cv2.imwrite(osp.join('dataset',str(i),f"{i}_{25*2+int(n)}.jpg"),oriws)
#         cv2.imwrite(osp.join('dataset',str(i),f"{i}_{25*3+int(n)}.jpg"),flipws)
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
# # produce dataset tail

# a function to random select a number of item in a list
# import shutil
# os.chdir('data')
# for i in range(20,80):
#     os.mkdir(osp.join('dataset',str(i)))
#     choosed_list=np.random.choice(os.listdir(osp.join('images',str(i))),np.random.choice([3,4,5],1,replace=False)[0],replace=False)

#     # copy pic form one folder to another
#     for pic in choosed_list:
#         shutil.copy(os.path.join('images',str(i),pic),osp.join('dataset',str(i),pic))
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
# # produce .npy
# model = InceptionResnetV1(pretrained='vggface2',classify=False).eval()
# mtcnn=MTCNN(image_size=150)

# path=os.path.join('data','dataset')
# os.chdir(path)

# feat=None
# label=np.array([]).astype(np.int64)
# for i in range(80):
#     for pic in os.listdir(str(i)):
#         img = Image.open(os.path.join(str(i),pic))

#         # # Get cropped and prewhitened image tensor
#         img_cropped = mtcnn(img)

#         if img_cropped is None:
#             img_cropped = img.resize((150,150))
#             img_cropped = F.to_tensor(np.float32(img_cropped))
#             img_cropped = (img_cropped-127.5)/128.0

#         v=model(img_cropped.unsqueeze(0))
#         if feat is not None:
#             feat=np.concatenate((feat,v.detach().numpy()),axis=0)
#         else:
#             feat=v.detach().numpy()

#         label=np.append(label,int(i))

# np.save('feat.npy',feat)
# np.save('label.npy',label)
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
a=np.load('data/dataset/label.npy')
print()