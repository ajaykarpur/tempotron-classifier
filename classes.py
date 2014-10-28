import math as m
import numpy as np
import random
from PIL import Image
from sklearn import decomposition
from skimage import filter as filt

class Classifier(object):

	def __init__(self, traindata, layers = 1):
		self.traindata = traindata
		self.testdata = None

		self.temp = Tempotron(len(traindata[0].data))

		self.classify()

		self.classification = []
		self.TP = 0
		self.FP = 0
		self.TN = 0
		self.FN = 0

	def classify(self):

		for image in self.traindata:
			self.temp.train(image.data)

	def test(self, testdata):

		self.testdata = testdata

		self.classification = []
		self.TP = 0
		self.FP = 0
		self.TN = 0
		self.FN = 0

		for image in testdata:
			result = self.temp.test(image.data)
			if (result == 1):
				if (image.digit == self.traindata[0].digit):
					self.TP += 1
				else:
					self.FP += 1
			else:
				if (image.digit == self.traindata[0].digit):
					self.FN += 1
				else:
					self.TN += 1

			self.classification.append(result)

class MNISTImage(object):

	def __init__(self, digit, image, data=None):
		self.digit = digit
		self.image = image
		self.data = data
		# self.encoded_data = self.encode()

	def encode(self):

		data_array = np.array(self.data).reshape((28,28))

		edges = filt.canny(data_array, sigma=3)

		def linear_mapping(data): # using principal components analysis
			pca = decomposition.PCA(n_components=1)
			pca.fit(data)
			mapping = pca.transform(data)

			return mapping

		return linear_mapping(edges)

class Tempotron(object):

	def __init__(self, length, Cm=4.9, Vreset=-63., Vthresh=-55., Vrest=-58., V0=2.12, Erev=-80., El=-58., gl=.02):
		self.Vreset = float(Vreset) # mV
		self.Vthresh = float(Vthresh) # mV
		self.Vrest = float(Vrest) # mV
		self.V0 = float(V0)
		self.Erev = float(Erev) # mV
		self.El = float(El) # mV
		self.gl = float(gl) # uS

		self.length = length

		# self.Rm = 1/gl
		# self.taum = Cm*self.Rm

		self.tau = 15 # in ms
		self.taus = self.tau/4

		self.weights = [random.random()]*length # initialize with randomly assigned weights

	def __PSP(self, t):

		return self.V0*(m.exp(-t/self.tau) - m.exp(-t/self.taus))

	def V(self, t):

		return self.weights[t]*(self.__PSP(t) + self.Vrest)

	def __cost(self, t):
		Vthresh = self.Vthresh
		spike = data[t]
		tmax = self.length - 1

		if (spike == 1):
			return Vthresh - self.V(tmax)
		elif (spike == 0):
			return self.V(tmax) - Vthresh

	def __syn_update(self, t, maxsize=.00008):

		tmax = self.length - 1
		return maxsize*self.__PSP(tmax - t)

	def train(self, data):

		for t, d in enumerate(data):
			self.weights[t] += self.__syn_update(t)

	def test(self, data):

		for t, d in enumerate(data):
			if (abs(self.V(t)) > abs(self.Vthresh)):
				return 1
		return 0