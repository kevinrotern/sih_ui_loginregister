import random
import qrcode
from PIL import Image, ImageDraw, ImageFont

base = Image.open('pce_id_blank.jpeg').convert('RGBA')
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
fnt = ImageFont.truetype('arial.ttf', 48)
d = ImageDraw.Draw(txt)
#base.show()
#name
name = input('Enter Your Full Name: ')
d.text((429, 1061),str(name), font=fnt, fill="black")

#branch
branch= input('Enter branch: ')
d.text((425, 1151),str(branch), font=fnt, fill="black")
out = Image.alpha_composite(base, txt)

out.save(str(name) + '.png')
idno = random.randint(10000000, 90000000)
QR = qrcode.make("Name:"+str(name) +'\n' + "Branch:"+str(branch)+'\n' +"Id.no:"+ str(idno))  #info is added in QR code
QR.save(str(idno) +".png")

ID = Image.open(name + '.png')
QR = Image.open(str(idno) + '.png')  # 25x25
ID.paste(QR, (65, 480))

base1 = Image.open('pce_id_back2.2.jpg').convert('RGBA')
txt1 = Image.new('RGBA', base1.size, (255, 255, 255, 0))
fnt1 = ImageFont.truetype('arial.ttf', 47)
d1 = ImageDraw.Draw(txt1)
#dob
#dob = input('Enter Your DOB: ')
d1.text((70,500),"Date of Birth :"+" 13/01/2002", font=fnt1, fill="black")

#email
#email = input('Enter Your email: ')
d1.text((70,570),"Email :"+" jayeshrajbhar123@gmail.com", font=fnt1, fill="black")

#addreess
#add = input('Enter Your add: ')
d1.text((70,670),"Address :"+" 102,GANESH NIWAS,SECTOR-5,"+"\n"+"                 BABA POSHA PATIL MARG,"+"\n"+"                 SANPADA", font=fnt1, fill="black")

#UNIQEID
fnt12 = ImageFont.truetype('arial.ttf', 70)
d1.text((333,1229),str(idno), font=fnt12, fill="black",)

#mob
#mob=int(input("Enter the mob"))
d1.text((70,900),"Tel/Mob : "+"9820109952", font=fnt1, fill="black")

out1 = Image.alpha_composite(base1, txt1)

new_image = Image.new('RGB',(ID.width+out1.width,ID.height), (250,250,250))
new_image.paste(ID,(0,0))
new_image.paste(out1,(ID.width,0))
new_image.save(str(name)+str(idno)+'.JPEG')
new_image.show()