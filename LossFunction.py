import torch
from torch import nn

class Lossfunction():
    def scaled_loss(y_pred, y_true, X, base_loss_fn=nn.MSELoss(reduction='none')):
        loss = base_loss_fn(y_pred, y_true)  # shape: (batch,)
        scaling = torch.abs(X)+0.5           # scale by |X| or any function of X
        scaled = scaling * loss
        return scaled.mean()