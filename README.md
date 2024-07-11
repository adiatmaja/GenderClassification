# 📊 Gabor Filter Influence in Gender Classification System Based on Fingerprints

This repository contains the code and documentation for my thesis project, "**Gabor Filter Influence in Gender Classification System Based on Fingerprints**". This research is conducted to fulfill the requirements for my Bachelor's degree.

## 📘 Introduction

The objective of this research is to explore the influence of Gabor filters in gender classification systems based on fingerprint images. By applying Gabor filters with various parameters, the study aims to gain insight into the role of Gabor filters in gender classification.

## 📂 Datasets

This research utilizes publicly accessible secondary datasets:
- [Sokoto Coventry Fingerprint Dataset (SOCOFing)](https://www.kaggle.com/datasets/ruizgara/socofing)
- [Family Fingerprint Dataset](https://data.mendeley.com/datasets/m4kz5ygxrn/1)

## 🔬 Methodology

The research involves the following steps:
1. **Data Collection**: Gathering a dataset of fingerprint images.
2. **Preprocessing**: Processing images using Gabor filters with various parameters.
3. **Classification**: Employing convolutional neural networks to extract relevant features and classify.
4. **Evaluation**: Evaluating the model's performance using stratified k-fold cross-validation with 5 folds. The evaluation metrics (weighted F1-score and AUC score) reported are averages across all folds. The result of each fold is stored in the `res` directory.

## 📈 Conclusion

The results of the conducted research indicate that the utilization of Gabor filters can enhance the performance of convolutional neural networks in gender classification systems based on fingerprints. The optimal parameter setting on both datasets is the default parameter, as it strikes a balance between the other two parameters. The default parameter exhibited an average value across all folds, with a weighted F1-score metric of 73.46% and an AUC score of 69.72% on the SOCOFing dataset, and a weighted F1-score of 70.1% and an AUC score of 74.41% on the Family dataset.

## 🛠 Dependencies

The project uses the following libraries:
- Python
- Tensorflow
- [Fingerprint Enhancement Python](https://pypi.org/project/fingerprint-enhancer/)
- opencv-python
- numpy
- scikit-learn

These dependencies are listed in the `requirements.txt` file.
