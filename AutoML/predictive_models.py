{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "83922a79",
   "metadata": {},
   "outputs": [],
   "source": [
    "from abc import ABC, abstractmethod\n",
    "from sklearn.linear_model import LinearRegression, ElasticNet, LogisticRegression\n",
    "from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor\n",
    "\n",
    "# абстрактный класс для всех моделей\n",
    "class BaseModel(ABC):\n",
    "    @abstractmethod\n",
    "    def __init__(self):\n",
    "        pass\n",
    "\n",
    "    @abstractmethod\n",
    "    def fit(self, X_train, y_train):\n",
    "        pass\n",
    "\n",
    "    @abstractmethod\n",
    "    def predict(self, X_test):\n",
    "        pass\n",
    "\n",
    "\n",
    "class LinearRegressionModel(BaseModel):\n",
    "    def __init__(self):\n",
    "        self.model = LinearRegression()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        return self.model.predict(X_test)\n",
    "\n",
    "\n",
    "class ElasticNetModel(BaseModel):\n",
    "    def __init__(self):\n",
    "        self.model = ElasticNet()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        return self.model.predict(X_test)\n",
    "\n",
    "\n",
    "class RandomForestRegressorModel(BaseModel):\n",
    "    def __init__(self):\n",
    "        self.model = RandomForestRegressor()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        return self.model.predict(X_test)\n",
    "\n",
    "\n",
    "class GradientBoostingRegressorModel(BaseModel):\n",
    "    def __init__(self):\n",
    "        self.model = GradientBoostingRegressor()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        return self.model.predict(X_test)\n",
    "\n",
    "\n",
    "class LogisticRegressionModel(BaseModel):\n",
    "    def __init__(self):\n",
    "        self.model = LogisticRegression()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        return self.model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "07b84069",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}