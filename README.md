# 1D-2D-Hyperelastic-Problem-Solver

1-D Axial Bar (Solved using Linear Elastic Method):  

This is a creation of a Deep Learning Neural Network Model of 1-D Hyperelastic bar using the linear elastic method. It is a combination of Trapezoidal Integration and Deep Energy method to present a relationship between predicted and actual displacement of infinitely many points on the bar. The libraries used were NumPy, TensorFlow, matplotlib and time. This model basically uses Length of the Bar, Cross-sectional Area, Applied load, Young's Modulus and Number of Points on the bar to predict the displacemet. The overall results resemble the real life conditions near perfectly.


We introduce an innovative approach to address finite deformation hyperelasticity using deep neural networks (DNNs). This method eliminates the need for discretization techniques like the Finite Element Method (FEM). Instead, it directly minimizes the system's potential energy as a loss function. To train the DNNs, we calculate gradient loss through backpropagation and subsequently employ a standard optimizer for minimization. This training process determines the neural network's parameters, including weights and biases. Once the network is trained, it enables significantly faster numerical solutions compared to conventional methods relying on finite elements.

# What is Finite Element Analysis

In the fields of engineering and materials science, solving partial differential equations (PDEs) is crucial. Because these problems are getting more complex, people often use computational methods like the Finite Element Method (FEM) to come up with approximate solutions for PDEs.

## 1-D Bar Linear Elastic Method: 
It uses Feedforward Neural Network to solve finite elemnt model problems based on 1 dimensional bar using 1D Trapezoidal numerical INtegration method. The results of this mmodel have accuracy upto 95%. It uses backpropagation method to improve its accuracy.

## 1-D Axial Bar solution using strong form:
Strong form solution of the bar is nothing but the application of Trapezoidal integration & gradient method to calculate the slope of different variables and measure the difference in their actual and prdicted values.

## 1-D Axial Bar solution using weak form:
This module uses weak form method to evaluate all the variables for the 1-D bar.

## 2-D beams:
This module helps to solve 2 Dminesionsal Hyperelastic problems using Trapeziodal, Simpson's and Montecarlo methods of Numerical INtegration. This module is also an application of Feedforward Neural Networks where the method of integration is selected as per the number of intermediate points chosen within the bar to calculate the stresses, strains and the bending of the 2 dimensional beam.

## Beam Fixed on both ends:
This module uses the same methods as stated in 2 dimensional beams to solve the "hyperelastic loaded beam fixed on both the ends" problem.
