import numpy as np

def calculate(list):
    if len(list) != 9: 
        return "List must contain nine numbers."
    else:
        list = np.array(list).reshape(3,3) 
        calculations = {"mean" : [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.flatten().mean().tolist()],
                        "variance" : [list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.flatten().var().tolist()],
                        "standart deviation" : [list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.flatten().std().tolist()],
                        "max" : [list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.flatten().max().tolist()],
                        "min" : [list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.flatten().min().tolist()],
                        "sum" : [list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.flatten().sum().tolist()]
                        }
    return calculations