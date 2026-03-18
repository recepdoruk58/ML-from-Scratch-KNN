import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import load_iris
from  sklearn.model_selection import train_test_split
from knn_scratch import SimpleKNN


iris=datasets.load_iris()
X,y= iris.data,iris.target

#Burada başarı oranını yükseltmek için normalizasyon işlemini uyguluyoruz.
X=(X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0))

#Başarı oranını biraz daha artırmak için shuffle işlemi yapıyoruz.
indisler=np.arange(X.shape[0])
np.random.shuffle(indisler)
X=X[indisler]
y=y[indisler]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=SimpleKNN(k=5)
model.fit(X_train,y_train)

predicts=model.predict(X_test)

print("ilk 20 tahmin: ",predicts[:20])
print("Gercek Sonuc: ",y_test[:20])

basari = np.sum(predicts== y_test) / len(y_test)

print(f"Yeni Başarı Oranı: %{basari * 100:.2f}")


plt.figure(figsize=(10, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=predicts, cmap='rainbow')
plt.title("KNN Tahmin Görselleştirmesi")
plt.xlabel("Sepal Length (Normalize)")
plt.ylabel("Sepal Width (Normalize)")
plt.savefig("KNN_Sonuc_grafigi.png")

