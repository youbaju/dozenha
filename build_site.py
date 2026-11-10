# يبني صفحات موقع دوزنها (عربي/إنجليزي في نفس الصفحة)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# روابط المتاجر: ضعها بعد النشر، وما دامت فارغة يظهر «قريباً»
LINKS = {
    'play': '',     # Google Play
    'chrome': '',   # Chrome Web Store
    'firefox': '',  # Firefox Add-ons
}

CSS = r"""
@font-face{font-family:DZCairo;src:url(fonts/cairo-arabic-wght-normal.woff2) format('woff2');font-weight:200 1000;font-display:swap;unicode-range:U+0600-06FF,U+0750-077F,U+0870-088E,U+0890-0891,U+0897-08E1,U+08E3-08FF,U+200C-200E,U+2010-2011,U+204F,U+2E41,U+FB50-FDFF,U+FE70-FE74,U+FE76-FEFC}
@font-face{font-family:DZCairo;src:url(fonts/cairo-latin-wght-normal.woff2) format('woff2');font-weight:200 1000;font-display:swap;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{--bg:#f6f3ee;--card:#fffdf9;--fg:#1f1c18;--muted:#6f675d;--line:#e4ddd2;--accent:#b5651d;--accent2:#f1dcc6;--hero:#2a2622}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#131210;--card:#1d1b18;--fg:#f1ece4;--muted:#a59d91;--line:#332f29;--accent:#e0954f;--accent2:#4a3019;--hero:#0d0c0b}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.8 DZCairo,system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif}
body.lang-ar .en,body.lang-en .ar{display:none!important}
a{color:var(--accent)}
.wrap{max-width:960px;margin:0 auto;padding:0 16px}
nav{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
nav .wrap{display:flex;align-items:center;gap:14px;height:60px}
.brand{display:flex;align-items:center;gap:8px;font-weight:800;font-size:19px;color:var(--fg);text-decoration:none}
.brand img{width:32px;height:32px;border-radius:9px}
nav .links{display:flex;gap:16px;margin-inline-start:auto;font-size:15px}
nav .links a{color:var(--fg);text-decoration:none;opacity:.8}
nav .links a:hover,nav .links a.on{opacity:1;color:var(--accent)}
.langbtn{border:1px solid var(--line);background:transparent;color:var(--fg);border-radius:9px;min-width:40px;height:34px;font:600 14px DZCairo,system-ui;cursor:pointer}
.hero{background:var(--hero);color:#fff;padding:56px 0 64px;text-align:center}
.hero img{width:96px;height:96px;border-radius:26px;box-shadow:0 12px 34px rgba(181,101,29,.45)}
.hero h1{font-size:40px;margin:14px 0 4px}
.hero p{font-size:20px;color:#e8dccd;margin:0 auto;max-width:640px}
.cta{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:26px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:12px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:16px}
.btn.primary{background:var(--accent);color:#fff}
.btn.ghost{background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.25)}
.btn.soon{opacity:.6;pointer-events:none}
.note-small{font-size:14px;color:#cbbfae;margin-top:12px}
.iphone{display:none;background:#5a3415;color:#fff;border-radius:14px;padding:14px;margin:22px auto 0;max-width:620px}
body.is-ios .iphone{display:block}
section{padding:46px 0}
h2{font-size:28px;margin:0 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}
.card h3{margin:0 0 6px;font-size:18px}
.card p{margin:0;color:var(--muted)}
.ico{font-size:26px}
.steps{counter-reset:s;list-style:none;padding:0;margin:0}
.steps li{counter-increment:s;position:relative;padding-inline-start:46px;margin:12px 0}
.steps li::before{content:counter(s);position:absolute;inset-inline-start:0;top:0;width:32px;height:32px;border-radius:50%;background:var(--accent2);color:var(--accent);font-weight:800;display:flex;align-items:center;justify-content:center}
.price{text-align:center}
.price .amt{font-size:30px;font-weight:800;color:var(--accent)}
.price.best{border:2px solid var(--accent)}
.badge{display:inline-block;background:var(--accent);color:#fff;border-radius:20px;padding:0 10px;font-size:13px}
.platforms{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.platforms span{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:4px 14px}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:8px 0}
summary{font-weight:700;cursor:pointer}
.doc{max-width:760px}
.doc h1{font-size:32px;margin:30px 0 4px}
.doc h2{font-size:21px;margin:28px 0 8px}
.doc .date{color:var(--muted)}
footer{border-top:1px solid var(--line);padding:26px 0 40px;color:var(--muted);font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px;align-items:center}
footer a{color:var(--muted)}
@media (max-width:640px){nav .links{gap:10px;font-size:13px}.hero h1{font-size:32px}.hero p{font-size:17px}.brand span{display:none}}
"""

