import gpytoolbox as gpy, polyscope as ps
ps.init()
V,F = gpy.read_mesh("data/penguin.obj")
ps_penguin = ps.register_surface_mesh("penguin", V, F)


V,F = gpy.icosphere(2)
ps.register_surface_mesh("sphere", V, F)
ps.show()