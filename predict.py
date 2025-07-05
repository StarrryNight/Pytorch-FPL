import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense
import numpy as np
import torch
from torch import nn
from graphing import graphing
from linearRegressionModel import linearRegressionModel
from LossFunction import Lossfunction

def guess(train_x, train_y, test_x, test_y, evaluationMetric)-> list[list[int],list[int],list[str] ]:
    res= [[],[],[]]

    train_x['opponent_index'], train_x['result'] = 0,0
    test_x['opponent_index'], test_x['result'] = 0,0
    
    namesList = train_x['name']
    train_x = train_x[evaluationMetric]
    test_x = test_x[evaluationMetric]
    #remove ireelaventstuff

    #new parameters
     
    #write new variable using difference between home and away teams and Compute next week performance
    
    
    train_x_tensor = torch.from_numpy(train_x.values).float()
    train_y_tensor = torch.from_numpy(train_y.values).float()
    test_x_tensor = torch.from_numpy(test_x.values).float()
    test_y_tensor = torch.from_numpy(test_y.values).float()
    
    
    
    #Create instance of model
    model = linearRegressionModel(num = len(evaluationMetric))

    #Set up loss function and op

    optimizer = torch.optim.SGD(params=model.parameters(), lr=0.001)

    torch.manual_seed(69)
    epochs = 1000

    for epoch in range(epochs):
        model.train()
        y_pred = model(train_x_tensor)

        loss = Lossfunction.scaled_loss(y_pred, train_y_tensor, train_y_tensor)
        print(loss)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    

    
    with torch.inference_mode():   
        print(model.state_dict())
        result = model(test_x_tensor).reshape(len(test_y_tensor))
        graphing.graph(result, test_y)   
        return([result.numpy(), test_y_tensor.numpy(), namesList])
    
    
    




    

    # You can return int_predictions or use it as needed






   
    return res

#[target_dat.at[playerID,'xP'],target_dat.at[playerID,'bonus'], target_dat.at[playerID,'bps'], target_dat.at[playerID,'influence'], target_dat.at[playerID,'minutes' ], target_dat.at[playerID,'total_points'], target_dat.at[playerID,'opponent_index']] 