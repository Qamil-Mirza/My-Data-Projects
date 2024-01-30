import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(16, 32, 3, stride=1, padding=1)
        self.fc1 = nn.Linear(32*8*8, 256)  # 32*8*8 from image dimension
        self.fc2 = nn.Linear(256, 10) # 10 classes for CIFAR-10

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x))) # feed through conv1, relu, and pool | x.shape = (batch_size, 16, 16, 16)
        x = self.pool(self.relu(self.conv2(x))) # feed through conv2, relu, and pool | x.shape = (batch_size, 32, 8, 8)
        x = x.view(-1, 32*8*8) # flatten the tensor | x.shape = (batch_size, 32*8*8)
        x = self.relu(self.fc1(x)) # feed through fc1 and relu 
        x = self.fc2(x)
        return x