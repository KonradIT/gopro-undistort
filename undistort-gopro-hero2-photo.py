import  sys
import  cv
import  numpy as np
 
if  __name__ ==  '__main__' :
 
    img =  cv.LoadImageM( 'gopro0467-small.jpeg'  )
 
    width =  img.width
    height =  img.height
 
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
 
 
    map1 =  cv.CreateImage ((width, height), cv.IPL_DEPTH_32F, 1 )
    map2 =  cv.CreateImage ((width, height), cv.IPL_DEPTH_32F, 1 )
    cv.InitUndistortMap (camera_matrix, dist_coeffs, map1, map2)
 
    
    undistimage =  cv.CloneMat (img)
    cv.Remap (img, undistimage, map1, map2)

    cv.NamedWindow("Source", 1)
    cv.ShowImage("Source", img)

    cv.NamedWindow("Undistorted", 1)
    cv.ShowImage("Undistorted", undistimage)

    cv.WaitKey(0)