import polyscope as ps, gpytoolbox as gpy

gpy.write_mesh("wingnut.obj", V, F)
ps.show()