JS = r"""
(function(){
  var KEY='dz_lang';
  function detect(){var l=(navigator.languages&&navigator.languages[0])||navigator.language||'ar';return /^ar/i.test(l)?'ar':'en';}
  var lang=detect(); try{var s=localStorage.getItem(KEY); if(s==='ar'||s==='en') lang=s;}catch(e){}
  function apply(){
    document.body.classList.remove('lang-ar','lang-en'); document.body.classList.add('lang-'+lang);
    document.documentElement.lang=lang; document.documentElement.dir=lang==='ar'?'rtl':'ltr';
    var t=document.body.getAttribute('data-title-'+lang); if(t) document.title=t;
    var b=document.getElementById('langbtn'); if(b){b.textContent=lang==='ar'?'EN':'ع';}
  }
  document.getElementById('langbtn').addEventListener('click',function(){lang=lang==='ar'?'en':'ar';try{localStorage.setItem(KEY,lang);}catch(e){}apply();});
  if(/iPhone|iPad|iPod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1)) document.body.classList.add('is-ios');
  apply();
})();
"""

def B(ar, en, tag='span'):
    return f'<{tag} class="ar">{ar}</{tag}><{tag} class="en">{en}</{tag}>'

def page(name, title_ar, title_en, body, desc_en):
    nav_items = [('index.html', 'الرئيسية', 'Home'), ('help.html', 'الشرح', 'Help'), ('about.html', 'من نحن', 'About'), ('privacy.html', 'الخصوصية', 'Privacy')]
    links = ''.join(f'<a href="{h}"{" class=on" if h == name else ""}>{B(a, e)}</a>' for h, a, e in nav_items)
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_ar}</title>
<meta name="description" content="{desc_en}">
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" href="icon-192.png">
<style>{CSS}</style>
</head>
<body class="lang-ar" data-title-ar="{title_ar}" data-title-en="{title_en}">
<nav><div class="wrap">
  <a class="brand" href="index.html"><img src="icon.svg" alt=""><span>{B('دوزنها', 'Dozenha')}</span></a>
  <div class="links">{links}</div>
  <button class="langbtn" id="langbtn" aria-label="Language">EN</button>
</div></nav>
{body}
<footer><div class="wrap">
  <span>© 2026 {B('دوزنها', 'Dozenha')}</span>
  <a href="help.html">{B('الشرح', 'Help')}</a><a href="about.html">{B('من نحن', 'About')}</a><a href="privacy.html">{B('سياسة الخصوصية', 'Privacy policy')}</a>
  <span>{B('يعمل على أندرويد والكمبيوتر', 'Works on Android and computers')}</span>
</div></footer>
<script>{JS}</script>
</body>
</html>
"""

def store_btn(key, ar, en, cls='ghost'):
    url = LINKS[key]
    if url:
        return f'<a class="btn {cls}" href="{url}" target="_blank" rel="noopener">{B(ar, en)}</a>'
    return f'<span class="btn {cls} soon">{B(ar + " — قريباً", en + " — coming soon")}</span>'

TAG_AR = 'تحكّم في دوزان وسرعة أي أغنية… من يوتيوب أو واتساب أو جهازك'
TAG_EN = 'Control the pitch & speed of any song — from YouTube, WhatsApp or your device'

# ---------------- الرئيسية ----------------
index = f"""
<header class="hero"><div class="wrap">
  <img src="icon.svg" alt="">
  <h1>{B('دوزنها', 'Dozenha')}</h1>
  <p>{B(TAG_AR, TAG_EN)}</p>
  <div class="cta">
    {store_btn('play', '▶ جرّب مجاناً على أندرويد', '▶ Try free on Android', 'primary')}
    {store_btn('chrome', 'للكمبيوتر: <bdi>Chrome</bdi> و <bdi>Edge</bdi>', 'For computers: Chrome & Edge')}
    {store_btn('firefox', 'Firefox', 'Firefox')}
  </div>
  <div class="note-small">{B('تجربة مجانية 7 أيام · بدون بطاقة دفع', '7-day free trial · no card required')}</div>
  <div class="iphone">{B('دوزنها يعمل حالياً على <b>أندرويد والكمبيوتر</b> فقط، ولا يعمل على الآيفون. افتح هذه الصفحة من الكمبيوتر لتجربته.', 'Dozenha currently works on <b>Android and computers</b> only — it doesn’t work on iPhone. Open this page on a computer to try it.')}</div>
</div></header>

