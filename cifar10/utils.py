import torch
import torch.nn as nn

class Trainer():
    def __init__(self, model, train_loader, test_loader, optimizer, criterion, device):
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device

    def train(self, epochs):

        losses = []
        for epoch in range(epochs):
            self.model.train()
            for images, labels in self.train_loader:
                images, labels = images.to(self.device), labels.to(self.device)
                self.optimizer.zero_grad()
                output = self.model(images)
                loss = self.criterion(output, labels)
                losses.append(loss.item())
                loss.backward()
                self.optimizer.step()
            
            print(f"Epoch {epoch+1} / {epochs} | Loss: {loss.item()}")

    def test(self):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in self.test_loader:
                images, labels = images.to(self.device), labels.to(self.device)
                outputs = self.model(images)

                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        test_accuracy = 100 * correct / total
        print(f"Test Accuracy: {test_accuracy}%")
        return test_accuracy
