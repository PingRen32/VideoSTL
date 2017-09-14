def locateface_cutimage(picfilepath):
    from imutils import face_utils
    import dlib
    import cv2
    
    # initialize dlib's face detector (HOG-based) and then create
    detector = dlib.get_frontal_face_detector()      
    # load the input image, resize it, and convert it to grayscale
    gray = cv2.imread(picfilepath)    
    # detect faces in the grayscale image
    rects = detector(gray, 1)
    
    for (i, rect) in enumerate(rects):
        if i >= 1:
            print ('Input video have more than one face.')
            break
        else:
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            gray = gray[x-w:x+2*w,y-h:y+2*h]
            cv2.imwrite(picfilepath, gray)

def locate_Tshape(shape):
    import numpy as np

    xy = np.zeros((1,2))
    #find left eye pupil location
    #achieve from point 37,40
    leftpupil = xy
    leftpupil[0][0] = 0.5*(shape[36][0]+shape[39][0])
    leftpupil[0][1] = 0.5*(shape[36][1]+shape[39][1])
    #find right eye pupil location
    #achieve from point 43,46
    rightpupil = xy
    rightpupil[0][0] = 0.5*(shape[42][0]+shape[42][0])
    rightpupil[0][1] = 0.5*(shape[45][0]+shape[45][0])
    #find nose location
    #achieve from point 34
    nose = xy
    nose[0][0] = shape[33][0]
    nose[0][1] = shape[33][1]
    
    #combine into matrix
    tshape = np.stack((leftpupil,rightpupil,nose))
    
    return tshape