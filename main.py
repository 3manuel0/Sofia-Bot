#Start date: 06/04/2021
import discord
import random
from asyncio import sleep
from discord.ext.commands.core import check
from speech import speachRecognation
import Scoring_
import counting_
import reversMyPhrase
import Animequotes
import studytimecounter
import time
import json
import Todo
from discord import player
from Myrandom import myrandom
from discord.ext import commands
from discord.ext.commands.bot import Bot
client = commands.Bot(command_prefix=('*'), help_command=None)

@client.event

async def on_ready():
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening , name="3manuel's orders"))
    print('Logged on as {0.user}'.format(client))


@client.command(aliases = ["sentence"])

async def phrase(ctx):
    await ctx.send(myrandom())

@client.command()

async def maker(ctx):
    await ctx.send('<@484672625692639241>')     

@client.command(aliases = ["Hi", "hi", "hello"])

async def Hello(ctx):
    if ctx.message.author.id == 484672625692639241:
        await ctx.send("Hi master "+ '<@' + str(ctx.message.author.id) + '>' + " :heart: Sophia is at your service 😊.")
        
    else:
        await ctx.send("Hi, " + '<@' + str(ctx.message.author.id) + '>' + " i hope you're having a wonderful day 😊.") 
@client.command(aliases = ["Help"])
async def help(ctx):
    await ctx.send("Games(only 1 game for now): :\n:video_game: The guessing game use the commands: *Ngame / *playGg / \n"
    +":video_game: To check your score use command: *score\n\n"
    +"Random stuff:\n:abc: To generate a random sentence (this is so stupid) use cmmands: *sentence / *phrase \n"
    +":abc: To get a random motivational quote use commands: *motivation / *motiv\n"
    +":abc: feel free to say hi to sophia commands: *Hi / *Hello") 

@client.command(aliases=["motiv"])

async def motivation(ctx):  
    f  = open('txt files/motivational quotes.txt', "r", encoding = "utf-8")
    my_quotes = f.readlines()
    f.close()
    await ctx.send(my_quotes[random.randrange(0, len(my_quotes))])

#The to do list stuff 
##############################################################
##############################################################
###############################################################
###############################################################

# @client.command(aliases = ["addtodo"])

# async def AddTodo(ctx, *, sttd):
#     if ctx.message.author.id == 484672625692639241:
#        myTodo = open('txt files/todo.txt', 'r', encoding="utf-8")
#        mylines = myTodo.readlines()
#        myTodo = open('txt files/todo.txt', 'a', encoding="utf-8")    
#        myTodo.write(str(len(mylines)+1)+ " :butterfly: " + sttd)
#        myTodo.write('\n')
#        myTodo.close()
#        await ctx.send("Added")
#     else: 
#         await ctx.send("You are not my master :angry:")          

# @client.command(aliases = ["todo"])

# async def Todo(ctx):
#     myTodo = open('txt files/todo.txt',"r", encoding="utf-8") 
#     STD = myTodo.read()
#     if len(STD) == 0:
#      await ctx.send("your to do list is empty :smile:")
#     else: 
#      await ctx.send("Things to do today:\n" + STD)
#     myTodo.close()  

# @client.command(aliases = ["cleartdl"])

# async def ClearTDL(ctx):
#     if ctx.message.author.id == 484672625692639241:
#         myTodo = open('txt files/todo.txt',"w", encoding="utf-8")
#         myTodo.write("")
#         myTodo.close()
#         await ctx.send("Cleared")
#     else:
#         await ctx.send("You are not my master :angry:")     

# @client.command(aliases=["cleartask"])

# async def taskclear(ctx , numb):
#   if ctx.message.author.id == 484672625692639241:
# #cheking if what is written is a number.
#     def isnotnumber():
#      try: 
#          float(numb)
#          return False
#      except ValueError:
#          return True

# #opening the file and assigning the lines of the file to a variable.
#     myfile = open('txt files/todo.txt',"r", encoding="utf-8")
#     mylines = myfile.readlines()
#     myfile.close()
#     mylines[int(numb)-1] = numb + " :butterfly: " + "This task is empty\n"
# #if what is written is not a number or a keyword.
#     if isnotnumber() and numb != "last":
#         #send this msg.
#         await ctx.send("what are you doing :rage:")
# #if what is written is a number or a keyword. 
#     else:

