
import sys
import os, errno
import cv
import numpy as np

def setupCV() :
    # Camera data for GoPro Hero2
    camera_matrix =  cv.CreateMat ( 3 , 3 , cv.CV_32FC1)
    cv.SetReal2D (camera_matrix, 0 , 0 , 767.4898 )
    cv.SetReal2D (camera_matrix, 0 , 1 , 0.0 )
    cv.SetReal2D (camera_matrix, 0 , 2 , 1296.0 )
    cv.SetReal2D (camera_matrix, 1 , 0 , 0.0 )
    cv.SetReal2D (camera_matrix, 1 , 1 , 762.59 )
    cv.SetReal2D (camera_matrix, 1 , 2 , 972.0 )
    cv.SetReal2D (camera_matrix, 2 , 0 , 0.0 )
    cv.SetReal2D (camera_matrix, 2 , 1 , 0.0 )
    cv.SetReal2D (camera_matrix, 2 , 2 , 1.0 )
 
    dist_coeffs =  cv.CreateMat ( 1 , 5 , cv.CV_32FC1)
    cv.SetReal2D (dist_coeffs, 0 , 0 , - 0.10541202873 )
    cv.SetReal2D (dist_coeffs, 0 , 1 , 0.0128245307133 )
    cv.SetReal2D (dist_coeffs, 0 , 2 , - 0.00171211222187 )
    cv.SetReal2D (dist_coeffs, 0 , 3 , 0.00142017123289 )
    cv.SetReal2D (dist_coeffs, 0 , 4 , - 0.000823813956231 )

    return [camera_matrix,dist_coeffs]

def undistort(srcImage, destImage, camera_matrix, dist_coeffs) :
    img =  cv.LoadImageM( srcImage )
 
    width =  img.width
    height =  img.height

    map1 =  cv.CreateImage ((width, height), cv.IPL_DEPTH_32F, 1 )
    map2 =  cv.CreateImage ((width, height), cv.IPL_DEPTH_32F, 1 )
    cv.InitUndistortMap (camera_matrix, dist_coeffs, map1, map2)
 
    undistImage =  cv.CloneMat (img)
    cv.Remap (img, undistImage, map1, map2)
    cv.SaveImage(destImage, undistImage)
    print "\tSaved to: ", destImage

def getOutputFileName(fileName):
    pre = 'undist-'
    ext = 'jpg'
    outputFileName = pre + fileName + '.' + ext
    return outputFileName

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise
 
if  __name__ ==  '__main__' :
    camera_matrix, dist_coeffs = setupCV()
    directory = sys.argv[1]
    mkdir_p(directory + 'undistorted')
    
    for somefile in os.listdir(directory):
        fileName, fileExtension = os.path.splitext(somefile)
        fileExtension = fileExtension[1:].strip()
        if (fileExtension in ['jpg', 'jpeg', 'JPG']):
            print "Converting: " + somefile
            destImage = getOutputFileName(fileName)
            undistort(directory + somefile, directory + 'undistorted/' + destImage, camera_matrix, dist_coeffs)

