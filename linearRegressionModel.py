import torch
from torch import nn
class linearRegressionModel(nn.Module):
    def __init__(self, num:int, *args, **kwargs,):
        super().__init__()
        self.linear = nn.Linear(num, 1)
    
    def forward(self, x: torch.Tensor) -> torch.tensor:
        return self.linear(x)