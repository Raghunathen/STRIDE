# Project Overview

## **Files and Functionality**
- **Taker.py**: Captures and saves images.
- **Flipper.py**: Augments the dataset by flipping images to generate additional samples.
- **Play_again.py**: Automates the model loop for continuous runs.
- **Models.ipynb**: Contains all model architecture definitions.
- **Training.ipynb**: Implements the training loop, evaluation, and related tasks.

## **Dataset Details**
### **Classes**
- **Up**: ~1,000 images (limited availability).
- **Down**: ~1,000 images (limited availability).
- **Left and Right**: Include flipped versions of each other for balance.
- **No-op**: ~13,000 images, but only 1,000 randomly selected for training per epoch to avoid bias.

---

# STRIDE and Experimentation History

## **STRIDE 0**
### **Architecture**
- 2 Conv Layers: 32 kernels each.

### **Performance**
- Loss: ~0.5 (as good as random predictions).
- **Issues**: Model struggled, particularly with turning right.

---

## **STRIDE 1**
### **Architecture**
- 4 Conv Layers: 32 kernels each.

### **Performance**
- 10 Epochs achieved ~85% accuracy.
- **Issues**: Still made bad moves, possibly due to insufficient data.

---

## **STRIDE 2**
### **Architecture**
- 5 Conv Layers: 32 kernels each.

### **Performance**
- Trained over ~270 epochs.
- Sweet spot for training accuracy: **80–90%** (higher led to overfitting).

---

## **STRIDE 3**

### **3.1**
#### **Architecture**
- 5 Conv Layers: Increasing kernel sizes (32, 64, 128, 256, 512).

#### **Performance**
- Epoch 5: Loss = 0.4077, Accuracy = 58.31%.
- Epoch 10: No significant improvement.

---

### **3.2**
#### **Architecture**
- 4 Conv Layers: (32, 64, 128, 256).
- Total Trainable Parameters: **5,107,781**.

#### **Performance**
- Epoch 5: Loss = 0.4788, Accuracy = 35.52%.
- Epoch 10: Loss = 0.4660, Accuracy = 39.68%.
- **Observation**: More parameters led to bad overfitting. Considered reducing complexity.

---

### **3.3**
#### **Architecture**
- 4 Conv Layers: (32, 32, 32, 8).
- Total Trainable Parameters: **169,933**.

#### **Performance**
- Epoch 5: Loss = 0.3377, Accuracy = 82.02%.
- Epoch 10: Loss = 0.3140, Accuracy = 89.52%.
- **Observation**: Good performance and generalized well. Needs new data due to variations in train colors.

---

### **3.4**
#### **Architecture**
- 4 Conv Layers: (32, 8, 32, 8).
- Total Trainable Parameters: **156,085**.

#### **Performance**
- Epoch 5: Loss = 0.3382, Accuracy = 81.55%.
- Epoch 10: Loss = 0.3145, Accuracy = 89.14%.
- **Observation**: Performance similar to 3.3. Threshold for trainable parameters seems optimal. Tweaking kernel sizes could improve results. Switching to black-and-white images is the next step to mitigate errors caused by color variations.

---

## **STRIDE 4 (YTD)**
### **Experiment**
- Converted images to grayscale (black-and-white) for training.

---

## **STRIDE 5 (YTD)**
### **Experiment**
- Applied Canny edge detection for preprocessing the images.