#       #if the keyword used is "last".        
#       if numb == "last":
#         numb = 0  
#         mylines[int(numb)-1]=""
#         myfile = open('txt files/todo.txt',"w", encoding="utf-8")
#         myfile.writelines(mylines)
#         myfile.close()
#         #clear the last task and send this msg.
#         await ctx.send("The last task was cleared")
#       #if the nuber is not 0 or a keyword.
#       else:
#         #if the file is empty.         
#         if len(mylines) == 0:

#           await ctx.send("Sorry but your to do list is empty")

#         #if the file is not empty.  
#         else:
#             #clear the task specified by numb "number".
#             myfile = open('txt files/todo.txt',"w", encoding="utf-8") 
#             myfile.writelines(mylines)
#             await ctx.send("task "+ numb + " is cleared") 
#             myfile.close()  
#   else:
      
#       #if the user in not me
#       await ctx.send("You can't do that please stop :disappointed_relieved:") 
# @client.command()
# async def rewrite(ctx, numb, *, newLine):
#     myfile = open("txt files/Todo.txt", "r", encoding="utf-8") 
#     mylines = myfile.readlines()
#     myfile.close()  
#     myfile = open("txt files/Todo.txt", "w", encoding="utf-8")
#     mylines[int(numb)-1] = numb + " :butterfly: " + newLine +"\n"
#     myfile.writelines(mylines)
#     await ctx.send("line number "+ numb +" has been changed to " + '" ' + newLine +' "')
#     myfile.close()
        
##################################################################################
################################################################################
####################################################################################
###############################################################################      

#The number guessing game.
#####################################################################################
#####################################################################################
#####################################################################################
# Theplayer = ""
# playing=False
# MyRandomNumbs=[]
# random_gen_numb=""
# repeatingNumber = None
# trycount = 0
# @client.command(aliases=["playGg","GuessingGame","Ggame", "Ngame", "ngame", "playgg"])
# async def MyGuessingGame(ctx):
#     global playing
#     global Theplayer                
#     global MyRandomNumbs
#     global random_gen_numb
#     global repeatingNumber                   
#     global trycount
#     My4digitNumber = ""       
#     if not playing:
#         trycount = 0
#         Theplayer = ctx.message.author
#         playing = True
#         for i in range(4):
#             randomNumb=str(random.randrange(10))
#             while randomNumb in MyRandomNumbs:
#                 randomNumb=str(random.randrange(10))
#             MyRandomNumbs.append(randomNumb)
#         random_gen_numb = My4digitNumber.join(MyRandomNumbs) 
#         await ctx.send("Try and guess the number") 
#     else:
#         await ctx.send('Complet the current game first before you run it again\nif you want to forfeit this game do " *ff "')

