# Quick Start
+ fork the repositories

  ```
  git clone https://github.com/huang624/Bert_for_QNLI.git
  ```

+ 執行Model_Traing_BERT_for_QNLI.ipynb,
  colab here:https://drive.google.com/file/d/1zuxC1WU05Avu3qvRWsjSufhSHeMthQxC/view?usp=sharing
  或是使用已訓練完成的模型:https://drive.google.com/drive/folders/1-Im1qgYOoPyj9VvyLBZdgoZ_G1_EJntt?usp=sharing

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

### tokenize <將Question、Sentence 轉換成 token id 、type_id 與 attention_mask>
由於colab GPU使用的限制，將tokenizer的max_length設為256

```Python
from transformers import BertTokenizerFast
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

train_encodings = tokenizer(train_question, train_sentence, padding='max_length', truncation=True, max_length=256)
eval_encodings = tokenizer(eval_question, eval_sentence, padding='max_length', truncation=True, max_length=256)

```


**max_length 設置參考:**

https://huggingface.co/docs/transformers/preprocessing
# 模型訓練

程式碼將會使用BERT-base-uncased來訓練模型

由於GPU使用上的限制，此程式將tokenizer的max_length設置為256

**Training_data:20000筆，Testing_data:2000筆，Validation_data:2000筆。**

**learning_rate=3e-5，batch_size = 8，epochs = 3**


# 模型效果

Accuracy = 0.8752

Matthews_corrcoef = 0.7505791330117884

Classification_report


|              | precision | recall | f1-score | support |
|--------------|:---------:|-------:|:--------:|--------:|
| 0            |    0.87   |   0.88 |  0.87    |   1229  |
| 1            |    0.89   |   0.87 |  0.88    |   1271  |
| accuracy     |           |        |  0.88    |   2500  |
| macro avg    |    0.88   |   0.88 |  0.88    |   2500  |
| weighted avg |    0.88   |   0.88 |  0.88    |   2500  |

Evaluation heatmap

![image](https://user-images.githubusercontent.com/88367016/151550184-a51e4d4e-4579-4fbf-8ef3-578607346628.png)


# Demo

![新分頁 - Google Chrome 2022-01-28 17-25-36_1](https://user-images.githubusercontent.com/88367016/151549634-c9339472-8f08-47e7-8d67-192e3bb5d356.gif)

![QNLI Demo - Google Chrome 2022-01-28 17-26-12](https://user-images.githubusercontent.com/88367016/151550076-b9938a33-7e16-47af-ac7b-02a8ed4f4265.gif)





