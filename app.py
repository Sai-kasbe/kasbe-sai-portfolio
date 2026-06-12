import streamlit as st
import base64
import os
from io import BytesIO
from PIL import Image

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Kasbe Sai | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------
# HELPERS
# -----------------------
def img_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

profile_b64 = img_to_base64("profile.jpeg")
bp_b64 = img_to_base64("bp/bp.png")
voting_b64 = img_to_base64("voting/voting.png")
encryption_b64 = img_to_base64("encryption/encryption.png")
resume_b64 = img_to_base64("resume.pdf")
def img_to_base64_rotated(path, angle=-90):
    if os.path.exists(path):
        img = Image.open(path)
        img = img.rotate(angle, expand=True)
        buf = BytesIO()
        img.save(buf, format="JPEG")
        return base64.b64encode(buf.getvalue()).decode()
    return ""

ai_cert_b64 = img_to_base64_rotated("certs/ai.jpeg")
msoffice_cert_b64 = img_to_base64("certs/msoffice.jpg")

# -----------------------
# GLOBAL CSS
# -----------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: radial-gradient(circle at 15% 0%, #102a4c 0%, #081224 35%, #050b18 100%);
    color: #ffffff;
}}

#MainMenu, footer, header {{visibility: hidden;}}

.block-container {{
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}}

h1, h2, h3, h4 {{
    font-family: 'Sora', sans-serif;
    color: #ffffff;
}}

p, li, span, div {{
    color: #cbd5e1;
}}

/* ---------- HERO ---------- */
.hero-wrap {{
    display: flex;
    align-items: center;
    gap: 50px;
    padding: 30px 10px 10px 10px;
}}

.profile-glow {{
    position: relative;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    flex-shrink: 0;
    transition: transform 0.35s ease;
}}

.profile-glow:hover {{
    transform: translateY(-4px) scale(1.02);
}}

.profile-glow::before {{
    content: "";
    position: absolute;
    inset: -10px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6, #3b82f6);
    filter: blur(24px);
    opacity: 0.5;
    z-index: 0;
    animation: pulse-glow 4s ease-in-out infinite;
}}

@keyframes pulse-glow {{
    0%, 100% {{ opacity: 0.4; transform: scale(1); }}
    50% {{ opacity: 0.7; transform: scale(1.05); }}
}}

.profile-glow img {{
    position: relative;
    z-index: 1;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid rgba(255,255,255,0.15);
    box-shadow: 0 12px 40px rgba(0,0,0,0.55), 0 0 0 8px rgba(59,130,246,0.06);
    transition: box-shadow 0.35s ease, border-color 0.35s ease;
}}

.profile-glow:hover img {{
    border-color: rgba(59,130,246,0.5);
    box-shadow: 0 16px 50px rgba(0,0,0,0.6), 0 0 0 10px rgba(59,130,246,0.12);
}}

.eyebrow {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    font-weight: 600;
    color: #93c5fd;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.3);
    padding: 6px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
}}

