



# Edge-to-Cloud IoT Intrusion Detection System

**Author:** Sushant Lnu | Auburn University Montgomery | s1nu163@aum.edu

---

## About
- Compares Logistic Regression, Random Forest, and Neural Network (MLP) for IoT intrusion detection
- Evaluates models on both accuracy and computational efficiency
- Designed for edge-to-cloud deployment using the CICIoT2023 dataset

---

## Dataset
- **CICIoT2023** — 47 network flow features, multiple attack categories
- Download: https://drive.google.com/drive/folders/1GWUFs5nqrt5tY8iIoaBK2T0QVkMZ77XH?usp=sharing
- Place at: `CICIOT23/train/train.csv`

---

## Requirements
- Python 3.12+, 8 GB RAM, no GPU needed
- Install dependencies: `pip install -r requirements.txt`
- Packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `plotly`, `jupyter`

---

## How to Run
```bash
git clone https://github.com/<your-username>/edge-to-cloud-ids.git
cd edge-to-cloud-ids
pip install -r requirements.txt
jupyter notebook Edge.ipynb
```


---

## Results

| Model | Accuracy | F1 Score | Deploy At |
|---|---|---|---|
| Logistic Regression | 81.67% | 0.7859 | Edge |
| Random Forest | **99.07%** | **0.9899** | Edge / Hybrid |
| Neural Network (MLP) | 97.51% | 0.9743 | Cloud |

---

## Architecture
```
IoT Devices → Edge Layer (LR / RF) → Cloud Layer (MLP)
              real-time detection     deep analysis
```

---


