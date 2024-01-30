from model import CNN
from utils import Trainer
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

def main():
    # set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # set transformations
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # download and load cifar10 dataset
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

    # create dataloaders
    train_loader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True, num_workers=2)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False, num_workers=2)

    # create model
    model = CNN().to(device)

    # define criterion and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    # create trainer
    trainer = Trainer(model, train_loader, test_loader, optimizer, criterion, device)
    trainer.train(epochs=30)

    # test model
    test_accuracy = trainer.test()

    return test_accuracy

if __name__ == "__main__":
    main()