<section><div class="wrap">
  <h2>{B('كل ما يحتاجه المغنّي والعازف', 'Everything singers and players need')}</h2>
  <div class="grid">
    <div class="card"><div class="ico">🎤</div><h3>{B('كاريوكي على طبقتك', 'Karaoke in your key')}</h3><p>{B('غنِّ أي أغنية كاريوكي من يوتيوب على طبقة صوتك، ودوزنها يتذكّر طبقتك لكل أغنية ويطبّقها تلقائياً.', 'Sing any YouTube karaoke track in your own key — Dozenha remembers your pitch for each song and applies it automatically.')}</p></div>
    <div class="card"><div class="ico">🎚️</div><h3>{B('الطبقة (الدوزان)', 'Pitch')}</h3><p>{B('ارفع أو اخفض أي أغنية بالتون أو النصف أو الربع، أو بشريط منزلق لأي قيمة حتى السنت الواحد.', 'Raise or lower any song by tones, semitones or quarter tones — or slide to any value, down to a single cent.')}</p></div>
    <div class="card"><div class="ico">⏱️</div><h3>{B('السرعة', 'Speed')}</h3><p>{B('بطّئ الأغنية للتمرين أو سرّعها، والطبقة تبقى كما هي.', 'Slow a song down to practice, or speed it up — the pitch stays the same.')}</p></div>
    <div class="card"><div class="ico">🔁</div><h3>{B('تكرار المقاطع', 'Loop sections')}</h3><p>{B('حدّد جملة صعبة وكرّرها، ودع السرعة ترتفع تدريجياً مع كل تكرار.', 'Pick a tricky phrase, loop it, and let the speed rise a little with every repeat.')}</p></div>
    <div class="card"><div class="ico">💾</div><h3>{B('حفظ المقاطع', 'Saved sections')}</h3><p>{B('احفظ مقاطعك لكل أغنية مع طبقتها وسرعتها، وارجع لها بضغطة.', 'Save sections for each song with their pitch and speed, and come back with one tap.')}</p></div>
    <div class="card"><div class="ico">▶️</div><h3>{B('يوتيوب', 'YouTube')}</h3><p>{B('لوحة دوزنها تظهر فوق الفيديو مباشرة. وعلى أندرويد: مشاركة ← دوزنها من تطبيق يوتيوب.', 'The Dozenha panel appears right over the video. On Android: Share → Dozenha from the YouTube app.')}</p></div>
    <div class="card"><div class="ico">📂</div><h3>{B('ملفات جهازك وواتساب', 'Your files & WhatsApp')}</h3><p>{B('افتح أي أغنية أو تسجيل، وعدّله، ونزّله MP3 أو M4A أو WAV وأرسله لمن تريد.', 'Open any song or recording, adjust it, and download it as MP3, M4A or WAV to share.')}</p></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <h2>{B('كيف أبدأ؟', 'How do I start?')}</h2>
  <div class="grid">
    <div class="card"><h3>{B('📱 على أندرويد', '📱 On Android')}</h3>
      <ol class="steps">
        <li>{B('ثبّت تطبيق دوزنها من Google Play.', 'Install the Dozenha app from Google Play.')}</li>
        <li>{B('اتبع شاشة الإعداد: ثبّت Firefox وأضف دوزنها إليه (مرة واحدة).', 'Follow the setup screen: install Firefox and add Dozenha to it (once).')}</li>
        <li>{B('من تطبيق يوتيوب: مشاركة ← دوزنها، وابدأ التمرين.', 'From the YouTube app: Share → Dozenha, and start practicing.')}</li>
      </ol></div>
    <div class="card"><h3>{B('💻 على الكمبيوتر', '💻 On a computer')}</h3>
      <ol class="steps">
        <li>{B('أضف دوزنها من متجر Chrome (يعمل أيضاً على Edge وBrave) أو متجر Firefox.', 'Add Dozenha from the Chrome Web Store (also works on Edge and Brave) or Firefox Add-ons.')}</li>
        <li>{B('افتح أي أغنية على يوتيوب واضغط زر دوزنها البرتقالي.', 'Open any song on YouTube and click the orange Dozenha button.')}</li>
        <li>{B('أو اضغط أيقونة دوزنها لفتح ملف من جهازك.', 'Or click the Dozenha icon to open a file from your computer.')}</li>
      </ol></div>
  </div>
  <div class="platforms">{''.join(f'<span>{B(a, e)}</span>' for a, e in [('✅ أندرويد', '✅ Android'), ('✅ Chrome', '✅ Chrome'), ('✅ Edge', '✅ Edge'), ('✅ Firefox', '✅ Firefox'), ('❌ الآيفون', '❌ iPhone')])}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <h2>{B('الأسعار', 'Pricing')}</h2>
  <p>{B('جرّب كل المزايا مجاناً 7 أيام (حتى 3 أغانٍ). بعدها اختر الخطة المناسبة. اشتراك واحد يفتح دوزنها على كل أجهزتك.', 'Try every feature free for 7 days (up to 3 songs). Then pick a plan — one subscription unlocks Dozenha on all your devices.')}</p>
  <div class="grid">
    <div class="card price"><h3>{B('شهري', 'Monthly')}</h3><div class="amt">{B('14.99 ريال', 'SAR 14.99')}</div><p>{B('شهرياً', 'per month')}</p></div>
    <div class="card price best"><span class="badge">{B('الأوفر', 'Best value')}</span><h3>{B('سنوي', 'Yearly')}</h3><div class="amt">{B('79 ريال', 'SAR 79')}</div><p>{B('سنوياً', 'per year')}</p></div>
    <div class="card price"><h3>{B('مدى الحياة', 'Lifetime')}</h3><div class="amt">{B('119 ريال', 'SAR 119')}</div><p>{B('دفعة واحدة', 'one-time')}</p></div>
  </div>
  <p class="note-small" style="color:var(--muted)">{B('الشراء يتم من داخل دوزنها بعد التجربة. يعمل على أندرويد والكمبيوتر فقط.', 'You buy from inside Dozenha after the trial. Works on Android and computers only.')}</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <h2>{B('أسئلة شائعة', 'FAQ')}</h2>
  <details><summary>{B('هل يناسب الكاريوكي؟', 'Is it good for karaoke?')}</summary><p>{B('نعم، وهذا من أكثر استخداماته. افتح أي فيديو كاريوكي على يوتيوب، وارفع أو اخفض الطبقة حتى تناسب صوتك، ودوزنها يتذكّرها لك في المرة القادمة.', 'Yes — it’s one of its most popular uses. Open any karaoke video on YouTube, raise or lower the pitch until it suits your voice, and Dozenha remembers it for next time.')}</p></details>
  <details><summary>{B('هل يعمل على الآيفون؟', 'Does it work on iPhone?')}</summary><p>{B('لا حالياً. دوزنها يعمل على أندرويد والكمبيوتر. مستخدم الآيفون يستطيع استخدامه على كمبيوتره.', 'Not at the moment. Dozenha works on Android and computers. iPhone users can use it on their computer.')}</p></details>
  <details><summary>{B('لماذا أحتاج Firefox على أندرويد؟', 'Why do I need Firefox on Android?')}</summary><p>{B('لأن تطبيق يوتيوب لا يسمح بأي تحكم في الصوت. Firefox يسمح لدوزنها بالعمل داخل يوتيوب بطريقة نظامية. تثبّته مرة واحدة فقط.', 'Because the YouTube app doesn’t allow any control over its sound. Firefox lets Dozenha work inside YouTube in a supported way. You install it once.')}</p></details>
  <details><summary>{B('هل يُرفع صوتي أو أغانيّ إلى الإنترنت؟', 'Are my songs uploaded anywhere?')}</summary><p>{B('لا. كل المعالجة تتم على جهازك. اقرأ <a href="privacy.html">سياسة الخصوصية</a>.', 'No. All processing happens on your device. Read the <a href="privacy.html">privacy policy</a>.')}</p></details>
  <details><summary>{B('هل الاشتراك يعمل على أكثر من جهاز؟', 'Does one subscription work on several devices?')}</summary><p>{B('نعم، مفتاح الترخيص يعمل على جوالك وكمبيوترك.', 'Yes — your license key works on your phone and your computer.')}</p></details>
