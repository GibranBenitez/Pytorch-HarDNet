import sys
import glob
import os
import pdb
import numpy as np
from PIL import Image

no_exp = ['082315_w_60', '082414_m_64', '082909_m_47', '083009_w_42', 
            '083013_w_47', '083109_m_60', '083114_w_55', '091914_m_46', 
            '092009_m_54', '092014_m_56', '092509_w_51', '092714_m_64', 
            '100514_w_51', '100914_m_39', '101114_w_37', '101209_w_61', 
            '101809_m_59', '101916_m_40', '111313_m_64', '120614_w_61']
frames = ['068', '082', '096', '110', '124', '138']
test_set = ['072414_m_23', '072609_w_23', '080609_w_27', '080714_m_23', 
            '081617_m_27', '091809_w_43', '101216_m_40']

intesities = ['BL1', 'PA4']
# intesities = ['PA1', 'PA4']
# intesities = ['BL1', 'PA3', 'PA4']
# intesities = ['BL1', 'PA1', 'PA2', 'PA3', 'PA4']

dataset_folder = "/export/space0/gibran/dataset/BioVid/PartA/crops/"

out_path = "/export/space0/gibran/dataset/BioVid/Class/ME67/CA2/"
# out_path = "/export/space0/gibran/dataset/BioVid/Class/ME67/CA2_1/"
# out_path = "/export/space0/gibran/dataset/BioVid/Class/ME67/CA3/"
# out_path = "/export/space0/gibran/dataset/BioVid/Class/ME67/CA5/"

for clss in intesities:
    cls_path = os.path.join(out_path, 'train', clss)
    if not os.path.isdir(cls_path):
        os.makedirs(cls_path)
    cls_path = os.path.join(out_path, 'test', clss)
    if not os.path.isdir(cls_path):
        os.makedirs(cls_path)

main_folder_list = os.listdir(dataset_folder)
main_folder_list.sort()

for i, main_folder in enumerate(main_folder_list):
    # if i < 45:
    #     continue
    if main_folder in no_exp:
        # print('Not expressive person')
        continue
    print('{}:'.format(main_folder))
    main_folder_path = os.path.join(dataset_folder, main_folder)
    folder_list = os.listdir(main_folder_path)
    folder_list.sort()

    for folder in folder_list:
        parts = folder.split("-")
        if parts[1] not in intesities:
            # print('Not in the intensity list')
            continue
        if parts[0] in test_set:
            sets = 'test'
        else:
            sets = 'train'
        print('   {} goes to {}:'.format(folder, sets))
        folder_path = os.path.join(main_folder_path, folder)

        for id_frame in frames:
            img_name = '{}_0{}.jpg'.format(folder, id_frame)
            img_or = os.path.join(folder_path, img_name)
            os.symlink(img_or, os.path.join(out_path, sets, parts[1]))
            # img = Image.open(img_or).convert('RGB')
            # img = img.resize((512,512), Image.BILINEAR)
            # img.save(os.path.join(out_path, img_name))
            # print('      {}'.format(img_name))