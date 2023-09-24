# 1D-2D-Hyperelastic-Problem-Solver

We introduce an innovative approach to address finite deformation hyperelasticity using deep neural networks (DNNs). This method eliminates the need for discretization techniques like the Finite Element Method (FEM). Instead, it directly minimizes the system's potential energy as a loss function. To train the DNNs, we calculate gradient loss through backpropagation and subsequently employ a standard optimizer for minimization. This training process determines the neural network's parameters, including weights and biases. Once the network is trained, it enables significantly faster numerical solutions compared to conventional methods relying on finite elements.

# What is Finite Element Analysis

In the fields of engineering and materials science, solving partial differential equations (PDEs) is crucial. Because these problems are getting more complex, people often use computational methods like the Finite Element Method (FEM) to come up with approximate solutions for PDEs.