# @client.command(aliases=["try"])
# async def Trynumb(ctx, myTry): 
#     global playing
#     global Theplayer
#     global MyRandomNumbs
#     global random_gen_numb
#     global trycount
#     trylist=[]                     
#     def repeatinganumber():
#         repeat = 0
#         true = 0
#         for numb in myTry:
#             trylist.append(numb)
#         if len(trylist) == 4:      
#             for number in trylist:
#                 repeat = 0                     
#                 for x in range(4):
#                     if number == trylist[x]:
#                         repeat+=1
#                     # print("this is the number "+number)
#                     # print("this is repeat "+str(repeat))    
#                 if repeat > 1:
#                     true+=1
#                 else:
#                     true+=0  
#             if true > 0:
#                 return True
#             else:
#                 return False 
#     repeatingNumber = repeatinganumber()                                   
#     # print(repeatingNumber)
#     if ctx.message.author == Theplayer and playing:
#         trycount+=1   
#         e=0
#         p=0
#         existingNumb = ""
#         numberinPlace = ""
#         mytry = []  
#         if len(myTry) == 4 and not repeatingNumber:
#             for numb in myTry:
#                     mytry.append(numb)
#             def nonumbers():
#                 noNumberCount = 0
#                 for number in mytry:
#                     if number not in MyRandomNumbs:
#                         noNumberCount+=1
#                 if noNumberCount == 4:
#                     return True  
#                 elif noNumberCount < 4:
#                     return False                        
#             for number in mytry:
#                 if number in MyRandomNumbs:
#                     if mytry.index(number) == MyRandomNumbs.index(number):
#                         p+=1
#                         numberinPlace = str(p)+"P"
#                         # print(number)
#                     else:
#                         e+=1
#                         existingNumb = str(e)+"E"
#                         # print(number)           
#             if nonumbers():
#                 existingNumb ="0E"     
#             await ctx.send(numberinPlace+" "+existingNumb)        
#             if myTry == random_gen_numb:
#                 score = 1000 - (trycount*100)
#                 Scoring_.playerScore(int(score), str(Theplayer))
#                 Theplayer = ""
#                 MyRandomNumbs=[]
#                 playing = False
#                 await ctx.send("Congrats you did guess the number, it took you "+ str(trycount)+" attempts, "+"your score is "+ str(score))     
#         else:
#                 await ctx.send("please enter a 4 digit number, and don't repeat any number please")             
#     elif not playing:
#         if Theplayer == "":
#             Theplayer = '"No one"'
#             await ctx.send("The game is not currently running the current player is "+str(Theplayer))
#     else:
#         await ctx.send("you're not the current player.The current player is "+ '"' + str(Theplayer) + '"')        
# @client.command(aliases=["FF", "ff"])
# async def forfeit(ctx):
#     global playing   
#     global Theplayer   
#     global MyRandomNumbs   
#     if playing and ctx.message.author==Theplayer:
#         MyRandomNumbs=[]
#         playing = False
#         Theplayer = ""
#         await ctx.send("You lost!\n don't worry you could always start again by typing "+'"*playGg"')
#     else:
#         await ctx.send("You have not started a game yet!\nor you are not the current player")
playing = None
@client.command(aliases = ["playGg", "thegG"])
async def numbersGame(ctx):
    MyRandomNumbs=[]
    global playing
    tryCount = 0
    if not playing:
        trycount = 0
        Theplayer = ctx.message.author
        playing = True
        My4digitNumber = ""
        for i in range(4):
            randomNumb=str(random.randrange(10))
            while randomNumb in MyRandomNumbs:
                randomNumb=str(random.randrange(10))
            MyRandomNumbs.append(randomNumb)
        random_gen_numb = My4digitNumber.join(MyRandomNumbs) 
        await ctx.send(f"the game is started type the number to play") 
    else:
        await ctx.send('Complet the current game first before you run it again\nif you want to forfeit this game do " *ff "') 
    def check(msg):
        return msg.author == Theplayer and msg.channel == ctx.channel   
    while playing:
        msg =  await client.wait_for('message', check=check)
        trylist=[]  
        myTry = msg.content                   
        def repeatinganumber():
            repeat = 0
            true = 0
            for numb in myTry:
                trylist.append(numb)
            if len(trylist) == 4:      
                for number in trylist:
                    repeat = 0                     
                    for x in range(4):
                        if number == trylist[x]:
                            repeat+=1
                        # print("this is the number "+number)
                        # print("this is repeat "+str(repeat))    
                    if repeat > 1:
                        true+=1
                    else:
                        true+=0  
                if true > 0:
                    return True
                else:
                    return False 
        repeatingNumber = repeatinganumber()
        if ctx.message.author == Theplayer and playing:
          e=0
          p=0
          existingNumb = ""
          numberinPlace = ""
          mytry = []
          if myTry == "ff":
                MyRandomNumbs=[]
                playing = False
                Theplayer = ""
                await ctx.send("You lost!\n don't worry you could always start again by typing "+'"*playGg"')    
          elif len(myTry) == 4 and not repeatingNumber:
              tryCount += 1
              for numb in myTry:
                      mytry.append(numb)
              def nonumbers():
                  noNumberCount = 0
                  for number in mytry:
                      if number not in MyRandomNumbs:
                          noNumberCount+=1
                  if noNumberCount == 4:
                      return True  
                  elif noNumberCount < 4:
                      return False                        
              for number in mytry:
                  if number in MyRandomNumbs:
                      if mytry.index(number) == MyRandomNumbs.index(number):
                          p+=1
                          numberinPlace = str(p)+"P"
                          # print(number)
                      else:
                          e+=1
                          existingNumb = str(e)+"E"
                          # print(number)           
              if nonumbers():
                  existingNumb ="0E"       
              await ctx.send(numberinPlace+" "+existingNumb)        
              if myTry == random_gen_numb:
                  score = 1000 - (tryCount*100)
                  Scoring_.playerScore(int(score), str(Theplayer))
                  Theplayer = ""
                  MyRandomNumbs=[]
                  playing = False
                  await ctx.send("Congrats you did guess the number, it took you "+ str(tryCount)+" attempts, "+"your score is "+ str(score))     
          else:
              await ctx.send("please enter a 4 digit number, and don't repeat any number please")             
        elif not playing:
                if Theplayer == "":
                    Theplayer = '"No one"'
                await ctx.send("The game is not currently running the current player is "+str(Theplayer))
        else:
            await ctx.send("you're not the current player.The current player is "+ '"' + str(Theplayer) + '"')
        
