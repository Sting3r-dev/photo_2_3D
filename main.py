import cv2

def ORB(img_color):
    img = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)
    orb = cv2.ORB_create()
    keypoints = orb.detect(img,None)
    keypoints, des = orb.compute(img, keypoints)
    return keypoints

def SIFT(img_color):
    img = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)
    sift = cv2.SIFT_create()
    keypoints, des = sift.detectAndCompute(img,None)
    return keypoints

def define_keypoints(input_img,algorythm_name):
    img = img
    if algorythm_name == "Orb":
        ORB(input_img)
    elif algorythm_name == "Sift":
        SIFT(input_img)
    else:
        return('Err')

if __name__ == "__main__":
    image='/workspaces/photo_2_3D/demo/IMG_20230331_063114.jpg'
    print(define_keypoints(image,'Orb'))


    