</div></section>
"""

# ---------------- الشرح ----------------
help_ = f"""
<main class="wrap doc">
<h1>{B('طريقة استخدام دوزنها', 'How to use Dozenha')}</h1>

<h2>{B('١. التثبيت', '1. Installing')}</h2>
<p><b>{B('أندرويد:', 'Android:')}</b> {B('ثبّت تطبيق دوزنها من Google Play، ثم اتبع شاشة «الإعداد لأول مرة»: ثبّت Firefox، ثم اضغط «أضف دوزنها إلى Firefox» واختر «إضافة».', 'Install the Dozenha app from Google Play, then follow the “First-time setup” screen: install Firefox, tap “Add Dozenha to Firefox” and choose “Add”.')}</p>
<p><b>{B('الكمبيوتر:', 'Computer:')}</b> {B('افتح صفحة دوزنها في متجر Chrome أو Firefox واضغط «إضافة». يُفضّل تثبيت أيقونته: اضغط 🧩 بجانب شريط العنوان ثم 📌.', 'Open the Dozenha page in the Chrome Web Store or Firefox Add-ons and click “Add”. Pin its icon: click 🧩 next to the address bar, then 📌.')}</p>

<h2>{B('٢. فتح أغنية من يوتيوب', '2. Opening a YouTube song')}</h2>
<ul>
<li>{B('<b>من تطبيق يوتيوب (أندرويد):</b> مشاركة ← دوزنها. تفتح الأغنية في Firefox ولوحة دوزنها جاهزة.', '<b>From the YouTube app (Android):</b> Share → Dozenha. The song opens in Firefox with the panel ready.')}</li>
<li>{B('<b>من تطبيق دوزنها:</b> «افتح يوتيوب مع دوزنها»، أو الصق رابط الأغنية.', '<b>From the Dozenha app:</b> “Open YouTube with Dozenha”, or paste a song link.')}</li>
<li>{B('<b>أيقونة «يوتيوب دوزنها»:</b> أضفها من التطبيق إلى الشاشة الرئيسية لفتح يوتيوب مع دوزنها مباشرة.', '<b>“YouTube · Dozenha” icon:</b> add it from the app to your home screen to open YouTube with Dozenha directly.')}</li>
<li>{B('إذا سألك Firefox «افتح في تطبيق YouTube؟» اختر <b>«ابقَ في Firefox»</b>.', 'If Firefox asks “Open in the YouTube app?”, choose <b>“Stay in Firefox”</b>.')}</li>
</ul>

