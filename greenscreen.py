from PIL import Image
im1 = Image.open('maxresdefault.jpg')
pixTOCUT = im1.load()
im2 = Image.open('BuFu0Pz.jpg')
pixTOADD = im2.load()

img = Image.new( im1.mode, im1.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        col=pixTOCUT[i,j]
        r=col[0]
        g=col[1]
        b=col[2]
        if not(i==0 or i==img.size[0]-1 or j==0 or j==img.size[1]-1):
            dir1=pixTOCUT[i-1,j][1]>pixTOCUT[i-1,j][0] and pixTOCUT[i-1,j][1]>pixTOCUT[i-1,j][2]
            dir2=pixTOCUT[i+1,j][1]>pixTOCUT[i+1,j][0] and pixTOCUT[i+1,j][1]>pixTOCUT[i+1,j][2]
            dir3=pixTOCUT[i,j-1][1]>pixTOCUT[i,j-1][0] and pixTOCUT[i,j-1][1]>pixTOCUT[i,j-1][2]
            dir4=pixTOCUT[i,j+1][1]>pixTOCUT[i,j+1][0] and pixTOCUT[i,j+1][1]>pixTOCUT[i,j+1][2]
            neighbor=int(dir1)+int(dir2)+int(dir3)+int(dir3)
        
        if g>r and g>b and ((i==0 or i==img.size[0] or j==0 or j==img.size[1]) or neighbor>=2):
            pixelsNew[i,j]=pixTOADD[i,j]
        else:
            pixelsNew[i,j]=pixTOCUT[i,j]
            
im1.close()
im2.close()
img.show()       
img.save("out.tif") 
img.close()