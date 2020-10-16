import matplotlib.image as mpimg

# Read in Alex pic
alexpic = np.array(mpimg.imread('Alex.jpg'))

# Top of hat
alexpic[400:770,425:575,0]=127
alexpic[400:770,425:575,1]=0
alexpic[400:770,425:575,2]=255

# Base of hat
alexpic[690:770,325:675,0]=127
alexpic[690:770,325:675,1]=0
alexpic[690:770,325:675,2]=255

# Ring
alexpic[610:680,425:575,0]=255
alexpic[610:680,425:575,1]=255
alexpic[610:680,425:575,2]=0

plt.imshow(alexpic)

plt.imsave('AlexHat.jpg', alexpic)