<h2>{B('٣. لوحة دوزنها', '3. The Dozenha panel')}</h2>
<p>{B('اضغط الزر البرتقالي العائم فوق الفيديو لإظهار اللوحة.', 'Tap the floating orange button over the video to show the panel.')}</p>
<ul>
<li>{B('<b>الطبقة:</b> أزرار التون والنصف والربع و±10 سنت، وشريط منزلق من −1200 إلى +1200 سنت (أوكتاف كامل).', '<b>Pitch:</b> tone, semitone, quarter-tone and ±10-cent buttons, plus a slider from −1200 to +1200 cents (a full octave).')}</li>
<li>{B('<b>السرعة:</b> من 0.5 إلى 1.5، والطبقة تبقى ثابتة.', '<b>Speed:</b> from 0.5 to 1.5 — the pitch stays the same.')}</li>
<li>{B('<b>تكرار مقطع:</b> اضغط «A بداية» ثم «B نهاية»، ويتكرر المقطع تلقائياً. «إلغاء» يوقف التكرار.', '<b>Loop a section:</b> press “A start”, then “B end”, and it loops automatically. “Clear” stops it.')}</li>
<li>{B('<b>رفع السرعة تدريجياً:</b> ابدأ ببطء، وفعّل الزر لترتفع السرعة 0.05 بعد كل عدد من التكرارات حتى 1×.', '<b>Gradual speed-up:</b> start slow and turn it on — speed rises by 0.05 every few loops until 1×.')}</li>
<li>{B('<b>مقاطعي:</b> اكتب اسماً واضغط «حفظ» لحفظ المقطع مع طبقته وسرعته. اضغط المقطع لتشغيله لاحقاً.', '<b>My sections:</b> type a name and press “Save” to store the section with its pitch and speed. Tap it to play it later.')}</li>
<li>{B('<b>تذكّر الطبقة:</b> دوزنها يحفظ آخر طبقة وسرعة لكل أغنية، ويطبّقها تلقائياً عندما تفتحها مرة أخرى. إذا فُتحت الأغنية من رابط، اضغط في أي مكان مرة واحدة لتطبيقها.', '<b>Remembered pitch:</b> Dozenha saves the last pitch and speed for each song and applies them when you open it again. If the song was opened from a link, tap anywhere once to apply.')}</li>
<li>{B('<b>↺ الأصل:</b> يرجع كل شيء كما كان: بدون تكرار، والطبقة والسرعة الأصلية.', '<b>↺ Reset:</b> returns everything to normal — no loop, original pitch and speed.')}</li>
<li>{B('<b>EN / ع:</b> لتبديل لغة الواجهة.', '<b>EN / ع:</b> switches the interface language.')}</li>
<li>{B('<b>على الكمبيوتر:</b> Alt+↑/↓ للطبقة نصف تون، وAlt+←/→ للسرعة.', '<b>On a computer:</b> Alt+↑/↓ changes pitch by a semitone, Alt+←/→ changes speed.')}</li>
</ul>

