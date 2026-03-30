# 🧬 DeepProtein-CNN: Natural Language Processing in Genomics

Welcome to the **DeepProtein-CNN** repository. 

As a **BSc (Hons) Biochemistry** student, I built this Deep Learning architecture to prove that biological amino acid sequences can be mathematically parsed exactly like human language. By combining biological domain knowledge with TensorFlow Keras abstractions, this neural network autonomously scans, dimensionally embeds, and detects synthetic pathogenic protein motifs with **92.79% accuracy** entirely from algorithmic scratch.

## 📊 The Deep Learning Pipeline

This repository utilizes a full 1D-Convolutional Neural Network pipeline, completely side-stepping traditional CPU decision trees in favor of GPU-accelerated Calculus.

```mermaid
graph TD
    A["Raw Protein Sequence<br/>Ex: 'VWYFG...'"] -->|"1. Char-Level Tokenization"| B("Numerical Integers<br/>Ex: [18, 20, 19, 9, 7]")
    B -->|"2. Dimensional Geometry"| C{"8D Embedding Layer"}
    C -->|"Maps Amino Acids into 3D Physics"| D["Tensor Matrix"]
    D -->|"3. Spatial Scanning"| E("1D Convolutional Neural Network")
    E -->|"Slides Kernel Size = 5"| F["Global Max Pooling"]
    F -->|"Shrinks to Critical Motifs"| G("Dense Output Layer")
    G -->|"Sigmoid Activation"| H(("Probability: 0% or 100%"))
    
    style A fill:#e1f5fe,stroke:#01579b
    style C fill:#fff3e0,stroke:#e65100
    style E fill:#e8f5e9,stroke:#1b5e20
    style H fill:#fce4ec,stroke:#880e4f

