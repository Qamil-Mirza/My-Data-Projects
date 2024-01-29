# import the classes from the model.py file and the utils.py file
from model import CNN
from utils import DigitDataLoader



# Here we write the main function which is the logic for preprocessing, training, and testing the model.

def main():
    data_loader = DigitDataLoader()
    train_data, train_labels, test_data, test_labels = data_loader.load_data()

    model = CNN()
    history = model.train(train_data, train_labels, epochs=10, batch_size=32, want_callbacks=True)
    model.evaluate(test_data, test_labels)


if __name__ == "__main__":
    main()