import numpy as np
from vispy.util import transforms as tr
from vispy import io

np.set_printoptions(suppress=True, precision=2)

def make_model_matrix(translate, rotation, scale):
    '''
    Returns a 4x4 model matrix.

    Arguments:
        -translation: x, y, z coordinates
        -rotation: x,y,z rotations (degrees)
        -scale: x,y,z scale.

    Returns:
        -model_matrix: 4x4 Numpy Array
    '''
    rx, ry, rz = rotation
    sm = tr.scale(scale).T
    rzm = tr.rotate(rz, [0, 0, 1]).T
    rym = tr.rotate(rz, [0, 1, 0]).T
    rxm = tr.rotate(rz, [1, 0, 0]).T
    trm = tr.translate(translate).T
    mm = trm @ rxm @ rym @ rzm @ sm
    print(mm)
    return mm

mm = make_model_matrix([1 ,2 , 3], [90, 45, 0], [2, 2, 2])
print(mm)

mesh_cyl = io.read_mesh("cylinder.obj")
vertices, faces, normals, texcoords = io.read_mesh("monkey.obj")

print(a)

assert len(vertices[0]) == 3, "Vertices are 3D!"
