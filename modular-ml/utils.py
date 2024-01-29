from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

class DigitDataLoader():
    @staticmethod
    def load_data():
        (train_data, train_labels), (test_data, test_labels) = mnist.load_data()
        train_data = train_data.reshape((60000, 28, 28, 1))
        train_data = train_data.astype('float32') / 255
        test_data = test_data.reshape((10000, 28, 28, 1))
        test_data = test_data.astype('float32') / 255
        train_labels = to_categorical(train_labels)
        test_labels = to_categorical(test_labels)
        return train_data, train_labels, test_data, test_labels
    
