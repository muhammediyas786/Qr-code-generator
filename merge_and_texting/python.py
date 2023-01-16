from PIL import Image,ImageFont,ImageDraw
import qrcode
import urllib.request




def merging(id):
    # Open the image
    urllib.request.urlretrieve(
    'https://eweb.pythonanywhere.com/media/wallpapers/background.jpg',
    "background.png")
    image1 = Image.open('background.png')
    image2 = Image.open(r"qr_codes/qr_code"+str(id)+".jpg")

    # Resize image2 to match the size of image1
    newsize = (300, 300)
    image2 = image2.resize(newsize)

    # Create a new image with the same size as image1
    result = Image.new("RGB", image1.size)

    # Paste image1 onto the new image
    result.paste(image1, (0, 0))

    # Paste image2 onto the new image, on top of image1
    result.paste(image2, (145, 440), image2)

    # Return the resulting image
    result.save('media/image'+str(id)+'.jpg')




def Texting(id,holder_status,link_from):
    img = Image.open(r'media/image'+str(id)+'.jpg')
    # Set font type and size
    font_type = ImageFont.truetype('arial.ttf',60)
    draw = ImageDraw.Draw(img)

    # Create a white color text "MY" to the image
    draw.text(xy=(270,200),text=holder_status, stroke_width=2, fill=('#ffffff'),font=font_type)
    
    
    # Create a white color text "MY" to the image
    draw.text(xy=(132,300),text=link_from, stroke_width=2, fill=('#ffffff'),font=font_type)
    
    # Return the final resulting image
    img.save('media/image'+str(id)+'.jpg')





def code_generating(link,id):

    # qr code generating with using a link
    img = qrcode.make(link)
    name = "qr_codes/qr_code"+str(id)+".jpg"
    img.save(name)
    

