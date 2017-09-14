import os 
from module_data import faciallandmarks
from module_data import getinput
from module_data import locating
import numpy as np

vidpath = input.get_video_directory_from_user()
# get a folder path for all picture storage
filepath = input.get_file_directory_from_user()
# acquire total frame numbers for looping
framenumber = input.video_to_image_input(vidpath, filepath)
framenumber = int(framenumber)
# generate a playground for meshing
meshnumber = input.meshnumber_input()

# Background remove
getinput.video_backgroud_subtractor(vidpath, filepath, framenumber)

tshape_dataset = np.zeros((framenumber,3,2))

# send all frame picture files through process
for x in range(0,framenumber):
    original_picfilepath = str(os.path.join(filepath, 'video_%d.png') % x)
    #Picture Process
    #turn pictures into graystyle
    input.graystyle(filepath,x) 
    
    #generate file path for graystyle pic
    gray_picfilepath = str(os.path.join(filepath, 'gray_%d.png') % x)
    
    #retrive landmark data as np matrix (68,2)
    shape = faciallandmarks.facial_point(gray_picfilepath)
      
    #for reference
    #("mouth", (48, 68)),
    #("right_eyebrow", (17, 22)),
    #("left_eyebrow", (22, 27)),
    #("right_eye", (36, 42)),
    #("left_eye", (42, 48)),
    #("nose", (27, 35)),
    #("jaw", (0, 17))
    
    #T shape locating two pupils and nose tip as a 'T' shape locator
    # leftpupil,rightpupil,nose in ((3,2)) matrix
    tshape = locating.locate_Tshape(shape)
    for a in range(0,2):
        for b in range(0,1):
            tshape_dataset[x][a][b] = tshape[a][b] 
    
# Find maxuimum scales
pupildist_eyenosedist = np.zeros((framenumber,2))

    # Cut image arround face to reduce calculation 
    
    # mark the filepath for background removed gray pic file for mesh generation
    backgroundremoved_gray_picfilepath = str(os.path.join(filepath, 'backgroudremoved_gray_%d.png') % x)
    
    #reduce image size to speed up locating facial landmarks
    #act on background removed pic
    locating.locateface_cutimage(filepath)  
