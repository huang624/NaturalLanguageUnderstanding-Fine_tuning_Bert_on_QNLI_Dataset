# QNLI

QNLI的Dataset會提供一句Question及一句Sentence，並要求模型判斷Sentence內是否包含Question的答案。

有包含，label = 0；不包含，label = 1。

範例如下圖
![image](https://user-images.githubusercontent.com/88367016/151115003-7e46cdea-fc1d-4c12-bc1e-283131d2a07d.png)



-程式碼將會使用BERT-base-uncased來訓練模型
Training_data:20000筆，Testing_data:2000筆，Validation_data:2000筆。


-模型效果

Accuracy = 0.875

matthews_corrcoef = 0.7505791330117884

classification_report

![image](https://user-images.githubusercontent.com/88367016/151115826-1d301ce3-e82d-4c3a-98e8-b725fc2e963f.png)
