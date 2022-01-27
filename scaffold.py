import keyboard
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

while not keyboard.is_pressed('esc'):
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y-1, z, block.COBBLESTONE)
