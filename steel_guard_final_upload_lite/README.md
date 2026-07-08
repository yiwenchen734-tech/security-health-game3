# Steel Guard：夜班危機 8 小時\n\n樂橙職業健康管理顧問有限公司 × 藍海保全 × 嘉仕達保全

保全業肌肉骨骼危害預防衛教遊戲（Streamlit 版）

這是一個以保全工作情境為核心的互動式衛教小遊戲，適合用於：

- 保全業職業安全衛生教育訓練
- 肌肉骨骼傷害預防宣導
- 臨場服務或團體衛教活動
- 手機或電腦快速互動體驗

遊戲主題為 **夜班值勤 × 職業傷害防衛戰**，玩家會在不同保全工作情境中做出選擇，學習如何預防：

- 搬重物造成的下背負擔
- 久坐監看造成的肩頸痠痛
- 久站站崗造成的足底與膝蓋壓力
- 樓梯巡邏造成的下肢負擔
- 訪客衝突造成的壓力與姿勢緊繃
- 夜班疲勞造成的姿勢崩壞與警覺下降

---

## 專案內容

```text
steel_guard_final_upload/
├─ app.py
├─ requirements.txt
├─ README.md
├─ basement_lift.jpg
├─ control_room.jpg
├─ gate_standing.jpg
├─ stairs_patrol.jpg
├─ front_desk_stress.jpg
└─ night_fatigue.jpg
```

---

## 使用方式（本機）

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 啟動程式

```bash
streamlit run app.py
```

---

## GitHub / Streamlit Community Cloud 部署方式

1. 將整個資料夾內容上傳到 GitHub Repository。
2. 到 [Streamlit Community Cloud](https://streamlit.io/cloud) 登入。
3. 選擇 **New app**。
4. 指定你的 GitHub repository。
5. Main file path 選擇：

```text
app.py
```

6. Deploy 即可。

---

## 遊戲特色

- 保全業專屬職場情境
- RPG 手遊風格插圖
- HP、警覺值、恢復力三項指標
- 裝備選擇系統
- 戰技卡收集
- 隨機突發事件
- 30 秒恢復任務
- 任務結算與健康建議

---

## 注意事項

- 圖片檔名請勿更改，`app.py` 會直接讀取同層圖片。
- 建議使用手機直式操作或一般電腦瀏覽器。
- 本遊戲為教育用途，不取代專業醫療建議。

---

## 適合延伸功能

之後如果你要擴充，也可以加入：

- 分數排行榜
- 答題音效
- 更多保全情境關卡
- 公司 Logo / 單位名稱客製化
- 教育訓練結束後 QR Code 掃描進入遊戲
- 結算畫面加入衛教重點下載



---

## 合作單位與版權

合作單位：樂橙職業健康管理顧問有限公司 × 藍海保全 × 嘉仕達保全

【版權聲明 Copyright © 2026 樂橙職業健康管理顧問有限公司．版權所有】。


---

## 圖片未偵測到時

若畫面出現「未偵測到場景圖」，請確認：

1. 圖片檔名完全一致，例如 `basement_lift.jpg`。
2. 圖片與 `app.py` 放在同一層資料夾。
3. 若你把 `app.py` 放在子資料夾，Streamlit 的 Main file path 要指到正確位置。
4. 本版本也支援將圖片放在 `images/` 或 `assets/` 資料夾。


---

## 輕量版說明

本版本已將原本 RPG 插圖由 PNG 改為 JPG，並壓縮尺寸，以利 GitHub / Streamlit 上傳與部署。

圖片檔名已同步修改於 `app.py`，請直接使用本資料夾內容上傳，不需要再改程式。
