import discord
from discord.ext import commands
from random import *
from Cybernator import Paginator

bot=commands.Bot(command_prefix='+')

color=discord.Color.green()
arrows=['◀️', '▶️']
d6_faces={1:'https://cdn.discordapp.com/attachments/792512944969482250/792513058962538496/Screenshot_20201227-003114.png', 2:'https://cdn.discordapp.com/attachments/792512944969482250/792513059393372180/Screenshot_20201227-003051.png', 3:'https://cdn.discordapp.com/attachments/792512944969482250/792513059628384316/Screenshot_20201227-003013.png', 4:'https://cdn.discordapp.com/attachments/792512944969482250/792513059859464192/Screenshot_20201227-003103.png', 5:'https://cdn.discordapp.com/attachments/792512944969482250/792513060228431882/Screenshot_20201227-003043.png', 6:'https://cdn.discordapp.com/attachments/792512944969482250/792513060447322112/Screenshot_20201227-003122.png'}

d12_faces={1:'https://cdn.discordapp.com/attachments/792512944969482250/792523990895296542/Screenshot_20201227-013948.png', 2:'https://cdn.discordapp.com/attachments/792512944969482250/792523991163207690/Screenshot_20201227-013236.png', 3:'https://cdn.discordapp.com/attachments/792512944969482250/792523991483023370/Screenshot_20201227-013223.png', 4:'https://cdn.discordapp.com/attachments/792512944969482250/792523991985553479/Screenshot_20201227-013245.png', 5:'https://cdn.discordapp.com/attachments/792512944969482250/792523992267227176/Screenshot_20201227-013203.png', 6:'https://cdn.discordapp.com/attachments/792512944969482250/792523992547852298/Screenshot_20201227-013916.png',  7:'https://cdn.discordapp.com/attachments/792512944969482250/792523992841977896/Screenshot_20201227-013154.png', 8:'https://cdn.discordapp.com/attachments/792512944969482250/792523993152225291/Screenshot_20201227-013301.png', 9:'https://cdn.discordapp.com/attachments/792512944969482250/792523993617268766/Screenshot_20201227-014012.png', 10:'https://cdn.discordapp.com/attachments/792512944969482250/792523993906282526/Screenshot_20201227-013329.png', 11:'https://cdn.discordapp.com/attachments/792512944969482250/792524026307543040/Screenshot_20201227-014028.png', 12:'https://cdn.discordapp.com/attachments/792512944969482250/792524026538885120/Screenshot_20201227-014005.png' }

d20_faces={1:'https://cdn.discordapp.com/attachments/792512944969482250/792657083853570068/Screenshot_20201227-101824.png', 2:'https://cdn.discordapp.com/attachments/792512944969482250/792657084168405022/Screenshot_20201227-102022.png', 3:'https://cdn.discordapp.com/attachments/792512944969482250/792657084369338368/Screenshot_20201227-102000.png', 4:'https://cdn.discordapp.com/attachments/792512944969482250/792657084667002910/Screenshot_20201227-102013.png', 5:'https://cdn.discordapp.com/attachments/792512944969482250/792657084898476052/Screenshot_20201227-101912.png', 6:'https://cdn.discordapp.com/attachments/792512944969482250/792657085169926165/Screenshot_20201227-101840.png', 7:'https://cdn.discordapp.com/attachments/792512944969482250/792657085350412318/Screenshot_20201227-101929.png', 8:'https://cdn.discordapp.com/attachments/792512944969482250/792657085552132136/Screenshot_20201227-101859.png', 9:'https://cdn.discordapp.com/attachments/792512944969482250/792657085769973761/Screenshot_20201227-102135.png', 10:'https://cdn.discordapp.com/attachments/792512944969482250/792657086089527316/Screenshot_20201227-102203.png', 11:'https://cdn.discordapp.com/attachments/792512944969482250/792657322941743144/Screenshot_20201227-102048.png', 12:'https://cdn.discordapp.com/attachments/792512944969482250/792657323184881664/Screenshot_20201227-101949.png', 13:'https://cdn.discordapp.com/attachments/792512944969482250/792657323441127454/Screenshot_20201227-102055.png', 14:'https://cdn.discordapp.com/attachments/792512944969482250/792657323658706964/Screenshot_20201227-101938.png', 15:'https://cdn.discordapp.com/attachments/792512944969482250/792657323863834624/Screenshot_20201227-102037.png', 16:'https://cdn.discordapp.com/attachments/792512944969482250/792657324082462720/Screenshot_20201227-101848.png', 17:'https://cdn.discordapp.com/attachments/792512944969482250/792657324346310656/Screenshot_20201227-102144.png', 18:'https://cdn.discordapp.com/attachments/792512944969482250/792657324820529172/Screenshot_20201227-103250.png', 19:'https://cdn.discordapp.com/attachments/792512944969482250/792657325105872916/Screenshot_20201227-101832.png', 20:'https://cdn.discordapp.com/attachments/792512944969482250/792657325361070130/Screenshot_20201227-102029.png' }

