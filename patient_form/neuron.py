from numpy import exp, array, dot, random
class NeuralNetwork():
    """Класс для нейронной сети"""

    def __init__(self):
        random.seed(1) #изменяет число для генерации
        """Инициализировали генератор случайных чисел"""

        self.synaptic_weights = 2 * random.random((7, 1)) - 1 # числа генерятся в промежутке от [-1:1), в общем виде: (b - a) * random_sample() + a

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output #ошибку вычисляем как разность между желаемым(известным) выходом и полученным

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            self.synaptic_weights = self.synaptic_weights + adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights)) #возможно проблемка здесь