.hero-name {{
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
    margin: 4px 0 6px 0;
    background: linear-gradient(90deg, #ffffff, #93c5fd);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero-roles {{
    font-size: 19px;
    font-weight: 600;
    color: #93c5fd;
    margin-bottom: 10px;
    letter-spacing: 0.3px;
}}

.hero-roles span.dot {{
    color: #3b82f6;
    margin: 0 8px;
}}

.hero-tagline {{
    font-size: 16px;
    color: #cbd5e1;
    max-width: 520px;
    margin-bottom: 8px;
    font-weight: 300;
}}

/* ---------- STAT CARDS ---------- */
.stat-card {{
    position: relative;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 26px 14px;
    text-align: center;
    transition: all 0.3s ease;
    overflow: hidden;
}}

.stat-card::after {{
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, rgba(59,130,246,0.18), transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
}}

.stat-card:hover {{
    transform: translateY(-6px);
    border-color: rgba(59,130,246,0.5);
    box-shadow: 0 12px 30px rgba(59,130,246,0.2);
}}

.stat-card:hover::after {{ opacity: 1; }}

.stat-num {{
    font-family: 'Sora', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    position: relative;
    z-index: 1;
}}

.stat-label {{
    font-size: 13px;
    color: #94a3b8;
    margin-top: 4px;
    font-weight: 500;
    letter-spacing: 0.3px;
    position: relative;
    z-index: 1;
}}

.stat-bar {{
    width: 36px;
    height: 3px;
    border-radius: 2px;
    margin: 8px auto 0 auto;
}}

/* ---------- SECTION HEADERS ---------- */
.section-eyebrow {{
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #3b82f6;
    font-weight: 700;
    margin-bottom: 4px;
}}

.section-title {{
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 24px;
    color: #ffffff;
}}

/* ---------- GLASS CARD ---------- */
.glass-card {{
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 28px;
    height: 100%;
    transition: all 0.25s ease;
}}

.glass-card:hover {{
    border-color: rgba(59,130,246,0.35);
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
    transform: translateY(-3px);
}}

/* ---------- SKILL BADGES ---------- */
.skill-badge {{
    display: inline-block;
    padding: 9px 18px;
    margin: 6px 6px 6px 0;
    border-radius: 999px;
    background: rgba(59,130,246,0.10);
    border: 1px solid rgba(59,130,246,0.35);
    color: #bfdbfe;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s ease;
}}

.skill-badge:hover {{
    background: rgba(59,130,246,0.25);
    border-color: #3b82f6;
    transform: translateY(-2px);
}}

/* ---------- PROJECT CARD ---------- */
.project-card {{
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: all 0.25s ease;
}}

.project-card:hover {{
    border-color: rgba(59,130,246,0.4);
    box-shadow: 0 14px 34px rgba(0,0,0,0.4);
    transform: translateY(-5px);
}}

.project-img-wrap {{
    overflow: hidden;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}}

.project-img {{
    width: 100%;
    height: 170px;
    object-fit: cover;
    display: block;
    transition: transform 0.45s ease;
}}

.project-card:hover .project-img {{
    transform: scale(1.07);
}}

.ps-box {{
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 14px;
    font-size: 13px;
    line-height: 1.55;
}}
.ps-box b {{ color: #93c5fd; }}

/* ---------- HERO CTA BUTTONS ---------- */
.cta-row {{
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 6px;
}}

.cta-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 190px;
    height: 50px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.25s ease;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(255,255,255,0.05);
    color: #ffffff !important;
}}

.cta-btn.primary {{
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    border-color: rgba(59,130,246,0.5);
    box-shadow: 0 6px 20px rgba(59,130,246,0.35);
}}

.cta-btn:hover {{
    transform: translateY(-3px);
    border-color: #3b82f6;
    box-shadow: 0 10px 28px rgba(59,130,246,0.4);
    background: rgba(59,130,246,0.18);
}}

.cta-btn.primary:hover {{
    background: linear-gradient(135deg, #4f8ff7, #7c81f2);
}}

.availability-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 600;
    color: #86efac;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.3);
    padding: 8px 16px;
    border-radius: 999px;
    margin: 18px 0 0 0;
}}

/* ---------- TIMELINE ---------- */
.timeline {{
    position: relative;
    padding-left: 32px;
}}

.timeline::before {{
    content: "";
    position: absolute;
    left: 7px;
    top: 6px;
    bottom: 6px;
    width: 2px;
    background: linear-gradient(180deg, #3b82f6, rgba(59,130,246,0.1));
}}

.timeline-item {{
    position: relative;
    margin-bottom: 26px;
}}

.timeline-item::before {{
    content: "";
    position: absolute;
    left: -32px;
    top: 4px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #081224;
    border: 3px solid #3b82f6;
    transition: all 0.2s ease;
}}

.timeline-item:hover::before {{
    background: #3b82f6;
    box-shadow: 0 0 0 4px rgba(59,130,246,0.2);
}}

.timeline-year {{
    font-family: 'Sora', sans-serif;
    font-size: 13px;
    font-weight: 800;
    color: #3b82f6;
    letter-spacing: 1px;
    margin-bottom: 4px;
}}

.timeline-content {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 14px 18px;
    transition: all 0.2s ease;
}}

.timeline-item:hover .timeline-content {{
    border-color: rgba(59,130,246,0.35);
    transform: translateX(4px);
}}

