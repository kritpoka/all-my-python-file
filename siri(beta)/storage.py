from re import T, escape
from gtts import gTTS, lang
import gtts 
import playsound

#variable 
greeting = gTTS(text='สวัสดี ฉันคือผู้ช่วยของคุณ คุณคือใคร',lang='th')
greeting.save("greeting.mp3")

ask1 = gTTS(text='สวัสดีคุณ',lang='th')
ask1.save("ask1.mp3")

ask2=gTTS(text='อยากให้ฉันช่วยอะไร',lang='th')
ask2.save("ask2.mp3")

tts = gTTS(text='hi')
tts.save("ask2.mp3")


#coding 
"""
playsound.playsound("greeting.mp3")

names=input("กรอกชื่อ: ")
names.save("names.mp3")
playsound.playsound("ask1.mp3")
playsound.playsound("names.mp3")
"""
playsound.playsound("ask2.mp3")




