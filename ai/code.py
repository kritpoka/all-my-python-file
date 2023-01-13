from re import T, escape
from gtts import gTTS
import gtts 
import playsound
from tkinter import*
"""
root = Tk()
root.title =("My GUI")
root.geometry()
root.mainloop()
"""

#variable 
tts = gTTS(text='สวัสดีค่ะวัยรุ่นเมโสโปเตเมีย ฉันคือผู้ช่วยที่ดีที่่สุดในยุคนี้ ว่าแต่คุณมีคำถามอะไร', lang='th')
tts.save("helloworld.mp3")
asking = gTTS(text="คุณอยากถามอะไร", lang="th")
asking.save("asking.mp3")
answers = gTTS(text='ขอบคุณสำหรับคำถามค่ะ',lang='th')
answers.save("answer.mp3")
onevoice = gTTS(text="จะไปรู้มั้ยฉันไม่ใช่ google ตัวจริง", lang='th')
onevoice.save("onevoice.mp3") 
thx = gTTS(text="ขอบคุณสำหรับคำถามค่ะ ถามได้ดีมาก", lang='th')
thx.save("thx.mp3")
yourq = gTTS(text="คำตอบของคุณคือ", lang="th")
yourq.save("yourq.mp3") 
askerror = gTTS(text="ขอโทษค่ะคำถามของคุณฉลาดเกินไป ฉันตอบไม่ได้", lang="th")
askerror.save("askerror.mp3")
sister = gTTS(text="สวัสดีคุณวัยรุ่น ฉันผู่คือช่วยคุณ โย่ว โย่ว", lang="th")
sister.save("sister.mp3")
areyou = gTTS(text="คุณคือใคร", lang="th")
areyou.save("areyou.mp3")


#program 
playsound.playsound("areyou.mp3")

who = input("คุณคือใคร :")

if who == "30062554":
    playsound.playsound("sister.mp3")
    playsound.playsound("asking.mp3")
else:
    playsound.playsound("helloworld.mp3", True) 

print("1.วันนี้อากาศเป็นอย่างไรบ้าง")
print("2.ทำอะไรอยู่")
print("3.เป็นอย่างไรบ้าง")
print("4.เธอชื่ออะไร")

value = input("เลือกหัวข้อ :")

playsound.playsound("thx.mp3", True)

playsound.playsound("yourq.mp3", True)

if value == "1":
    playsound.playsound("onevoice.mp3", True)
else:
    playsound.playsound("askerror.mp3", True)






