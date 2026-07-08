import streamlit as st
import random
from pathlib import Path

# -----------------------------
# 客製化資訊
# -----------------------------
GAME_TITLE = "🛡️ STEEL GUARD"
GAME_SUBTITLE = "夜班危機 8 小時｜保全業肌肉骨骼危害預防遊戲"
COMPANY_LINE = "樂橙職業健康管理顧問有限公司 × 藍海保全 × 嘉仕達保全"
COPYRIGHT_TEXT = "Copyright © 2026 樂橙職業健康管理顧問有限公司．版權所有"


# =========================================================
# Steel Guard：夜班危機 8 小時
# 保全業肌肉骨骼危害預防衛教遊戲
# 可直接部署於 Streamlit Community Cloud / GitHub
# =========================================================

st.set_page_config(
    page_title="Steel Guard：夜班危機 8 小時｜樂橙職業健康管理顧問有限公司 × 藍海保全 × 嘉仕達保全",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CSS：手機版遊戲風格
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #1e293b 0%, #0d1117 45%, #05070a 100%);
    color: #c9d1d9;
}
html, body {
    font-family: "SF Pro", "PingFang TC", "Microsoft JhengHei", sans-serif;
}
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 760px;
}
.game-title {
    text-align: center;
    color: #f8fafc;
    font-weight: 900;
    font-size: 30px;
    margin-bottom: 0px;
    letter-spacing: 1px;
}
.subtitle {
    text-align:center;
    color:#94a3b8;
    font-size:14px;
    margin-bottom:20px;
}
.story-box {
    background: rgba(22, 27, 34, 0.95);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 18px;
    border: 2px solid #30363d;
    box-shadow: 0 10px 28px rgba(0,0,0,0.28);
}
.story-box h3 {
    color: #f0f6fc;
    font-size: 21px;
    margin-bottom: 12px;
    font-weight: 900;
}
.story-box p, .story-box li {
    font-size: 16px;
    line-height: 1.7;
    color: #cbd5e1;
}
.tip-box {
    background: rgba(15, 23, 42, 0.95);
    padding: 16px;
    border-radius: 16px;
    border-left: 6px solid #38bdf8;
    margin-bottom: 16px;
}
.skill-card {
    background: linear-gradient(135deg, #172554, #0f172a);
    border: 2px solid #60a5fa;
    border-radius: 18px;
    padding: 18px;
    margin: 14px 0;
    box-shadow: 0 8px 20px rgba(59,130,246,0.15);
}
.skill-card h4 {
    color: #bfdbfe;
    margin: 0 0 8px 0;
    font-weight: 900;
}
.skill-card p {
    color: #e2e8f0;
    line-height: 1.7;
}
.status-card {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 12px 14px;
    margin-bottom: 10px;
}
.metric-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 700;
}
.hp-text {
    font-size: 25px;
    font-weight: 950;
    color: #ef4444;
}
.sense-text {
    font-size: 21px;
    font-weight: 900;
    color: #38bdf8;
}
.recovery-text {
    font-size: 21px;
    font-weight: 900;
    color: #22c55e;
}
.badge {
    display:inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #1e293b;
    border: 1px solid #475569;
    color: #e2e8f0;
    font-weight: 800;
    margin: 3px 4px 3px 0;
    font-size: 13px;
}
.stButton>button {
    width: 100%;
    padding: 17px 12px !important;
    background-color: #161b22 !important;
    color: #e6edf3 !important;
    border-radius: 14px !important;
    font-size: 16px !important;
    font-weight: 850 !important;
    border: 2px solid #30363d !important;
    margin-bottom: 11px;
    white-space: normal !important;
    height: auto !important;
    transition: all 0.2s ease;
}
.stButton>button:hover {
    background-color: #1e3a8a !important;
    border-color: #60a5fa !important;
    transform: translateY(-1px);
}
div[data-testid="stImage"] > img {
    border-radius: 18px;
    border: 2px solid #30363d;
}
.small-note {
    color:#94a3b8;
    font-size:13px;
    line-height:1.6;
}
hr {
    border-color: #334155;
}
.footer-box {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.7;
    padding: 18px 8px 4px 8px;
    margin-top: 18px;
}
.company-tag {
    text-align: center;
    color: #dbeafe;
    font-weight: 850;
    font-size: 14px;
    margin-top: -8px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 遊戲資料
# -----------------------------
ITEMS = {
    "護腰腰帶": {
        "emoji": "🦺",
        "desc": "遇到搬物關卡時，若選錯可減少一點傷害。",
        "effect": "lift_protect"
    },
    "減壓鞋墊": {
        "emoji": "👟",
        "desc": "遇到久站關卡時，降低足底與膝蓋負擔。",
        "effect": "stand_protect"
    },
    "水壺": {
        "emoji": "💧",
        "desc": "夜班疲勞時可提升恢復力。",
        "effect": "recovery_boost"
    },
    "伸展卡": {
        "emoji": "🃏",
        "desc": "完成恢復任務時，額外恢復 HP。",
        "effect": "stretch_boost"
    }
}

RANDOM_EVENTS = [
    "住戶臨時請你幫忙搬包裹，現場沒有推車。",
    "凌晨巡邏時發現地下室有障礙物，通道需要維持暢通。",
    "監視器畫面異常，需要連續盯著中控畫面確認狀況。",
    "主管臨時通知站崗延長 1 小時。",
    "訪客情緒激動，你需要在櫃檯前長時間站立協調。",
    "夜班後段開始想睡，不自覺駝背滑手機。",
]

LEVELS = [
    {
        "key": "lift",
        "title": "潛伏的重物腰斬者",
        "time": "凌晨 02:00",
        "image": "basement_lift.jpg",
        "caption": "地下室巡邏：阻礙物搬運中",
        "story": "巡邏時發現消防通道被一箱重物擋住。你需要在不傷到自己的情況下排除障礙。",
        "question": "你會怎麼做？",
        "options": [
            {
                "text": "直膝彎腰，用手臂力量迅速將箱子甩開。",
                "correct": False,
                "damage": 30,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "腰椎紅燈！",
                "feedback": "直膝彎腰會讓下背承受較大的剪力與壓力，尤其在疲勞、夜班或突然用力時更容易誘發不適。",
            },
            {
                "text": "蹲下、背挺直、箱子貼身，用大腿力量穩健站起。",
                "correct": True,
                "damage": 0,
                "sense": 12,
                "recovery": 4,
                "feedback_title": "完美防禦！",
                "feedback": "你使用了正確搬物策略：靠近物品、蹲下、貼身、用腿力，能有效降低腰部負擔。",
            }
        ],
        "skill_name": "蹲下搬物",
        "skill_tip": "口訣：靠近、蹲下、貼身、用腿力。若物品過重，應找人協助或使用推車。"
    },
    {
        "key": "sit",
        "title": "中控室的烏龜頸幻影",
        "time": "清晨 05:00",
        "image": "control_room.jpg",
        "caption": "中控室馬拉松：抵抗僵硬中",
        "story": "你已經盯著監視器好幾個小時，脖子和肩膀開始僵硬。烏龜頸幻影正在靠近。",
        "question": "哪一個做法比較能保護肩頸與下背？",
        "options": [
            {
                "text": "屁股坐滿椅子，背部有支撐，螢幕約在視線高度，定時站起來活動。",
                "correct": True,
                "damage": 0,
                "sense": 10,
                "recovery": 6,
                "feedback_title": "坐姿防線建立！",
                "feedback": "良好坐姿加上定時活動，比單純硬撐更能降低肩頸與下背負擔。",
            },
            {
                "text": "癱坐在椅子上，頭前伸靠近螢幕，撐到交班再說。",
                "correct": False,
                "damage": 30,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "頸椎鎖死！",
                "feedback": "頭前伸、駝背與癱坐會增加肩頸與下背負擔。久坐時最重要的是支撐、視線高度與定時變換姿勢。",
            }
        ],
        "skill_name": "中控室三招",
        "skill_tip": "坐滿、支撐、定時動。每 30–60 分鐘起身 1–3 分鐘，可做收下巴、肩胛後夾與胸口伸展。"
    },
    {
        "key": "stand",
        "title": "豪宅大門的足底滅殺者",
        "time": "早上 08:00",
        "image": "gate_standing.jpg",
        "caption": "社區大門守衛：雙腳壓力戰",
        "story": "下班前最後挑戰，你需要在社區大門站崗 2 小時。足底滅殺者準備攻擊你的腳底、膝蓋與下背。",
        "question": "請找出哪一個是危險站姿。",
        "options": [
            {
                "text": "雙膝死鎖，把重心完全壓在單腳，硬撐到交班。",
                "correct": True,
                "damage": 0,
                "sense": 12,
                "recovery": 4,
                "feedback_title": "風險辨識成功！",
                "feedback": "這是危險站姿。膝蓋死鎖與單腳承重會增加關節、足底與下背負擔。",
            },
            {
                "text": "微幅調整重心，膝蓋保持一點彈性，空檔做腳踝轉圈。",
                "correct": False,
                "damage": 15,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "判斷失誤！",
                "feedback": "這其實是正確策略。久站時應避免膝蓋死鎖，並以小幅度變換重心降低局部壓力。",
            }
        ],
        "skill_name": "久站保命站姿",
        "skill_tip": "口訣：膝蓋不鎖死、重心常交換、腳踝小活動。鞋墊、止滑鞋與短暫坐休也很重要。"
    },
    {
        "key": "stairs",
        "title": "巡邏樓梯的膝蓋破壞者",
        "time": "上午 09:30",
        "image": "stairs_patrol.jpg",
        "caption": "樓梯巡邏：膝蓋與足踝負荷戰",
        "story": "電梯暫停，你需要巡邏樓梯間。樓梯破壞者會在你疲勞、趕時間時偷襲膝蓋。",
        "question": "哪一個巡邏方式比較安全？",
        "options": [
            {
                "text": "一次跨兩階快速衝上去，越快完成越好。",
                "correct": False,
                "damage": 20,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "膝蓋受到衝擊！",
                "feedback": "疲勞時快速跨階容易增加膝蓋與足踝負擔，也可能提高跌倒風險。",
            },
            {
                "text": "扶手輔助、步伐穩定，必要時分段休息。",
                "correct": True,
                "damage": 0,
                "sense": 10,
                "recovery": 5,
                "feedback_title": "穩定巡邏成功！",
                "feedback": "使用扶手、控制速度、保持穩定，比快速硬衝更能降低受傷風險。",
            }
        ],
        "skill_name": "樓梯巡邏三原則",
        "skill_tip": "扶手、穩定、分段。巡邏不是競速，安全完成才是重點。"
    },
    {
        "key": "stress",
        "title": "訪客衝突的肩頸壓力獸",
        "time": "上午 10:30",
        "image": "front_desk_stress.jpg",
        "caption": "櫃檯協調：壓力與姿勢控制",
        "story": "訪客情緒激動，你需要長時間站在櫃檯協調。壓力獸會讓你聳肩、憋氣、下顎緊繃。",
        "question": "你會怎麼讓身體不要一起進入警報狀態？",
        "options": [
            {
               "text": "肩膀聳高、憋氣、整個人僵住，先撐過去再說。",
                "correct": False,
                "damage": 20,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "壓力獸附身！",
                "feedback": "長時間憋氣與聳肩會增加肩頸緊繃，也會讓疲勞感更明顯。",
            },
            {
                "text": "放鬆肩膀、慢慢吐氣，雙腳重心交替，讓身體保持彈性。",
                "correct": True,
                "damage": 0,
                "sense": 8,
                "recovery": 10,
                "feedback_title": "壓力控制成功！",
                "feedback": "面對壓力事件時，呼吸、肩膀放鬆與重心轉換能幫助身體降低緊繃。",
            }
        ],
        "skill_name": "壓力事件身體降溫",
        "skill_tip": "吐氣放慢、肩膀放下、下顎放鬆、重心交換。身體穩定，處理衝突也更穩。"
    },
    {
        "key": "fatigue",
        "title": "夜班疲勞的滑手機陷阱",
        "time": "交班前",
        "image": "night_fatigue.jpg",
        "caption": "夜班尾聲：疲勞與姿勢崩壞",
        "story": "交班前最容易鬆懈，你開始想睡，身體不自覺駝背、低頭滑手機。",
        "question": "哪一個做法比較能撐住最後的健康防線？",
        "options": [
            {
                "text": "設定短暫活動提醒，起身走動、補水、做 30 秒伸展。",
                "correct": True,
                "damage": 0,
                "sense": 8,
                "recovery": 12,
                "feedback_title": "疲勞防線成功！",
                "feedback": "微休息不是偷懶，而是維持警覺、降低痠痛與避免姿勢崩壞的重要策略。",
            },
            {
                "text": "繼續低頭滑手機，身體歪一邊，反正快下班了。",
                "correct": False,
                "damage": 25,
                "sense": 0,
                "recovery": 0,
                "feedback_title": "疲勞陷阱啟動！",
                "feedback": "低頭、歪斜與久坐不動會讓肩頸、下背與眼睛負擔增加。越接近下班，越需要小幅度活動。",
            }
        ],
        "skill_name": "夜班微休息",
        "skill_tip": "每 30–60 分鐘做 1–3 分鐘微休息：起身、補水、肩頸活動、腳踝轉圈。"
    },
]


# -----------------------------
# 狀態初始化
# -----------------------------
def init_state():
    defaults = {
        "screen": "start",
        "level_index": 0,
        "hp": 100,
        "guard_sense": 0,
        "recovery": 0,
        "item": None,
        "cards": [],
        "history": [],
        "random_event": random.choice(RANDOM_EVENTS),
        "pending_feedback": None,
        "practice_done": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def restart_game():
    for key in [
        "screen", "level_index", "hp", "guard_sense", "recovery", "item",
        "cards", "history", "random_event", "pending_feedback", "practice_done"
    ]:
        if key in st.session_state:
            del st.session_state[key]
    init_state()


init_state()


# -----------------------------
# 小工具
# -----------------------------
def clamp_values():
    st.session_state.hp = max(0, min(120, st.session_state.hp))
    st.session_state.guard_sense = max(0, st.session_state.guard_sense)
    st.session_state.recovery = max(0, st.session_state.recovery)


def show_header():
    st.markdown(f"<h1 class='game-title'>{GAME_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>{GAME_SUBTITLE}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle' style='font-size:15px; color:#bfdbfe; font-weight:800;'>合作單位｜{COMPANY_LINE}</p>", unsafe_allow_html=True)


def show_status():
    item_label = "尚未選擇"
    if st.session_state.item:
        item_label = f"{ITEMS[st.session_state.item]['emoji']} {st.session_state.item}"

    st.markdown(f"""
    <div class='status-card'>
        <div class='metric-label'>目前裝備</div>
        <div>{item_label}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-label'>HP 體力</div><div class='hp-text'>{st.session_state.hp}%</div>", unsafe_allow_html=True)
        st.progress(st.session_state.hp / 120)
    with col2:
        st.markdown(f"<div class='metric-label'>警覺值</div><div class='sense-text'>{st.session_state.guard_sense}</div>", unsafe_allow_html=True)
        st.progress(min(st.session_state.guard_sense / 60, 1.0))
    with col3:
        st.markdown(f"<div class='metric-label'>恢復力</div><div class='recovery-text'>{st.session_state.recovery}</div>", unsafe_allow_html=True)
        st.progress(min(st.session_state.recovery / 45, 1.0))


def show_image_if_exists(image_name, caption):
    """
    Streamlit Cloud 有時候執行目錄不一定等於 app.py 所在資料夾。
    因此這裡會依序搜尋：
    1. app.py 同一層
    2. 目前執行目錄
    3. images/ 子資料夾
    4. assets/ 子資料夾
    """
    app_dir = Path(__file__).parent
    candidates = [
        app_dir / image_name,
        Path.cwd() / image_name,
        app_dir / "images" / image_name,
        Path.cwd() / "images" / image_name,
        app_dir / "assets" / image_name,
        Path.cwd() / "assets" / image_name,
    ]

    for image_path in candidates:
        if image_path.exists():
            st.image(str(image_path), caption=caption, use_container_width=True)
            return

    searched = "<br>".join([str(p) for p in candidates])
    st.markdown(f"""
    <div class='story-box' style='text-align:center; border-style:dashed;'>
        <h3>🎬 場景圖：{caption}</h3>
        <p class='small-note'>目前未偵測到圖片檔 <b>{image_name}</b>。<br>
        請確認圖片檔名完全一致，並放在 app.py 同一層，或放在 images / assets 資料夾。</p>
        <p class='small-note'><b>程式已搜尋路徑：</b><br>{searched}</p>
    </div>
    """, unsafe_allow_html=True)


def apply_item_effect(level_key, damage):
    item = st.session_state.item
    if not item:
        return damage, None

    effect = ITEMS[item]["effect"]

    if level_key == "lift" and effect == "lift_protect" and damage > 0:
        return max(0, damage - 10), "🦺 護腰腰帶降低了搬物失誤傷害：傷害 -10。"

    if level_key == "stand" and effect == "stand_protect" and damage > 0:
        return max(0, damage - 10), "👟 減壓鞋墊降低了久站失誤傷害：傷害 -10。"

    if level_key == "fatigue" and effect == "recovery_boost":
        st.session_state.recovery += 5
        return damage, "💧 水壺幫助你維持夜班狀態：恢復力 +5。"

    return damage, None


def answer_level(option):
    level = LEVELS[st.session_state.level_index]

    damage = option["damage"]
    damage, item_msg = apply_item_effect(level["key"], damage)

    st.session_state.hp -= damage
    st.session_state.guard_sense += option["sense"]
    st.session_state.recovery += option["recovery"]

    if option["correct"] and level["skill_name"] not in st.session_state.cards:
        st.session_state.cards.append(level["skill_name"])

    st.session_state.history.append({
        "level": level["title"],
        "choice": option["text"],
        "correct": option["correct"],
        "damage": damage,
        "skill": level["skill_name"],
    })

    clamp_values()

    st.session_state.pending_feedback = {
        "correct": option["correct"],
        "title": option["feedback_title"],
        "feedback": option["feedback"],
        "skill_name": level["skill_name"],
        "skill_tip": level["skill_tip"],
        "damage": damage,
        "item_msg": item_msg
    }
    st.session_state.screen = "feedback"
    st.rerun()


def next_level():
    st.session_state.pending_feedback = None
    st.session_state.random_event = random.choice(RANDOM_EVENTS)

    # 每 2 關後插入一次實作任務
    if st.session_state.level_index in [1, 3] and not st.session_state.practice_done:
        st.session_state.screen = "practice"
        st.session_state.practice_done = True
        return

    st.session_state.practice_done = False
    st.session_state.level_index += 1

    if st.session_state.level_index >= len(LEVELS):
        st.session_state.screen = "ending"
    else:
        st.session_state.screen = "level"



def show_footer():
    st.markdown(f"""
    <div class='footer-box'>
        <div>合作單位｜{COMPANY_LINE}</div>
        <div>【版權聲明 {COPYRIGHT_TEXT}】</div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# 畫面：開始
# -----------------------------
show_header()

if st.session_state.screen == "start":
    st.markdown("""
    <div class='story-box'>
        <h3>🎮 任務初始化</h3>
        <p>你是今晚值勤的守衛「小全」。</p>
        <p>保全工作不是只有站崗與巡邏，也是一場對抗 <b>久站、久坐、搬物、樓梯、疲勞與壓力</b> 的身體防衛戰。</p>
        <p>你的任務：撐過夜班危機 8 小時，在下班前蒐集護體戰技，降低職業傷害風險。</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎒 選擇你的值勤裝備")
    item_options = list(ITEMS.keys())
    selected_item = st.radio(
        "每次任務只能帶一項裝備，不同裝備會影響關卡效果：",
        item_options,
        format_func=lambda x: f"{ITEMS[x]['emoji']} {x}｜{ITEMS[x]['desc']}"
    )

    st.info(f"⚠️ 今晚突發事件：{st.session_state.random_event}")

    if st.button("🚀 開始夜班任務"):
        st.session_state.item = selected_item
        st.session_state.screen = "level"
        st.rerun()


# -----------------------------
# 畫面：關卡
# -----------------------------
elif st.session_state.screen == "level":
    show_status()
    level = LEVELS[st.session_state.level_index]

    st.markdown(
        f"<span class='badge'>任務 {st.session_state.level_index + 1} / {len(LEVELS)}</span>"
        f"<span class='badge'>⏰ {level['time']}</span>",
        unsafe_allow_html=True
    )

    show_image_if_exists(level["image"], level["caption"])

    st.markdown(f"""
    <div class='story-box'>
        <h3>{st.session_state.level_index + 1}. {level['title']}</h3>
        <p>{level['story']}</p>
        <p><b>問題：</b>{level['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 隨機事件，不一定造成扣分，主要增加代入感
    st.markdown(f"""
    <div class='tip-box'>
        <b>⚠️ 現場變數：</b>{st.session_state.random_event}
    </div>
    """, unsafe_allow_html=True)

    for idx, option in enumerate(level["options"]):
        if st.button(option["text"], key=f"level_{st.session_state.level_index}_option_{idx}"):
            answer_level(option)


# -----------------------------
# 畫面：回饋
# -----------------------------
elif st.session_state.screen == "feedback":
    show_status()
    fb = st.session_state.pending_feedback

    if fb["correct"]:
        st.success(f"✅ {fb['title']}")
    else:
        st.error(f"💥 {fb['title']} 體力值 -{fb['damage']}%")

    if fb["item_msg"]:
        st.info(fb["item_msg"])

    st.markdown(f"""
    <div class='story-box'>
        <h3>戰鬥回饋</h3>
        <p>{fb['feedback']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='skill-card'>
        <h4>🃏 戰技卡：{fb['skill_name']}</h4>
        <p>{fb['skill_tip']}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("繼續值勤 ➡️"):
        next_level()
        st.rerun()


# -----------------------------
# 畫面：實作任務
# -----------------------------
elif st.session_state.screen == "practice":
    show_status()

    st.markdown("""
    <div class='story-box'>
        <h3>🧘 30 秒恢復任務</h3>
        <p>你找到短暫空檔，可以做一組不影響值勤的小動作。</p>
        <ul>
            <li>收下巴 5 次</li>
            <li>肩胛往後夾 5 次</li>
            <li>腳踝轉圈，左右各 5 次</li>
            <li>慢慢吐氣 3 回合，讓肩膀放下</li>
        </ul>
        <p>完成後點擊下方按鈕，恢復你的戰鬥體力。</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✅ 我完成恢復任務"):
        bonus = 10
        if st.session_state.item == "伸展卡":
            bonus += 8
            st.success("🃏 伸展卡發動！恢復效果提升。")
        st.session_state.hp += bonus
        st.session_state.recovery += 10
        clamp_values()
        st.success(f"恢復成功！HP +{bonus}，恢復力 +10。")

    if st.button("返回夜班任務 ➡️"):
        st.session_state.level_index += 1
        if st.session_state.level_index >= len(LEVELS):
            st.session_state.screen = "ending"
        else:
            st.session_state.screen = "level"
        st.rerun()


# -----------------------------
# 畫面：結算
# -----------------------------
elif st.session_state.screen == "ending":
    st.balloons()
    show_status()

    hp = st.session_state.hp
    sense = st.session_state.guard_sense
    recovery = st.session_state.recovery

    if hp >= 100 and sense >= 50:
        title = "🏅 傳奇鋼鐵守衛者"
        desc = "你不只成功下班，還能準確辨識職業傷害風險，是保全業健康防衛的模範。"
    elif hp >= 75:
        title = "🥈 精銳夜班衛士"
        desc = "你的值勤策略大致良好，已具備多數肌肉骨骼傷害預防觀念。"
    elif hp >= 45:
        title = "🩹 需要強化的巡邏員"
        desc = "你撐過任務，但身體負擔偏高。建議複習久站、久坐與搬物保護技巧。"
    else:
        title = "🚑 急需復健支援的預備役"
        desc = "你太常硬撐了！建議重新挑戰，優先練習姿勢變換、微休息與正確搬物。"

    st.markdown(f"""
    <div class='story-box' style='border: 2px solid #22c55e; background: rgba(20,83,45,0.28);'>
        <h3>🎉 任務完成：值勤健康報告</h3>
        <p style='font-size:22px; font-weight:900; color:#bbf7d0;'>{title}</p>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📋 本次表現")
    st.write(f"**最終 HP：** {hp}%")
    st.write(f"**風險警覺值：** {sense}")
    st.write(f"**恢復力：** {recovery}")

    st.markdown("### 🃏 已獲得護體戰技")
    if st.session_state.cards:
        for card in st.session_state.cards:
            st.markdown(f"<span class='badge'>🃏 {card}</span>", unsafe_allow_html=True)
    else:
        st.warning("本次沒有成功收集戰技卡，建議重新挑戰。")

    st.markdown("### 🔎 建議複習重點")
    suggestions = []
    if hp < 75:
        suggestions.append("減少硬撐，增加微休息與姿勢變換。")
    if sense < 45:
        suggestions.append("加強職業傷害風險辨識，例如危險搬物、久站死鎖、頭前伸。")
    if recovery < 35:
        suggestions.append("加強恢復策略，例如補水、伸展、呼吸放鬆與下班後放鬆。")
    if not suggestions:
        suggestions.append("表現良好，可將本次學到的戰技應用於實際值勤。")

    for s in suggestions:
        st.write(f"- {s}")

    with st.expander("查看本次選擇紀錄"):
        for h in st.session_state.history:
            mark = "✅" if h["correct"] else "❌"
            st.write(f"{mark} **{h['level']}**｜{h['choice']}｜傷害 -{h['damage']}")

    st.markdown("""
    <p class='small-note'>
    *本遊戲為職場健康促進與肌肉骨骼傷害預防衛教用途，不取代醫療診斷或治療。
    若已有明顯疼痛、麻木、無力或症狀持續，建議尋求專業評估。
    </p>
    """, unsafe_allow_html=True)

    if st.button("🔄 重新挑戰"):
        restart_game()
        st.rerun()


# -----------------------------
# 全站頁尾
# -----------------------------
show_footer()
