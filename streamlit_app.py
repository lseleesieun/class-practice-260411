import html

import streamlit as st


# Edit this profile block to personalize the page.
PROFILE = {
	"name": "이시은",
	"headline": "좋아하는 것을 오래, 깊게 만드는 사람",
	"intro": "안녕하세요! 새로운 것을 배우고, 작은 아이디어를 직접 만들어 보는 걸 좋아합니다.",
	"affiliation": "청주교육대학교",
	"dream": "사람들의 일상을 더 즐겁고 편리하게 만드는 사람이 되고 싶습니다.",
	"foods": ["떡볶이", "파스타", "딸기 케이크"],
}

FOOD_ICONS = {
	"떡볶이": "🍲",
	"파스타": "🍝",
	"딸기 케이크": "🍰",
}

st.set_page_config(page_title=f"{PROFILE['name']} 소개 페이지", page_icon="✨", layout="wide")

st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

	:root {
		--ink: #20242b;
		--paper: #fffdf8;
		--coral: #ff6b5e;
		--yellow: #ffc94a;
		--blue: #4d9de0;
		--mint: #39c6a0;
		--violet: #9c83e6;
		--pink: #f08db7;
	}

	.stApp {
		background-color: var(--paper);
		background-image: repeating-linear-gradient(135deg, rgba(32, 36, 43, 0.025) 0 1px, transparent 1px 9px);
		color: var(--ink);
		font-family: 'Gowun Dodum', sans-serif;
	}
	.stMainBlockContainer { max-width: 1080px; padding-top: 2rem; }
	h1, h2, h3, p, div, span, label { letter-spacing: 0; }
	.eyebrow {
		color: var(--coral); font-size: 15px; font-weight: 700;
		text-transform: uppercase; margin-bottom: 12px;
	}
	.hero-title {
		color: var(--ink); font-family: 'Jua', sans-serif;
		font-size: 58px; line-height: 1.16; margin: 0 0 18px;
	}
	.hero-title span { color: var(--blue); }
	.hero-copy { font-size: 19px; line-height: 1.8; max-width: 590px; }
	.section-label {
		color: var(--coral); font-size: 14px; font-weight: 700;
		margin: 8px 0 4px; text-transform: uppercase;
	}
	.section-title {
		color: var(--ink); font-family: 'Jua', sans-serif;
		font-size: 32px; margin: 0 0 20px;
	}
	.info-block {
		min-height: 150px; padding: 22px; border: 2px solid var(--ink);
		border-radius: 8px; color: var(--ink);
	}
	.info-block h3 { font-family: 'Jua', sans-serif; font-size: 21px; margin: 0 0 12px; }
	.info-block p { font-size: 17px; line-height: 1.65; margin: 0; }
	.affiliation { background: #dceeff; }
	.dream { background: #e2f8ed; }
	.favorite { background: #fff0c7; }
	.food-item {
		min-height: 112px; display: flex; align-items: center; gap: 14px;
		padding: 18px; border: 2px solid var(--ink); border-radius: 8px;
		font-family: 'Jua', sans-serif; font-size: 20px;
	}
	.food-item span { font-size: 34px; }
	.food-0 { background: #ffdcd5; }
	.food-1 { background: #dceeff; }
	.food-2 { background: #f0e9ff; }
	.closing-note {
		padding: 24px 28px; background: var(--ink); color: white;
		border-radius: 8px; font-size: 18px; line-height: 1.7;
	}
	@media (max-width: 700px) {
		.hero-title { font-size: 42px; }
		.hero-copy { font-size: 17px; }
	}
	</style>
	""",
	unsafe_allow_html=True,
)

name = html.escape(PROFILE["name"])
headline = html.escape(PROFILE["headline"])
intro = html.escape(PROFILE["intro"])
affiliation = html.escape(PROFILE["affiliation"])
dream = html.escape(PROFILE["dream"])

st.markdown('<div class="eyebrow">A LITTLE INTRODUCTION</div>', unsafe_allow_html=True)
st.markdown(
	f'<div class="hero-title">안녕,<br><span>나는 {name}</span></div>'
	f'<div class="hero-copy"><strong>{headline}</strong><br>{intro}</div>',
	unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">WHO I AM</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">나를 소개합니다</div>', unsafe_allow_html=True)

about_columns = st.columns(3, gap="medium")
about_items = [
	("affiliation", "🏫", "나의 소속", affiliation),
	("dream", "🚀", "나의 꿈", dream),
	("favorite", "🌟", "나를 표현하는 말", headline),
]

for column, (style, icon, title, description) in zip(about_columns, about_items):
	with column:
		st.markdown(
			f'<div class="info-block {style}"><h3>{icon} &nbsp;{title}</h3>'
			f'<p>{description}</p></div>',
			unsafe_allow_html=True,
		)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">MY FAVORITES</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">좋아하는 음식</div>', unsafe_allow_html=True)

food_columns = st.columns(max(len(PROFILE["foods"]), 1), gap="medium")
for index, (column, food) in enumerate(zip(food_columns, PROFILE["foods"])):
	icon = FOOD_ICONS.get(food, "🍽️")
	with column:
		st.markdown(
			f'<div class="food-item food-{index % 3}"><span>{icon}</span>{html.escape(food)}</div>',
			unsafe_allow_html=True,
		)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
	f'<div class="closing-note">앞으로의 목표<br><strong>{dream}</strong></div>',
	unsafe_allow_html=True,
)
