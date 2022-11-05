def watermarkWithPicture(oPic,wPic,size,scale): 
# This function watermarks the original image with the watermark image. 
# The strength of the watermark (0-100) is supplied and determines  
# how transparent the watermark image will be. The watermark is 
# scaled by using the specified scale factor (it could be smaller or larger) 
# # Requires tasks 1-3 to be completed. (Greyscale, Scaling, Simple blending)  
# Will be improved by task 4. (Blending based on luminance) # 
   
   wPic = scaleP(scale)
   wPic = greyP(wPic)
   oPic = blendP(oPic,wPic,75,75,size)
   wPic = luminanceP(wPic)
  
      
   
   return(oPic)
   show(oPic)   
   
      

#Task1 Greyscale
def greyP(wPic):
   pixels = getPixels(wPic)

   for pix in pixels:
      greyV=(getRed(pix) + getGreen(pix) + getBlue(pix)) / 3
      setRed(pix, greyV)
      setGreen(pix, greyV)
      setBlue(pix, greyV)
   show(wPic)
   return(wPic) 
    
    

#Task2 Scaling
def scaleP(scale):
   width = getWidth(wPic)
   height = getHeight(wPic)
   newPic = makeEmptyPicture(width * int(scale),height * int(scale))
   
   if scale > 1:
      for x in range(0, width):
         for y in range(0, height):
            pix = getPixel(wPic, x, y)
            
            for x1 in range(x * int(scale), x * int(scale) + int(scale)):
               for y1 in range(y * int(scale), y * int(scale) + int(scale)):
                  pix1 = getPixel(newPic,x1,y1)
                  setColor(pix1, getColor(pix))
   else:  
       for x in range(0, width):
         for y in range(0, height):
            pix = getPixel(wPic, x, y)      
            for x2 in range(x / int(scale), x / int(scale) + int(scale)):
               for y2 in range(y / int(scale), y / int(scale) + int(scale)):
                  pix2 = getPixel(newPic,x2,y2)
                  setColor(pix2, getColor(pix))
   show(newPic)
   return newPic                                    
   
   

#Task3 Blending
def blendP(oPic, wPic, xstart, ystart, size):

   for x in range(0, getWidth(wPic)):
      for y in range(0, getHeight(wPic)):
         pix = getPixel(oPic, xstart + x, ystart + y)
         pix1 = getPixel(wPic, x, y)
         newRed = getRed(pix) * size / 100 + getRed(pix1) * (100 - size) / 100
         newGreen = getGreen(pix) * size / 100 + getGreen(pix1) * (100 - size) / 100
         newBlue = getBlue(pix) * size / 100 + getBlue(pix1) * (100 - size) / 100
         newColour = makeColor(newRed, newGreen, newBlue)
         setColor(pix, newColour)
   show(oPic)


#Task4 Luminance blending
def luminanceP(wPic):

   pixels = getPixels(wPic)
   for pix in pixels:
      r = getRed(pix)
      g = getGreen(pix)
      b = getBlue(pix)
      lum = makeColor( r + g + b / 3)
      setColor(pix, lum)
   show(wPic)

#Task5 Text
def textP():
   addText(pic,45,45,"WonJun Jo dom",red)
   addText(pic,60,60,"C3341243 C3313933 ",red)
   
   show(pic)
   