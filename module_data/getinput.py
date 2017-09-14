def get_video_directory_from_user():
    import os

    vidpath = input('Input video file path:')
    vidpath = str(vidpath)
    
    while os.path.isfile(vidpath)==False:
        print('%r is not a directory. Try again.' % vidpath)
        vidpath = input('Input video directory for faciallandmarks:')
        vidpath = str(vidpath)
        return vidpath
    else:
        return vidpath

def meshnumber_input():
    print('\n Enter desired mesh number for 3D mesheing:')
    print('\n Note that the higher mesh number is, the longer time needed for result to complete.')
    mesh = input('\n Enter int (1-100)')
    mesh = int(mesh)
    while 1 <= mesh <= 100:
        return mesh
    else:
        mesh = input('\n Input out of range, try again:') 
        mesh = int(mesh)
    

def get_file_directory_from_user():
    import os

    filepath = input('Input a directory path for file storage:')
    filepath = str(filepath)
    while os.path.isdir(filepath)==False:
        print('%r is not a directory. Try again.' % filepath)
        filepath = input('Input a directory path for file storage:')
        filepath = str(filepath)
    else:
        return filepath

def video_to_image_input(vidpath,filepath): 
    import cv2
    import os
    import sys

    try:
        vidcap = cv2.VideoCapture(vidpath)
    except:
        print ("Problem opening video")
        sys.exit(1)

    count = 0     
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(filepath, 'video_%d.png') % count, image)
            count += 1
        else:
            break
            return count
        cv2.destroyAllWindows()
        vidcap.release()
        
def pic_size(path):
    import numpy as np
    import cv2
    
    #return the size of picture
    image = cv2.imread(path)
    height = np.size(image, 0)
    width = np.size(image, 1)
    
    return(height,width)
        
def graystyle(picpath):
    #turn BGR pic into graystyle for faster processing
    import cv2
    import os
    
    image = cv2.imread(picpath)
    cvt_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(picpath, cvt_image)
        
def video_backgroud_subtractor(vidpath,filepath,framenumber):
    import cv2
    import os
    
    pic = cv2.VideoCapture(vidpath)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    for x in range (0,framenumber):
        frame = pic.read()
        fgmask = fgbg.apply(frame)
        backgroudremovedpic = cv2.bitwise_and(pic, pic, mask = fgmask)
        backgroudremovedpic = cv2.cvtColor(backgroudremovedpic,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(filepath, 'backgroudremoved_gray_%d.png') % x, backgroudremovedpic)     
