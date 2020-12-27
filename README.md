# TOC-project神奇海螺

## 使用說明
- 基本操作
    - 所有用到英文的指令大小寫皆可
    - 隨時輸入任何字若沒觸發到都會有提示
- 架構圖
    1. 輸入`召喚海螺`開始使用神奇海螺
    2. 選擇功能 -> `擲筊`或`抽籤`
    3. 以下分成`擲筊`與`抽籤`來說明
- `擲筊` 
     - a.`輸入問題`
        - 任何文字訊息皆可
     - b.`擲筊結果`
        - 會根據機率出現以下四種結果
            - 聖筊
            - 陰筊
            - 笑筊
            - 立筊
       
- `抽籤`
     a. `抽數字`
        1. 輸入數字範圍
        2. 輸出中獎結果
     b. `抽選項`
        1. 輸入選項，以換行分隔
        2. 輸出結果
- `結果`
    - 每項功能結尾皆會跳回主選單

## 使用示範
### 輸入個人資訊
![](https://i.imgur.com/RAXRooY.jpg)
![](https://i.imgur.com/3VkDy82.jpg)
![](https://i.imgur.com/JhK01qT.jpg)
![](https://i.imgur.com/OCsoSBk.jpg)
### 增肌
![](https://i.imgur.com/OodsURE.jpg)
![](https://i.imgur.com/95lZAGO.jpg)
![](https://i.imgur.com/DOj8yEs.jpg)
![](https://i.imgur.com/bgeHzOf.jpg)
![](https://i.imgur.com/R2vy5FN.jpg)
![](https://i.imgur.com/TfHJx3t.jpg)
![](https://i.imgur.com/6ZEIZzI.jpg)
![](https://i.imgur.com/2iNuLe8.jpg)
### 減脂(生酮飲食)
![](https://i.imgur.com/Aej3bXd.jpg)
![](https://i.imgur.com/shzYGJD.jpg)
![](https://i.imgur.com/nxUfsPP.jpg)
![](https://i.imgur.com/pvibAF1.jpg)
![](https://i.imgur.com/xqbqg5A.jpg)
![](https://i.imgur.com/hsoAJeE.jpg)
![](https://i.imgur.com/7KyAzOK.jpg)
### 隨時畫FSM
![](https://i.imgur.com/kk8b9aa.jpg)
### 聊天機器人
![](https://i.imgur.com/co5NtdJ.jpg)
![](https://i.imgur.com/v0uG700.jpg)


## FSM
![](/img/fsm.jpg)
### state說明
- user: 輸入fitness開始使用健身小幫手
- input_gender: 輸入男生或女生
- input_age: 輸入年齡(整數)
- input_height: 輸入身高(整數)
- input_weight: 輸入體重(整數)
- input_days: 輸入一周運動天數(整數)
- choose: 顯示個人資訊，並選擇要增肌還是減脂
- muscle: 選擇要看增肌所需的熱量或是進入搜尋健身影片模式
- show_video: 輸入想訓練的部位
- get_video: 秀出youtube推薦的健身影片
- thin: 選擇要低醣飲食還是生酮飲食
- thin_type1: 說明何謂低醣飲食
- thin_type2: 說明何謂生酮飲食
- show_cal: 顯示使用者的BMR與TDEE
- show_food: 根據使用者要增肌或低醣飲食或生酮飲食，顯示使用者一天三大營養素應該各吃多少
- show_img: 根據使用者要增肌或低醣飲食或生酮飲食，回傳三大營養素比例的圓餅圖
- query: 作者事先整理過衛生署公布的各食物營養素，使用者可輸入他想要查詢的食物，會回傳所有相關該關鍵字的食物三大營養素提供給作者參考







	```


	```
