# 1D-2D-Hyperelastic-Problem-Solver

1-D Axial Bar (Solved using Linear Elastic Method): \n
This is a creation of a Deep Learning Neural Network Model of 1-D Hyperelastic bar using the linear elastic method. It is a combination of Trapezoidal Integration and Deep Energy method to present a relationship between predicted and actual displacement of infinitely many points on the bar. The libraries used were NumPy, TensorFlow, matplotlib and time. This model basically uses Length of the Bar, Cross-sectional Area, Applied load, Young's Modulus and Number of Points on the bar to predict the displacemet. The overall results resemble the real life conditions near perfectly.


We introduce an innovative approach to address finite deformation hyperelasticity using deep neural networks (DNNs). This method eliminates the need for discretization techniques like the Finite Element Method (FEM). Instead, it directly minimizes the system's potential energy as a loss function. To train the DNNs, we calculate gradient loss through backpropagation and subsequently employ a standard optimizer for minimization. This training process determines the neural network's parameters, including weights and biases. Once the network is trained, it enables significantly faster numerical solutions compared to conventional methods relying on finite elements.

# What is Finite Element Analysis

In the fields of engineering and materials science, solving partial differential equations (PDEs) is crucial. Because these problems are getting more complex, people often use computational methods like the Finite Element Method (FEM) to come up with approximate solutions for PDEs.
