import joblib
import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms

memory = joblib.memory.Memory("./cache", mmap_mode="r", verbose=0)

NUM_CHANNELS = 1
IMG_HEIGHT = 64
IMG_WIDTH = 256
toTensor = transforms.ToTensor()

################################# Image preprocessing:

def preprocess_image_from_file(path):
    x = Image.open(path).convert("L")  # Convert to grayscale
        
    # Resize (preserving aspect ratio)
    new_width = int(
        IMG_HEIGHT * x.size[0] / x.size[1]
    )
    x = x.resize((new_width, IMG_HEIGHT))    
    x = toTensor(x)  # Convert to tensor (normalizes to [0, 1])
    #print(x.shape)
    #sys.exit()
    return x

################################# CTC Preprocessing:

def pad_batch_images(x):
    max_width = max(x, key=lambda sample: sample.shape[2]).shape[2]
    x = torch.stack([F.pad(i, pad=(0, max_width - i.shape[2])) for i in x], dim=0)
    return x

def ctc_batch_preparation(batch):
    x, xl = zip(*batch)
    # Zero-pad images to maximum batch image width
    x = pad_batch_images(x)
    xl = torch.tensor(xl, dtype=torch.int32)
    return x, xl