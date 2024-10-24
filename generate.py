import pyrosim.pyrosim as ps

# Global parameters
l = 1 # length
w = 1 # width 
h = 1 # height 

x = 0
y = 0
z = 0

def Create_World():
    ps.Start_SDF("box.sdf")
    global z, l, w, h
    for i in range(10):
        ps.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])
        z += h
        l = 0.9 * l
        w = 0.9 * w
        h = 0.9 * h
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")
    
    foot_position = [x, y, z]
    torso_position = [x, y, z + 1] 
    head_position = [x, y, z + 2]  

    ps.Send_Cube(name="Foot", pos=foot_position, size=[1, 1, 2]) 
    
    ps.Send_Cube(name="Torso", pos=torso_position, size=[3, 1, 1])

    ps.Send_Joint(name="Foot_Torso", 
                 parent="Torso", 
                 child="Foot", 
                 type="revolute", 
                 position=[0, 0, 0])

   
    ps.Send_Cube(name="Head", pos=head_position, size=[1, 1, 1])
    
    
    ps.Send_Joint(name="Head_Torso", 
                 parent="Head", 
                 child="Torso", 
                 type="revolute", 
                 position=[0, 0, 0])
    
    ps.End()

# Create_World()
Create_Robot()
