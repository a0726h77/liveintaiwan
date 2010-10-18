# coding:utf8

import Image,ImageDraw,ImageFont
import random

# ----------------------- Settings -----------------------------------------
charNum = 4
# actual background size is 300 * 70
width = 240
height = 50
charNum = 4
interval = width/charNum
fontSize = 36
chImgW = fontSize+10
chImgH = fontSize+10
lineNum = random.randint(2,5)
font = ImageFont.truetype('fonts/MSJH.TTF',fontSize)
alphArr = ['A','B','C','D','E','F','G','H',
		'J','K','L','M','N','P','R','S','T',
		'W','X','Z','2','3','4','5','6','8']

# ----------------------- Create a background -----------------------------------------
image = Image.open('images/bg.jpg')
draw = ImageDraw.Draw(image)

# ----------------------- Generate a couple of alphabets ------------------------------
for i in range(0,charNum):
	# Create a small image to hold one character. Background is black
	charImg = Image.new('RGB',(chImgW, chImgH),(0,0,0))
	tmpDraw = ImageDraw.Draw(charImg)
	# Draw text on this image
	tmpDraw.text(
			(3, 1), 
			random.choice(alphArr), 
			font = font, 
			fill = (random.randint(20,150), random.randint(20,140), random.randint(160,200))
			)
	# Rotate a little bit, do some trick if you want
	charImg = charImg.rotate(random.randint(-30,30))

	# Create a mask which is same size of the small image
	mask = Image.new('L',(chImgW, chImgH),0) 
	mask.paste(charImg,(0,0))

	# Generate Random X Y
	hpos = 10 + (i*interval + random.randint(10,interval-10))
	vpos = random.randint(10, 20)

	# Paste twice for the visibility
	image.paste(charImg,(hpos,vpos),mask)
	image.paste(charImg,(hpos,vpos),mask)


# ----------------------- Draw a couple of lines -----------------------------------------
for i in range(0,lineNum):
	draw.line(
			(random.randint(6,width-6),random.randint(3,height-3),random.randint(6,width-6),random.randint(3,height-3)),
			fill = (random.randint(80,150), random.randint(80,220), random.randint(160,220))
			)

# save it
image.save('images/captcha.jpg')

#------------------------ Note -----------------------------------------------------------
# if it's web site like django, it'll be like
#out = StringIO()
#image.save(out,"JPEG")
#out.seek(0)
#response = HttpResponse()
#response['Content-Type'] = 'image/jpeg'
#response.write(out.read())
#return response