@client.command()
async def score(ctx):
    player = str(ctx.message.author)
    myfile="playersscores.json"
    with open(myfile, "r") as file:
        mydata = json.load(file)
    if player in mydata:
        score = mydata[player]["score"]
        await ctx.send("Your total score is "+ str(score))
    else:
        await ctx.send("You haven't played yet")            
####################################################################################################
########################################################################################################
############################################################################################################
@client.command(aliases=["rev"])
async def reverse(ctx , *,sentence):
    result = reversMyPhrase.reversemysentence(str(sentence))
    await ctx.send(result)
@client.command(aliases=["randaq"])
async def randomAnimeQ(ctx):
    quote = Animequotes.RandomAnimeQuote()
    await ctx.send(quote)
@client.command(aliases=["randacq"])
async def randomCharQ(ctx, *,characterName):
    quote = Animequotes.RandomAnimeCharQuote(characterName)
    await ctx.send(quote)    
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    mysource = "./music/Thousand Foot Krutch - Be Somebody.mp3"
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)  
    if voice == None or not voice.is_playing():
        vc = await channel.connect()
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild) 
        vc.play(discord.FFmpegPCMAudio(executable="./ffmpeg-N-103752-g59719a905c-win64-gpl/bin/ffmpeg.exe", source=mysource))
    else:
        while 1:
            voice.play(discord.FFmpegPCMAudio(executable="./ffmpeg-N-103752-g59719a905c-win64-gpl/bin/ffmpeg.exe", source=mysource))    
 
            
           
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect() 
Count = 0
startcounting = True
@client.command()
async def repeat(ctx, numb, *,text):
    global startcounting 
    global Count
    startcounting = True
    mycount = int(numb) / 60
    await ctx.send(f"sending '{text}' every {mycount} min" )
    while startcounting:
        stoprepeat() 
        time.sleep(int(numb)) 
        Count+=1 
        await ctx.send(counting_.function(text))
@client.command()
async def stoprepeat(ctx):
    global startcounting
    startcounting = False
    await ctx.send("Ok i will stop now xD")    
@client.command()
async def settimer(ctx, numb, *,mytext = None):
    gif = "https://tenor.com/view/happy-mochi-gif-20079211"
    gif2 ="https://tenor.com/view/quality-quality-work-good-job-thumbs-up-good-gif-12270521" 
    gif3 = "https://tenor.com/view/anime-star-laugh-laughing-giggle-gif-12377043"
    gif4 = "https://tenor.com/view/wow-gif-20343480"
    gif5 = "https://tenor.com/view/thumbs-up-double-thumbs-up-like-agreed-yup-gif-11663223"
    gifs = [gif, gif2, gif3, gif4, gif5]
    mygif = gifs[random.randrange(len(gifs))]
    t = True
    if ctx.message.author.id != 484672625692639241:
        mytext = None
        await ctx.send("you're not '<@484672625692639241>', no data will be stored")    
    if mytext == None:
        text = f"{numb} mins have passed\n" + mygif
        await ctx.send(f"count started ({numb} min)" )
        while t:
            await sleep(int(numb)*60)
            t = False
    else:    
        text = f"Good job you have been studying/doing {mytext} for {numb} min\n" + mygif
        await ctx.send(f"count started ({numb} min)" )
        while t:
            await sleep(int(numb)*60)
            t = False
        studytimecounter.studies(int(numb), mytext)        
    await ctx.send(text) 