.timeline-content b {{ color: #ffffff; }}

/* ---------- CONTACT GRID ---------- */
.contact-grid {{
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin: 24px 0 18px 0;
}}

.contact-pill {{
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 999px;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 600;
    color: #ffffff !important;
    text-decoration: none !important;
    transition: all 0.25s ease;
}}

.contact-pill:hover {{
    border-color: #3b82f6;
    background: rgba(59,130,246,0.15);
    transform: translateY(-3px);
}}

.project-body {{
    padding: 20px 22px 22px 22px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}}

.project-title {{
    font-family: 'Sora', sans-serif;
    font-size: 19px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}}

.project-desc {{
    font-size: 14px;
    color: #94a3b8;
    margin-bottom: 14px;
    line-height: 1.5;
    flex-grow: 1;
}}

.tech-row {{
    margin-bottom: 16px;
}}

.tech-pill {{
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    color: #cbd5e1;
    margin: 0 6px 6px 0;
}}

/* ---------- BUTTONS ---------- */
.btn-row {{ display: flex; gap: 10px; flex-wrap: wrap; }}

.btn-primary, .btn-outline {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}}

.btn-primary {{
    background: linear-gradient(90deg, #3b82f6, #2563eb);
    color: #ffffff !important;
    box-shadow: 0 4px 14px rgba(59,130,246,0.35);
}}
.btn-primary:hover {{ filter: brightness(1.12); transform: translateY(-2px); }}

.btn-outline {{
    background: rgba(255,255,255,0.04);
    border-color: rgba(255,255,255,0.18);
    color: #ffffff !important;
}}
.btn-outline:hover {{
    border-color: #3b82f6;
    background: rgba(59,130,246,0.12);
    transform: translateY(-2px);
}}

/* ---------- CERT / ACHIEVEMENT ---------- */
.cert-card {{
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    border-left: 4px solid #3b82f6;
    border-radius: 14px;
    padding: 18px 22px;
    height: 100%;
    transition: all 0.2s ease;
}}
.cert-card:hover {{ border-left-color: #8b5cf6; transform: translateX(4px); }}

.cert-title {{ font-weight: 700; font-size: 15px; color: #ffffff; margin-bottom: 2px; }}
.cert-sub {{ font-size: 13px; color: #94a3b8; }}

/* ---------- CERTIFICATE CARDS (with image) ---------- */
.cert-card-img {{
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: all 0.25s ease;
}}

.cert-card-img:hover {{
    border-color: rgba(59,130,246,0.4);
    box-shadow: 0 14px 34px rgba(0,0,0,0.4);
    transform: translateY(-5px);
}}

.cert-thumb-wrap {{
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    cursor: zoom-in;
}}

.cert-thumb {{
    width: 100%;
    height: 200px;
    object-fit: cover;
    display: block;
    transition: transform 0.45s ease, filter 0.3s ease;
}}

.cert-card-img:hover .cert-thumb {{
    transform: scale(1.06);
}}

.cert-zoom-hint {{
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(8,18,36,0.0);
    color: #ffffff;
    font-size: 13px;
    font-weight: 600;
    opacity: 0;
    transition: all 0.3s ease;
    backdrop-filter: blur(0px);
}}

.cert-thumb-wrap:hover .cert-zoom-hint {{
    opacity: 1;
    background: rgba(8,18,36,0.45);
    backdrop-filter: blur(2px);
}}

.cert-card-body {{
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    gap: 8px;
}}

.cert-verified-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 700;
    color: #86efac;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.3);
    padding: 4px 12px;
    border-radius: 999px;
    width: fit-content;
}}

.cert-card-title {{
    font-family: 'Sora', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #ffffff;
}}

.cert-card-issuer {{
    font-size: 13px;
    font-weight: 600;
    color: #93c5fd;
}}

.cert-card-desc {{
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.55;
    flex-grow: 1;
}}

/* ---------- CERTIFICATE LIGHTBOX ---------- */
.cert-lightbox {{
    display: none;
    position: fixed;
    inset: 0;
    z-index: 2000;
    background: rgba(5,11,24,0.88);
    backdrop-filter: blur(6px);
    align-items: center;
    justify-content: center;
    cursor: zoom-out;
    animation: fadeInLb 0.2s ease;
}}

.cert-lightbox.open {{ display: flex; }}

@keyframes fadeInLb {{
    from {{ opacity: 0; }}
    to {{ opacity: 1; }}
}}

.cert-lightbox img {{
    max-width: 90vw;
    max-height: 88vh;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}}

.cert-lightbox .lb-close {{
    position: absolute;
    top: 24px;
    right: 32px;
    color: #ffffff;
    font-size: 32px;
    font-weight: 700;
    cursor: pointer;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
}}

.cert-lightbox .lb-close:hover {{
    background: rgba(59,130,246,0.25);
    border-color: #3b82f6;
}}

.ach-card {{
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    border-left: 4px solid #f59e0b;
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 14px;
    transition: all 0.2s ease;
}}
.ach-card:hover {{ border-left-color: #fbbf24; transform: translateX(4px); }}

/* ---------- DIVIDER ---------- */
.section-divider {{
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.12), transparent);
    margin: 50px 0;
    border: none;
}}

/* ---------- FOOTER ---------- */
.footer-wrap {{
    text-align: center;
    padding: 40px 0 10px 0;
}}

.footer-icons a {{
    display: inline-block;
    margin: 0 10px;
    width: 46px;
    height: 46px;
    line-height: 46px;
    border-radius: 50%;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.12);
    color: #ffffff !important;
    text-decoration: none;
    font-size: 18px;
    transition: all 0.2s ease;
}}

.footer-icons a:hover {{
    background: #3b82f6;
    border-color: #3b82f6;
    transform: translateY(-3px);
}}

.footer-copy {{
    font-size: 13px;
    color: #64748b;
    margin-top: 18px;
}}

@media (max-width: 768px) {{
    .hero-wrap {{ flex-direction: column; text-align: center; }}
    .hero-name {{ font-size: 38px; }}
    .hero-tagline {{ margin: 0 auto 8px auto; }}
}}

/* ---------- STREAMLIT NATIVE BUTTON FIX (resume / github / linkedin) ---------- */
div[data-testid="stDownloadButton"] button,
div[data-testid="stLinkButton"] a {{
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
}}

div[data-testid="stDownloadButton"] button p,
div[data-testid="stLinkButton"] a p,
div[data-testid="stLinkButton"] a span {{
    color: #ffffff !important;
}}

div[data-testid="stDownloadButton"] button:hover,
div[data-testid="stLinkButton"] a:hover {{
    border-color: #3b82f6 !important;
    background: rgba(59,130,246,0.15) !important;
    color: #ffffff !important;
}}

html {{
    scroll-behavior: smooth;
}}

/* ---------- SCROLL PROGRESS BAR ---------- */
.scroll-progress {{
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    width: 0%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    z-index: 1001;
    transition: width 0.1s ease-out;
}}

/* ---------- TOP NAV ---------- */
.topnav {{
    position: sticky;
    top: 0;
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    flex-wrap: wrap;
    padding: 14px 26px;
    margin: -2.5rem -1rem 30px -1rem;
    background: rgba(8,18,36,0.78);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}}

.topnav .nav-logo {{
    font-family: 'Sora', sans-serif;
    font-weight: 800;
    font-size: 17px;
    color: #ffffff;
    letter-spacing: 0.5px;
    white-space: nowrap;
}}

.topnav .nav-links {{
    display: flex;
    align-items: center;
    gap: 4px;
    flex-wrap: wrap;
    justify-content: center;
    flex-grow: 1;
}}

.topnav a.nav-link {{
    color: #cbd5e1 !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.3px;
    padding: 8px 14px;
    border-radius: 999px;
    transition: all 0.2s ease;
}}

.topnav a.nav-link:hover {{
    color: #ffffff !important;
    background: rgba(59,130,246,0.18);
}}

.topnav a.nav-link.active {{
    color: #ffffff !important;
    background: rgba(59,130,246,0.25);
}}

.topnav a.hire-me {{
    display: inline-flex;
    align-items: center;
    white-space: nowrap;
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    color: #ffffff !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 700;
    padding: 9px 20px;
    border-radius: 999px;
    box-shadow: 0 4px 14px rgba(59,130,246,0.4);
    transition: all 0.2s ease;
}}

.topnav a.hire-me:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(59,130,246,0.55);
}}

@media (max-width: 900px) {{
    .topnav {{ flex-direction: column; gap: 10px; }}
    .topnav .nav-links {{ gap: 2px; }}
    .topnav a.nav-link {{ font-size: 12px; padding: 6px 10px; }}
}}

/* ---------- REFINED SECTION HEADINGS ---------- */
.section-eyebrow {{
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #3b82f6;
    font-weight: 700;
    margin-bottom: 6px;
}}

.section-title {{
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 24px;
    color: #ffffff;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}}

.hero-name {{
    font-size: 48px;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------
# SCROLL PROGRESS BAR
# -----------------------
st.markdown('<div class="scroll-progress" id="scrollProgress"></div>', unsafe_allow_html=True)

# -----------------------
# TOP NAVIGATION
# -----------------------
st.markdown("""
<div class="topnav" id="topnav">
    <div class="nav-logo">Kasbe Sai</div>
    <div class="nav-links">
        <a class="nav-link" data-section="home" href="#home">🏠 Home</a>
        <a class="nav-link" data-section="about" href="#about">👨‍💻 About</a>
        <a class="nav-link" data-section="skills" href="#skills">🛠 Skills</a>
        <a class="nav-link" data-section="projects" href="#projects">🚀 Projects</a>
        <a class="nav-link" data-section="certifications" href="#certifications">📜 Certifications</a>
        <a class="nav-link" data-section="achievements" href="#achievements">🏆 Achievements</a>
        <a class="nav-link" data-section="contact" href="#contact">📬 Contact</a>
    </div>
    <a class="hire-me" href="#contact">Hire Me 🚀</a>
</div>

<script>
const sections = ["home","about","skills","projects","certifications","achievements","contact"];

function updateNav() {{
    const doc = window.parent.document;
    const scrollEl = doc.querySelector('section.main') || doc.documentElement;
    const scrollTop = scrollEl.scrollTop || doc.documentElement.scrollTop;
    const scrollHeight = (scrollEl.scrollHeight || doc.documentElement.scrollHeight) - (scrollEl.clientHeight || doc.documentElement.clientHeight);
    const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    const bar = doc.getElementById("scrollProgress");
    if (bar) {{ bar.style.width = progress + "%"; }}

    let current = "home";
    for (const id of sections) {{
        const el = doc.getElementById(id);
        if (el) {{
            const rect = el.getBoundingClientRect();
            if (rect.top <= 140) {{ current = id; }}
        }}
    }}
    doc.querySelectorAll("a.nav-link").forEach(a => {{
        if (a.getAttribute("data-section") === current) {{
            a.classList.add("active");
        }} else {{
            a.classList.remove("active");
        }}
    }});
}}

const mainSection = window.parent.document.querySelector('section.main');
if (mainSection) {{
    mainSection.addEventListener('scroll', updateNav);
}}
window.parent.document.addEventListener('scroll', updateNav);
setTimeout(updateNav, 300);
</script>
""", unsafe_allow_html=True)

# -----------------------
# HOME ANCHOR
# -----------------------
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# -----------------------
# HERO SECTION
# -----------------------
st.markdown(f"""
<div class="hero-wrap">
    <div class="profile-glow">
        <img src="data:image/jpeg;base64,{profile_b64}">
    </div>
    <div>
        <div class="eyebrow">👋 Available for opportunities</div>
        <div class="hero-name">Kasbe Sai</div>
        <div class="hero-roles">Python Developer <span class="dot">•</span> Machine Learning Engineer <span class="dot">•</span> Full Stack Developer</div>
        <div class="hero-tagline">Building intelligent, secure and data-driven applications.</div>
        <div class="hero-tagline" style="font-size:14px; color:#64748b;">📍 Hyderabad, Telangana, India</div>
        <div class="availability-badge">🟢 Available for Internships, Freelance Projects and Entry-Level Software Roles</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Stat cards
s1, s2, s3, s4 = st.columns(4)
stats = [
    ("3+", "Projects", "#3b82f6"),
    ("2", "Live Apps", "#10b981"),
    ("2", "Certifications", "#8b5cf6"),
    ("7.61", "CGPA", "#f59e0b"),
]
for col, (num, label, color) in zip([s1, s2, s3, s4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
            <div class="stat-bar" style="background:{color};"></div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# Hero CTA buttons (premium glassmorphism)
resume_href = f"data:application/pdf;base64,{resume_b64}" if resume_b64 else "#"
st.markdown(f"""
<div class="cta-row">
    <a class="cta-btn primary" href="{resume_href}" download="Kasbe_Sai_Resume.pdf">📄 Download Resume</a>
    <a class="cta-btn" href="https://github.com/Sai-kasbe" target="_blank">💻 GitHub</a>
    <a class="cta-btn" href="https://www.linkedin.com/in/kasbe-sai" target="_blank">🔗 LinkedIn</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# ABOUT SECTION
# -----------------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">ABOUT</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">A bit about me</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <p style="font-size:16px; color:#cbd5e1; line-height:1.7; margin:0;">
    Final-year B.Tech Computer Science and Engineering (Data Science) student with hands-on experience
    in Python, machine learning, cybersecurity and full-stack development.
    <br><br>
    Built and deployed real-world applications including healthcare analytics dashboards,
    secure encryption systems and blockchain-based voting platforms.
    <br><br>
    Focused on creating practical, secure and user-friendly software solutions.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# SKILLS SECTION
# -----------------------
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">SKILLS</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Tools & Technologies</div>', unsafe_allow_html=True)

skills = ["Python", "Streamlit", "Flask", "Django", "Machine Learning",
          "Scikit-Learn", "SQLite", "Git", "GitHub", "HTML", "CSS", "JavaScript"]

badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
st.markdown(f'<div class="glass-card">{badges_html}</div>', unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# PROJECTS SECTION
# -----------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">PORTFOLIO</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects & Live Applications</div>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-img-wrap"><img class="project-img" src="data:image/png;base64,{bp_b64}"></div>
        <div class="project-body">
            <div class="project-title">Smart Blood Pressure Monitoring</div>
            <div class="project-desc">Machine Learning based healthcare dashboard for blood pressure prediction and BMI analytics.</div>
            <div class="ps-box">
                <b>Problem:</b> Manual BP tracking offers no predictive insight into health trends.<br>
                <b>Solution:</b> Built an ML-powered dashboard that predicts BP levels, analyzes BMI and visualizes health insights in real time.
            </div>
            <div class="tech-row">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Streamlit</span>
                <span class="tech-pill">Scikit-Learn</span>
            </div>
            <div class="btn-row">
                <a class="btn-outline" href="https://github.com/Sai-kasbe/smart-bp-monitoring" target="_blank">⭐ GitHub</a>
                <a class="btn-primary" href="https://smart-bp-monitoring-vxv6zrd6nkjqnrwgnemakf.streamlit.app/" target="_blank">🔗 Live Demo</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-img-wrap"><img class="project-img" src="data:image/png;base64,{voting_b64}"></div>
        <div class="project-body">
            <div class="project-title">Blockchain-Based Online Voting System</div>
            <div class="project-desc">Secure voting platform with OTP verification, role-based access control and result visualization.</div>
            <div class="ps-box">
                <b>Problem:</b> Need for secure, tamper-resistant digital voting.<br>
                <b>Solution:</b> Developed an OTP-based voting platform with role-based access and real-time result visualisation.
            </div>
            <div class="tech-row">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Streamlit</span>
                <span class="tech-pill">SQLite</span>
            </div>
            <div class="btn-row">
                <a class="btn-outline" href="https://github.com/Sai-kasbe/online-voting-system" target="_blank">⭐ GitHub</a>
                <a class="btn-primary" href="https://online-voting-system-kdlgdtqbpwnfmcvnckmlkb.streamlit.app" target="_blank">🔗 Live Demo</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-img-wrap"><img class="project-img" src="data:image/png;base64,{encryption_b64}"></div>
        <div class="project-body">
            <div class="project-title">Advance Encryption Tool</div>
            <div class="project-desc">AES-256 secure file encryption platform with authentication and access control.</div>
            <div class="ps-box">
                <b>Problem:</b> Sensitive files need strong protection during storage and sharing.<br>
                <b>Solution:</b> Built an AES-256 encryption platform with authenticated access control and bulk file encryption.
            </div>
            <div class="tech-row">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Flask</span>
                <span class="tech-pill">SQLite</span>
            </div>
            <div class="btn-row">
                <a class="btn-outline" href="https://github.com/Sai-kasbe/Advance-Encryption-Tool" target="_blank">⭐ GitHub</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# CERTIFICATIONS SECTION
# -----------------------
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">CREDENTIALS</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""
    <div class="cert-card-img">
        <div class="cert-thumb-wrap" onclick="document.getElementById('lb-ai').classList.add('open')">
            <img class="cert-thumb" src="data:image/jpeg;base64,{ai_cert_b64}">
            <div class="cert-zoom-hint">🔍 Click to enlarge</div>
        </div>
        <div class="cert-card-body">
            <div class="cert-verified-badge">🏅 Verified Certificate</div>
            <div class="cert-card-title">Artificial Intelligence For All</div>
            <div class="cert-card-issuer">IUCEE Foundation • 2025</div>
            <div class="cert-card-desc">Completed foundational training in Artificial Intelligence concepts, applications, and modern AI technologies.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="cert-card-img">
        <div class="cert-thumb-wrap" onclick="document.getElementById('lb-ms').classList.add('open')">
            <img class="cert-thumb" src="data:image/jpeg;base64,{msoffice_cert_b64}">
            <div class="cert-zoom-hint">🔍 Click to enlarge</div>
        </div>
        <div class="cert-card-body">
            <div class="cert-verified-badge">🏅 Verified Certificate</div>
            <div class="cert-card-title">Microsoft Office Certification</div>
            <div class="cert-card-issuer">Udemy</div>
            <div class="cert-card-desc">Completed training in Microsoft Office tools including Word, Excel, and PowerPoint.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Lightbox overlays for certificate enlargement
st.markdown(f"""
<div class="cert-lightbox" id="lb-ai" onclick="this.classList.remove('open')">
    <div class="lb-close" onclick="document.getElementById('lb-ai').classList.remove('open')">✕</div>
    <img src="data:image/jpeg;base64,{ai_cert_b64}" onclick="event.stopPropagation()">
</div>
<div class="cert-lightbox" id="lb-ms" onclick="this.classList.remove('open')">
    <div class="lb-close" onclick="document.getElementById('lb-ms').classList.remove('open')">✕</div>
    <img src="data:image/jpeg;base64,{msoffice_cert_b64}" onclick="event.stopPropagation()">
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# ACHIEVEMENTS SECTION
# -----------------------
st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">RECOGNITION</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Achievements</div>', unsafe_allow_html=True)

st.markdown("""
<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-year">2025</div>
        <div class="timeline-content">🚀 <b>Participant</b> — Kalam's Space Convention 2K25</div>
    </div>
    <div class="timeline-item">
        <div class="timeline-year">2025</div>
        <div class="timeline-content">🤖 <b>Certified</b> — Artificial Intelligence For All, IUCEE Foundation</div>
    </div>
    <div class="timeline-item">
        <div class="timeline-year">2024</div>
        <div class="timeline-content">🥈 <b>Runner-Up</b> — Data Wizard Competition, IKARUS National Level Technical Fest</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# -----------------------
# CONTACT / FOOTER
# -----------------------
st.markdown("""
<div class="footer-wrap" id="contact">
    <div class="section-eyebrow" style="text-align:center;">GET IN TOUCH</div>
    <div class="section-title" style="text-align:center; border-bottom:none;">Let's build something great</div>
    <div class="contact-grid">
        <a class="contact-pill" href="mailto:saisunilkasbe@gmail.com">📧 saisunilkasbe@gmail.com</a>
        <a class="contact-pill" href="https://github.com/Sai-kasbe" target="_blank">💻 GitHub</a>
        <a class="contact-pill" href="https://www.linkedin.com/in/kasbe-sai" target="_blank">🔗 LinkedIn</a>
        <a class="contact-pill" href="#" style="cursor:default;">📍 Hyderabad, Telangana, India</a>
    </div>
    <div class="footer-copy">© 2026 Kasbe Sai · Built with Streamlit</div>
</div>
""", unsafe_allow_html=True)
