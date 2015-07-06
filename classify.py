from matplotlib.pyplot import figure, show
# import pickle

from classes import *
from MNIST import imagelist

# def store_data():
# 	train0 = imagelist(0, 'data/train0.jpg')
# 	train1 = imagelist(1, 'data/train1.jpg')
# 	train2 = imagelist(2, 'data/train2.jpg')
# 	train3 = imagelist(3, 'data/train3.jpg')
# 	train4 = imagelist(4, 'data/train4.jpg')
# 	train5 = imagelist(5, 'data/train5.jpg')
# 	train6 = imagelist(6, 'data/train6.jpg')
# 	train7 = imagelist(7, 'data/train7.jpg')
# 	train8 = imagelist(8, 'data/train8.jpg')
# 	train9 = imagelist(9, 'data/train9.jpg')

# 	test0 = imagelist(0, 'data/test0.jpg')
# 	test1 = imagelist(1, 'data/test1.jpg')
# 	test2 = imagelist(2, 'data/test2.jpg')
# 	test3 = imagelist(3, 'data/test3.jpg')
# 	test4 = imagelist(4, 'data/test4.jpg')
# 	test5 = imagelist(5, 'data/test5.jpg')
# 	test6 = imagelist(6, 'data/test6.jpg')
# 	test7 = imagelist(7, 'data/test7.jpg')
# 	test8 = imagelist(8, 'data/test8.jpg')
# 	test9 = imagelist(9, 'data/test9.jpg')

# 	with open('data/train.pickle', 'w') as f:
# 		pickle.dump([train0, train1, train2, train3, train4, train5, train6, train7, train8, train9], f)

# 	with open('data/test.pickle', 'w') as f:
# 		pickle.dump([test0, test1, test2, test3, test4, test5, test6, test7, test8, test9], f)

# def retrieve_data():
# 	with open('data/train.pickle') as f:
# 		train0, train1, train2, train3, train4, train5, train6, train7, train8, train9 = pickle.load(f)

# 	with open('data/test.pickle') as f:
# 		test0, test1, test2, test3, test4, test5, test6, test7, test8, test9 = pickle.load(f)

if __name__ == '__main__':

	title_font = {'fontname':'Arial', 'size':'12', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'}
	axis_font = {'fontname':'Arial', 'size':'12'}

	train0 = imagelist(0, 'data/train0.jpg')
	train1 = imagelist(1, 'data/train1.jpg')

	test0 = imagelist(0, 'data/test0.jpg')
	test1 = imagelist(1, 'data/test1.jpg')

	class0 = Classifier(train0[0:10], iterations=800)
	class0.test(train0[0:10])

	print "class0(test0): ", class0.classification
	print "TP: ", class0.TP
	print "FP: ", class0.FP
	print "TN: ", class0.TN
	print "FN: ", class0.FN

	fig00 = figure()
	ax00 = fig00.add_subplot(111)
	
	time = range(0, len(train0[0].encoded_data))
	voltage00 = [class0.temp.V(t) for t in time]

	ax00.plot(time, voltage00)
	ax00.set_ylabel('Voltage (mV)', **axis_font)
	ax00.set_xlabel('Time (ms)', **axis_font)

	#-----------

	class0.test(train1[0:10])

	print "class0(test1): ", class0.classification
	print "TP: ", class0.TP
	print "FP: ", class0.FP
	print "TN: ", class0.TN
	print "FN: ", class0.FN

	fig01 = figure()
	ax01 = fig01.add_subplot(111)
	
	voltage01 = [class0.temp.V(t) for t in time]

	ax01.plot(time, voltage01)
	ax01.set_ylabel('Voltage (mV)', **axis_font)
	ax01.set_xlabel('Time (ms)', **axis_font)

	class1 = Classifier(train1[0:10], iterations=800)
	class1.test(train1[0:10])

	print "class1(test1): ", class1.classification
	print "TP: ", class1.TP
	print "FP: ", class1.FP
	print "TN: ", class1.TN
	print "FN: ", class1.FN

	fig11 = figure()
	ax11 = fig11.add_subplot(111)
	
	voltage11 = [class1.temp.V(t) for t in time]

	ax11.plot(time, voltage11)
	ax11.set_ylabel('Voltage (mV)', **axis_font)
	ax11.set_xlabel('Time (ms)', **axis_font)

	class1.test(train0[0:10])

	print "class1(test0): ", class1.classification
	print "TP: ", class1.TP
	print "FP: ", class1.FP
	print "TN: ", class1.TN
	print "FN: ", class1.FN

	fig10 = figure()
	ax10 = fig10.add_subplot(111)
	
	voltage10 = [class0.temp.V(t) for t in time]

	ax10.plot(time, voltage10)
	ax10.set_ylabel('Voltage (mV)', **axis_font)
	ax10.set_xlabel('Time (ms)', **axis_font)

	#-----

	spiketrain = figure()
	stax = spiketrain.add_subplot(111)
	
	time = range(0, len(train0[0].encoded_data))
	input0 = train0[0].encoded_data

	stax.plot(time, input0)
	stax.set_ylabel('spike', **axis_font)
	stax.set_xlabel('pixel number', **axis_font)

	show()

	"http://cs.nyu.edu/~roweis/data.html"