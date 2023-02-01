import torch

class Identity(torch.nn.Module):
    def forward(self, x):
        return x

def init():
    global model
    model = Identity()

