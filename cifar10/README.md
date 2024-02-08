# CIFAR10 Classification With Pytorch
Here I try to implement a model to classify images in the cifar-10 dataset with PyTorch, a library which I have no experience in. The ultimate goal of this small project is not to develop a really accurate model. I'm actually more focused on developing my own intuition and understanding for how PyTorch works in relation to TensorFlow and Keras. As such, model accuracy will play a secondary role here.

I may or may not try implementing other models to see how they perform. We'll see how it pans out AHAHAHHA. Here's a breakdown of each file:

main.py: Executable file for data loading, model training and model evaluation
model.py: Acts as model development file for modularity
utils.py: Acts as the file to define the training class which carries out the training and testing logic
test.ipynb: A rough run of the end to end process for model creation before modularizing the code