#%%
import os, glob, shutil
from PIL import Image
import time
from tqdm import tqdm

#%%
org_dir = "C:/Users/smcljy/00_Works/221116_DICOM_image_Anonymized/backup_data/MDX1/image"
save_dir = "C:/Users/smcljy/00_Works/221116_DICOM_image_Anonymized/backup_data_medison"
working_path = glob.glob(org_dir+'/**')

#%% remove report image
n = 1
for wrk_path in tqdm(working_path):
# for wrk_path in working_path[13:14]:
    working_path_deep = glob.glob(wrk_path+'/**')
    # os.mkdir(save_dir+wrk_path[-9:])
    # move_dir = save_dir+wrk_path[-9:]
    # remove data information
    if n < 10:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_00'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_00'+str(n)
    elif n < 100:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_0'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_0'+str(n)
    else:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_'+str(n)
        
    for path in working_path_deep:
        os.mkdir(move_dir+path[-9:])
        data_move_path = move_dir+path[-9:]
        
        # bmp file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.bmp' in f:
                    file_to_move = os.path.join(root, f)
                    # shutil.copy2 to copy with metadata
                    img = Image.open(file_to_move)
                    # report image exclusion
                    if img.size[0] > img.size[1]:
                        shutil.copy(file_to_move, data_move_path)
                    else:
                        pass

        # cne file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.cne' in f:
                    file_to_move = os.path.join(root, f)
                    shutil.copy(file_to_move, data_move_path)
        
        # qus file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.qus' in f:
                    file_to_move = os.path.join(root, f)
                    shutil.copy(file_to_move, data_move_path)
    n += 1
    
    time.sleep(0.1)
#%% contain report image
n = 1
for wrk_path in tqdm(working_path):
# for wrk_path in working_path[13:14]:
    working_path_deep = glob.glob(wrk_path+'/**')
    # os.mkdir(save_dir+wrk_path[-9:])
    # move_dir = save_dir+wrk_path[-9:]
    # remove data information
    if n < 10:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_00'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_00'+str(n)
    elif n < 100:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_0'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_0'+str(n)
    else:
        os.mkdir(save_dir+wrk_path[-9:-2]+'_'+str(n))
        move_dir = save_dir+wrk_path[-9:-2]+'_'+str(n)
        
    for path in tqdm(working_path_deep):
        os.mkdir(move_dir+path[-9:])
        data_move_path = move_dir+path[-9:]
        
        # bmp file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.bmp' in f:
                    file_to_move = os.path.join(root, f)
                    # shutil.copy2 to copy with metadata
                    shutil.copy(file_to_move, data_move_path)

        # cne file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.cne' in f:
                    file_to_move = os.path.join(root, f)
                    shutil.copy(file_to_move, data_move_path)
        
        # qus file copy
        for root, subdirs, files in os.walk(path):
            for f in files:
                if '.qus' in f:
                    file_to_move = os.path.join(root, f)
                    shutil.copy(file_to_move, data_move_path)

        time.sleep(0.1)
        
    n += 1
    
    time.sleep(0.1)