<h2>{B('٤. ملفات جهازك وواتساب', '4. Your files and WhatsApp')}</h2>
<ul>
<li>{B('<b>أندرويد:</b> من التطبيق «مشغّل الملفات»، أو من واتساب: اضغط مطولاً على التسجيل ← مشاركة ← دوزنها.', '<b>Android:</b> open “File player” in the app, or from WhatsApp: long-press the recording → Share → Dozenha.')}</li>
<li>{B('<b>الكمبيوتر:</b> اضغط أيقونة دوزنها في أي صفحة غير يوتيوب، أو زر «فتح ملف من جهازك» في اللوحة.', '<b>Computer:</b> click the Dozenha icon on any page other than YouTube, or “Open a file from your device” in the panel.')}</li>
<li>{B('<b>التنزيل:</b> اختر MP3 أو M4A أو WAV واضغط «تنزيل». على أندرويد تُحفظ في التنزيلات ← Dozenha، ويمكنك مشاركتها أو حفظها في مكان آخر.', '<b>Download:</b> choose MP3, M4A or WAV and press “Download”. On Android files go to Downloads → Dozenha, and you can share them or save them elsewhere.')}</li>
</ul>

<h2>{B('٥. التجربة والاشتراك', '5. Trial and subscription')}</h2>
<ul>
<li>{B('التجربة المجانية: 7 أيام، حتى 3 أغانٍ مختلفة، و3 مقاطع محفوظة، وتنزيلان.', 'Free trial: 7 days, up to 3 different songs, 3 saved sections and 2 downloads.')}</li>
<li>{B('للاشتراك: اضغط شارة الخطة في أعلى اللوحة ← «اشترِ دوزنها برو». يصلك مفتاح ترخيص بالبريد.', 'To subscribe: tap the plan badge at the top of the panel → “Buy Dozenha Pro”. You’ll receive a license key by email.')}</li>
<li>{B('للتفعيل: الصق المفتاح في خانة «عندك مفتاح ترخيص؟» واضغط «تفعيل». نفس المفتاح يعمل على جوالك وكمبيوترك.', 'To activate: paste the key under “Have a license key?” and press “Activate”. The same key works on your phone and computer.')}</li>
<li>{B('لنقل المفتاح إلى جهاز جديد: «إلغاء التفعيل من هذا الجهاز» ثم فعّله في الجهاز الجديد.', 'To move your key to a new device: “Deactivate on this device”, then activate it on the new one.')}</li>
</ul>

