import cv2, os, pathlib, numpy as np

path = pathlib.Path(__file__).parent.absolute()

finalimg = 4
copy = None

for file in os.listdir(f'{path}/frames'):

    src = cv2.imread(f'{path}/frames/{file}')
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    _,alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    clean = cv2.merge(rgba,4)

    if type(finalimg) == type(4): finalimg = clean
    else: finalimg = np.concatenate((finalimg, clean), axis=1)
    copy = clean
    # cv2.imshow('a', finalimg)
    # cv2.waitKey()
finalimg = np.concatenate((finalimg, copy), axis=1)
finalimg = np.concatenate((finalimg, copy), axis=1)
cv2.imwrite(f"{path}/final.png", finalimg)

