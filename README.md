# FPL Points Predictor with PyTorch ⚽📊

A machine learning-based Fantasy Premier League (FPL) points prediction system that uses PyTorch neural networks to forecast player performance and help optimize team selections.

## 🎯 Overview

This project uses a custom neural network built with PyTorch to predict FPL player points based on various performance metrics including expected goals (xG), assists, clean sheets, minutes played, and other key statistics. The system processes historical gameweek data to train a deep learning model that can forecast future player performance with improved accuracy over traditional linear regression.

## ✨ Features

- **Deep Learning Predictions**: Uses PyTorch neural networks for more complex pattern recognition
- **Custom Loss Functions**: Implements scaled loss functions for better training
- **Historical Analysis**: Processes multiple gameweek datasets for robust model training
- **Performance Visualization**: Interactive scatter plots showing prediction accuracy
- **Data Cleaning**: Automated handling of player transfers, injuries, and data inconsistencies
- **Model Evaluation**: Comprehensive loss tracking and model state inspection
- **Tensor Operations**: Efficient GPU/CPU computation with PyTorch tensors

## 🛠️ Libraries

- **Python 3.x**
- **PyTorch** - Deep learning framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Matplotlib/Seaborn** - Visualization
- **Custom Modules**:
  - `linearRegressionModel.py` - Neural network architecture
  - `LossFunction.py` - Custom loss functions
  - `graphing.py` - Visualization utilities

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FPL-Points-Predictor.git
   cd FPL-Points-Predictor
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install torch pandas numpy matplotlib seaborn scikit-learn
   ```

## 🚀 Usage

### Basic Usage

Run the main prediction script:

```bash
python main.py
```

### Configuration

Modify the following parameters in `main.py`:

- `using_week`: The gameweek to use for training data
- `target_week`: The gameweek to predict
- `evaluationMetric`: List of features to use for prediction
   - Comment out unwanted metrics to ignore

### Example Configuration

```python
using_week = 15  # Train on gameweek 15 data
target_week = 19  # Predict gameweek 19 performance

evaluationMetric = [
    'xP',          
    'minutes',      
    'assists',      
    'clean_sheets', 
    'expected_goal_involvements',
    'expected_goals',
    'expected_goals_conceded',
    'starts'
]
```

## 🔧 How It Works

1. **Data Preparation**: User chooses training and target gameweeks in `main.py`
2. **Data Cleaning**: Data sent to `cleanup.py` for preprocessing and validation
3. **Neural Network Training**: 
   - Features are converted to PyTorch tensors
   - Custom neural network processes input through multiple layers
   - Scaled loss function optimizes model parameters
   - SGD optimizer updates weights over 1000 epochs
4. **Prediction**: Trained model predicts points for target gameweek
5. **Visualization**: Results plotted with actual vs predicted performance

## 🧠 Model Architecture

The neural network consists of:
- **Input Layer**: Dense layer with neurons matching feature count
- **Hidden Layers**: Multiple dense layers with ReLU activation
- **Output Layer**: Single neuron for regression prediction
- **Custom Loss**: Scaled loss function for better training stability

## 📊 Model Performance

The system evaluates prediction accuracy using:
- **Loss Tracking**: Real-time loss monitoring during training
- **Model State Inspection**: Weight and bias analysis
- **Scatter Plot Visualization**: Shows prediction vs actual performance correlation
- **Player Labeling**: Highlights high-performing players for easy identification

## 🔍 Key Improvements Over Linear Regression

- **Non-linear Relationships**: Neural networks can capture complex patterns
- **Feature Interactions**: Automatic learning of feature combinations
- **Scaled Loss Functions**: Better handling of different value ranges
- **Tensor Operations**: Efficient computation and memory usage

## ⚠️ Disclaimer

This tool is for educational and entertainment purposes only. FPL predictions are inherently uncertain and should not be used as the sole basis for financial decisions. Always do your own research and consider multiple factors when making FPL team selections.

## 🚧 Current Limitations

- Model performance depends heavily on data quality and feature selection
- Requires significant computational resources for training
- May overfit on small datasets
- Predictions are probabilistic and should be used as guidance only

---

**Happy FPL Managing! 🏆** 