<h2>{B('٦. حل المشاكل', '6. Troubleshooting')}</h2>
<details><summary>{B('لا يظهر زر دوزنها على يوتيوب', 'The Dozenha button doesn’t appear on YouTube')}</summary><p>{B('حدّث الصفحة. وعلى أندرويد تأكد أنك في Firefox وليس في تطبيق يوتيوب، وأن الإضافة مفعّلة من قائمة الإضافات.', 'Reload the page. On Android make sure you are in Firefox, not the YouTube app, and that the add-on is enabled in the add-ons menu.')}</p></details>
<details><summary>{B('الصوت متأخر قليلاً عن الصورة عند تغيير الطبقة', 'Sound is slightly behind the video when the pitch is changed')}</summary><p>{B('هذا طبيعي في تغيير الطبقة المباشر (جزء من الثانية). عند الطبقة الأصلية لا يوجد أي تأخير.', 'That’s normal for live pitch shifting (a fraction of a second). At the original pitch there’s no delay.')}</p></details>
<details><summary>{B('الأغنية تفتح في تطبيق يوتيوب بدل Firefox', 'The song opens in the YouTube app instead of Firefox')}</summary><p>{B('عندما يسألك Firefox اختر «ابقَ في Firefox». ويمكنك من إعدادات Firefox ضبط «فتح الروابط في التطبيقات» على «أبداً».', 'When Firefox asks, choose “Stay in Firefox”. You can also set “Open links in apps” to “Never” in Firefox settings.')}</p></details>
</main>
"""

# ---------------- من نحن ----------------
about = f"""
<main class="wrap doc">
<h1>{B('من نحن', 'About')}</h1>
<p>{B('دوزنها فكرة وُلدت من داخل الموسيقى. صمّمه موسيقي سعودي، عازف عود ومغنٍّ ومدرّس موسيقى متخصص في المقامات العربية، بعد سنوات من مواجهة نفس المشكلة كل يوم: أغنية جميلة على يوتيوب، لكن طبقتها لا تناسب الصوت، أو دوزانها لا يوافق العود، أو سرعتها أعلى من أن يُتمرّن عليها.', 'Dozenha was born inside music. It was designed by a Saudi musician — an oud player, singer and music teacher specializing in Arabic maqam — after years of facing the same problem every day: a beautiful song on YouTube whose key doesn’t suit the voice, whose tuning doesn’t match the oud, or whose tempo is too fast to practice with.')}</p>
<p>{B('أردنا أداة بسيطة تفهم الموسيقي العربي: تحكّم دقيق بالطبقة يشمل أرباع الأصوات، وتكرار للجمل الصعبة، وسرعة تتدرّج مع التمرين، وتعمل على الجوال الذي يحمله العازف في يده وليس على الكمبيوتر فقط.', 'We wanted a simple tool that understands the Arab musician: precise pitch control that includes quarter tones, looping for difficult phrases, speed that grows with practice — and that works on the phone a musician actually holds, not only on a computer.')}</p>
<p>{B('دوزنها لكل مغنٍّ يبحث عن طبقته، ولكل عازف يريد أن يعزف مع أغنيته المفضّلة، ولكل مدرّس يريد أن يرسل لطلابه الأغنية على دوزان العود.', 'Dozenha is for every singer looking for their key, every player who wants to play along with a favorite song, and every teacher who wants to send students a song in the oud’s tuning.')}</p>
<h2>{B('مكتبات مفتوحة المصدر', 'Open-source credits')}</h2>
<p>{B('يستخدم دوزنها هذه المكتبات والخطوط المجانية، مع الشكر لأصحابها:', 'Dozenha uses these free libraries and fonts, with thanks to their authors:')}</p>
<ul>
<li><b>lamejs</b> — {B('لحفظ الأغاني بصيغة MP3. الرخصة: LGPL-3.0.', 'MP3 encoding. License: LGPL-3.0.')} <a href="https://github.com/zhuker/lamejs" target="_blank" rel="noopener">github.com/zhuker/lamejs</a></li>
<li><b>mp4-muxer</b> — {B('لحفظ الأغاني بصيغة M4A. الرخصة: MIT.', 'M4A export. License: MIT.')} <a href="https://github.com/Vanilagy/mp4-muxer" target="_blank" rel="noopener">github.com/Vanilagy/mp4-muxer</a></li>
<li><b>Cairo</b> — {B('خط الواجهة. الرخصة: SIL Open Font License 1.1.', 'Interface font. License: SIL Open Font License 1.1.')} <a href="https://github.com/Gue3bara/Cairo" target="_blank" rel="noopener">github.com/Gue3bara/Cairo</a></li>
</ul>
<h2>{B('التواصل', 'Contact')}</h2>
<p>{B('لأي سؤال أو اقتراح، تواصل معنا عبر صفحة دوزنها في Google Play أو متجر Chrome.', 'For any question or suggestion, contact us through the Dozenha page on Google Play or the Chrome Web Store.')}</p>
</main>
"""

# ---------------- الخصوصية ----------------
privacy = f"""
<main class="wrap doc">
<h1>{B('سياسة الخصوصية', 'Privacy policy')}</h1>
<p class="date">{B('آخر تحديث: 9 نوفمبر 2026', 'Last updated: November 9, 2026')}</p>
<p>{B('تنطبق هذه السياسة على إضافة دوزنها لمتصفحات Chrome وEdge وFirefox، وعلى تطبيق دوزنها لأندرويد. باختصار: <b>دوزنها لا يجمع بياناتك الشخصية، ولا يرفع أغانيك أو صوتك إلى أي مكان.</b>', 'This policy covers the Dozenha extension for Chrome, Edge and Firefox, and the Dozenha app for Android. In short: <b>Dozenha does not collect your personal data and never uploads your songs or audio anywhere.</b>')}</p>

<h2>{B('١. معالجة الصوت', '1. Audio processing')}</h2>
<p>{B('تغيير الطبقة والسرعة يتم بالكامل على جهازك. لا يُرسل صوت الفيديوهات ولا ملفاتك ولا تسجيلاتك إلى أي خادم.', 'Pitch and speed changes happen entirely on your device. Video audio, your files and your recordings are never sent to any server.')}</p>

<h2>{B('٢. ما يُحفظ على جهازك فقط', '2. What is stored only on your device')}</h2>
<ul>
<li>{B('المقاطع التي تحفظها (رقم الفيديو، اسم المقطع، وقت البداية والنهاية، الطبقة والسرعة).', 'Sections you save (video ID, section name, start and end time, pitch and speed).')}</li>
<li>{B('إعداداتك مثل لغة الواجهة.', 'Your settings, such as the interface language.')}</li>
<li>{B('بيانات الفترة التجريبية (تاريخ بدايتها وعدد الأغاني والتنزيلات المستخدمة).', 'Trial information (start date and the number of songs and downloads used).')}</li>
<li>{B('مفتاح الترخيص بعد التفعيل.', 'Your license key after activation.')}</li>
</ul>
<p>{B('هذه البيانات تبقى في متصفحك أو جوالك، ولا نستطيع نحن الاطلاع عليها. حذف الإضافة أو التطبيق يحذفها.', 'This data stays in your browser or phone and we cannot see it. Removing the extension or the app deletes it.')}</p>

