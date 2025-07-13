import torch

print("PyTorch версия:", torch.__version__)
print("CUDA доступна:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Количество GPU:", torch.cuda.device_count())
    print("Текущее GPU:", torch.cuda.current_device())
    print("Имя GPU:", torch.cuda.get_device_name(0))
else:
    print("CUDA недоступна")