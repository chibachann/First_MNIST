import torch

# Check if CUDA is available
print(torch.__version__)
train_on_gpu = torch.cuda.is_available()
print(f'Train on GPU: {train_on_gpu}')
