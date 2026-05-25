# === 自動生成フィールド（編集不要）===
TITLE = '食品ロス・廃棄コスト計算【無料】簡単・無料計算'
DESCRIPTION = '捨てた食品の金額・CO2量を記録して食品ロス削減をサポート。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '捨てた食品の金額・CO2量を記録して食品ロス削減をサポート。'
COLOR1 = '#E0E7FF'
COLOR2 = '#F0F4FF'
COLOR_BTN = '#6366F1'
FOOTER_LINKS = [('https://appadaycreator.github.io/fridge-tracker/', 'Fridge Tracker'), ('https://appadaycreator.github.io/expiry-date-tracker/', '食品賞味期限管理ツール'), ('https://appadaycreator.github.io/green-diary-app/', 'Green Diary App')]

# ================================================================
# 以下の3フィールドを実装してください
# ================================================================
# ヒント:
#   - MAIN_HTML: class="card" を使ったUI、class="result" で結果を隠す
#   - JS_CODE: DOMContentLoadedで初期化、onclick or addEventListener を使う
#   - 結果表示: document.getElementById('result').classList.add('show')
#   - 色参照: CSS変数 var(--btn, #6366F1) または直接 #6366F1 を使用
#
# === MAIN_HTML サンプル ===
# MAIN_HTML = """
# <div class="card">
#   <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">⚡ タイトル</h2>
#   <label>入力項目</label>
#   <input type="number" id="val1" placeholder="数値を入力" min="0">
#   <button class="btn" style="margin-top:20px;" onclick="calc()">計算する</button>
#   <div class="result" id="result" style="margin-top:16px;">
#     <div class="card" style="text-align:center;">
#       <div id="output" style="font-size:2rem;font-weight:700;color:#6366F1;"></div>
#       <p id="msg" style="color:#666;font-size:14px;margin-top:8px;"></p>
#     </div>
#   </div>
# </div>
# """
# === JS_CODE サンプル ===
# JS_CODE = """
# document.addEventListener('DOMContentLoaded', () => {
#   document.getElementById('val1').addEventListener('keydown', e => {
#     if (e.key === 'Enter') calc();
#   });
# });
# function calc() {
#   const v = parseFloat(document.getElementById('val1').value);
#   if (isNaN(v) || v <= 0) { alert('正しい値を入力してください'); return; }
#   const result = v * 2; // 実際のロジックに置き換える
#   document.getElementById('output').textContent = result.toFixed(0);
#   document.getElementById('msg').textContent = '計算完了';
#   document.getElementById('result').classList.add('show');
# }
# """

CUSTOM_CSS = """"""

# ↓ スケルトンを参考に、サービス固有のUI・ロジックを実装してください
MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">♻️ 食品ロス・廃棄コスト計算</h2>
  <!-- 入力フィールドをここに追加 -->

  <button class="btn" style="margin-top:20px;" onclick="calculate()">計算する</button>
  <div class="result" id="result" style="margin-top:16px;">
    <div class="card" style="text-align:center;">
      <div id="output" style="font-size:2.2rem;font-weight:700;color:#6366F1;padding:12px 0;"></div>
      <p id="detail" style="color:#666;font-size:14px;margin-top:4px;"></p>
    </div>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """// ★ここだけ実装（約10行）★
const CFG = {{
  inputs: ['val1'],         // 変更: ['val1','val2',...] など input の id
  error: '値を入力してください', // 変更: バリデーションエラー文
}};
function calcLogic(vals) {{
  const [v1] = vals;  // 変更: vals[0],vals[1]... で各入力値を取得
  const result = v1;  // 変更: 実際の計算式
  const detail = '';  // 変更: 補足説明（単位など）
  return {{ result, detail }};
}}
// ★以下変更不要★
document.addEventListener('DOMContentLoaded',()=>{{
  CFG.inputs.forEach(id=>{{ const el=document.getElementById(id); if(el) el.addEventListener('keydown',e=>{{ if(e.key==='Enter') calculate(); }}); }});
}});
function calculate(){{
  const vals=CFG.inputs.map(id=>parseFloat(document.getElementById(id)?.value)||0);
  if(!vals[0]){{ alert(CFG.error); return; }}
  const {{result,detail}}=calcLogic(vals);
  document.getElementById('output').textContent=typeof result==='number'?result.toLocaleString():result;
  const d=document.getElementById('detail'); if(d) d.textContent=detail||'';
  document.getElementById('result').classList.add('show');
}}"""

FAQ = [
    ("食品ロス・廃棄コスト計算は無料で使えますか？", "はい、完全無料・登録不要でご利用いただけます。"),
    ("計算結果は正確ですか？", "参考値としてご活用ください。重要な判断の際は専門家・公式機関にご確認ください。"),
    ("何回でも計算できますか？", "はい、回数制限なく何度でもご利用いただけます。条件を変えて比較にお使いください。"),
    ("入力したデータはどこかに保存されますか？", "いいえ。すべての計算はブラウザ内で処理され、データのサーバー送信は行いません。"),
    ("スマートフォンで利用できますか？", "はい、PC・スマートフォン・タブレットすべてに対応しています。"),
]

HOW_TO = [
    "入力フォームの各項目を確認する",
    "必要な数値・条件をすべて入力する",
    "計算ボタンをクリックして結果を取得する",
    "計算結果と詳細な内訳を確認する",
    "条件を変えて複数パターンを比較する",
]

