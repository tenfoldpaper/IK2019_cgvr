import numpy as np
from vispy.util import transforms as tr
from vispy import io

np.set_printoptions(suppress=True, precision=2)

class Mesh:
    
    def __init__(self, obj_filename, pos, rot, scl):

        vertices, faces, normals, textcoords = io.read_mesh("monkey.obj")
        assert len(vertices[0]) == 3, "Vertices are 3D!"
        assert len(faces[0]) == 3, "Mesh must be triangulated!"
        self.vertices = vertices
        self.faces = faces
        self.normals = normals
        self.textcoords = textcoords
        self.position = pos
        self.rotation = rot
        self.scale = scl
    
    @property
    def model_matrix(self):
        '''
        Returns a 4x4 model matrix.

        Arguments:
            -translation: x, y, z coordinates
            -rotation: x,y,z rotations (degrees)
            -scale: x,y,z scale.

        Returns:
            -model_matrix: 4x4 Numpy Array
        '''
        rx, ry, rz = self.rotation
        sm = tr.scale(self.scale).T
        rzm = tr.rotate(rz, [0, 0, 1]).T
        rym = tr.rotate(rz, [0, 1, 0]).T
        rxm = tr.rotate(rz, [1, 0, 0]).T
        trm = tr.translate(self.position).T
        mm = trm @ rxm @ rym @ rzm @ sm
        return mm
    
monkey = Mesh('monkey.obj', pos=[10, 2, 3], rot=[90, 45, 0], scl=[2, 2, 2])
monkey.vertices
monkey.faces
#monkey.send()
#monkey.draw()