@client.command()
async def Myday(ctx):
    data = studytimecounter.getData()
    await ctx.send(data)
@client.command()
async def writeday(ctx, *,data = "you didnt comment on this "):
    sofiasQuote = studytimecounter.writeData(data)
    studytimecounter.clearDay()
    await ctx.send(sofiasQuote)   
@client.command(aliases = ["addtodo", "addtd"])
async def addTodo(ctx):
    discordID = ctx.message.author.id 
    addingTodo = True
    todo = ""
    author = ctx.message.author
    def check(msg):
        return msg.author == author and msg.channel == ctx.channel
    while addingTodo:
        await ctx.send("type something else if you wish to add more things to your todo list, if you're done type 'done', note this will timeout after 30s ")
        try:
           msg = await client.wait_for('message', check=check, timeout = 30)
           todo = msg.content
        except:
            todo = "done"
            await ctx.send("you took more than 30s :persevere:\n try again if you need to add something")
        if todo == "done":
            addingTodo = False
            await ctx.send("all done :thumbsup:")
        else:
            Todo.addTodo(discordID, todo)
    if todo != "done":            
        await ctx.send("all done :thumbsup:")
@client.command(aliases=["todolist", "tdl"])
async def myTodoList(ctx):
    discordID = ctx.message.author.id
    author = ctx.message.author
    mytodo = Todo.showTdL(discordID, author)
    await ctx.send(mytodo)
@client.command(aliases=["cleartask", "Clear"])
async def clear(ctx):
    author = ctx.message.author
    discordID = ctx.message.author.id
    await ctx.send(Todo.showTdL(discordID, author) + "\n type the line number or type all to clear the list")
    def check(msg):
        return msg.author == author and msg.channel == ctx.channel
    msg = await client.wait_for('message', check=check) 
    cleared = Todo.clearTask(discordID, msg.content)
    await ctx.send(cleared)
@client.command(aliases = ["setemote"])
async def setEmote(ctx, *,emote):
    myemote = str(emote)
    discordID = ctx.message.author.id
    myEmote = Todo.customEmote(discordID, myemote)
    getMyEmote = Todo.getEmote(str(discordID))
    await ctx.send(f"emote changed your new emote is {getMyEmote}")
@client.command(aliases=["giverole"])
async def getUser(ctx, role, *,id):
    user = await ctx.message.guild.query_members(user_ids=[id])
    user = user[0]
    await user.add_roles(discord.utils.get(user.guild.roles, name= role))
    await ctx.send('<@&907709736210825296>')
@client.command()
async def sendDm(ctx, *, msg):
    user = ctx.message.author
    await user.send(msg)
@client.command(aliases = ["remindme", "reminder", "remind"])
async def reminderMe(ctx, time, *,message = 'reminder'):
    remindMe= True
    user = ctx.message.author
    def convertTime():
        times = ["s", "m", "h"]                       
        time_dict = {"s" : 1, "m" : 60, "h" :3600}  
        Unit = time[-1]
        newTime = time.translate({ord(Unit):None}) 
        if Unit in times:
            return int(newTime) * time_dict[Unit]
        else:
            return (f":worried: error {time} not found in time data {times}")         
    try:
        await ctx.send(f"i will reminde you to '{message}' after {time}")
        while remindMe:
            await sleep(convertTime())
            remindMe = False
        await user.send(message)
    except:
        await ctx.send(convertTime())  
@client.command()
async def speech(ctx):
    channel = ctx.author.voice.channel
    try:
       vc = await channel.connect()
    except:
        vc = None   
    await ctx.send(speachRecognation())

client.run("")
