### Auto-generated code ###

from OpenGL.GL import *
import PIL.Image

def rocky_robot_body_frame():

    materials = {}
    image = PIL.Image.open('images/rock.jpeg')
    image = image.tostring('raw', 'RGBX', 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 502, 505, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    materials['Material.001'] = texture_id
    
    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glBindTexture(GL_TEXTURE_2D, materials['Material.001'])
    glColor([1.0, 1.0, 1.0])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, -0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.807, -1.007])
    glNormal3fv([0.0, 1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.293, 0.807, -1.007])
    glNormal3fv([0.0, 1.0, -0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.293, 0.807, -0.493])
    glNormal3fv([0.0, 1.0, -0.0])
    glTexCoord2fv([0.0, 1.0])
    glVertex3fv([0.807, 0.807, -0.493])
    glEnd()
    glColor([0.281226, 0.094747, 0.233503])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -1.007])
    glNormal3fv([0.0, -1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -0.493])
    glNormal3fv([0.0, -1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -0.493])
    glNormal3fv([0.0, -1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -1.007])
    glEnd()
    glColor([0.281226, 0.094747, 0.233503])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -1.007])
    glNormal3fv([1.0, 0.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.807, -1.007])
    glNormal3fv([1.0, 0.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.807, -0.493])
    glNormal3fv([1.0, 0.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -0.493])
    glEnd()
    glColor([0.281226, 0.094747, 0.233503])
    glBegin(GL_POLYGON)
    glNormal3fv([-0.0, -0.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -0.493])
    glNormal3fv([-0.0, -0.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.807, -0.493])
    glNormal3fv([-0.0, -0.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.807, -0.493])
    glNormal3fv([-0.0, -0.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -0.493])
    glEnd()
    glColor([0.281226, 0.094747, 0.233503])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, -0.0, -0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -0.493])
    glNormal3fv([-1.0, -0.0, -0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.807, -0.493])
    glNormal3fv([-1.0, -0.0, -0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.807, -1.007])
    glNormal3fv([-1.0, -0.0, -0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -1.007])
    glEnd()
    glColor([0.281226, 0.094747, 0.233503])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.807, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.807, 0.293, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.293, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.293, 0.807, -1.007])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.6, 0.807, 0.0])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.6, 0.807, -0.49])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.6, 0.293, -0.49])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.6, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6, 0.807, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.8, 0.807, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.8, 0.293, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6, 0.293, -0.49])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.8, 0.807, -0.49])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.8, 0.807, 0.0])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.8, 0.293, 0.0])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.8, 0.293, -0.49])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.8, 0.807, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6, 0.807, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6, 0.293, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.8, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6, 0.293, 0.0])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6, 0.293, -0.49])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.8, 0.293, -0.49])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.8, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.8, 0.807, 0.0])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.8, 0.807, -0.49])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6, 0.807, -0.49])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6, 0.807, 0.0])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.83, 0.68, -0.493])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.83, 0.68, -1.007])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.83, 0.42, -1.007])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.83, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.83, 0.68, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.93, 0.68, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.93, 0.42, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.83, 0.42, -1.007])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.93, 0.68, -1.007])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.93, 0.68, -0.493])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.93, 0.42, -0.493])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.93, 0.42, -1.007])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.93, 0.68, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.83, 0.68, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.83, 0.42, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.93, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.83, 0.42, -0.493])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.83, 0.42, -1.007])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.93, 0.42, -1.007])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.93, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.309111, 0.605616])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.93, 0.68, -0.493])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.93, 0.68, -1.007])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.83, 0.68, -1.007])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.83, 0.68, -0.493])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.17, 0.68, -0.493])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.17, 0.68, -1.007])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.17, 0.42, -1.007])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.17, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.17, 0.68, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.27, 0.68, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.27, 0.42, -1.007])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.17, 0.42, -1.007])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.27, 0.68, -1.007])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.27, 0.68, -0.493])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.27, 0.42, -0.493])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.27, 0.42, -1.007])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.27, 0.68, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.17, 0.68, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.17, 0.42, -0.493])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.27, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.17, 0.42, -0.493])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.17, 0.42, -1.007])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.27, 0.42, -1.007])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.27, 0.42, -0.493])
    glEnd()
    glColor([0.64, 0.339886, 0.578888])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.27, 0.68, -0.493])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.27, 0.68, -1.007])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.17, 0.68, -1.007])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.17, 0.68, -0.493])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.3, 0.807, 0.0])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.3, 0.807, -0.49])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.3, 0.293, -0.49])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.3, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.3, 0.807, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.5, 0.807, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.5, 0.293, -0.49])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.3, 0.293, -0.49])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.5, 0.807, -0.49])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.5, 0.807, 0.0])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.5, 0.293, 0.0])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.5, 0.293, -0.49])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.5, 0.807, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.3, 0.807, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.3, 0.293, 0.0])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.5, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.3, 0.293, 0.0])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.3, 0.293, -0.49])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.5, 0.293, -0.49])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.5, 0.293, 0.0])
    glEnd()
    glColor([0.64, 0.221496, 0.558292])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.5, 0.807, 0.0])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.5, 0.807, -0.49])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.3, 0.807, -0.49])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.3, 0.807, 0.0])
    glEnd()
    glEndList()

    return gl_list

