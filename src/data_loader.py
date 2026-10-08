import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

def get_loaders(train_dir, test_dir, img_size=150, batch_size=32, val_split=0.2, seed=42):
    train_tf = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.RandomRotation(15),
        transforms.RandomHorizontalFlip(),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
    ])
    eval_tf = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
    ])

    full_aug = datasets.ImageFolder(train_dir, transform=train_tf)    # for training
    full_clean = datasets.ImageFolder(train_dir, transform=eval_tf)   # for validation
    test_ds = datasets.ImageFolder(test_dir, transform=eval_tf)

    g = torch.Generator().manual_seed(seed)  # same split every run
    idx = torch.randperm(len(full_aug), generator=g).tolist()
    n_val = int(val_split * len(idx))
    train_ds = Subset(full_aug, idx[n_val:])
    val_ds = Subset(full_clean, idx[:n_val])

    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=True),
        DataLoader(val_ds, batch_size=batch_size),
        DataLoader(test_ds, batch_size=batch_size),
        full_aug.class_to_idx,
    )
