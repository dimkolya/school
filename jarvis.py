import os
import discord
import datetime
import pyglet
import googletrans
import requests
import matplotlib.pyplot as plt
from numpy import *
from math import *
from sympy import *
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.utils import get
from random import randint
from pyowm import OWM
from time import sleep
from googletrans import Translator

bot=commands.Bot(command_prefix='.')
#symbols
numbers=['0','1','2','3','4','5','6','7','8','9']
eng=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rus=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
maths=['-','+','/','*',',','(',')','.','%']
#words
hello=['привет','прив','хай','доробо','дорообо','дарова']
bad=['censored']
#sentence
end=['.','!','?']
#parserdata
currency=['австралийский доллар','азербайджанский манат','армянский драм','белорусский рубль','болгарский лев','бразильский реал','венгерский форинт',
'вона республики корея','гонконгский доллар','датская крона','доллар','евро','индийская рупия','казахстанский тенге','канадский доллар','киргизский сом','юань',
'молдавский лей','новый туркменский манат','норвежская крона','польский злотый','румынский лей','СДР','cингапурский доллар','таджикский сомони','турецкая лира',
'узбекский сум','украинская гривна','фунт стерлингов','чешская крона','шведская крона','швейцарский франк','южноафриканский рэнд','японская йена']
#weather
weaeng=['thunderstorm with light rain','thunderstorm with rain','thunderstorm with heavy rain','light thunderstorm','thunderstorm','heavy thunderstorm',
'ragged thunderstorm','thunderstorm with light drizzle','thunderstorm with drizzle','thunderstorm with heavy drizzle','light intensity drizzle','drizzle',
'heavy intensity drizzle','light intensity drizzle rain','drizzle rain','heavy intensity drizzle rain','shower rain and drizzle','heavy shower rain and drizzle',
'shower drizzle','light rain','moderate rain','heavy intensity rain','very heavy rain','extreme rain','freezing rain','light intensity shower rain','shower rain',
'heavy intensity shower rain','ragged shower rain','light snow','snow','heavy snow','sleet','light shower sleet','shower sleet','light rain and snow','rain and snow',
'light shower snow','lower snow','heavy shower snow','mist','smoke','haze','sand/ dust whirls','fog','sand','dust','volcanic ash','squalls','tornado','clear sky',
'few clouds','scattered clouds','broken clouds','overcast clouds']
wearu=['гроза с небольшим дождем','гроза с дождем','гроза с сильным дождем','слабая гроза','гроза','сильная гроза','местами гроза','гроза с мелким дождиком',
'гроза с моросью','гроза с сильным дождиком','слабая морось','морось','сильная морось','слабо моросящий дождь','моросящий дождь','сильно моросящий дождь','ливень',
'сильный ливень','слабый ливень','идет слабый дождь','идет дождь','идет сильный дождь','идет очень сильный дождь','идет очень сильный дождь','град',
'идет слабый дождь','льет дождь','льет сильный дождь','местами льет дождь','идет слабый снег','идет снег','идет сильный снег','мокрый снег',
'легкий дождь с мокрым снегом','дождь с мокрым снегом','слабый дождь со снегом','идет дождь со снегом','ливень со снегом','снег','метель','туман','смог','дымка',
'песчано-пыльные вихри','туман','песок','пыль','вулканический пепел','шквал','торнадо','небо чистое','малооблачно','переменная облачность','облачно','пасмурно']
#date
week=['Суббота','Воскресение','Понедельник','Вторник','Среда','Четверг','Пятница']
month=['','января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
#everyone
everyone=['оhуохай','гомл','goml','ujvk','пщьд','сахалар','мллыахха','млбб','mlbb']
#help
jarvis=['**.{текст}** - для перевода текста;\n',
'**/{функция, зависящая от x} [область определения функции (необяз.)]** - для получения графика функции. Пример: /2*x+1 [-4;6];\n',
'**Время** - для получения информации о текущем времени;\n',
'**ГДЗ {название предмета/учебника/задачника} {номер задания}** - для получения готового решения домашней работы по интересующему вас предмету;\n',
"**(функция, зависящая от x)'** - для получения производной функции. Пример вызова команды: (x+2)'",
'**Дата** - для получения информации о сегодняшней дате;\n',
'**Интеграл {функция, зависящая от x} от {нижний предел} до {верхний предел}** - для получения интеграла функции. Пределы вводятся для получения определенного интеграла (в противном случае будет вычислен непоределенный интеграл).;\n',
'**{Название валюты}** - для получения информации о курсе валюты;\n',
'**Найди {слово, которое вас интересует}** - для получения информации из википедии об интересующем вас слове;\n',
'**Новости/Новости из {политики, общества, науки}/Новости в {Якутии, Мире}** - для получения информации о последних новостях;\n',
'**Погода/Погода {название города}** - для получения информации о погоде в Якутске/в городе {название города};\n',
'**Факт** - для того, чтобы узнать случайный факт из интернета.\n']
hlp=['ГДЗ {название предмета/учебника/задачника} {номер задания} - gdz;\n',
'{Название валюты} - cur;\n',
'Найди {слово, которое вас интересует} - find;\n',
'{математическое выражение} - math.\n']
gdz=['алгебра','рымкевич']
jhelp='Вы можете воспользоваться следующими командами:\n'
hhelp='Используйте одну из следующих команд для получения подробностей по функциям:\n'
hgdz='Имеется доступ к ГДЗ по следующим предметам/учебникам/задачникам: '
hcur='Вы можете получить информацию о курсе относительно рубля для следующих валют: '
hfind='Вся информация берется с сайта https://ru.wikipedia.org/wiki/.'
hmath='Кальулятор работает на синтаксисе языка питон и большинство функций взяты с библиотеки math.py, их список можно узнать на сайте https://pythonworld.ru/moduli/modul-math.html.'
hmath+=' Также есть несколько дополнительных функций: 1) gcd(a,b) - НОД(a,b); 2) lcm(a,b) - НОК(a,b).'
for i in range(len(jarvis)):
    jhelp+=str(i+1)+') '+jarvis[i]
jhelp+='Чтобы узнать о каждой функции подробнее напишите "**помощь**". Также есть **калькулятор**, для использования которого, надо просто написать выражение, значение которого вы хотите получить.'
for i in range(len(hlp)):
    hhelp+=str(i+1)+') '+hlp[i]
for i in range(len(gdz)-1):
    hgdz+=gdz[i]+', '
hgdz+=gdz[i+1]+'. Пример вызова команды: "гдз алгебра 1.1".'
for i in range(len(currency)-1):
    hcur+=currency[i]+', '
hcur+=currency[i]+'.'
#mathfunc
res=0
def gcd(a, b):
    if a*b==0:
        return a+b
    elif a > b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
def lcm(a, b):
    return (a*b)//gcd(a,b)
#logic
col=[0xff9900,0xa840ff,0x0300e0,0x40f7ff,0xffbcfb]
ncol=randint(0,len(col)-1)
def nextcol():
    global ncol
    ncol=(ncol+1)%len(col)
#main
@bot.event
async def on_ready():
    channel=bot.get_channel(689799258504953937)
    print('J.A.R.V.I.S connected')
    await channel.send('J.A.R.V.I.S подключен к серверу.')
@bot.event
async def on_message(message):
    msg=message.content.lower()
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    if message.author!=bot.user and len(msg)>0:
        if msg=='джарвис':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Джарвис/Jarvis <:jarvis:757261821374890074>',description=jhelp))
            nextcol()
        elif msg=='помощь':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Помощь/Help <:jarvis:757261821374890074>',description=hhelp))
            nextcol()
        elif msg=='gdz':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Помощь/Help <:jarvis:757261821374890074>',description=hgdz))
            nextcol()
        elif msg=='cur':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Помощь/Help <:jarvis:757261821374890074>',description=hcur))
            nextcol()
        elif msg=='find':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Помощь/Help <:jarvis:757261821374890074>',description=hfind))
            nextcol()
        elif msg=='math':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Помощь/Help <:jarvis:757261821374890074>',description=hmath))
            nextcol()
        elif msg=='время':
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Время/Time :clock1:',description=str(datetime.datetime.now())[11:-7]))
            nextcol()
        elif msg=='дата':
            y,m,d=map(int,str(datetime.datetime.now())[:11].split('-'))
            if m==1 or m==10:
                mk=1
            elif m==5:
                mk=2
            elif m==8:
                mk=3
            elif m==2 or m==3 or m==11:
                mk=4
            elif m==6:
                mk=5
            elif m==9 or m==12:
                mk=6
            else:
                mk=0
            yk=(6+y%100+y%100//4)%7
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Дата/Date :date:',description=week[(d+yk+mk)%7]+', '+str(d)+' '+month[m]+' '+str(y)+' г.'))
            nextcol()
        elif msg[:6]=='погода':
            owm=OWM('OWM_TOKEN')
            mgr=owm.weather_manager()
            city='Якутск'
            if len(msg)>6:
                city=msg[7:]
            city=city.replace(' ','-')
            observation=mgr.weather_at_place(city)
            w=observation.weather
            deg=w.wind()['deg']
            if deg>338 or deg<=23:
                direction='Северный'
            elif deg<=68:
                direction='Северо-Восточный'
            elif deg<=113:
                direction='Восточный'
            elif deg<=158:
                direction='Юго-Восточный'
            elif deg<=203:
                direction='Южный'
            elif deg<=248:
                direction='Юго-Западный'
            elif deg<=293:
                direction='Западный'
            else:
                direction='Северо-Западный'
            for i in range(len(city)-1):
                if city[i]==' ':
                    city=city[:i+1]+city[i+1].upper()+city[i+2:]
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Погода/Weather :white_sun_rain_cloud:',description='Сейчас в городе '+city[0].upper()+city[1:]+' '+wearu[weaeng.index(str(w.detailed_status))]+', температура воздуха составляет '+str(w.temperature('celsius')['temp'])+' °C, влажность '+str(w.humidity)+'%. Ветер '+direction+', скорость: '+str(w.wind()['speed'])+' м/с.'))
            nextcol()
        elif msg in currency:
            link='http://www.finmarket.ru/currency/rates/'
            full_page=requests.get(link,headers=headers)
            soup=BeautifulSoup(full_page.content,'html.parser')
            convert=soup.tbody.findAll('td')
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Валюта/Currency :dollar:',description='Курс на данный момент: '+convert[2+5*currency.index(msg)].text+' '+msg+' = '+convert[3+5*currency.index(msg)].text+' рублей.'))
            nextcol()
        elif msg[:7]=='новости':
            section=msg[7:].replace(' ','')
            link='https://yandex.ru/news/'
            if section=='изполитики':
                full_page=requests.get(link+'rubrik/politics',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей в области политики:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+': '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link+'rubrik/politics'))
            elif section=='изобщества':
                full_page=requests.get(link+'rubric/society',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей в общественности:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'\n'+'Подробнее на сайте: '+link+'rubrik/society'))
            elif section=='изнауки':
                full_page=requests.get(link+'rubric/science',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей в общественности:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link+'rubric/science'))
            elif section=='вякутии':
                full_page=requests.get(link+'region/yakutsk',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей в Якутии:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link+'region/yakutsk'))
            elif section=='вмире':
                full_page=requests.get(link+'rubric/world',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей в Мире:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link+'rubric/world'))
            elif section=='прокоронавирус':
                full_page=requests.get(link+'rubric/koronavirus',headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей про коронавирус:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link+'rubric/world'))
            else:
                full_page=requests.get(link,headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                news=soup.findAll('h2',{'class':'news-card__title'})
                ntime=soup.findAll('span',{'class':'mg-card-source__time'})
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Новости/News :newspaper:',description='Из последних новостей:\n'+ntime[0].text+' - '+news[0].text+'.\n'+ntime[1].text+' - '+news[1].text+'.\n'+ntime[2].text+' - '+news[2].text+'.\n'+'Подробнее на сайте: '+link))
            nextcol()
        elif msg[:5]=='найди':
            word=msg[6:].replace(' ','_')
            link='https://ru.wikipedia.org/wiki/'+word
            full_page=requests.get(link,headers=headers)
            soup=BeautifulSoup(full_page.content,'html.parser')
            info=soup.findAll('p')
            if len(info)==1:
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description='Найдено слишком много значений слова, введите более конкретное значение.'))
            elif len(info)>1 and info[1].text=='Вы можете:\n':
                for i in range(len(word)-1):
                    if word[i]=='-' or word[i]==' ':
                        word=word[:i+1]+word[i+1].upper()+word[i+2:]
                link='https://ru.wikipedia.org/wiki/'+word
                full_page=requests.get(link,headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                info=soup.findAll('p')
                if len(info)==1:
                    await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description='Найдено слишком много значений слова, введите более конкретное значение.'))
                elif len(info)>1 and info[1].text=='Вы можете:\n':
                    link='https://ru.wikipedia.org/wiki/'+word.replace(' ','-')
                    full_page=requests.get(link,headers=headers)
                    soup=BeautifulSoup(full_page.content,'html.parser')
                    info=soup.findAll('p')
                    if len(info)==1:
                        await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description='Найдено слишком много значений слова, введите более конкретное значение.'))
                    elif info[1].text=='Вы можете:\n':
                        link='https://ru.wikipedia.org/wiki/'+word.replace(' ','').upper()
                        full_page=requests.get(link,headers=headers)
                        soup=BeautifulSoup(full_page.content,'html.parser')
                        info=soup.findAll('p')
                        if len(info)==1:
                            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description='Найдено слишком много значений слова, введите более конкретное значение.'))
                        elif info[1].text=='Вы можете:\n':
                            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description='Информация не найдена. Вы также можете создать такую страницу, помочь в этом может руководство для быстрого старта.'))
                        else:
                            fix=soup.tbody.findAll('p')
                            k=(info[0].text=='Состояниеотпатрулирована\n')+len(fix)
                            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description=info[k].text.replace('\n','')))
                    else:
                        fix=soup.tbody.findAll('p')
                        k=(info[0].text=='Состояниеотпатрулирована\n')+len(fix)
                        await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description=info[k].text.replace('\n','')))
                else:
                    fix=soup.tbody.findAll('p')
                    k=(info[0].text=='Состояниеотпатрулирована\n')+len(fix)
                    await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description=info[k].text.replace('\n','')))
            else:
                fix=soup.tbody.findAll('p')
                k=(info[0].text=='Состояниеотпатрулирована\n')+len(fix)
                embed=discord.Embed(description = "текст")
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Википедия/Wikipedia <:wikipedia:757232846317420656>',description=info[k].text.replace('\n','')))
            nextcol()
        #translator
        elif msg[0]=='.':
            translator=Translator()
            ans0=translator.translate(msg[1:],dest='ru')
            if ans0.text==msg[1:] or ans0.src=='ru':
                ans=translator.translate(msg[1:],dest='en')
                lang=googletrans.LANGUAGES.get(ans.dest)
                ans=ans.text
                for i in range(len(ans)-1):
                    if ans[i] in end:
                        ans=ans[:i+1]+ans[i+1].upper()+ans[i+2:]
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Переводчик/Translator <:googletranslator:758301393500504094>',description='**Russian**: '+msg[1:]+'\n\n**'+lang[0].upper()+lang[1:]+'**: '+ans[0].upper()+ans[1:]))
            else:
                ans=translator.translate(msg[1:],dest='ru')
                lang=googletrans.LANGUAGES.get(ans.src)
                ans=ans.text
                for i in range(len(ans)-1):
                    if ans[i] in end:
                        ans=ans[:i+1]+ans[i+1].upper()+ans[i+2:]
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Переводчик/Translator <:googletranslator:758301393500504094>',description='**'+lang[0].upper()+lang[1:]+'**: '+msg[1:]+'\n\n**Russian**: '+ans[0].upper()+ans[1:]))
            nextcol()
        elif msg=='факт':
            link='https://randstuff.ru/fact/'
            full_page=requests.get(link,headers=headers)
            soup=BeautifulSoup(full_page.content,'html.parser')
            await message.channel.send(embed=discord.Embed(color=col[ncol],title='Факт/Fact :mag:',description=soup.find('td').text))
            nextcol()
        #text
        msg=msg.replace(' ','')
        s=0
        for i in range(len(bad)):
            if bad[i] in msg:
                s=1
                break
        if (s==1 or msg=='нах'):
            await message.channel.send(f'{message.author.mention}, не выражаться')
        elif msg[-2:]=='ша':
            await message.channel.send('лава')
        elif msg in hello or msg[:6]=='доробо':
            await message.channel.send('До рo б'+randint(2,6)*'о')
        elif msg in everyone:
            await message.channel.send('@everyone')
        elif msg[:3]=='гдз':
            subject=msg[3:]
            if subject[:6]=='физика':
                print(1)
            elif subject[:7]=='алгебра':
                p=subject[7:subject.index('.')]
                n=subject[subject.index('.')+1:]
                link='https://gdz.ru/class-11/algebra/nikolskij-potapov/'+p+'-nom-'+n+'/'
                full_page=requests.get(link,headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                src=soup.findAll('div',{'class':'with-overtask'})
                for i in range(len(src)):
                    await message.channel.send('https:'+src[i].img.get('src'))
            elif subject[:8]=='рымкевич':
                n=subject[8:]
                link='https://reshak.ru/otvet/otvet10.php?otvet1='+n+'&var=1var'
                full_page=requests.get(link,headers=headers)
                soup=BeautifulSoup(full_page.content,'html.parser')
                src1=soup.find('div',{'class':'pic_otvet1'})
                src2=soup.find('div',{'class':'pic_otvet2'})
                src3=soup.find('div',{'class':'pic_otvet3'})
                await message.channel.send('Решение №1\nhttps://reshak.ru'+src1.img.get('src')+'\nРешение №2\nhttps://reshak.ru'+src2.img.get('src')+'\nРешение №3\nhttps://reshak.ru'+src3.img.get('src'))
        #calc
        m=1
        integral=msg
        info=0
        if msg[:8]=='интеграл' and msg.count('от')==0:
            integral=integral.replace('интеграл','')
            info=1
        elif msg[:8]=='интеграл' and msg.count('от')!=0:
            integral=integral.replace('интеграл','')
            integral=integral[:integral.index('о')]
            info=2
        elif msg[0]=='(' and msg[-2]+msg[-1]==")'":
            integral=integral[1:-2]
            info=3
        check=integral.replace('gcd','')
        check=check.replace('lcm','')
        check=check.replace('factorial','')
        check=check.replace('ceil','')
        check=check.replace('copysign','')
        check=check.replace('fabs','')
        check=check.replace('floor','')
        check=check.replace('fmod','')
        check=check.replace('frexp','')
        check=check.replace('ldexp','')
        check=check.replace('fsum','')
        check=check.replace('isfinite','')
        check=check.replace('isinf','')
        check=check.replace('isnan','')
        check=check.replace('modf','')
        check=check.replace('trunc','')
        check=check.replace('expm','')
        check=check.replace('exp','')
        check=check.replace('log1p','')
        check=check.replace('log10','')
        check=check.replace('log2','')
        check=check.replace('log','')
        check=check.replace('pow','')
        check=check.replace('sqrt','')
        check=check.replace('acosh','')
        check=check.replace('asinh','')
        check=check.replace('atanh','')
        check=check.replace('cosh','')
        check=check.replace('sinh','')
        check=check.replace('tanh','')
        check=check.replace('acos','')
        check=check.replace('asin','')
        check=check.replace('atan','')
        check=check.replace('cos','')
        check=check.replace('sin','')
        check=check.replace('tan','')
        check=check.replace('hypot','')
        check=check.replace('degrees','')
        check=check.replace('radians','')
        check=check.replace('erfc','')
        check=check.replace('erf','')
        check=check.replace('lgamma','')
        check=check.replace('gamma','')
        check=check.replace('res','')
        check=check.replace('pi','')
        check=check.replace('e','')
        check=check.replace('x','')
        for i in range(len(check)):
            if (check[i] in maths or check[i] in numbers)==0:
                m=0
                break
        if m==1:
            if msg[0]=='/':
                x1=-5
                x2=5
                gr=msg[1:]
                if msg[-1]==']':
                    odz=gr[gr.index('[')+1:-1]
                    gr=gr[:gr.index('[')]
                    odz=odz.replace(',',';')
                    x1,x2=map(int,odz.split(';'))
                x1=max(x1,-20)
                x2=min(x2,20)
                f=gr
                x=linspace(x1, x2, 100)
                i=0
                y1=eval(gr)
                fig,ax=plt.subplots()
                ax.plot(x,y1,color='blue',label='f(x)')
                ax.grid(True)
                ax.axhline(y=0,lw=2,color='black')
                ax.axvline(x=0,lw=2,color='black')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.legend()
                fig.savefig('1.jpg')
                file=discord.File('1.jpg',filename='1.jpg')
                await message.channel.send('**График/Graph** :chart_with_downwards_trend:\n```f(x) = '+f+'```',file=file)
            elif info==1:
                x=symbols('x')
                f=eval(msg[8:])
                ans=integrate(f,x)
                ans=str(ans)
                i=len(ans)-1
                while ans[i]=='0':
                    ans=ans[:-1]
                    i-=1
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Интеграл/Integral :chart_with_upwards_trend:',description='```integral('+integral+')dx = '+ans+'+C```'))
                nextcol()
            elif info==2:
                x=symbols('x')
                f=eval(msg[8:msg.index('о')])
                a=float(msg[msg.rindex('т')+1:msg.index('д')])
                b=float(msg[msg.rindex('о')+1:])
                ans=integrate(f,(x,a,b))
                ans=str(ans)
                i=len(ans)-1
                while ans[i]=='0':
                    ans=ans[:-1]
                    i-=1
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Интеграл/Integral :chart_with_upwards_trend:',description='```integral ('+integral+')dx from '+str(a)+' to '+str(b)+' = '+ans+'```'))
                nextcol()
            elif info==3:
                x=symbols('x')
                f=eval(msg[1:-2])
                ans=diff(f)
                ans=str(ans)
                i=len(ans)-1
                while ans[i]=='0':
                    ans=ans[:-1]
                    i-=1
                await message.channel.send(embed=discord.Embed(color=col[ncol],title='Производная/Derivative :chart_with_upwards_trend:',description='```derivative('+integral+') = '+ans+'```'))
                nextcol()
            else:
                err0=0
                i=0
                check=msg.replace('(','').replace(')','')
                while i<len(check)-3:
                    if check[i]+check[i+1]=='**':
                        i+=2
                        while i<len(check)-3 and check[i] in numbers:
                            i+=1
                        if check[i]+check[i+1]=='**':
                            err0=1
                            break
                    i+=1
                err1=0
                for i in range(len(check)-2):
                    if check[i]+check[i+1]=='**':
                        j=0
                        p=0
                        while i+j+2<len(check) and check[i+j+2] in numbers:
                            j+=1
                        while i-p-1>0 and check[i-p-1] in numbers:
                            p+=1
                        if j*p>25:
                            err1=1
                            break
                err2=0
                for i in range(len(msg)-2):
                    if msg[i]+msg[i+1]=='**' and msg[i+2]=='(':
                        err2=1
                        break
                if err0==1 or err2==1:
                    await message.channel.send('В выражении операция, требующая большой памяти, если есть возможность, упростите её.')
                elif err1==1 or len(str(eval(msg)))>2000:
                    await message.channel.send('Число имеет слишком много знаков.')
                elif message.author!=bot.user:
                    global res
                    res=eval(msg)
                    await message.channel.send(embed=discord.Embed(color=col[ncol],title='Калькулятор/Calculator <:calc:757261789632397393>',description=str(res)))
                    nextcol()
token=open('token.txt','r').readline()
bot.run(token)
