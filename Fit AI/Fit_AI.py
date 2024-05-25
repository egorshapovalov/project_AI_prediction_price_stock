from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from joblib import dump

# Загружаем данные ирисов
df = pd.read_csv('Прошлые данные - YNDX.csv')
# Преобразуем столбец "Дата" в числовой формат
df["Дата"] = pd.to_datetime(df["Дата"], format="%d.%m.%Y")

X = pd.DataFrame({"Год": df["Дата"].dt.year, "Месяц": df["Дата"].dt.month, "День":df["Дата"].dt.day})
y = df["Цена"].apply(lambda x: float(x.replace(",", ".")))

# Разделим данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создадим модель Случайный лес для регрессии
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Обучим модель на обучающем наборе данных
model.fit(X_train, y_train)

# сохраняем модель
dump(model, 'model_yndx.joblib')

