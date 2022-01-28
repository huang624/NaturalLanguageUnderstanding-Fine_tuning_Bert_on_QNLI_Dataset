# 資料處理
### Dataset介紹

QNLI的Dataset會提供一句Question及一句Sentence，並要求模型判斷Sentence內是否包含Question的答案。

有包含，label = 0；不包含，label = 1。

範例如下圖
![image](https://user-images.githubusercontent.com/88367016/151115003-7e46cdea-fc1d-4c12-bc1e-283131d2a07d.png)

### 資料型態

+ Training Data
![image](https://user-images.githubusercontent.com/88367016/151513750-d360efa2-0b22-432d-a646-2bb3c5037a9c.png)

+ Validation Data
![image](https://user-images.githubusercontent.com/88367016/151514035-27bdd87d-f464-4699-a749-7b757165230a.png)

+ Test Data (＊Label皆為-1)
![image](https://user-images.githubusercontent.com/88367016/151514210-544ad912-5d1d-4e40-a09c-62d56ea25d13.png)

### tokenize <將Question、Sentence 轉換成 token id 、tpye_id 與 attention_mask>
由於colab GPU使用的限制，將tokenizer的max_length設為256

![image](https://user-images.githubusercontent.com/88367016/151518658-773efaf5-8976-45ca-85ae-77c0648ba5d2.png)


**max_length 設置參考:**

https://huggingface.co/docs/transformers/preprocessing
https://blog.csdn.net/qq_33293040/article/details/105439750
https://stackoverflow.com/questions/65246703/how-does-max-length-padding-and-truncation-arguments-work-in-huggingface-bertt

# 模型訓練

程式碼將會使用BERT-base-uncased來訓練模型

由於GPU使用上的限制，此程式將tokenizer的max_length設置為256

**Training_data:20000筆，Testing_data:2000筆，Validation_data:2000筆。**

**learning_rate=3e-5，batch_size = 8，epochs = 3**


# 模型效果

Accuracy = 0.8752

Matthews_corrcoef = 0.7505791330117884

Classification_report

![image](https://user-images.githubusercontent.com/88367016/151115826-1d301ce3-e82d-4c3a-98e8-b725fc2e963f.png)


# Demo

![新分頁 - Google Chrome 2022-01-28 17-25-36](https://user-images.githubusercontent.com/88367016/151549245-7a09ba41-966d-4ea3-b8b1-7745465feb09.gif)