@bot.event
async def on_ready():
	print('Бот работает')
	
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="+команды"))

@bot.command(pass_context=True)

async def команды(ctx):
	info=discord.Embed(title='Информация', colour=color, description='Префикс бота "+"\n\nБот для бросания игровых костей в рп\n**Создан по спецзаказу ТКМП**')
	info.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
	
	#[][][][]
	
	com=discord.Embed(title='Команды', colour=color, inline=False)
	com.add_field(name='``+кинуть_монетку``', value='Бросок монетки')
	com.add_field(name='``+кинуть_д6``', value='Бросок кубика д6')
	com.add_field(name='``+кинуть_д12``', value='Бросок кубика д12')
	com.add_field(name='``+кинуть_д20``', value='Бросок кубика д20')
	com.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
	
	#[][][][][][][]
	
	msg=await ctx.send(embed=info)
	embeds=[info, com]
	page=Paginator(bot, msg, only=ctx.author, use_more=False, embeds=embeds, reactions=arrows)
	await page.start()
	
@bot.command()

async def кинуть_д6(ctx):
	res=[]
	for _ in range (5):
		res.append(randint(1,6))
	res=choice(res)
	emb=discord.Embed(title='Бросок кубика д6', colour=color)
	emb.add_field(name='На кубике д6 выпало число:', value= res)
	emb.set_footer(text=f'Кубик кинул {ctx.author.name}', icon_url=ctx.author.avatar_url)
	emb.set_image(url=d6_faces[res])
	await ctx.send(embed=emb)
	
@bot.command()

async def кинуть_д12(ctx):
	res=[]
	for _ in range (5):
		res.append(randint(1,12))
	res=choice(res)
	emb=discord.Embed(title='Бросок кубика д12', colour=color)
	emb.add_field(name='На кубике д12 выпало число:', value= res)
	emb.set_image(url=d12_faces[res])
	emb.set_footer(text=f'Кубик кинул {ctx.author.name}', icon_url=ctx.author.avatar_url)
	await ctx.send(embed=emb)
	
@bot.command()

async def кинуть_д20(ctx):
	res=[]
	for _ in range (5):
		res.append(randint(1,20))
	res=choice(res)
	emb=discord.Embed(title='Бросок кубика д20', colour=color)
	emb.add_field(name='На кубике д20 выпало число:', value= res)
	emb.set_footer(text=f'Кубик кинул {ctx.author.name}', icon_url=ctx.author.avatar_url)
	emb.set_image(url=d20_faces[res])
	await ctx.send(embed=emb)
	
@bot.command()

async def кинуть_монетку(ctx):
	res=[]
	for _ in range (5):
		res.append(randint(1,2))
	res=choice(res)
	if res==1:
		res=True
	else:
		res=False
	emb=discord.Embed(title='Бросок монетки', colour=color)
	emb.add_field(name='На монетке выпало', value= res)
	emb.set_footer(text=f'Монетку кинул {ctx.author.name}', icon_url=ctx.author.avatar_url)
	emb.set_image(url='https://ru1.anyfad.com/items/t1@fc62187e-6cb8-49e3-9461-52932e877fc6/Monetka-Mario.jpg')
	await ctx.send(embed=emb)
	
bot.run('NzkyNTA1NDE2MTA5MTI5ODE4.X-esLw.WG54yQHWInXqu_h_HeNl2eHqCCM')