def rocky_robot_head_frames(animation):

    frames = []

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    if not animation: return frames

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.047372])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.304372])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.304372])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.047372])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.304372])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.304372])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.304372])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.304372])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.304372])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.047372])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.047372])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.304372])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.047372])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.047372])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.047372])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.047372])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.047372])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.304372])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.304372])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.047372])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.047372])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.304372])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.304372])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.047372])
    glEnd()
    glEndList()
    
    frames.append(gl_list)
    
    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0575])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3145])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3145])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0575])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.3145])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.3145])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.3145])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.3145])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3145])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0575])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0575])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3145])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.0575])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.0575])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.0575])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.0575])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0575])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3145])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3145])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0575])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0575])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3145])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3145])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0575])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.067628])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.324628])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.324628])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.067628])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.324628])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.324628])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.324628])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.324628])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.324628])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.067628])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.067628])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.324628])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.067628])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.067628])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.067628])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.067628])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.067628])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.324628])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.324628])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.067628])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.067628])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.324628])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.324628])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.067628])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0715])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3285])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3285])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0715])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.3285])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.3285])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.3285])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.3285])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3285])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0715])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0715])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3285])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.0715])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.0715])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.0715])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.0715])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0715])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3285])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3285])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0715])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0715])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3285])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3285])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0715])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.069011])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.326011])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.326011])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.069011])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.326011])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.326011])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.326011])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.326011])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.326011])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.069011])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.069011])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.326011])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.069011])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.069011])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.069011])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.069011])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.069011])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.326011])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.326011])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.069011])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.069011])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.326011])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.326011])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.069011])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.062001])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.319001])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.319001])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.062001])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.319001])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.319001])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.319001])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.319001])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.319001])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.062001])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.062001])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.319001])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.062001])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.062001])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.062001])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.062001])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.062001])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.319001])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.319001])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.062001])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.062001])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.319001])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.319001])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.062001])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.052999])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.309999])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.309999])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.052999])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.309999])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.309999])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.309999])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.309999])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.309999])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.052999])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.052999])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.309999])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.052999])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.052999])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.052999])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.052999])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.052999])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.309999])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.309999])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.052999])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.052999])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.309999])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.309999])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.052999])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.045989])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.302989])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.302989])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.045989])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.302989])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.302989])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.302989])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.302989])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.302989])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.045989])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.045989])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.302989])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.045989])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.045989])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.045989])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.045989])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.045989])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.302989])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.302989])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.045989])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.045989])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.302989])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.302989])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.045989])
    glEnd()
    glEndList()
    
    frames.append(gl_list)

    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glNormal3fv([-1.0, 0.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glNormal3fv([0.0, 0.0, -1.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glNormal3fv([1.0, 0.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glNormal3fv([0.0, 0.0, 1.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.0435])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.4215, 0.393, -1.3005])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.3005])
    glNormal3fv([0.0, -1.0, 0.0])
    glVertex3fv([0.6785, 0.393, -1.0435])
    glEnd()
    glColor([0.64, 0.2216, 0.5584])
    glBegin(GL_POLYGON)
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.0435])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.6785, 0.707, -1.3005])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.3005])
    glNormal3fv([0.0, 1.0, 0.0])
    glVertex3fv([0.4215, 0.707, -1.0435])
    glEnd()
    glEndList()
    
    frames.append(gl_list)
    
    return frames