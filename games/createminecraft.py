from ursina import *
from ursina.application import pause  
from ursina.prefabs.first_person_controller import FirstPersonController

import random2
'''
from re import T, escape
from gtts import gTTS, lang
import gtts
import playsound
'''

app = Ursina()

#texture
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound',loop = False, autoplay = True)
block_pick = 1

#sound
grass_put_sound = Audio('sound/dig/grass2',loop = False, autoplay = False)
grass_break_sound = Audio('sound/block/rooted_dirt/break1',loop = False, autoplay = False)
stone_put_sound = Audio('sound/dig/stone2',loop = False, autoplay = False)
stone_break_sound = Audio('sound/dig/stone1',loop = False, autoplay = False)
brick_put_sound = Audio('sound/block/deepslate_bricks/step1',loop = False, autoplay = False)
dirt_put_sound = Audio('sound/block/rooted_dirt/step5',loop = False, autoplay = False)
block_break_sound = Audio('sound/damage/fallbig',loop = False, autoplay = False)
sound_background = Audio('sound/song/calm_ambient_7540.mp3',loop = True, autoplay = False)


#screen settings
window.fps_counter.enable = False
window.exit_button.visible = False

#random variables
ran = random.randint(0,10)
'''
#speech
greeting = gTTS(text='สวัสดีค่ะ ยินดีต้อนรับสู่เกมอันยิ่งใหญ่ของนักพัฒนาสุดหล่อ', lang='th')
greeting.save("greeting.mp3")
'''

sound_background.play()

def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']: 
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

    if block_pick == 1:
        menu.block_pick_one()
    if block_pick == 2:
        menu.block_pick_two()
    if block_pick == 3:
        menu.block_pick_three()
    if block_pick == 4:
        menu.block_pick_four()

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5,
        )
    
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: 
                    voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                    grass_put_sound.play()           
                if block_pick == 2: 
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                    stone_put_sound.play() 
                if block_pick == 3: 
                    voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                    brick_put_sound.play() 
                if block_pick == 4: 
                    voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                    dirt_put_sound.play()
            
            if key == 'right mouse down':
                block_break_sound.play()
                destroy(self)
                    
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True,
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6),
        )
    
    def active(self):
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.position = Vec2(0.4,-0.6)

class Menu(Entity):
    def __init__(self):
        super(Menu, self).__init__(
            parent = camera.ui,
            model = 'assets/block',
            scale = 0.05,
            rotation = Vec3(0,45,45),
            position = Vec2(-0.7,-0.4),
        )
    
    def block_pick_one(self):
        self.texture = grass_texture
    def block_pick_two(self):
        self.texture = stone_texture
    def block_pick_three(self):
        self.texture = brick_texture
    def block_pick_four(self):
        self.texture = dirt_texture


#def Sound():
    #playsound.playsound("greeting.mp3")

for z in range(15):
    for x in range(15):
        for y in range(3):
            voxel = Voxel(position = (x,y,z))

#Sound()
player = FirstPersonController(position=(x,10,z))
sky = Sky()
hand = Hand()
menu = Menu()


app.run()


