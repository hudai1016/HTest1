import numpy as np
import theano
import theano.tensor as T
def Layer(object):
    def __init__(self,input,in_size,out_size,activation_function=None):
        self.W=theano.shared(np.random.normal(0,1,(in_size,out_size)))
        self.b=theano.shared(np.zeros((out_size,)+0.1))
