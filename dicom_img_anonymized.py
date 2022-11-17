#%%
import os
import pydicom
from deid.dicom.pixels import DicomCleaner
from PIL import Image, ImageDraw
import numpy as np

#%%
dir_path = 'C:/Users/smcljy/00_Works/221116_DICOM_image_Anonymized/UNHIDE/S 020'

filelist = []

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        filelist.append(file_path)

#%%
save_dir = "C:/Users/smcljy/00_Works/221116_DICOM_image_Anonymized/UNHIDE_ANM"

# file_info = filelist[0][61:66]+filelist[0][80:]

# file_info

#%%
def de_identifier_for_multi_clean_pixel(filename):
    try:
        Metadata = pydicom.filereader.dcmread(str(filename))
    except: return 'de_identifier // file reading error. '
    try:            
        # de-identify
        Metadata.StudyDate                       = ""
        Metadata.SeriesDate                      = ""
        Metadata.AcquisitionDate                 = ""
        Metadata.ContentDate                     = ""
        Metadata.AcquisitionDateTime             = ""
        Metadata.StudyTime                       = ""
        Metadata.SeriesTime                      = ""
        Metadata.AcquisitionTime                 = ""
        Metadata.ContentTime                     = ""
        # Metadata.ReferencedPerformedProcedureStepSequence[0]['ReferencedSOPInstanceUID'] = "1.2.410.200001.1.1185.839537548.4.20220714.1113845690.173.1"
        # Metadata.ReferencedSOPInstanceUID        = "1.2.410.200001.1.1185.839537548.4.20220700.1000000690.173.1"
        Metadata.ReferencedPerformedProcedureStepSequence = ""
        Metadata.StudyInstanceUID                = ""
        Metadata.SeriesInstanceUID               = ""
        Metadata.StudyID                         = ""
        Metadata.PerformedProcedureStepStartDate = ""
        Metadata.PerformedProcedureStepStartTime = ""
        Metadata.PerformedProcedureStepID        = ""
  
        Metadata.save_as(save_dir+file_info)
            # TODO - revive
            # sql_query(True)  
 
    except:            
 
            # TODO - revive
            # sql_query(False)  
            return 'de_identifier error'
        
    return save_dir+file_info

#%%
for file in filelist[:-1]:
    file_info = file[61:66]+file[80:]
    client = DicomCleaner(deid='dicom.ultrasound')
    client.detect(de_identifier_for_multi_clean_pixel(file))
    client.clean()
    client.save_dicom(output_folder="C:/Users/smcljy/00_Works/221116_DICOM_image_Anonymized/UNHIDE_ANM/S 020")

# report page convert to png
report_file = filelist[-1]
ds = pydicom.dcmread(report_file)
file_info = report_file[61:66]+report_file[80:]
save_path = save_dir+file_info

new_image = ds.pixel_array.astype(float)
scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0
scaled_image = np.uint8(scaled_image)
final_image = Image.fromarray(scaled_image)

box_color_RGBA  = (225,225,225,255)
fill_color_RGBA = (225,225,225,255)

draw = ImageDraw.Draw(final_image, 'RGBA') # RGBA
# bbox draw
# rectangle(point1_x, point1_y, point2_x, point2_y)
draw.rectangle((100,125,250,150), outline=box_color_RGBA, fill=fill_color_RGBA, width = 3) #fill
draw.rectangle((650,125,800,150), outline=box_color_RGBA, fill=fill_color_RGBA, width = 3) #fill
draw.rectangle((650,1120,830,1150), outline=(255,255,255,255), fill=(255,255,255,255), width = 3) #fill

# final_image.show()

final_image.save(save_path+'.png')

#%%
# final_image.save(save_path+'.png')