import numpy as np
import cv2
import pydicom as dicom
from skimage import exposure



ds=dicom.dcmread('040c69444ceb71b8a9f714090f1175db.dicom/040c69444ceb71b8a9f714090f1175db.dicom')
dcm_sample=ds.pixel_array
dcm_sample=exposure.equalize_adapthist(dcm_sample)




cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Resized Window', 1920, 1080)
cv2.imshow('Resized Window',dcm_sample)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