<h2>{B('٣. التحقق من الاشتراك', '3. Subscription verification')}</h2>
<p>{B('عند تفعيل مفتاح الترخيص، ثم مرة كل أسبوع تقريباً، يرسل دوزنها <b>مفتاح الترخيص فقط</b> مع اسم عام للجهاز («Dozenha») إلى خدمة Lemon Squeezy للتأكد من صلاحيته. لا يُرسل أي شيء آخر.', 'When you activate a license key, and about once a week afterwards, Dozenha sends <b>only the license key</b> and a generic device name (“Dozenha”) to Lemon Squeezy to check that it is valid. Nothing else is sent.')}</p>

<h2>{B('٤. الشراء والدفع', '4. Purchases and payment')}</h2>
<p>{B('الشراء يتم عبر Lemon Squeezy، وهي البائع الرسمي التي تعالج الدفع والضرائب. بيانات الدفع والبريد الإلكتروني تُدخلها في صفحتهم مباشرة وتخضع <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">لسياسة خصوصيتهم</a>. دوزنها لا يرى بيانات بطاقتك.', 'Purchases are handled by Lemon Squeezy, the merchant of record that processes payment and taxes. You enter your payment details and email directly on their page, under <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">their privacy policy</a>. Dozenha never sees your card details.')}</p>

<h2>{B('٥. ما لا نفعله', '5. What we don’t do')}</h2>
<ul>
<li>{B('لا نستخدم أدوات تحليل أو تتبّع أو إعلانات.', 'No analytics, tracking or advertising.')}</li>
<li>{B('لا نقرأ سجل التصفح، ولا نصل إلى أي موقع غير يوتيوب.', 'We don’t read your browsing history or access any site other than YouTube.')}</li>
<li>{B('لا نبيع أو نشارك أي بيانات مع أي جهة.', 'We don’t sell or share any data with anyone.')}</li>
</ul>

<h2>{B('٦. الصلاحيات', '6. Permissions')}</h2>
<ul>
<li>{B('<b>الوصول إلى youtube.com:</b> لإظهار لوحة دوزنها وتعديل صوت الفيديو الذي تشاهده.', '<b>Access to youtube.com:</b> to show the Dozenha panel and adjust the audio of the video you are watching.')}</li>
<li>{B('<b>التخزين:</b> لحفظ مقاطعك وإعداداتك على جهازك.', '<b>Storage:</b> to keep your sections and settings on your device.')}</li>
<li>{B('<b>الاتصال بـ api.lemonsqueezy.com:</b> للتحقق من مفتاح الترخيص فقط.', '<b>Connecting to api.lemonsqueezy.com:</b> only to verify your license key.')}</li>
<li>{B('<b>تطبيق أندرويد:</b> يفتح الملفات التي تختارها أنت فقط، ويحفظ الأغاني المعدّلة في مجلد التنزيلات عندما تطلب ذلك.', '<b>Android app:</b> opens only the files you choose, and saves edited songs to your Downloads folder when you ask it to.')}</li>
</ul>

<h2>{B('٧. الأطفال', '7. Children')}</h2>
<p>{B('دوزنها لا يجمع بيانات من أي مستخدم، بمن فيهم الأطفال.', 'Dozenha does not collect data from any user, including children.')}</p>

<h2>{B('٨. التغييرات والتواصل', '8. Changes and contact')}</h2>
<p>{B('إذا تغيّرت هذه السياسة سنحدّث التاريخ أعلاه. لأي سؤال عن الخصوصية تواصل معنا عبر صفحة دوزنها في Google Play أو متجر Chrome.', 'If this policy changes, we will update the date above. For any privacy question, contact us through the Dozenha page on Google Play or the Chrome Web Store.')}</p>
<!-- البريد (اختياري لاحقاً): <p>البريد: ...</p> -->
</main>
"""

pages = [
    ('index.html', 'دوزنها – تحكّم في دوزان وسرعة أي أغنية', 'Dozenha – Control the pitch & speed of any song', index),
    ('help.html', 'طريقة الاستخدام – دوزنها', 'How to use – Dozenha', help_),
    ('about.html', 'من نحن – دوزنها', 'About – Dozenha', about),
    ('privacy.html', 'سياسة الخصوصية – دوزنها', 'Privacy policy – Dozenha', privacy),
]
for name, ta, te, body in pages:
    open(name, 'w').write(page(name, ta, te, body, TAG_EN))
print('built', [p[0] for p in pages])
