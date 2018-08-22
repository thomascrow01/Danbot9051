from PIL import Image, ImageDraw, ImageFont
import datetime
import calendar
now = datetime.datetime.now()

image = Image.open('D:/Joseph/Pictures/alone blank.png')
font_type = ImageFont.truetype("segoeprb.ttf", 16)
draw = ImageDraw.Draw(image)
draw.text(xy=(355,70),text="Alone on a",font=font_type)
draw.text(xy=(360,95),text=str(now.strftime('%A')),font=font_type)
if now.hour >=0 and now.hour < 12:
    draw.text(xy=(370,120),text="morning?",font=font_type)
if now.hour >=12 and now.hour < 18:
    draw.text(xy=(370,120),text="afternoon?",font=font_type)
if now.hour >=18 and now.hour < 24:
    draw.text(xy=(370,120),text="night?",font=font_type)
image.show()
image.save("aloneout.png")
