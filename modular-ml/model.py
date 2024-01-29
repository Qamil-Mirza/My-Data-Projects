import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

class CNN():
    def __init__(self):
        self.model = self._build()

    def _build(self):
        model = models.Sequential()

        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.25))

        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Dropout(0.25))

        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Flatten())
        model.add(layers.Dropout(0.5))

        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Dropout(0.5))

        model.add(layers.Dense(10, activation='softmax'))

        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        return model
    
    def train(self, train_data, train_labels, epochs=10, batch_size=32, want_callbacks=True):
        # define callbacks 
        if want_callbacks == True:
            es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)
            mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
            callbacks = [es, mc]
        else:
            callbacks = None

        history = self.model.fit(train_data, train_labels, epochs=epochs, 
                                 batch_size=batch_size, callbacks=callbacks, 
                                 validation_split=0.2)
        return history
    
    def evaluate(self, test_data, test_labels):
        test_loss, test_acc = self.model.evaluate(test_data, test_labels)
        print(f"Test accuracy: {test_acc}")
