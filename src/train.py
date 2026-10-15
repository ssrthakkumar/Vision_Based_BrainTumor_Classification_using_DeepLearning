import torch
import torch.nn as nn

def run_epoch(model, loader, device, criterion, optimizer=None):
    training = optimizer is not None
    model.train() if training else model.eval()
    total_loss, correct, total = 0, 0, 0
    with torch.set_grad_enabled(training):
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            out = model(x)
            loss = criterion(out, y)
            if training:
                optimizer.zero_grad()   # purane gradients saaf
                loss.backward()         # galti kis weight ki wajah se hui
                optimizer.step()        # weights sudharo
            total_loss += loss.item() * x.size(0)
            correct += (out.argmax(1) == y).sum().item()
            total += x.size(0)
    return total_loss / total, correct / total

def fit(model, train_loader, val_loader, device, epochs=10, lr=1e-3, save_path='best_model.pth'):
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    history = {'train_loss': [], 'train_acc': [], 'val_loss': [], 'val_acc': []}
    best_val = 0
    for ep in range(epochs):
        tl, ta = run_epoch(model, train_loader, device, criterion, optimizer)
        vl, va = run_epoch(model, val_loader, device, criterion)
        for k, v in zip(history, [tl, ta, vl, va]):
            history[k].append(v)
        if va > best_val:
            best_val = va
            torch.save(model.state_dict(), save_path)  # best model save
        print(f"Epoch {ep+1}/{epochs} | train acc {ta:.3f} loss {tl:.3f} | val acc {va:.3f} loss {vl:.3f}")
    return history
