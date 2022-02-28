import numpy as np

def calculate(ls):
  '''Function that uses Numpy to return the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

  :param ls: list containing 9 digits (list)
  :return info: dictionary with the the mean, variance, standard deviation, max, min, and sum (dict)
  '''
  
  if len(ls) < 9:
    raise ValueError('List must contain nine numbers.')
    
  m = np.array(ls).reshape(3,3)

  
  info = {
    'mean': [m.mean(axis=0).tolist(),
             m.mean(axis=1).tolist(), 
             m.mean().tolist()],
    'variance': [m.var(axis=0).tolist(),
                 m.var(axis=1).tolist(),
                 m.var().tolist()],
    'standard deviation':[m.std(axis=0).tolist(),
                          m.std(axis=1).tolist(),
                          m.std().tolist()],
    'max': [m.max(axis=0).tolist(),
           m.max(axis=1).tolist(), 
           m.max().tolist()],
    'min': [m.min(axis=0).tolist(),
            m.min(axis=1).tolist(), 
            m.min().tolist()],
    'sum': [m.sum(axis=0).tolist(),
            m.sum(axis=1).tolist(), 
            m.sum().tolist()]
  }
  return info