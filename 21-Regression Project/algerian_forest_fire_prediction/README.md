# Algerian Forest Fires --- Fire Weather Index (FWI) Prediction

## 1. Project Overview

This project analyzes the Algerian Forest Fires dataset and trains
regression models to estimate the **Fire Weather Index (FWI)** from
observed weather conditions, fire-weather indicators, fire-class
information, and region.

The work is organized into three notebooks:

-   `21.3-Algerian-dataset.ipynb` --- data loading, cleaning, and
    preparation.
-   `21.4-Algerian-EDA.ipynb` --- exploratory data analysis and
    visualization.
-   `21.5-Algerian Model Training.ipynb` --- feature preparation, model
    training, and evaluation.

## 2. Objective

The objective is to build and compare regression models that predict the
numerical value of **FWI**. FWI is the target variable in the
model-training notebook.

This is a **regression task**, not a classification task: the model
estimates a continuous FWI value rather than directly predicting whether
a fire will occur. The dataset's `Classes` field (`fire` / `not fire`)
is used as an input feature after encoding; it is not the target in the
documented training workflow.

## 3. Dataset Description

The cleaned dataset contains **244 observations** from two Algerian
regions:

-   Bejaia
-   Sidi-Bel Abbes

The raw file contains date fields, weather measurements, Fire Weather
Index System components, a fire class label, and a region identifier.

  Feature         Description
  --------------- ------------------------------------------------------
  `Temperature`   Temperature observation
  `RH`            Relative humidity
  `Ws`            Wind speed
  `Rain`          Rainfall
  `FFMC`          Fine Fuel Moisture Code
  `DMC`           Duff Moisture Code
  `DC`            Drought Code
  `ISI`           Initial Spread Index
  `BUI`           Build-Up Index
  `FWI`           **Target:** Fire Weather Index
  `Classes`       Fire / not-fire class, encoded as 1 / 0 for training
  `Region`        Region identifier used in the prepared data

The original dataset also contains `day`, `month`, and `year`. These
date fields are removed from the model inputs in the training notebook.

### Class distribution

  Class         Observations      Share
  ----------- -------------- ----------
  Fire                   138      56.6%
  Not fire               106      43.4%
  **Total**          **244**   **100%**

The classes are not perfectly balanced, but neither class is a small
minority in this dataset.

## 4. Data Preparation

The notebooks document the following preparation steps:

1.  Loaded the source dataset and identified the two regional sections.
2.  Removed the separator/header row and other problematic rows during
    cleaning.
3.  Standardized column names by stripping extra spaces.
4.  Normalized inconsistent `Classes` labels and handled the missing
    class value.
5.  Corrected invalid numeric entries and converted numeric fields to
    suitable numeric types.
6.  Removed `day`, `month`, and `year` from the model inputs.
7.  Encoded `Classes` as `not fire = 0` and `fire = 1`.
8.  Split the data into training and test sets using a 75:25 split
    (`random_state=42`).
9.  Identified features with absolute pairwise correlation above 0.85 in
    the training data and removed `BUI` and `DC`.
10. Standardized the model inputs using `StandardScaler`.

The final regression input features are the remaining
weather/FWI-related measurements plus the encoded `Classes` and `Region`
fields, excluding the target `FWI` and the removed `BUI` and `DC`
features.

## 5. Exploratory Data Analysis --- Key Observations

The correlation analysis and visualizations provide several useful
observations:

-   **Temperature and relative humidity:** a negative correlation
    (approximately **-0.65**) was observed. Higher temperatures tend to
    coincide with lower relative humidity in these observations.
-   **Temperature and FFMC:** a positive correlation (approximately
    **+0.68**) was observed.
-   **RH and ISI:** a negative correlation (approximately **-0.69**) was
    observed.
-   **FFMC and ISI:** a positive correlation (approximately **+0.74**)
    was observed.
-   **DMC and DC:** a very strong positive correlation (approximately
    **+0.88**).
-   **DMC and BUI:** a very strong positive correlation (approximately
    **+0.98**). This high correlation motivated removing `BUI` and `DC`
    under the notebook's correlation-threshold procedure.
-   **FWI distribution:** the EDA notebook reports positive skewness
    (approximately **1.15**), suggesting that higher FWI values are less
    common than lower values.
-   **Class counts:** the cleaned dataset contains 138 `fire` and 106
    `not fire` observations.

These are associations in this dataset, not proof that one variable
causes another. The observations are also limited to the two represented
regions and the available sample period.

## 6. Models and Evaluation

The notebook evaluates two regression techniques on the held-out test
set:

-   Linear Regression
-   Lasso Regression

The reported metrics are:

  Metric                             Linear Regression   Lasso Regression
  -------------------------------- ------------------- ------------------
  Mean Squared Error (MSE)                      0.6871             2.9733
  Mean Absolute Error (MAE)                     0.6313             1.2377
  Root Mean Squared Error (RMSE)                0.8289             1.7243
  R² score                                      0.9881             0.9487

### How to interpret the metrics

-   **MSE, MAE, and RMSE:** lower values indicate smaller prediction
    errors.
-   **R²:** a value closer to 1 indicates that the model explains more
    of the variation in the test-set target values.

Linear Regression has lower error values and a higher R² score than
Lasso Regression in the documented experiment.

## 7. Model Selection and Conclusion

**Linear Regression is selected as the best-performing model among the
two models tested.** On the held-out test set, it achieved an R² score
of **0.9881**, an MAE of **0.6313**, and an RMSE of **0.8289**. Lasso
Regression achieved an R² score of **0.9487**, with higher MAE
(**1.2377**) and RMSE (**1.7243**).

The results indicate that Linear Regression predicts FWI more accurately
than the tested Lasso model for this particular train/test split. The
dataset's weather and fire-weather variables show meaningful
relationships, and the prepared inputs provide a strong signal for
estimating FWI.

This conclusion is limited to the two evaluated models and the reported
split. The dataset is small (244 observations), and the notebooks do not
establish performance on independent regions or future seasons.
Cross-validation and external testing would be valuable before relying
on the model in operational fire-risk monitoring.

### Important interpretation note

The model predicts **FWI**, not the occurrence of a fire itself.
Although `Classes` is included as an input feature in the notebook, it
is a fire/not-fire label. In a real forecasting scenario, this feature
should only be used if it is genuinely available at prediction time;
otherwise, it could make the task unrealistically easy or introduce
target-information leakage. A separate classification model would be
needed to predict the `fire` / `not fire` label directly.

## 8. Technologies Used

-   Python
-   pandas and NumPy
-   Matplotlib and Seaborn
-   scikit-learn
-   Jupyter Notebook

## 9. Reproducibility Notes

The training notebook refers to a local Windows file path for its
cleaned CSV. Update that path to the location of the cleaned dataset in
your environment before rerunning the notebook. The reported metrics
above are the outputs recorded in the uploaded notebook; they may differ
if the data, preprocessing, split, or library versions change.
