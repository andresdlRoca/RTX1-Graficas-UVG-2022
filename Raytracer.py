from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3))
# stone = Material(diffuse = (0.4, 0.4, 0.4))
# grass = Material(diffuse = (0.3, 1, 0.3))
# snow = Material(diffuse = (1,1,1))
# button = Material(diffuse = (0,0,0))
# carrot = Material(diffuse = (1, 0.64, 0))

rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

rtx.scene.append( Sphere(V3(0,0,-10), 2, brick)  )
# rtx.scene.append( Sphere(V3(-4,-2,-15), 1.5, stone)  )
# rtx.scene.append( Sphere(V3(2,2,-8), 0.2, grass)  )

# #Body
# rtx.scene.append( Sphere(V3(0,-3,-10), 3, snow) )
# rtx.scene.append( Sphere(V3(0, -0.5, -10), 2.5, snow) )
# rtx.scene.append( Sphere(V3(0,2.5,-10), 2, snow) )

# #Buttons
# rtx.scene.append( Sphere(V3(0,-2, -5), 0.4, button))
# rtx.scene.append( Sphere(V3(0,-1, -5), 0.2, button))
# rtx.scene.append( Sphere(V3(0,0, -5), 0.2, button))

# #Nose
# rtx.scene.append( Sphere(V3(0,1.5,-5), 0.2, carrot))

# #Smile
# rtx.scene.append( Sphere(V3(-0.5, 1.2, -5), 0.1, button))
# rtx.scene.append( Sphere(V3(-0.2, 1, -5), 0.1, button))
# rtx.scene.append( Sphere(V3(0.2, 1, -5), 0.1, button))
# rtx.scene.append( Sphere(V3(0.5, 1.2, -5), 0.1, button))

# #Eyes
# rtx.scene.append( Sphere(V3(-0.4, 1.8, -5), 0.1, button))
# rtx.scene.append( Sphere(V3(0.4, 1.8, -5), 0.1, button))


rtx.glRender()

rtx.glFinish("output.bmp")