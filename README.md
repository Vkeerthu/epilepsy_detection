


# Epilepsy Detection using LSTM, BiLSTM, and GRU 🧠💻

## Overview

This repository contains the implementation of an Epilepsy Detection system using Long Short-Term Memory (LSTM), Bidirectional LSTM (BiLSTM), and Gated Recurrent Unit (GRU) neural networks. The goal is to predict epileptic seizures based on EEG (Electroencephalogram) data.

![Epilepsy Detection](/images/eeg_detection.png)

## Models Implemented

- **LSTM (Long Short-Term Memory):** A type of recurrent neural network (RNN) known for handling long-range dependencies.
- **BiLSTM (Bidirectional LSTM):** An extension of LSTM that processes the input sequence in both forward and backward directions.
- **GRU (Gated Recurrent Unit):** Another variant of RNN, similar to LSTM but with a simplified architecture.

## Dataset

The model is trained on the [Epileptic Seizure Recognition Data Set](https://archive.ics.uci.edu/ml/datasets/Epileptic+Seizure+Recognition) from UCI Machine Learning Repository.

## Requirements

- Python 3.x
- TensorFlow
- Keras
- Other dependencies (specified in requirements.txt)

## Setup



    
4. Run the Jupyter Notebook or Python scripts to train and evaluate the models.

## Usage

- Execute the provided Jupyter Notebook `epilepsy_detection.ipynb` for a step-by-step walkthrough.
- Alternatively, use the Python scripts in the `scripts/` directory for training and testing specific models.

## Results

| Model      | Accuracy | Precision | Recall | F1 Score |
|------------|----------|-----------|--------|----------|
| LSTM       | 90%      | 91%       | 89%    | 90%      |
| BiLSTM     | 92%      | 92%       | 91%    | 92%      |
| GRU        | 89%      | 88%       | 90%    | 89%      |

## Contributions

Contributions are welcome! Feel free to open issues, submit pull requests, or provide suggestions for improvement.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify this template to fit the specific details of your project. You can replace the placeholder URLs, directory structure, and model results with the actual information from your project.
