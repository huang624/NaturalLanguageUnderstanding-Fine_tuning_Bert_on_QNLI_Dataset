# Dataset

QNLI的Dataset會提供一句Question及一句Sentence，並要求模型判斷Sentence內是否包含Question的答案。

有包含，label = 0；不包含，label = 1。

範例如下圖
![image](https://user-images.githubusercontent.com/88367016/151115003-7e46cdea-fc1d-4c12-bc1e-283131d2a07d.png)

# 模型訓練

程式碼將會使用BERT-base-uncased來訓練模型

由於GPU使用上的限制，此程式將tokenizer的max_length設置為256

Training_data:20000筆，Testing_data:2000筆，Validation_data:2000筆。

learning_rate=3e-5

# 模型效果

Accuracy = 0.8752

Matthews_corrcoef = 0.7505791330117884

Classification_report

![image](https://user-images.githubusercontent.com/88367016/151115826-1d301ce3-e82d-4c3a-98e8-b725fc2e963f.png)
