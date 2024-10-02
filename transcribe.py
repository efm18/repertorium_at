import gc
import os
import random

import fire
import numpy as np
import torch
from lightning.pytorch import Trainer
from lightning.pytorch.loggers.wandb import WandbLogger
from torch.utils.data import DataLoader

from data.config import DS_CONFIG
from my_utils.dataset import CTCDataset
from models.model import CTCTrainedCRNN
from models.model import LightningE2EModelUnfolding

# Seed
random.seed(42)
np.random.seed(42)
torch.manual_seed(42)

# Deterministic behavior
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True


def test(
    ds_name,
    checkpoint_path,
    encoding_type="char",
    ctc="greedy"
):
    gc.collect()
    torch.cuda.empty_cache()

    # Check if checkpoint path exists
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(f"Checkpoint path {checkpoint_path} does not exist")

    # Check if dataset exists
    if ds_name not in DS_CONFIG.keys():
        raise NotImplementedError(f"Test dataset {ds_name} not implemented")

    # Dataset
    test_ds = CTCDataset(
        name=ds_name,
        img_folder=DS_CONFIG[ds_name]["images"],
        encoding_type=encoding_type,
    )
    test_loader = DataLoader(
        test_ds, batch_size=1, shuffle=False, num_workers=20
    )  # prefetch_factor=2

    # Model
    if ds_name == "aligned":
        model = LightningE2EModelUnfolding.load_from_checkpoint(
            checkpoint_path, ctc=ctc, ytest_i2w=test_ds.i2w
        )
    else:    
        model = CTCTrainedCRNN.load_from_checkpoint(
            checkpoint_path, ctc=ctc, ytest_i2w=test_ds.i2w, ds_name=ds_name
        )
    model.freeze()

    # Test: automatically auto-loads the best weights from the previous run
    trainer = Trainer(
        precision="16-mixed",
    )
    trainer.test(model, dataloaders=test_loader)    


if __name__ == "__main__":
    fire.Fire(test)