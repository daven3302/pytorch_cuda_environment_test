import torch
tensor = torch.Tensor()
tensor = tensor.to('cuda')
name = tensor.device
print(torch.cuda.get_device_name(name))