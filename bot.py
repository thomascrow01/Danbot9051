# Work with Python 3.6
import discord
from alone import *
from PIL import Image, ImageDraw, ImageFont
TOKEN = 'MjcxOTI5OTUxNzk0NjI2NTYx.DYPG5g.FMDge03SUhapL-q2g8tsTEF5ke8'

client = discord.Client()

prefix = '&'

file = open('msgs.txt','r')
data = file.readlines()
commands = []
for i in data:
    temp = i.strip().split(',')
    print(str(temp[1]))
    commands.append(temp)
file.close()

print(commands)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    m = str(message).lower()      

    for i in commands:
        if message.content == i[0]:
            msg = i[1]
            await client.send_message(message.channel, msg)
        
    if message.content == (prefix + "ritter"):
        msg = '**trains** \n <:rit1:264632942733557761><:rit2:264632943144730644><:rit3:264632943476080640> \n <:rit4:264632943639527434><:rit5:264632943421554691><:rit6:264632945367580672> \n <:rit7:264632944755212289><:rit8:264632945401135104><:rit9:264632945115922434>'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == (prefix + "marie"):
        #msg = '**Now this bitch I would fuck her so hard her kids would feel it. Plz Nintendo give me a Marie fucking sim I would pay mountains of cash.** \n <:marie1:405326048872366090><:marie2:405326051758178314><:marie3:405326050050965504><:marie4:405326049098858498> \n <:marie5:405326050923511808><:marie6:405326052479598592><:marie7:405326050810396673><:marie8:405326049291927552> \n <:marie9:405326050877374464><:marie10:405326052425072641><:marie11:405326052974657537><:marie12:405326050655076363> \n <:marie13:405326050042576896><:marie14:405326051095347200><:marie15:405326050059354125><:marie16:405326049795112962>'.format(message)
        msg = 'Now this bitch I would fuck her so hard her kids would feel it. Plz Nintendo give me a Marie fucking sim I would pay mountains of cash.'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == (prefix + 'chelsea'):
        msg = "Remember when you asked me who I liked in term 2? Well, I have a confession to make... The person I like is you, Chelsea. From when I first talked to you, I saw you as a kind, intelligent, pretty, funny and strong-opinioned person. From then on, I liked you for your personality and kindness towards everyone. After careful thought, I have decided that my secret cannot be held back anymore, and I would like to know if you would like to be my first girlfriend.".format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == (prefix + 'lollie'):
        msg = "Can please get rid of the dumb fucking lollie bot. It's fucking stupid it makes it sound like we are super desperate to find a fucking date and the dumb fucking images that pop up".format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == (prefix + 'pasta'):
        msg = "chelsea - George's letter \nlollie - Cotton's sperg \n".format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == (prefix + 'lewd'):
        msg = "https://cdn.discordapp.com/attachments/436028618485792768/450206367819497482/hinokalewd.png".format(message)
        await client.send_message(message.channel, msg)
        
    #if message.content == ('succ'):
        #msg = 'S U C C \nU \nC \nC'.format(message)
        #await client.send_message(message.channel, msg)
    

        
    if message.content.startswith(prefix + 'fc'): 
        msg = "0361-9574-6041 dan\n3153-9628-9995 may\n0920-5030-1151 joe\n1306-4931-3543 gin\n3866-9206-5223 ang\n4124-5082-9752 aki \n1564-3621-7080 tom ashoo8 \n1521-7977-4558 tom bleach".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix+'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix+'alone'):
        alone()
        await client.send_file(message.channel, 'aloneout.png')

    if message.content.startswith(prefix+'juice'):
        #juice(str(message.content[5:]))

        W = 140
        Ws = 65
        def juice(juicebox):
            image = Image.open('juiceblank.png')
            font_type_s = ImageFont.truetype("segoeprb.ttf", 16)
            font_type_l = ImageFont.truetype("segoeprb.ttf", 30)
            draw = ImageDraw.Draw(image)
            widths = font_type_s.getsize(juicebox)[0]
            draw.text((188+(Ws-widths)/2,360),text=juicebox,font=font_type_s)
            width = font_type_l.getsize(juicebox)[0]
            w = draw.textsize(juicebox)
            print(width)
            print(widths)
            draw.text((550+(W-width)/2, 325), juicebox, font=font_type_l)
            image.save("juiceout.png") 
        juice(str(message.content[7:]))
        await client.send_file(message.channel, 'juiceout.png')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
