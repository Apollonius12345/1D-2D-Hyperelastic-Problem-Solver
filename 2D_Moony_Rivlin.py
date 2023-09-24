from dolfin import *
import fenics as fe
import time

start_time = time.time()

# Optimization options for the form compiler
parameters["form_compiler"]["cpp_optimize"] = True
ffc_options = {"optimize": True, "eliminate_zeros": True, "precompute_basis_const": True, "precompute_ip_const": True}

# Create mesh and define function space
mesh = RectangleMesh(Point(0.0, 0.0), Point(4.0, 1.0), 200, 50, "crossed")
V = VectorFunctionSpace(mesh, "Lagrange", 2)

# Define Dirichlet boundary
left_boundary = CompiledSubDomain("near(x[0], side) && on_boundary", side=0.0, tol=10e-15)
bcs = DirichletBC(V, Expression(("0.0", "0.0"), degree=2), left_boundary)

# Define functions and kinematics
du = TrialFunction(V)
v = TestFunction(V)
u = Function(V)
d = u.geometric_dimension()
I = Identity(d)
F = I + grad(u)
C = F.T * F
J = det(F)

# Elasticity parameters
c1 = Constant(630)
c2 = Constant(-1.2)
c = Constant(100)
d = 2 * (c1 + 2 * c2)

# Strain energy density
psi = c * (J - 1) ** 2 - d * ln(J) + c1 * (tr(C) - 2) + c2 * (0.5 * (tr(C) ** 2 - tr(C * C) - 1))

# Total potential energy
Pi = psi * dx - dot(Expression(("0.0", "-10.0"), degree=2), u) * ds(1)

# Compute first variation of Pi
F = derivative(Pi, u, v)

# Compute Jacobian of F
J = derivative(F, u, du)
problem = NonlinearVariationalProblem(F, u, bcs, J)
solver = NonlinearVariationalSolver(problem)
prm = solver.parameters
prm['newton_solver']['linear_solver'] = 'petsc'
solver.solve()

# Save solution in VTK format
file = File("./output/fem/mooneyrivlin/beam2d_4x1_fem_v1.pvd")
file << u

# Compute norms
L2_norm = norm(u, norm_type="L2")
H1_norm = norm(u, norm_type="H1")
H10_norm = norm(u, norm_type="H10")
energy_norm = sqrt(assemble(psi * dx))

print(f"L2 norm = {L2_norm:.10f}")
print(f"H1 norm = {H1_norm:.10f}")
print(f"H10 norm = {H10_norm:.10f}")
print(f"Energy norm = {energy_norm:.10f}")
print(f"Running time = {time.time() - start_time:.3f}")

# Plot solution and stress intensity
plot(u, title='Displacement', mode='displacement')
F = I + grad(u)
C = F.T * F
J = sqrt(det(C))
I1 = tr(C)
I2 = 0.5 * (I1 ** 2 - tr(C * C))
second_Piola = (2 * c1 + 2 * c2 * I1) * I - 2 * c2 * C.T + (2 * c * (J - 1) * J - d) * inv(C.T)
S_dev = second_Piola - (1. / 3) * tr(second_Piola) * I
von_Mises = sqrt(3. / 2 * inner(S_dev, S_dev))
V = FunctionSpace(mesh, "Lagrange", 2)
W = TensorFunctionSpace(mesh, "Lagrange", 2)
von_Mises = project(von_Mises, V)
Stress = project(second_Piola, W)
plot(von_Mises, title='Stress intensity')

# Compute magnitude of displacement
u_magnitude = sqrt(dot(u, u))
u_magnitude = project(u_magnitude, V)
plot(u_magnitude, 'Displacement magnitude')

# Save results to VTK files
File('./output/fem/elasticity/mooneyrivlin/displacement.pvd') << u
File('./output/fem/elasticity/mooneyrivlin/von_mises.pvd') << von_Mises
File('./output/fem/elasticity/mooneyrivlin/magnitude.pvd') << u_magnitude
File('./output/fem/elasticity/mooneyrivlin/stress.pvd') << Stress
