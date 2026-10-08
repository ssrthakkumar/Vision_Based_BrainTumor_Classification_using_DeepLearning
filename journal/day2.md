# Day 2: Data Preprocessing (PyTorch)

## What I did
- Resized all images to 150x150 (the CNN needs a fixed input size; notumor images were 225x225, the rest 512x512)
- Converted to tensors with `ToTensor()`, which scales pixels from 0-255 to 0-1 (small values make training stable)
- Applied augmentation (rotation, flip, shift) on training data only, so the model sees varied images and overfits less
- Split training data 80/20 into train (4480) and validation (1120); test (1600) stays untouched until the end

## Key learning
- Validation and test data must NOT be augmented, otherwise the accuracy numbers are unreliable
- Fixed the random seed so the train/val split is the same every run (reproducible results)
- Moved clean code into `src/data_loader.py` (shared with the team); the messy notebook stays private

## Plan for Day 3
Learn CNN basics (convolution, pooling) and build the first model in PyTorch
