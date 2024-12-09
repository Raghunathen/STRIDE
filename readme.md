# Project Overview

**STRIDE**, “Surfer’s Tactical Response and Decision Engine” is a DL model that classifies images with fine, minute details—at real-time speeds. What does that mean? Well... it’s a bot that plays Subway Surfers! It leverages convolutional neural networks (CNNs) for image classification to make quick decisions, such as moving up, down, left, right, or staying still (no-op). Through iterative experiments with architecture, data preprocessing, and training strategies, STRIDE aims to be a infinite runner. A Far Fetched aim.

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
- 4 Conv Layers: 32 kernels each. 3x3 Kernels.

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
- **Observation**: Performance similar to 3.3. Threshold for trainable parameters seems optimal. Tweaking kernel sizes could improve results. 

---

### **3.5**
#### **Architecture**
- 4 Conv Layers: (32, 32, 32,  8) with 5x5 Kernels.
- Total Trainable Parameters: **163,277**.

#### **Performance**
- Epoch 5: Loss = 0.3430, Accuracy = 80.32%.
- Epoch 10: Loss = 0.3199, Accuracy = 87.65%.
- **Observation**: Increasing kernel size, Switching to black-and-white images is the next step to mitigate errors caused by color variations.

---

## **STRIDE 4**
### **Experiment**
- Converted images to grayscale (black-and-white) for training.

### **4.1**
#### **Architecture**
- 4 Conv Layers: (32, 32, 32, 8) with 3x3 Kernels
- Total Trainable Parameters: **169,933**.

#### **Performance**
- Epoch 5: Loss = 0.3520, Accuracy = 77.10%.
- Epoch 10: Loss = 0.3264, Accuracy = 85.46%.
- **Observation**: The intuition behind using black-and-white images is to help the model generalize better. However, the current performance isn't on par with our best model (3.3). The next step is to train the model further and tweak the architecture. Reducing the number of parameters might be sufficient. We'll run a few more epochs and reassess before making a final decision.
- Epoch 20: Loss = 0.3092, Accuracy = 90.73%
- **Observation**: The model shows improved performance compared to earlier epochs but exhibits signs of overfitting in specific scenarios. To verify this, it was tested on a validation set, yielding a high loss of **1.0400**, which confirmed the hypothesis. The next step is to reduce the number of parameters to mitigate overfitting and prevent excessive learning.

---

## **STRIDE 5 (YTD)**
### **Experiment**
- Applied Canny edge detection for preprocessing the images.
