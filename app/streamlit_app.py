import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time, random
from datetime import datetime, timedelta
from io import BytesIO

# ─────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PredictaShield – Industrial AI Platform",
    page_icon="🛡️", layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;900&family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ══════════════════════════════════════════
   ROOT DESIGN TOKENS  — v5.1 Refined
══════════════════════════════════════════ */
:root{
  --bg:#030916;
  --bg1:#071040;
  --bg2:#0A123D;
  --bg3:#0D1847;
  --bg4:#101E52;
  --bg-glass:rgba(7,13,48,0.88);
  --bgc:rgba(8,15,42,0.9);

  --a1:#00D4FF;
  --a2:#3B82F6;
  --a3:#39ff14;
  --aw:#ffc107;
  --ar:#ff2d55;
  --ap:#818CF8;
  --at:#06B6D4;
  --ao:#ff6b35;

  --t1:#EEF4FF;
  --t2:#7090C8;
  --t3:#3A5A8C;

  --bd:rgba(79,140,255,0.13);
  --bd2:rgba(37,99,235,0.28);
  --bd3:rgba(0,212,255,0.40);

  --gc:rgba(37,99,235,0.26);
  --gg:rgba(57,255,20,0.26);
  --go:rgba(59,130,246,0.26);
  --gw:rgba(255,193,7,0.26);
  --gr:rgba(255,45,85,0.26);
  --gp:rgba(129,140,248,0.26);

  --r4:20px;
  --r3:14px;
  --r2:10px;
  --r1:8px;
  --shadow-xl:0 28px 72px rgba(0,0,0,0.75),0 10px 28px rgba(0,5,46,0.65);
  --shadow-card:0 8px 32px rgba(0,5,46,0.55);
  --shadow-sm:0 3px 12px rgba(0,5,46,0.45);
  --shadow-glow-c:0 0 24px rgba(0,212,255,0.28),0 0 48px rgba(0,212,255,0.12);
  --shadow-glow-g:0 0 24px rgba(57,255,20,0.28),0 0 48px rgba(57,255,20,0.10);
  --shadow-glow-o:0 0 24px rgba(255,107,53,0.25),0 0 48px rgba(255,107,53,0.10);
}

/* ══════════════════════════════════════════
   BASE
══════════════════════════════════════════ */
html,body,[class*="css"]{
  font-family:'Inter',system-ui,sans-serif!important;
  background:linear-gradient(160deg,#030916 0%,#050d2a 40%,#0A123D 100%)!important;color:var(--t1)!important;
  -webkit-font-smoothing:antialiased!important;
  text-rendering:optimizeLegibility!important;
  font-feature-settings:'kern' 1,'liga' 1!important;
}
section[data-testid="stSidebar"],header[data-testid="stHeader"],#MainMenu,footer{display:none!important;}
.main .block-container{
  padding-top:0!important;padding-left:2rem!important;
  padding-right:2rem!important;max-width:1560px!important;
}

/* ══════════════════════════════════════════
   NAVBAR — Apex Glass · v6.0
══════════════════════════════════════════ */
.navbar{
  position:sticky;top:0;z-index:9999;
  background:
    linear-gradient(180deg,
      rgba(2,7,18,0.98) 0%,
      rgba(4,10,26,0.96) 60%,
      rgba(6,13,34,0.94) 100%);
  backdrop-filter:blur(60px) saturate(240%) brightness(1.06) contrast(1.02);
  -webkit-backdrop-filter:blur(60px) saturate(240%) brightness(1.06) contrast(1.02);
  padding:0 2.4rem;
  display:flex;align-items:center;justify-content:space-between;
  height:64px;
  border-bottom:none;
  box-shadow:
    0 1px 0 rgba(0,212,255,0.08),
    0 2px 0 rgba(0,212,255,0.03),
    0 4px 32px rgba(0,0,0,0.90),
    0 16px 64px rgba(0,4,36,0.75),
    inset 0 1px 0 rgba(255,255,255,0.035);
}

/* Animated chromatic bottom border — triple-layer */
.navbar::before{
  content:'';
  position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,
    transparent 0%,
    rgba(0,212,255,0)    4%,
    rgba(59,130,246,0.5) 18%,
    rgba(0,212,255,0.9)  35%,
    rgba(160,220,255,1)  50%,
    rgba(0,212,255,0.9)  65%,
    rgba(59,130,246,0.5) 82%,
    rgba(0,212,255,0)    96%,
    transparent 100%);
  background-size:300% 100%;
  animation:nbChrome 7s cubic-bezier(0.45,0,0.55,1) infinite;
  filter:blur(0.4px);
}
/* Glass-depth top line */
.navbar::after{
  content:'';
  position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,
    transparent 0%,
    rgba(255,255,255,0.03) 15%,
    rgba(255,255,255,0.08) 50%,
    rgba(255,255,255,0.03) 85%,
    transparent 100%);
  pointer-events:none;
}
@keyframes nbChrome{
  0%   { background-position:150% 0; opacity:0.6; }
  50%  { background-position:-50% 0; opacity:1;   }
  100% { background-position:-200% 0; opacity:0.6; }
}

/* ── BRAND ── */
.nb-brand{
  display:flex;align-items:center;gap:0.55rem;
  font-family:'Orbitron',monospace;font-size:0.92rem;font-weight:900;
  letter-spacing:0.20em;color:var(--a1);white-space:nowrap;flex-shrink:0;
  text-shadow:
    0 0 20px rgba(0,212,255,0.80),
    0 0 42px rgba(0,212,255,0.28),
    0 0 80px rgba(0,212,255,0.10);
  transition:all 0.35s cubic-bezier(0.4,0,0.2,1);
  cursor:default;
  user-select:none;
}
.nb-brand:hover{
  text-shadow:
    0 0 28px rgba(0,212,255,1.00),
    0 0 56px rgba(0,212,255,0.45),
    0 0 100px rgba(0,212,255,0.18);
  letter-spacing:0.22em;
}
.nb-brand .brand-icon{
  width:34px;height:34px;border-radius:9px;
  background:linear-gradient(145deg,rgba(0,212,255,0.15),rgba(37,99,235,0.10));
  border:1px solid rgba(0,212,255,0.22);
  display:flex;align-items:center;justify-content:center;
  font-size:1.05rem;flex-shrink:0;
  box-shadow:
    0 0 14px rgba(0,212,255,0.25),
    0 0 28px rgba(0,212,255,0.10),
    inset 0 1px 0 rgba(255,255,255,0.07);
  transition:all 0.3s ease;
  filter:drop-shadow(0 0 6px rgba(0,212,255,0.6));
}
.nb-brand:hover .brand-icon{
  box-shadow:
    0 0 22px rgba(0,212,255,0.45),
    0 0 44px rgba(0,212,255,0.18),
    inset 0 1px 0 rgba(255,255,255,0.10);
  background:linear-gradient(145deg,rgba(0,212,255,0.22),rgba(37,99,235,0.16));
  transform:rotate(-5deg) scale(1.05);
}
.nb-brand .brand-txt{
  display:flex;flex-direction:column;gap:0;
}
.nb-brand .brand-main{
  display:flex;align-items:baseline;gap:0.05em;
  font-size:0.92rem;font-weight:900;letter-spacing:0.18em;
}
.nb-brand .brand-ps{ color:var(--a1); }
.nb-brand .brand-s2{ color:rgba(0,170,210,0.80); }
.nb-brand .brand-tag{
  font-family:'JetBrains Mono',monospace;
  font-size:0.41rem;font-weight:500;
  color:rgba(0,212,255,0.50);letter-spacing:0.06em;
  background:linear-gradient(135deg,rgba(0,212,255,0.09),rgba(0,212,255,0.04));
  border:1px solid rgba(0,212,255,0.16);
  border-radius:4px;padding:2px 7px;margin-left:6px;vertical-align:middle;
  box-shadow:inset 0 1px 0 rgba(0,212,255,0.07);
  transition:all 0.25s ease;
  white-space:nowrap;
}
.nb-brand:hover .brand-tag{
  border-color:rgba(0,212,255,0.32);
  background:rgba(0,212,255,0.12);
  color:rgba(0,212,255,0.85);
}

/* ── NAV PILL CONTAINER ── */
.nb-links{
  display:flex;gap:0.08rem;align-items:center;
  background:linear-gradient(180deg,rgba(255,255,255,0.020),rgba(255,255,255,0.008));
  border:1px solid rgba(255,255,255,0.055);
  border-radius:14px;
  padding:0.30rem 0.32rem;
  backdrop-filter:blur(16px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.04),
    inset 0 -1px 0 rgba(0,0,0,0.2),
    0 2px 16px rgba(0,0,0,0.45);
}

/* ── NAV BUTTONS ── */
.nbtn{
  font-family:'Orbitron',monospace;
  font-size:0.48rem;font-weight:700;
  letter-spacing:0.11em;text-transform:uppercase;
  color:rgba(70,105,160,1);
  background:transparent;
  border:1px solid transparent;
  border-radius:10px;
  padding:0.44rem 0.76rem;
  cursor:pointer;
  position:relative;
  white-space:nowrap;
  overflow:hidden;
  transition:
    color        0.20s cubic-bezier(0.4,0,0.2,1),
    background   0.20s cubic-bezier(0.4,0,0.2,1),
    border-color 0.20s cubic-bezier(0.4,0,0.2,1),
    box-shadow   0.20s cubic-bezier(0.4,0,0.2,1),
    transform    0.16s cubic-bezier(0.34,1.56,0.64,1),
    letter-spacing 0.20s ease;
}
/* Shine sweep on hover */
.nbtn::before{
  content:'';
  position:absolute;top:0;left:-100%;width:100%;height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.06),transparent);
  transition:left 0.4s ease;
  pointer-events:none;
}
/* Active/hover underline bar */
.nbtn::after{
  content:'';
  position:absolute;bottom:4px;left:50%;right:50%;
  height:1.5px;border-radius:2px;
  background:linear-gradient(90deg,transparent,rgba(0,212,255,0.9),transparent);
  transition:left 0.22s cubic-bezier(0.4,0,0.2,1),
             right 0.22s cubic-bezier(0.4,0,0.2,1),
             opacity 0.22s ease;
  opacity:0;
}
.nbtn:hover{
  color:rgba(200,235,255,0.95);
  border-color:rgba(0,212,255,0.16);
  background:linear-gradient(160deg,rgba(0,212,255,0.065),rgba(37,99,235,0.04));
  text-shadow:0 0 12px rgba(0,212,255,0.50);
  transform:translateY(-1.5px);
  letter-spacing:0.12em;
  box-shadow:
    0 4px 20px rgba(0,3,40,0.5),
    0 0 14px rgba(0,212,255,0.10),
    inset 0 1px 0 rgba(0,212,255,0.06);
}
.nbtn:hover::before{ left:100%; }
.nbtn:hover::after { left:18%;right:18%;opacity:0.55; }
.nbtn.active{
  color:#00e8ff;
  background:linear-gradient(160deg,
    rgba(0,212,255,0.16) 0%,
    rgba(0,212,255,0.09) 50%,
    rgba(37,99,235,0.08) 100%);
  border-color:rgba(0,212,255,0.35);
  box-shadow:
    0 0 22px rgba(0,212,255,0.20),
    0 0 44px rgba(0,212,255,0.08),
    inset 0 1px 0 rgba(0,212,255,0.18),
    inset 0 -1px 0 rgba(0,212,255,0.06),
    inset 0 0 20px rgba(0,212,255,0.04);
  text-shadow:
    0 0 12px rgba(0,212,255,0.85),
    0 0 24px rgba(0,212,255,0.35);
  transform:translateY(-1.5px);
  letter-spacing:0.12em;
}
.nbtn.active::after{
  left:12%;right:12%;opacity:1;
  background:linear-gradient(90deg,transparent,rgba(0,212,255,1),transparent);
  height:2px;
  filter:blur(0.5px);
}

/* ── RIGHT CLUSTER ── */
.nb-right{
  display:flex;align-items:center;gap:0.65rem;flex-shrink:0;
}
/* Separator pill */
.nb-sep{
  width:1px;height:22px;
  background:linear-gradient(180deg,
    transparent,rgba(79,140,255,0.25),transparent);
}

/* ── LIVE INDICATOR ── */
.ldot{
  display:inline-block;width:7px;height:7px;
  background:var(--a3);border-radius:50%;
  box-shadow:0 0 8px var(--a3),0 0 18px rgba(57,255,20,0.55);
  animation:liveBlip 2.2s ease-in-out infinite;
  margin-right:4px;vertical-align:middle;flex-shrink:0;
}
@keyframes liveBlip{
  0%   { transform:scale(1.0); opacity:1;
         box-shadow:0 0 7px var(--a3),0 0 16px rgba(57,255,20,0.5); }
  35%  { transform:scale(1.4); opacity:0.9;
         box-shadow:0 0 14px var(--a3),0 0 0 6px rgba(57,255,20,0),0 0 30px rgba(57,255,20,0.35); }
  65%  { transform:scale(0.85);opacity:1;
         box-shadow:0 0 5px var(--a3),0 0 12px rgba(57,255,20,0.4); }
  100% { transform:scale(1.0); opacity:1;
         box-shadow:0 0 7px var(--a3),0 0 16px rgba(57,255,20,0.5); }
}
.nb-live-wrap{
  display:flex;align-items:center;gap:5px;
  background:rgba(57,255,20,0.04);
  border:1px solid rgba(57,255,20,0.12);
  border-radius:20px;padding:4px 10px;
  box-shadow:0 0 12px rgba(57,255,20,0.06);
}
.nb-live-label{
  font-family:'JetBrains Mono',monospace;
  font-size:0.53rem;font-weight:700;
  color:rgba(57,255,20,0.90);letter-spacing:0.13em;
  text-shadow:0 0 10px rgba(57,255,20,0.55);
}

/* ── ENGINE TAG ── */
.nav-v{
  font-family:'JetBrains Mono',monospace;font-size:0.48rem;
  color:rgba(0,212,255,0.68);
  border:1px solid rgba(0,212,255,0.16);
  border-radius:7px;
  padding:4px 11px;letter-spacing:0.09em;
  background:linear-gradient(135deg,rgba(0,212,255,0.07),rgba(0,212,255,0.03));
  box-shadow:
    0 0 12px rgba(0,212,255,0.08),
    inset 0 1px 0 rgba(0,212,255,0.07);
  text-shadow:0 0 10px rgba(0,212,255,0.45);
  transition:all 0.22s ease;
  cursor:default;
}
.nav-v:hover{
  border-color:rgba(0,212,255,0.32);
  background:rgba(0,212,255,0.10);
  color:rgba(0,212,255,0.95);
  box-shadow:0 0 20px rgba(0,212,255,0.16);
  text-shadow:0 0 14px rgba(0,212,255,0.70);
}

/* ══════════════════════════════════════════
   KPI CARDS — Apex Glassmorphism · v6.0
══════════════════════════════════════════ */
.kc {
  position: relative;
  /* Deep multi-layer glass base */
  background:
    linear-gradient(145deg,
      rgba(10,18,50,0.92) 0%,
      rgba(6,12,36,0.88) 55%,
      rgba(8,14,42,0.85) 100%);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  border-radius: 20px;
  padding: 1.45rem 1.35rem 1.25rem;
  overflow: hidden;
  isolation: isolate;
  cursor: default;
  /* Fluid layout */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 148px;
  /* Default shadow stack */
  box-shadow:
    0 1px 0 rgba(255,255,255,0.06) inset,
    0 -1px 0 rgba(0,0,0,0.35) inset,
    0 12px 40px rgba(0,0,0,0.65),
    0 4px 16px rgba(0,2,30,0.55),
    0 0 0 1px rgba(255,255,255,0.04) inset;
  /* Transition everything smoothly */
  transition:
    transform    0.32s cubic-bezier(0.34,1.36,0.64,1),
    box-shadow   0.32s cubic-bezier(0.4,0,0.2,1),
    background   0.32s ease,
    border-color 0.32s ease;
}

/* ── Layer 1: animated gradient border (mask trick) ── */
.kc::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: 20px;
  padding: 1.5px;
  background: linear-gradient(135deg, #FF6B9D 0%, #C84B9E 40%, #FF9A3C 100%);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0.65;
  transition: opacity 0.32s ease, filter 0.32s ease;
}

/* ── Layer 2: glass sheen + noise texture ── */
.kc::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: 20px;
  background:
    linear-gradient(145deg,
      rgba(255,255,255,0.075) 0%,
      rgba(255,255,255,0.020) 30%,
      transparent            55%,
      rgba(255,255,255,0.010) 100%);
  pointer-events: none;
}

/* ── Animated inner ambient glow (pseudo via box-shadow on hover) ── */
.kc:hover {
  transform: translateY(-9px) scale(1.025);
  box-shadow:
    0 1px 0 rgba(255,255,255,0.08) inset,
    0 -1px 0 rgba(0,0,0,0.35) inset,
    0 24px 64px rgba(255,100,150,0.20),
    0 12px 32px rgba(0,0,0,0.70),
    0 0 48px rgba(255,100,150,0.08),
    0 0 0 1px rgba(255,255,255,0.06) inset;
}
.kc:hover::before {
  opacity: 1;
  filter: blur(0.5px) brightness(1.15);
}

/* ── Colour variants ── */
/* Cyan → Blue */
.kc.g::before { background: linear-gradient(135deg,#00D4FF 0%,#00A8D8 35%,#2563EB 100%); }
.kc.g:hover   { box-shadow:
    0 1px 0 rgba(0,212,255,0.12) inset,
    0 24px 64px rgba(0,212,255,0.20),
    0 12px 32px rgba(0,0,0,0.65),
    0 0 56px rgba(0,212,255,0.10); }

/* Pink → Orange */
.kc.o::before { background: linear-gradient(135deg,#FF6B9D 0%,#FF5080 35%,#FF9A3C 100%); }
.kc.o:hover   { box-shadow:
    0 1px 0 rgba(255,100,150,0.12) inset,
    0 24px 64px rgba(255,100,150,0.20),
    0 12px 32px rgba(0,0,0,0.65),
    0 0 56px rgba(255,100,150,0.10); }

/* Blue → Violet */
.kc.y::before { background: linear-gradient(135deg,#3B82F6 0%,#6366F1 45%,#7C3AED 100%); }
.kc.y:hover   { box-shadow:
    0 1px 0 rgba(99,102,241,0.12) inset,
    0 24px 64px rgba(99,102,241,0.22),
    0 12px 32px rgba(0,0,0,0.65),
    0 0 56px rgba(99,102,241,0.10); }

/* Purple → Pink */
.kc.r::before { background: linear-gradient(135deg,#8B5CF6 0%,#A855F7 40%,#EC4899 100%); }
.kc.r:hover   { box-shadow:
    0 1px 0 rgba(168,85,247,0.12) inset,
    0 24px 64px rgba(168,85,247,0.22),
    0 12px 32px rgba(0,0,0,0.65),
    0 0 56px rgba(168,85,247,0.10); }

/* Cyan → Purple */
.kc.p::before { background: linear-gradient(135deg,#00D4FF 0%,#818CF8 50%,#8B5CF6 100%); }
.kc.p:hover   { box-shadow:
    0 1px 0 rgba(129,140,248,0.12) inset,
    0 24px 64px rgba(129,140,248,0.20),
    0 12px 32px rgba(0,0,0,0.65),
    0 0 56px rgba(129,140,248,0.10); }

/* ── Sub-elements ── */
.kc-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 0.65rem;
  position: relative; z-index: 2;
}

/* Icon badge */
.kc-ic {
  font-size: 1.4rem;
  display: inline-flex; align-items: center; justify-content: center;
  width: 42px; height: 42px;
  background: linear-gradient(145deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 12px;
  text-shadow: 0 0 14px rgba(255,255,255,0.45);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.08),
    0 4px 12px rgba(0,0,0,0.35);
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
  flex-shrink: 0;
}
.kc:hover .kc-ic {
  transform: scale(1.10) rotate(-4deg);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.12),
    0 6px 18px rgba(0,0,0,0.45),
    0 0 14px rgba(255,255,255,0.06);
}

/* Trend chip (top-right) */
.kc-trend {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.52rem; font-weight: 700;
  letter-spacing: 0.05em;
  padding: 3px 8px; border-radius: 20px;
  position: relative; z-index: 2;
  line-height: 1;
  margin-top: 2px;
}
.kc-trend.up   { background:rgba(57,255,20,0.10); color:#39ff14; border:1px solid rgba(57,255,20,0.22); }
.kc-trend.warn { background:rgba(255,193,7,0.10); color:#ffc107; border:1px solid rgba(255,193,7,0.22); }
.kc-trend.crit { background:rgba(255,45,85,0.10);  color:#ff2d55; border:1px solid rgba(255,45,85,0.22); }

/* Label */
.kc-l {
  font-family: 'Inter', sans-serif;
  font-size: 0.70rem; font-weight: 600;
  color: rgba(155,185,230,0.70);
  text-transform: uppercase; letter-spacing: 0.09em;
  position: relative; z-index: 2;
  margin-bottom: 0.22rem;
}

/* Value */
.kc-v {
  font-family: 'Orbitron', monospace;
  font-size: 1.92rem; font-weight: 800;
  color: #FFFFFF;
  line-height: 1.08;
  letter-spacing: -0.015em;
  text-shadow:
    0 0 18px rgba(255,255,255,0.50),
    0 0 36px rgba(255,255,255,0.15);
  position: relative; z-index: 2;
}

/* Bottom bar: desc + micro-bar */
.kc-bottom {
  position: relative; z-index: 2;
  margin-top: 0.55rem;
}
.kc-desc {
  font-family: 'Inter', sans-serif;
  font-size: 0.62rem; color: rgba(100,140,195,0.60);
  letter-spacing: 0.03em; line-height: 1.4;
}
/* Micro progress bar */
.kc-bar {
  height: 2px; width: 100%; margin-top: 0.5rem;
  background: rgba(255,255,255,0.05);
  border-radius: 2px; overflow: hidden;
}
.kc-bar-fill {
  height: 100%; border-radius: 2px;
  background: linear-gradient(90deg, var(--a1), rgba(37,99,235,0.6));
  animation: kcBarIn 1.4s cubic-bezier(0.4,0,0.2,1) forwards;
  transform-origin: left;
}
@keyframes kcBarIn {
  from { width: 0%; opacity: 0; }
  to   { opacity: 1; }
}

/* ══════════════════════════════════════════
   HERO
══════════════════════════════════════════ */
.hero{position:relative;padding:3.6rem 0 2.5rem;overflow:hidden;}
.hgrid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(0,212,255,0.022) 1px,transparent 1px),
    linear-gradient(90deg,rgba(0,212,255,0.022) 1px,transparent 1px);
  background-size:60px 60px;
  mask-image:radial-gradient(ellipse 92% 82% at 50% 40%,black 5%,transparent 100%);
  pointer-events:none;}
.horb{position:absolute;border-radius:50%;filter:blur(120px);pointer-events:none;}
.ho1{width:620px;height:620px;background:rgba(0,212,255,0.038);top:-240px;left:-140px;animation:hof 12s ease-in-out infinite;}
.ho2{width:400px;height:400px;background:rgba(255,107,53,0.028);top:-110px;right:-80px;animation:hof 9s ease-in-out infinite reverse;}
.ho3{width:280px;height:280px;background:rgba(57,255,20,0.018);bottom:-110px;left:36%;animation:hof 15s ease-in-out infinite;}
.ho4{width:200px;height:200px;background:rgba(180,77,255,0.018);bottom:20px;right:22%;animation:hof 10s ease-in-out infinite 3s;}
.ho5{width:160px;height:160px;background:rgba(59,130,246,0.025);top:30%;right:8%;animation:hof 7s ease-in-out infinite 1.5s;}
@keyframes hof{0%,100%{transform:translateY(0) scale(1);}50%{transform:translateY(-32px) scale(1.08);}}
.htitle{
  font-family:'Orbitron',monospace;font-size:3.4rem;font-weight:900;
  background:linear-gradient(135deg,#00d4ff 0%,#90eeff 22%,#ffffff 44%,#ffd0b0 66%,#ff6b35 86%,#ff4520 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;background-size:300% 300%;
  line-height:1.04;letter-spacing:0.09em;margin-bottom:0.6rem;
  animation:htt 7s ease-in-out infinite,tga 5s ease-in-out infinite alternate;
}
@keyframes htt{0%{background-position:0% 50%;}50%{background-position:100% 50%;}100%{background-position:0% 50%;}}
@keyframes tga{from{filter:drop-shadow(0 0 5px rgba(0,212,255,0.15));}to{filter:drop-shadow(0 0 36px rgba(0,212,255,0.70));}}
.hbadge{display:inline-flex;align-items:center;gap:5px;
  background:rgba(0,212,255,0.05);border:1px solid rgba(0,212,255,0.17);
  border-radius:26px;padding:5px 14px;font-size:0.62rem;color:var(--a1);
  letter-spacing:0.08em;text-transform:uppercase;font-weight:600;
  margin-right:0.4rem;margin-bottom:0.35rem;
  transition:all 0.22s;backdrop-filter:blur(10px);
  box-shadow:0 0 10px rgba(0,212,255,0.05);}
.hbadge:hover{background:rgba(0,212,255,0.10);border-color:rgba(0,212,255,0.40);
  box-shadow:0 0 18px rgba(0,212,255,0.18);transform:translateY(-1px);}
.hero-stat{display:inline-flex;align-items:center;gap:0.5rem;
  background:rgba(5,12,38,0.7);border:1px solid rgba(79,140,255,0.15);
  border-radius:10px;padding:0.55rem 1rem;margin-right:0.6rem;margin-top:0.4rem;
  backdrop-filter:blur(12px);}
.hero-stat-v{font-family:'Orbitron',monospace;font-size:1.1rem;font-weight:800;color:var(--a1);
  text-shadow:0 0 12px rgba(0,212,255,0.5);}
.hero-stat-l{font-size:0.63rem;color:var(--t2);text-transform:uppercase;letter-spacing:0.08em;}

/* ══════════════════════════════════════════
   CARDS — premium glass morphism v2
══════════════════════════════════════════ */
.card{
  background:linear-gradient(150deg,rgba(8,16,50,0.94) 0%,rgba(4,10,34,0.90) 100%);
  border:1px solid rgba(79,140,255,0.13);border-radius:var(--r4);
  padding:1.3rem 1.5rem;margin:0.42rem 0;
  transition:border-color 0.24s,box-shadow 0.24s,transform 0.24s;
  position:relative;overflow:hidden;backdrop-filter:blur(18px);
  box-shadow:0 0 14px rgba(37,99,235,0.04),0 4px 18px rgba(0,5,46,0.35);
}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,212,255,0.18),rgba(79,140,255,0.12),transparent);
  pointer-events:none;}
.card:hover{border-color:rgba(37,99,235,0.30);transform:translateY(-1px);
  box-shadow:0 0 0 1px rgba(37,99,235,0.09),0 0 28px rgba(37,99,235,0.12),var(--shadow-card);}

/* Section header */
.sh{font-family:'Orbitron',monospace;font-size:0.60rem;font-weight:700;
  letter-spacing:0.26em;text-transform:uppercase;color:var(--t2);
  display:flex;align-items:center;gap:0.7rem;margin-bottom:1.2rem;padding:0.1rem 0;}
.sh::before{content:'';width:3px;height:18px;flex-shrink:0;border-radius:3px;
  background:linear-gradient(180deg,#00d4ff 0%,rgba(37,99,235,0.2) 100%);
  box-shadow:0 0 12px rgba(0,212,255,0.55),0 0 24px rgba(0,212,255,0.18);}
.sh::after{content:'';flex:1;height:1px;
  background:linear-gradient(90deg,rgba(0,212,255,0.15),rgba(79,140,255,0.06),transparent);}

/* Page title component */
.page-header{padding:1.1rem 0 0.5rem;margin-bottom:0.5rem;}
.page-header-title{font-family:'Orbitron',monospace;font-size:1.65rem;font-weight:900;
  margin-bottom:0.3rem;letter-spacing:0.06em;}
.page-header-sub{color:var(--t2);font-size:0.83rem;letter-spacing:0.02em;line-height:1.5;}
.page-header-line{height:2px;margin-top:0.8rem;border-radius:1px;
  background:linear-gradient(90deg,var(--a1),rgba(37,99,235,0.4),transparent);}

/* Divider */
.div{border:none;height:1px;margin:2.2rem 0;
  background:linear-gradient(90deg,transparent,rgba(0,212,255,0.14),rgba(79,140,255,0.10),rgba(0,212,255,0.14),transparent);}

/* Status badges */
.bh,.bw,.bc{border-radius:24px;padding:4px 15px;font-size:0.67rem;font-weight:600;
  font-family:'JetBrains Mono',monospace;letter-spacing:0.07em;backdrop-filter:blur(8px);}
.bh{background:rgba(57,255,20,0.07);color:var(--a3);border:1px solid rgba(57,255,20,0.32);
  box-shadow:0 0 12px rgba(57,255,20,0.16),inset 0 0 10px rgba(57,255,20,0.04);}
.bw{background:rgba(255,193,7,0.07);color:var(--aw);border:1px solid rgba(255,193,7,0.32);
  box-shadow:0 0 12px rgba(255,193,7,0.16),inset 0 0 10px rgba(255,193,7,0.04);}
.bc{background:rgba(255,45,85,0.07);color:var(--ar);border:1px solid rgba(255,45,85,0.32);
  box-shadow:0 0 12px rgba(255,45,85,0.16),inset 0 0 10px rgba(255,45,85,0.04);}

/* RUL bar */
.rt{background:rgba(0,212,255,0.04);border-radius:10px;height:10px;width:100%;
  border:1px solid rgba(0,212,255,0.08);overflow:hidden;margin-top:0.45rem;
  box-shadow:inset 0 2px 5px rgba(0,0,0,0.4);}
.rf{height:100%;border-radius:10px;transition:width 1.1s cubic-bezier(0.4,0,0.2,1);}

/* Metric tiles */
.mtile{background:linear-gradient(140deg,rgba(8,15,48,0.94),rgba(4,10,32,0.90));
  border:1px solid rgba(79,140,255,0.13);border-radius:var(--r3);
  padding:0.8rem 1rem;display:flex;align-items:center;gap:0.85rem;
  transition:all 0.24s cubic-bezier(0.4,0,0.2,1);backdrop-filter:blur(14px);
  box-shadow:0 0 8px rgba(37,99,235,0.04);}
.mtile:hover{border-color:rgba(0,212,255,0.28);transform:translateY(-3px);box-shadow:0 6px 20px rgba(0,5,46,0.55),0 0 18px rgba(0,212,255,0.10);}
.mtile-ic{font-size:1.4rem;flex-shrink:0;}
.mtile-v{font-family:'Orbitron',monospace;font-size:1.1rem;font-weight:900;color:var(--a1);
  text-shadow:0 0 14px rgba(0,212,255,0.5);}
.mtile-l{font-size:0.57rem;color:var(--t3);text-transform:uppercase;letter-spacing:0.1em;margin-top:2px;}

/* Sensor live card */
.sensor-card{background:linear-gradient(150deg,rgba(10,18,61,0.94),rgba(5,11,46,0.9));
  border:1px solid rgba(79,140,255,0.15);border-radius:var(--r3);
  padding:0.95rem 0.8rem;position:relative;overflow:hidden;
  transition:all 0.26s cubic-bezier(0.4,0,0.2,1);text-align:center;isolation:isolate;
  box-shadow:0 0 10px rgba(37,99,235,0.06);}
.sensor-card::before{content:'';position:absolute;top:0;left:0;right:0;height:1.5px;
  background:linear-gradient(90deg,transparent,#2563EB,var(--a1),#2563EB,transparent);
  animation:scan 3.2s ease-in-out infinite;pointer-events:none;}
.sensor-card::after{content:'';position:absolute;inset:0;border-radius:var(--r3);
  background:radial-gradient(ellipse at 50% 0%,rgba(37,99,235,0.06) 0%,transparent 70%);
  pointer-events:none;}
@keyframes scan{0%{opacity:0.1;}50%{opacity:1;}100%{opacity:0.1;}}
.sensor-card:hover{border-color:rgba(37,99,235,0.35);transform:translateY(-5px);
  box-shadow:0 0 28px rgba(37,99,235,0.2),0 0 48px rgba(0,212,255,0.08),var(--shadow-card);}

/* Chat bubbles */
.cu{background:linear-gradient(145deg,rgba(13,24,71,0.92),rgba(10,18,61,0.88));
  border:1px solid rgba(37,99,235,0.18);border-radius:18px 18px 2px 18px;
  padding:0.78rem 1.1rem;margin:0.5rem 0;max-width:66%;margin-left:auto;
  font-size:0.84rem;box-shadow:var(--shadow-sm);backdrop-filter:blur(12px);}
.cb{background:linear-gradient(145deg,rgba(10,18,61,0.9),rgba(5,11,46,0.86));
  border:1px solid rgba(79,140,255,0.12);border-radius:18px 18px 18px 2px;
  padding:0.78rem 1.1rem;margin:0.5rem 0;max-width:72%;
  font-size:0.84rem;box-shadow:var(--shadow-sm);backdrop-filter:blur(12px);}

/* Timeline & Feature tiles */
.tl-item{display:flex;gap:1.2rem;margin-bottom:1.15rem;align-items:flex-start;}
.tl-dot{width:34px;height:34px;border-radius:50%;
  background:linear-gradient(135deg,rgba(11,26,46,0.95),rgba(8,19,32,0.9));
  border:2px solid var(--a1);display:flex;align-items:center;justify-content:center;
  font-size:0.65rem;flex-shrink:0;
  box-shadow:0 0 14px rgba(0,212,255,0.35),0 0 28px rgba(0,212,255,0.1);}
.ftile{background:linear-gradient(150deg,rgba(10,18,61,0.92),rgba(5,11,46,0.88));
  border:1px solid rgba(79,140,255,0.12);border-radius:var(--r3);
  padding:1.05rem 1.1rem;transition:all 0.24s cubic-bezier(0.4,0,0.2,1);
  cursor:default;position:relative;overflow:hidden;backdrop-filter:blur(12px);}
.ftile::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(37,99,235,0.18),rgba(79,140,255,0.1),transparent);}
.ftile:hover{border-color:rgba(37,99,235,0.28);transform:translateY(-5px);
  box-shadow:0 0 24px rgba(37,99,235,0.14),var(--shadow-card);}

/* ══════════════════════════════════════════
   STREAMLIT OVERRIDES
══════════════════════════════════════════ */
h1,h2,h3{font-family:'Orbitron',monospace!important;letter-spacing:0.05em!important;}
h1{color:var(--a1)!important;font-size:1.4rem!important;}
h2{color:var(--t1)!important;font-size:1.08rem!important;}
h3{color:var(--t2)!important;font-size:0.9rem!important;font-weight:500!important;}

/* Buttons */
.stButton>button{
  background:linear-gradient(135deg,#00b8e0 0%,#006b8c 100%)!important;
  color:#e8faff!important;font-family:'Orbitron',monospace!important;
  font-weight:700!important;font-size:0.63rem!important;letter-spacing:0.1em!important;
  border:1px solid rgba(0,212,255,0.3)!important;border-radius:var(--r2)!important;
  padding:0.55rem 1.6rem!important;
  transition:all 0.24s cubic-bezier(0.4,0,0.2,1)!important;
  box-shadow:0 0 22px rgba(0,212,255,0.24),0 2px 10px rgba(0,0,0,0.45)!important;}
.stButton>button:hover{
  background:linear-gradient(135deg,#00e8ff 0%,#00b0d4 60%,#0070a0 100%)!important;
  transform:translateY(-3px)!important;color:#ffffff!important;
  box-shadow:0 0 40px rgba(0,212,255,0.70),0 8px 26px rgba(0,0,0,0.5)!important;
  border-color:rgba(0,212,255,0.6)!important;}
.stButton>button:active{transform:translateY(-1px)!important;}

/* Inputs */
.stNumberInput input,.stTextInput input,div[data-baseweb="select"]>div{
  background:rgba(5,11,46,0.9)!important;color:var(--t1)!important;
  border:1px solid rgba(79,140,255,0.15)!important;border-radius:var(--r1)!important;
  font-family:'Inter',sans-serif!important;transition:border-color 0.2s,box-shadow 0.2s!important;}
.stNumberInput input:focus,.stTextInput input:focus{
  border-color:rgba(37,99,235,0.5)!important;
  box-shadow:0 0 0 3px rgba(37,99,235,0.12),0 0 12px rgba(37,99,235,0.15)!important;}

/* Metric containers */
div[data-testid="metric-container"]{
  background:linear-gradient(145deg,rgba(10,18,61,0.92),rgba(5,11,46,0.88))!important;
  border:1px solid rgba(79,140,255,0.12)!important;border-radius:var(--r4)!important;padding:1rem!important;
  box-shadow:0 0 10px rgba(37,99,235,0.05)!important;}

/* Expanders */
.stExpander{background:linear-gradient(145deg,rgba(10,18,61,0.9),rgba(5,11,46,0.86))!important;
  border:1px solid rgba(79,140,255,0.12)!important;border-radius:var(--r3)!important;
  transition:border-color 0.2s,box-shadow 0.2s!important;}
.stExpander:hover{border-color:rgba(37,99,235,0.25)!important;
  box-shadow:0 0 16px rgba(37,99,235,0.08)!important;}

/* Nav row (hidden functional buttons) */
div[data-testid="stHorizontalBlock"]>div>div>div>.stButton>button{
  background:transparent!important;color:var(--t3)!important;
  border:1px solid transparent!important;font-family:'Orbitron',monospace!important;
  font-size:0.52rem!important;letter-spacing:0.06em!important;
  padding:0.3rem 0.32rem!important;border-radius:5px!important;box-shadow:none!important;}
div[data-testid="stHorizontalBlock"]>div>div>div>.stButton>button:hover{
  background:rgba(0,212,255,0.07)!important;color:var(--a1)!important;
  border-color:var(--bd)!important;transform:none!important;box-shadow:none!important;}

/* Dataframe */
div[data-testid="stDataFrame"]{border:1px solid rgba(79,140,255,0.12)!important;
  border-radius:var(--r3)!important;overflow:hidden;
  box-shadow:var(--shadow-sm)!important;}

/* File uploader */
div[data-testid="stFileUploader"]{background:rgba(5,11,46,0.8)!important;
  border:1px dashed rgba(37,99,235,0.25)!important;border-radius:var(--r3)!important;
  transition:border-color 0.2s!important;}
div[data-testid="stFileUploader"]:hover{border-color:rgba(37,99,235,0.45)!important;}

/* Radio */
.stRadio>div{gap:0.65rem!important;}
.stRadio label span{font-family:'Inter',sans-serif!important;}

/* Date input */
div[data-baseweb="datepicker"] input{background:rgba(5,11,46,0.9)!important;
  border-color:rgba(79,140,255,0.15)!important;color:var(--t1)!important;border-radius:var(--r1)!important;}

/* Download button */
.stDownloadButton>button{
  background:linear-gradient(135deg,#1a8a00 0%,var(--a3) 100%)!important;
  color:#010912!important;font-weight:700!important;letter-spacing:0.08em!important;
  border:1px solid rgba(57,255,20,0.3)!important;
  box-shadow:0 0 22px rgba(57,255,20,0.32),0 2px 10px rgba(0,0,0,0.45)!important;}
.stDownloadButton>button:hover{
  background:linear-gradient(135deg,#88ff44 0%,var(--a3) 100%)!important;
  box-shadow:0 0 40px rgba(57,255,20,0.68),0 8px 26px rgba(0,0,0,0.5)!important;
  border-color:rgba(57,255,20,0.6)!important;}

/* Select box */
div[data-baseweb="select"]{border-radius:var(--r1)!important;}

/* Scrollbar */
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:rgba(5,11,46,0.6);}
::-webkit-scrollbar-thumb{
  background:linear-gradient(180deg,rgba(37,99,235,0.4),rgba(37,99,235,0.18));
  border-radius:6px;}
::-webkit-scrollbar-thumb:hover{background:rgba(37,99,235,0.6);}

/* ══════════════════════════════════════════
   RESULT INDICATOR CARDS (diagnosis)
══════════════════════════════════════════ */
.result-card{
  background:linear-gradient(150deg,rgba(8,16,50,0.96),rgba(4,10,34,0.92));
  border:1px solid rgba(79,140,255,0.13);border-radius:var(--r4);
  padding:1.4rem 1.5rem;position:relative;overflow:hidden;
  transition:border-color 0.24s,box-shadow 0.24s,transform 0.24s;}
.result-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  border-radius:var(--r4) var(--r4) 0 0;pointer-events:none;}
.result-card:hover{transform:translateY(-3px);}

/* Global page footer */
.ps-footer{
  margin-top:3.5rem;padding:2rem 0 1.4rem;
  border-top:1px solid rgba(0,212,255,0.08);
  text-align:center;position:relative;overflow:hidden;
}
.ps-footer::before{content:'';position:absolute;top:0;left:10%;right:10%;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,212,255,0.4),rgba(37,99,235,0.3),rgba(0,212,255,0.4),transparent);
  animation:nbline 8s ease-in-out infinite;}
.ps-footer-brand{font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:800;
  color:var(--a1);letter-spacing:0.16em;text-shadow:0 0 20px rgba(0,212,255,0.45);margin-bottom:0.35rem;}
.ps-footer-sub{font-size:0.67rem;color:var(--t3);letter-spacing:0.08em;line-height:1.8;}
.ps-footer-dots{display:flex;justify-content:center;gap:1.2rem;margin:0.6rem 0;flex-wrap:wrap;}
.ps-footer-dot{font-size:0.6rem;color:#2a4a70;letter-spacing:0.06em;text-transform:uppercase;}
.ps-footer-dot::before{content:'·';margin-right:0.5rem;color:#1a3050;}

/* Page title accent */
.page-title{padding:0.9rem 0 0.45rem;}

/* Info row pills */
.info-pill{display:inline-block;background:rgba(0,212,255,0.06);
  border:1px solid rgba(0,212,255,0.15);border-radius:20px;
  padding:3px 12px;font-size:0.66rem;color:var(--t2);
  font-family:'JetBrains Mono',monospace;margin-right:0.4rem;}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
# MODEL STUBS
# ─────────────────────────────────────────────────────────
class StubAI4I:
    def predict(self,X):
        np.random.seed(int(np.sum(np.array(X).flatten())*37)%(2**31))
        return [1 if np.random.random()<0.22 else 0 for _ in range(len(X))]

class StubNASA:
    n_features_in_=26
    def predict(self,X):
        v=np.array(X).flatten()
        np.random.seed(int(np.sum(v)*13)%(2**31))
        return [max(5,int(150-v[0]*0.8+np.random.randint(-20,20))) for _ in range(len(X))]

@st.cache_resource
def load_models():
    try:
        import joblib
        return joblib.load("../models/ai4i_model.pkl"), joblib.load("../models/nasa_rul_model.pkl")
    except:
        return StubAI4I(), StubNASA()

ai4i_model, nasa_model = load_models()

# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────
def fuse(failure,rul):
    if failure==1 or rul<30:  return "🔴 CRITICAL","bc","#ff2d55"
    elif rul<80:               return "🟡 WARNING","bw","#ffc107"
    else:                      return "🟢 HEALTHY","bh","#39ff14"

def rul_bar(rul,mx=200):
    p=min(int(rul/mx*100),100)
    c="#ff2d55" if p<20 else "#ffc107" if p<50 else "#39ff14"
    return f'<div class="rt"><div class="rf" style="width:{p}%;background:linear-gradient(90deg,{c}66,{c});box-shadow:0 0 8px {c}77"></div></div><div style="font-size:0.67rem;color:#6a8faf;margin-top:3px"><span style="color:{c};font-weight:600">{rul}</span> cycles &nbsp;·&nbsp;<span style="color:{c}">{p}%</span></div>'

def pdk(val, lbl, icon, cls="", desc="Updated just now", trend=None, bar=None):
    """
    val   — display value (str)
    lbl   — label (str)
    icon  — emoji icon
    cls   — variant class: g/o/y/r/p
    desc  — bottom description text
    trend — tuple (text, direction) e.g. ("↑ Active", "up") or ("⚠ Check", "warn")
    bar   — 0-100 fill for micro progress bar (or None)
    """
    # Build trend chip HTML
    trend_html = ""
    if trend:
        t_text, t_cls = trend
        trend_html = f'<span class="kc-trend {t_cls}">{t_text}</span>'

    # Build micro-bar HTML
    bar_html = ""
    if bar is not None:
        bar_w = max(0, min(100, int(bar)))
        bar_html = f'''<div class="kc-bar">
          <div class="kc-bar-fill" style="width:{bar_w}%"></div>
        </div>'''

    return f'''<div class="kc {cls}">
      <div class="kc-top">
        <div class="kc-ic">{icon}</div>
        {trend_html}
      </div>
      <div>
        <div class="kc-l">{lbl}</div>
        <div class="kc-v">{val}</div>
      </div>
      <div class="kc-bottom">
        <div class="kc-desc">{desc}</div>
        {bar_html}
      </div>
    </div>'''

def page_header(title, subtitle, color="#00d4ff"):
    st.markdown(f"""<div class="page-header">
      <div class="page-header-title" style="color:{color};text-shadow:0 0 28px {color}55">{title}</div>
      <div class="page-header-sub">{subtitle}</div>
      <div class="page-header-line" style="background:linear-gradient(90deg,{color},{color}44,transparent)"></div>
    </div>""", unsafe_allow_html=True)

def render_footer():
    st.markdown("""<div class="ps-footer">
      <div class="ps-footer-brand">🛡️ PREDICTASHIELD v5.0</div>
      <div class="ps-footer-dots">
        <span class="ps-footer-dot">AI4I 2020 · UCI Dataset</span>
        <span class="ps-footer-dot">NASA C-MAPSS</span>
        <span class="ps-footer-dot">Scikit-learn</span>
        <span class="ps-footer-dot">Streamlit</span>
        <span class="ps-footer-dot">Plotly</span>
      </div>
      <div class="ps-footer-sub">Industrial Predictive Maintenance Intelligence Platform<br>
        AI-generated outputs — verify critical decisions with a qualified technician</div>
    </div>""", unsafe_allow_html=True)

def pdark(fig, accent="#00d4ff"):
    """Premium chart theme matching reference: deep navy, electric blue gradients, neon glow traces."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(5,11,46,0.97)",
        font=dict(color="#c8daf8", family="Inter, sans-serif", size=11),
        xaxis=dict(
            gridcolor="rgba(37,99,235,0.08)",
            zerolinecolor="rgba(0,212,255,0.1)",
            tickfont=dict(color="rgba(79,140,255,0.6)", size=9.5, family="JetBrains Mono"),
            linecolor="rgba(37,99,235,0.1)",
            showgrid=True, ticks="outside", ticklen=3, tickcolor="rgba(37,99,235,0.15)",
        ),
        yaxis=dict(
            gridcolor="rgba(37,99,235,0.08)",
            zerolinecolor="rgba(0,212,255,0.1)",
            tickfont=dict(color="rgba(79,140,255,0.6)", size=9.5, family="JetBrains Mono"),
            linecolor="rgba(37,99,235,0.1)",
            showgrid=True, ticks="outside", ticklen=3, tickcolor="rgba(37,99,235,0.15)",
        ),
        legend=dict(
            bgcolor="rgba(5,11,46,0.92)",
            bordercolor="rgba(79,140,255,0.2)",
            borderwidth=1,
            font=dict(size=10, family="Inter", color="#a0c0e0"),
            itemsizing="constant",
            itemclick="toggleothers",
        ),
        margin=dict(l=22, r=22, t=52, b=22),
        title_font=dict(family="Orbitron, monospace", color="#E0EAFF", size=11),
        hoverlabel=dict(
            bgcolor="rgba(5,11,46,0.97)",
            bordercolor="rgba(0,212,255,0.4)",
            font=dict(family="Inter", color="#e0f0ff", size=11),
        ),
        colorway=["#00D4FF","#3B82F6","#39ff14","#60A5FA","#818CF8","#06B6D4","#A78BFA","#ffc107"],
    )
    # Subtle inner border effect via shape
    fig.add_shape(type="rect", xref="paper", yref="paper",
        x0=0, y0=0, x1=1, y1=1,
        line=dict(color="rgba(79,140,255,0.1)", width=1))
    return fig

# Subplot-specific dark theme (no axes override at top level)
def pdark_sub(fig):
    """For make_subplots figures."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(5,11,46,0.97)",
        font=dict(color="#c8daf8", family="Inter, sans-serif", size=10),
        legend=dict(
            bgcolor="rgba(5,11,46,0.92)",
            bordercolor="rgba(79,140,255,0.2)",
            borderwidth=1,
            font=dict(size=9.5, family="Inter", color="#a0c0e0"),
        ),
        title_font=dict(family="Orbitron, monospace", color="#E0EAFF", size=11),
        hoverlabel=dict(
            bgcolor="rgba(5,11,46,0.97)",
            bordercolor="rgba(0,212,255,0.4)",
            font=dict(family="Inter", color="#e0f0ff", size=11),
        ),
        margin=dict(l=22, r=22, t=60, b=22),
    )
    n_axes = len([k for k in fig.to_dict().get("layout", {}) if k.startswith("xaxis")])
    for i in range(1, max(n_axes + 1, 8)):
        suffix = "" if i == 1 else str(i)
        fig.update_layout(**{
            f"xaxis{suffix}": dict(
                gridcolor="rgba(37,99,235,0.08)",
                zerolinecolor="rgba(0,212,255,0.08)",
                tickfont=dict(color="rgba(79,140,255,0.6)", size=9, family="JetBrains Mono"),
                linecolor="rgba(37,99,235,0.08)",
                showgrid=True,
            ),
            f"yaxis{suffix}": dict(
                gridcolor="rgba(37,99,235,0.08)",
                zerolinecolor="rgba(0,212,255,0.08)",
                tickfont=dict(color="rgba(79,140,255,0.6)", size=9, family="JetBrains Mono"),
                linecolor="rgba(37,99,235,0.08)",
                showgrid=True,
            ),
        })
    # Update subplot title fonts
    for ann in fig.layout.annotations:
        ann.font.update(family="Orbitron, monospace", color="#8BAED4", size=9.5)
    return fig

def gen_ts(n=120,seed=42):
    np.random.seed(seed); t=np.linspace(0,12,n)
    rpm_arr=1500+60*np.cos(t*0.65)+np.random.normal(0,18,n)
    torque_arr=42+4*np.sin(t*1.1)+np.random.normal(0,1.2,n)
    return pd.DataFrame({
        "cycle":np.arange(1,n+1),
        "air_temp":298+2.5*np.sin(t)+np.random.normal(0,0.5,n),
        "process_temp":308+1.8*np.sin(t+1)+np.random.normal(0,0.35,n),
        "rpm":rpm_arr,
        "torque":torque_arr,
        "tool_wear":np.clip(np.linspace(0,210,n)+np.random.normal(0,4,n),0,220),
        "rul":np.clip(np.linspace(210,15,n)+np.random.normal(0,6,n),0,300),
        "vibration":np.abs(0.5+0.3*np.sin(t*2.1)+np.random.normal(0,0.1,n)),
        "pressure":np.clip(100+8*np.sin(t*0.8)+np.random.normal(0,2,n),80,130),
        "power":np.abs(rpm_arr*torque_arr/9549),
        "efficiency":np.clip(88-np.linspace(0,30,n)+np.random.normal(0,1.5,n),50,100),
        "temperature_diff":np.abs((308+1.8*np.sin(t+1))-(298+2.5*np.sin(t)))+np.random.normal(0,0.2,n),
    })

def ai_rec(failure,rul,air_t,proc_t,rpm,torque,tool_wear):
    issues,actions,priority=[],[],""
    if failure==1:
        issues.append("⚠️ AI4I model detected **imminent machine failure**")
        actions.append("🔴 **STOP MACHINE IMMEDIATELY** — Risk of catastrophic breakdown")
        priority="CRITICAL"
    if rul<30:
        issues.append(f"🔋 RUL critically low: **{rul} cycles remaining**")
        actions.append("🔴 Emergency maintenance required within **24 hours**")
        if not priority: priority="CRITICAL"
    elif rul<80:
        issues.append(f"🔋 RUL degrading — **{rul} cycles** remaining")
        actions.append("🟡 Schedule preventive maintenance within **72 hours**")
        if not priority: priority="WARNING"
    if tool_wear>180:
        issues.append(f"🔧 Tool wear critical: **{tool_wear:.0f} min** (replace at 200)")
        actions.append("🔧 Replace cutting tool at next scheduled stop")
    elif tool_wear>120:
        issues.append(f"🔧 Tool wear elevated: **{tool_wear:.0f} min** — monitor closely")
        actions.append("🔧 Inspect tool — schedule replacement soon")
    if air_t>310:
        issues.append(f"🌡️ High air temperature: **{air_t:.1f} K** (normal <308)")
        actions.append("❄️ Check cooling system and ventilation immediately")
    if abs(rpm-1500)>200:
        issues.append(f"⚙️ RPM deviation: **{rpm:.0f} rpm** (nominal 1500 ±200)")
        actions.append("⚙️ Inspect drive belt and motor frequency controller")
    if torque>65:
        issues.append(f"🔩 High torque: **{torque:.1f} Nm** (threshold 65)")
        actions.append("🔩 Reduce workload or check for mechanical obstruction")
    if not issues:
        issues=["✅ All sensor readings within normal range",
                "✅ No failure indicators from AI models",
                f"✅ Healthy remaining useful life: **{rul} cycles**"]
        actions=["📋 Continue standard monitoring schedule",
                 "📅 Next scheduled inspection recommended in 7 days",
                 "📊 Log current readings for trend baseline"]
        priority="HEALTHY"
    return issues,actions,priority

def cond_score(failure,rul,tool_wear):
    s=100
    if failure==1: s-=50
    s-=max(0,(200-rul)/2)
    s-=max(0,(tool_wear-100)/2)
    return max(0,min(100,round(s)))

def make_machine_review_report(machine_id,machine_type,install_date,last_maint,age_days,
                                air_t,proc_t,rpm,torque,tool_wear,
                                failure,rul,status,score,priority,
                                issues,actions,sched_df,rtitle,rdesc):
    ts=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sep="="*65
    def clean(x):
        for c in ['**','🔴','✅','🟡','🔧','📋','📅','📊','❄️','⚙️','🔩','🌡️','🔋','⚠️','🟢']:
            x=x.replace(c,'')
        return x.strip()
    issues_txt="\n".join(f"  [{i+1}] {clean(x)}" for i,x in enumerate(issues))
    actions_txt="\n".join(f"  [{i+1}] {clean(x)}" for i,x in enumerate(actions))
    next_d=(datetime.now()+timedelta(days=1 if priority=="CRITICAL" else 3 if priority=="WARNING" else 7)).strftime('%Y-%m-%d')
    # Radar dimensions
    rul_h=min(100,rul/2)
    tool_h=max(0,100-tool_wear/2)
    temp_h=max(0,100-(air_t-295)*5)
    rpm_h=max(0,100-abs(rpm-1500)/10)
    torq_h=max(0,100-(torque-40)*2)
    # Maintenance schedule rows
    sched_txt="\n".join(
        f"  {row['Task']:<28} Priority: {row['Priority']:<8} Due: {row['Due Date']}  Status: {row['Status']}"
        for _,row in sched_df.iterrows()
    )
    return f"""{sep}
        PREDICTASHIELD v5.0 — MACHINE REVIEW REPORT
{sep}
  Generated    :  {ts}
  Report ID    :  MR-{datetime.now().strftime('%Y%m%d%H%M%S')}
  Platform     :  PredictaShield v5.0 Industrial AI
{sep}

[1] MACHINE IDENTITY
  Machine ID        : {machine_id}
  Machine Type      : {machine_type}
  Installation Date : {install_date}
  Last Maintenance  : {last_maint}
  Age (days)        : {age_days} days

[2] SENSOR INPUT PARAMETERS
  Air Temperature    : {air_t:.2f} K        (Normal: 290–308 K)
  Process Temp       : {proc_t:.2f} K        (Normal: 298–315 K)
  Rotational Speed   : {rpm:.0f} rpm       (Normal: 1000–1700 rpm)
  Torque             : {torque:.2f} Nm        (Normal: 20–65 Nm)
  Tool Wear          : {tool_wear:.0f} min          (Warning: 120  Critical: 180)

[3] AI MODEL RESULTS
  AI4I Classification  : {"FAILURE DETECTED" if failure else "HEALTHY — No Failure"}
  NASA RUL Estimate    : {rul} cycles remaining
  Fusion Status        : {status.replace('🔴','CRITICAL').replace('🟡','WARNING').replace('🟢','HEALTHY')}
  Condition Score      : {score} / 100  ({'Critical' if score<40 else 'Warning' if score<70 else 'Healthy'} range)

[4] HEALTH RADAR DIMENSIONS  (0–100 scale)
  Condition Score      : {score:.0f} / 100
  RUL Health           : {rul_h:.0f} / 100
  Tool Health          : {tool_h:.0f} / 100
  Temperature Health   : {temp_h:.0f} / 100
  RPM Health           : {rpm_h:.0f} / 100
  Torque Health        : {torq_h:.0f} / 100
  Target Threshold     : 80 / 100 (all dimensions)

[5] DETECTED ISSUES
{issues_txt}

[6] RECOMMENDED ACTIONS
{actions_txt}

[7] AI RECOMMENDATION
  Priority   : {priority}
  Summary    : {clean(rtitle)}
  Detail     : {clean(rdesc)}
  Confidence : {"HIGH" if score>70 else "MEDIUM" if score>40 else "HIGH (DANGER)"}
  Generated  : {ts}

[8] MAINTENANCE SCHEDULE
  {'Task':<28} {'Priority':<8} {'Due Date':<14} Status
  {'-'*65}
{sched_txt}
  Next Recommended Check : {next_d}

{sep}
  MODELS  : AI4I 2020 RandomForest + NASA C-MAPSS Regressor
  REPORT  : Full Machine Review — PredictaShield v5.0
  DISCLAIMER : AI-generated report — verify with qualified technician
{sep}
""".encode()

def make_report(air_t,proc_t,rpm,torque,tool_wear,cycle,failure,rul,status,score,issues,actions,priority,rtitle,rdesc):
    ts=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sep="="*65
    issues_txt="\n".join(f"  [{i+1}] {x.replace('**','').replace('🔴','').replace('✅','').replace('🟡','').strip()}" for i,x in enumerate(issues))
    actions_txt="\n".join(f"  [{i+1}] {x.replace('**','').replace('🔴','').replace('🟡','').replace('🔧','').replace('📋','').replace('📅','').replace('📊','').strip()}" for i,x in enumerate(actions))
    return f"""{sep}
        PREDICTASHIELD v4.0 — MACHINE DIAGNOSIS REPORT
{sep}
  Generated :  {ts}
  Report ID :  PS-{datetime.now().strftime('%Y%m%d%H%M%S')}
{sep}

[1] SENSOR INPUT PARAMETERS
  Air Temperature    : {air_t:.2f} K
  Process Temp       : {proc_t:.2f} K
  Rotational Speed   : {rpm:.0f} rpm
  Torque             : {torque:.2f} Nm
  Tool Wear          : {tool_wear:.0f} min
  Operating Cycle    : {cycle}

[2] AI MODEL RESULTS
  AI4I Classification  : {"⚠ FAILURE DETECTED" if failure else "✅ HEALTHY — No Failure"}
  NASA RUL Estimate    : {rul} cycles remaining
  Fusion Status        : {status.replace('🔴','RED').replace('🟡','YELLOW').replace('🟢','GREEN')}
  Condition Score      : {score} / 100

[3] DETECTED ISSUES
{issues_txt}

[4] ACTION PLAN
{actions_txt}

[5] AI RECOMMENDATION
  Priority   : {priority}
  Summary    : {rtitle}
  Detail     : {rdesc}
  Confidence : {"HIGH" if score>70 else "MEDIUM" if score>40 else "HIGH (DANGER)"}
  Timestamp  : {ts}

[6] MAINTENANCE SCHEDULE
  Next Check     : {(datetime.now()+timedelta(days=1 if priority=="CRITICAL" else 3 if priority=="WARNING" else 7)).strftime('%Y-%m-%d')}
  Priority Level : {priority}
  Recommended By : PredictaShield AI v4.0

{sep}
  MODELS USED:  AI4I 2020 RandomForest + NASA C-MAPSS Regressor
  PLATFORM   :  PredictaShield v4.0 | Industrial AI Maintenance
  DISCLAIMER :  AI-generated report — verify with qualified technician
{sep}
""".encode()


# ─────────────────────────────────────────────────────────
# NAV
# ─────────────────────────────────────────────────────────
if "page" not in st.session_state: st.session_state.page="Home"
PAGES=["Home","Smart Diagnosis","Fleet Monitoring","Analytics","Sensor Dashboard","Machine Review","FAQ + AI Chat","About"]
ICONS=["🏠","⚙️","🏭","📊","📡","🔬","💬","ℹ️"]

active=st.session_state.page
nb=[]
for p,ic in zip(PAGES,ICONS):
    cls="nbtn active" if p==active else "nbtn"
    nb.append(f'<button class="{cls}">{ic}&nbsp;{p}</button>')
st.markdown(f"""
<div class="navbar">
  <div class="nb-brand">
    <div class="brand-icon">🛡️</div>
    <div class="brand-txt">
      <div class="brand-main">
        <span class="brand-ps">PREDICTA</span><span class="brand-s2">SHIELD</span>
        <span class="brand-tag">v5.0</span>
      </div>
    </div>
  </div>
  <div class="nb-links">{"".join(nb)}</div>
  <div class="nb-right">
    <div class="nb-live-wrap">
      <span class="ldot"></span>
      <span class="nb-live-label">LIVE</span>
    </div>
    <div class="nb-sep"></div>
    <span class="nav-v">AI ENGINE</span>
  </div>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="margin-top:0.35rem"></div>', unsafe_allow_html=True)
nc=st.columns(len(PAGES))
for i,(p,ic) in enumerate(zip(PAGES,ICONS)):
    with nc[i]:
        if st.button(f"{ic} {p}",key=f"nb_{p}",use_container_width=True):
            st.session_state.page=p; st.rerun()
page=st.session_state.page
st.markdown('<hr class="div" style="margin-top:0.1rem">', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════
if page=="Home":
    st.markdown("""
    <div class="hero">
      <div class="hgrid"></div>
      <div class="horb ho1"></div><div class="horb ho2"></div><div class="horb ho3"></div>
      <div class="horb ho4"></div><div class="horb ho5"></div>
      <div style="position:relative;z-index:2">
        <div style="margin-bottom:0.85rem">
          <span class="hbadge">🤖 Dual AI Models</span><span class="hbadge">⚡ Real-Time Analysis</span>
          <span class="hbadge">🏭 Industrial Grade</span><span class="hbadge">🔮 Predictive Intelligence</span>
          <span class="hbadge">📄 Auto Reports</span>
        </div>
        <div class="htitle">PREDICTASHIELD</div>
        <div style="font-size:0.78rem;color:#4e70a8;letter-spacing:0.20em;text-transform:uppercase;margin-bottom:0.75rem;font-weight:600;font-family:'Orbitron',monospace">
          Industrial Predictive Maintenance Intelligence Platform v5.0
        </div>
        <div style="font-size:0.96rem;color:#9ab8d8;max-width:700px;line-height:1.9;margin-bottom:1.6rem">
          Dual-model AI fusion combining <strong style="color:#00d4ff">failure classification</strong> (AI4I 2020)
          and <strong style="color:#ff6b35">remaining useful life regression</strong> (NASA C-MAPSS)
          for real-time machine health decisioning — predict failures <em>before</em> they happen,
          review machine condition, and download full diagnosis reports.
        </div>
        <div>
          <span class="hero-stat"><span class="hero-stat-v">99.2%</span><span class="hero-stat-l">Model Accuracy</span></span>
          <span class="hero-stat"><span class="hero-stat-v">2</span><span class="hero-stat-l">AI Models</span></span>
          <span class="hero-stat"><span class="hero-stat-v">40%</span><span class="hero-stat-l">Downtime Reduction</span></span>
          <span class="hero-stat"><span class="hero-stat-v">&lt;1s</span><span class="hero-stat-l">Diagnosis Time</span></span>
          <span class="hero-stat"><span class="hero-stat-v">∞</span><span class="hero-stat-l">Machines Supported</span></span>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sh">PLATFORM METRICS</div>', unsafe_allow_html=True)
    kc=st.columns(6)
    kpi_data=[
        ("99.2%","Model Accuracy","🎯","",  "RandomForest on UCI AI4I",  ("↑ Validated","up"),  99),
        ("2",    "AI Models",     "🤖","o",  "AI4I + NASA C-MAPSS",       ("Active","up"),       100),
        ("8",    "Dashboard Pages","📊","y", "Full analytics suite",      ("All online","up"),   100),
        ("40%",  "Downtime Reduction","📉","g","vs reactive maintenance", ("↑ Proven","up"),     40),
        ("24 hrs","Fault Lead Time","⏱️","", "Avg advance warning",       ("Optimal","up"),      72),
        ("∞",    "Machines",      "♾️","o",  "Unlimited fleet scale",     ("Scalable","up"),     85),
    ]
    for col,(v,l,ic,cls2,d,tr,br) in zip(kc,kpi_data):
        col.markdown(pdk(v,l,ic,cls2,d,tr,br),unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    lc,rc=st.columns([1.4,1],gap="large")
    with lc:
        st.markdown('<div class="sh">SYSTEM MODULES</div>', unsafe_allow_html=True)
        for dot,title,clr,desc in [
            ("🔵","AI4I Failure Predictor","#00d4ff","RandomForest classifier on UCI AI4I 2020 (10k samples). Detects failures from 5 process parameters with 99%+ accuracy. Identifies TWF, HDF, PWF, OSF, RNF failure modes."),
            ("🟠","NASA RUL Estimator","#ff6b35","Regression model on NASA C-MAPSS turbofan data. Predicts remaining useful life across 4 flight conditions using up to 26 sensor features."),
            ("🟢","Fusion Decision Engine","#39ff14","Combines both model outputs → HEALTHY / WARNING / CRITICAL verdict with condition score 0–100 and AI-generated recommendation."),
            ("📊","Analytics + Machine Review","#ffc107","Advanced time-series charts, scatter plots, temperature trends, RUL degradation, correlation heatmaps, and full machine health review panel."),
            ("📄","Auto Report Generator","#ff2d55","Download complete diagnosis reports with sensor data, model results, issue list, action plan, maintenance schedule, and AI recommendation."),
        ]:
            st.markdown(f"""
            <div class="card" style="border-left:3px solid {clr};background:linear-gradient(135deg,{clr}04 0%,var(--bgc) 42%)">
              <div style="display:flex;align-items:center;gap:0.55rem;margin-bottom:0.3rem">
                <div style="width:24px;height:24px;background:{clr}14;border:1px solid {clr}40;border-radius:6px;
                  display:flex;align-items:center;justify-content:center;font-size:0.72rem;
                  box-shadow:0 0 6px {clr}28;flex-shrink:0">{dot}</div>
                <div style="font-family:'Orbitron',monospace;font-size:0.73rem;color:{clr};font-weight:700;
                  letter-spacing:0.05em;text-shadow:0 0 6px {clr}50">{title}</div>
              </div>
              <div style="font-size:0.82rem;color:#a8c4e0;line-height:1.7;padding-left:30px">{desc}</div>
            </div>""", unsafe_allow_html=True)

    with rc:
        st.markdown('<div class="sh">NAVIGATION GUIDE</div>', unsafe_allow_html=True)
        for num,title,desc,clr in [
            ("01","🏠 HOME","Platform overview, KPIs, tech stack","#00d4ff"),
            ("02","⚙️ SMART DIAGNOSIS","Manual entry or CSV batch prediction + report","#ff6b35"),
            ("03","🏭 FLEET MONITORING","Multi-machine dashboard + fleet health score","#39ff14"),
            ("04","📊 ANALYTICS","Deep sensor trend charts and correlations","#ffc107"),
            ("05","🔬 MACHINE REVIEW","Single machine deep health review panel","#ff2d55"),
            ("06","💬 FAQ + AI CHAT","30+ Q&A knowledge base + AI assistant","#00d4ff"),
        ]:
            st.markdown(f"""
            <div style="display:flex;align-items:flex-start;gap:0.75rem;margin:0.5rem 0;
              background:var(--bgc);border:1px solid var(--bd);border-radius:8px;padding:0.6rem 0.85rem">
              <div style="font-family:'Orbitron',monospace;font-size:0.58rem;color:{clr};
                background:{clr}12;border:1px solid {clr}35;border-radius:50%;width:26px;height:26px;
                display:flex;align-items:center;justify-content:center;flex-shrink:0;
                box-shadow:0 0 6px {clr}20">{num}</div>
              <div>
                <div style="font-size:0.68rem;font-weight:700;color:#e8f4ff;letter-spacing:0.07em;font-family:'Orbitron',monospace">{title}</div>
                <div style="font-size:0.75rem;color:#6a8faf;margin-top:1px">{desc}</div>
              </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    st.markdown('<div class="sh">BUSINESS IMPACT</div>', unsafe_allow_html=True)
    ic4=st.columns(4)
    for col,(v,l,clr,ic5,cls,tr,br) in zip(ic4,[
        ("⬇ 40%","Unplanned Downtime","#00d4ff","📉","",  ("↓ Proven","up"),  60),
        ("⬆ 25%","Asset Lifespan",    "#39ff14","📈","g",  ("↑ Extended","up"),75),
        ("⬇ 30%","Maintenance Cost",  "#ff6b35","💰","o",  ("↓ Savings","up"), 70),
        ("⬆ 15%","OEE Score",         "#ffc107","⚙️","y",  ("↑ Efficiency","up"),85),
    ]): col.markdown(pdk(v,l,ic5,cls,f"vs baseline",tr,br),unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    st.markdown('<div class="sh">TECH STACK</div>', unsafe_allow_html=True)
    tcols=st.columns(8)
    for col,(ic6,t) in zip(tcols,[("🐍","Python 3.11"),("🧠","Scikit-learn"),("🌊","Streamlit"),("📊","Plotly"),
        ("🐼","Pandas/NumPy"),("🚀","NASA C-MAPSS"),("🏭","UCI AI4I 2020"),("📦","Joblib")]):
        with col:
            st.markdown(f"""<div class="card" style="text-align:center;padding:0.55rem 0.25rem">
              <div style="font-size:1.1rem;margin-bottom:3px">{ic6}</div>
              <div style="font-size:0.6rem;color:var(--t2)">{t}</div></div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align:center;padding:2.2rem 0 0.6rem;color:#162d48;font-size:0.66rem;letter-spacing:0.1em">
      🛡️ PredictaShield v4.0 &nbsp;·&nbsp; AI4I 2020 + NASA C-MAPSS &nbsp;·&nbsp; Built with Streamlit + Plotly
    </div>""", unsafe_allow_html=True)
    render_footer()


# ═══════════════════════════════════════════════════════
# SMART DIAGNOSIS
# ═══════════════════════════════════════════════════════
elif page=="Smart Diagnosis":
    page_header("⚙️ SMART DIAGNOSIS", "AI-powered real-time machine health analysis, review & downloadable report", "#00d4ff")

    imode=st.radio("",["🖊️ Manual Entry","📂 CSV Upload"],horizontal=True)
    st.markdown("<div style='margin-top:0.6rem'></div>", unsafe_allow_html=True)

    if imode=="🖊️ Manual Entry":
        st.markdown('<div class="sh">AI4I SENSOR INPUTS</div>', unsafe_allow_html=True)
        c1,c2,c3=st.columns(3)
        with c1:
            air_t=st.number_input("🌡️ Air Temperature [K]",value=298.1,step=0.1)
            proc_t=st.number_input("🔥 Process Temperature [K]",value=308.6,step=0.1)
        with c2:
            rpm=st.number_input("⚙️ Rotational Speed [rpm]",value=1551,step=10)
            torque=st.number_input("🔩 Torque [Nm]",value=42.8,step=0.1)
        with c3:
            tool_wear=st.number_input("🔧 Tool Wear [min]",value=0,step=1)

        st.markdown('<div class="sh" style="margin-top:1rem">NASA RUL SENSOR INPUTS</div>', unsafe_allow_html=True)
        try: nf=nasa_model.n_features_in_
        except: nf=26
        ne=nf-1
        st.caption(f"Cycle + {ne} sensor values — model expects **{nf}** features")
        nc1,nc2,nc3=st.columns(3)
        nasa_in=[]
        cycle=nc1.number_input("🔄 Cycle",value=1,step=1); nasa_in.append(float(cycle))
        for i in range(1,ne+1):
            col2=[nc1,nc2,nc3][i%3]
            nasa_in.append(col2.number_input(f"📡 Sensor {i}",value=0.0,step=0.1,key=f"s{i}"))

        st.markdown("<div style='margin-top:0.9rem'></div>", unsafe_allow_html=True)
        if st.button("🔍  RUN FULL AI DIAGNOSIS"):
            with st.spinner("Running AI models & generating analysis…"):
                time.sleep(0.55)
            failure=ai4i_model.predict(np.array([[air_t,proc_t,rpm,torque,tool_wear]]))[0]
            rul=int(nasa_model.predict(np.array([nasa_in]))[0])
            status,badge_cls,sclr=fuse(failure,rul)
            score=cond_score(failure,rul,tool_wear)
            issues,actions,priority=ai_rec(failure,rul,air_t,proc_t,rpm,torque,tool_wear)

            rec_cfg={
                "HEALTHY":("#39ff14","rgba(57,255,20,0.06)","✅ MACHINE IN GOOD HEALTH","No immediate maintenance required. System operating within all normal parameters. Continue standard monitoring."),
                "WARNING": ("#ffc107","rgba(255,193,7,0.06)","🟡 MAINTENANCE WINDOW APPROACHING","Schedule preventive maintenance within 72 hours to avoid unplanned downtime. Monitor closely."),
                "CRITICAL":("#ff2d55","rgba(255,45,85,0.06)","🔴 IMMEDIATE ACTION REQUIRED","Stop machine operation immediately. High risk of imminent failure. Escalate to maintenance team now."),
            }
            rclr,rbg,rtitle,rdesc=rec_cfg[priority]

            st.markdown('<hr class="div">', unsafe_allow_html=True)
            st.markdown('<div class="sh">DIAGNOSIS RESULT</div>', unsafe_allow_html=True)

            r1,r2,r3,r4=st.columns(4)
            fclr="#ff2d55" if failure else "#39ff14"
            with r1:
                st.markdown(f"""<div class="card" style="border-top:2px solid {fclr};background:linear-gradient(135deg,{fclr}06 0%,var(--bgc) 50%)">
                  <div style="font-size:0.63rem;color:#6a8faf;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.38rem">AI4I Classification</div>
                  <div style="font-family:'Orbitron',monospace;font-size:1.18rem;color:{fclr};text-shadow:0 0 12px {fclr}70">{'⚠️ FAILURE' if failure else '✅ HEALTHY'}</div>
                  <div style="font-size:0.7rem;color:#6a8faf;margin-top:0.28rem">{'Failure detected' if failure else 'All clear'}</div>
                </div>""", unsafe_allow_html=True)
            with r2:
                st.markdown(f"""<div class="card" style="border-top:2px solid #00d4ff;background:linear-gradient(135deg,rgba(0,212,255,0.045) 0%,var(--bgc) 50%)">
                  <div style="font-size:0.63rem;color:#6a8faf;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.38rem">NASA RUL</div>
                  <div style="font-family:'Orbitron',monospace;font-size:1.18rem;color:#00d4ff;text-shadow:0 0 12px rgba(0,212,255,0.6)">{rul} <span style="font-size:0.62rem;color:#6a8faf">cycles</span></div>
                  {rul_bar(rul)}
                </div>""", unsafe_allow_html=True)
            with r3:
                st.markdown(f"""<div class="card" style="border-top:2px solid {sclr};background:linear-gradient(135deg,{sclr}06 0%,var(--bgc) 50%)">
                  <div style="font-size:0.63rem;color:#6a8faf;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.38rem">Fusion Status</div>
                  <div style="font-family:'Orbitron',monospace;font-size:1.18rem;color:{sclr};text-shadow:0 0 12px {sclr}70">{status}</div>
                  <div style="margin-top:0.45rem"><span class="{badge_cls}">{priority}</span></div>
                </div>""", unsafe_allow_html=True)
            with r4:
                sc_c="#ff2d55" if score<40 else "#ffc107" if score<70 else "#39ff14"
                st.markdown(f"""<div class="card" style="border-top:2px solid {sc_c};background:linear-gradient(135deg,{sc_c}06 0%,var(--bgc) 50%)">
                  <div style="font-size:0.63rem;color:#6a8faf;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.38rem">Condition Score</div>
                  <div style="font-family:'Orbitron',monospace;font-size:1.18rem;color:{sc_c};text-shadow:0 0 12px {sc_c}70">{score}/100</div>
                  <div class="rt" style="margin-top:0.42rem"><div class="rf" style="width:{score}%;background:linear-gradient(90deg,{sc_c}55,{sc_c})"></div></div>
                </div>""", unsafe_allow_html=True)

            # Machine Review
            st.markdown('<hr class="div">', unsafe_allow_html=True)
            st.markdown('<div class="sh">MACHINE CONDITION REVIEW</div>', unsafe_allow_html=True)
            mx1,mx2=st.columns(2,gap="large")
            with mx1:
                issues_html="".join(f'<div style="font-size:0.82rem;color:#a8c4e0;margin:0.3rem 0;padding:0.38rem 0.6rem;background:rgba(0,212,255,0.04);border-radius:5px;border-left:2px solid rgba(0,212,255,0.2)">{x}</div>' for x in issues)
                st.markdown(f"""<div class="card"><div style="font-family:'Orbitron',monospace;font-size:0.68rem;color:#00d4ff;margin-bottom:0.7rem;letter-spacing:0.08em">🔍 DETECTED ISSUES ({len(issues)})</div>{issues_html}</div>""", unsafe_allow_html=True)
            with mx2:
                actions_html="".join(f'<div style="font-size:0.82rem;color:#a8c4e0;margin:0.3rem 0;padding:0.38rem 0.6rem;background:rgba(57,255,20,0.04);border-radius:5px;border-left:2px solid rgba(57,255,20,0.2)">{x}</div>' for x in actions)
                st.markdown(f"""<div class="card"><div style="font-family:'Orbitron',monospace;font-size:0.68rem;color:#39ff14;margin-bottom:0.7rem;letter-spacing:0.08em">💡 ACTION PLAN ({len(actions)})</div>{actions_html}</div>""", unsafe_allow_html=True)

            st.markdown(f"""<div class="card" style="border-left:4px solid {rclr};background:{rbg}">
              <div style="font-family:'Orbitron',monospace;font-size:0.7rem;color:{rclr};font-weight:700;
                letter-spacing:0.07em;margin-bottom:0.42rem;text-shadow:0 0 7px {rclr}50">💡 AI RECOMMENDATION</div>
              <div style="font-size:0.98rem;font-weight:700;color:#e8f4ff;margin-bottom:0.28rem">{rtitle}</div>
              <div style="font-size:0.83rem;color:#a8c4e0">{rdesc}</div>
              <div style="margin-top:0.75rem;display:flex;flex-wrap:wrap;gap:1.1rem;font-size:0.72rem;color:#6a8faf">
                <span>🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
                <span>🎯 Confidence: {"HIGH" if score>70 else "MEDIUM" if score>40 else "HIGH (DANGER)"}</span>
                <span>📊 Score: <span style="color:{rclr}">{score}/100</span></span>
                <span>🔋 RUL: <span style="color:{rclr}">{rul} cycles</span></span>
              </div>
            </div>""", unsafe_allow_html=True)

            # Overall Present Condition Panel
            st.markdown('<hr class="div">', unsafe_allow_html=True)
            st.markdown('<div class="sh">OVERALL PRESENT MACHINE CONDITION</div>', unsafe_allow_html=True)
            demo=gen_ts()
            sensor_now={"🌡️ Air Temp":f"{air_t:.1f} K","🔥 Proc Temp":f"{proc_t:.1f} K",
                        "⚙️ RPM":f"{rpm:.0f}","🔩 Torque":f"{torque:.1f} Nm",
                        "🔧 Tool Wear":f"{tool_wear:.0f} min","🔋 Est. RUL":f"{rul} cyc"}
            cols6=st.columns(6)
            for col,(lbl,val) in zip(cols6,sensor_now.items()):
                with col:
                    st.markdown(f"""<div class="mtile">
                      <div class="mtile-ic">{lbl.split()[0]}</div>
                      <div><div class="mtile-v" style="font-size:0.88rem">{val}</div>
                      <div class="mtile-l">{' '.join(lbl.split()[1:])}</div></div>
                    </div>""", unsafe_allow_html=True)

            # Charts
            st.markdown('<hr class="div">', unsafe_allow_html=True)
            st.markdown('<div class="sh">SENSOR ANALYSIS CHARTS</div>', unsafe_allow_html=True)
            sa,sb=st.columns(2)
            with sa:
                ft=go.Figure()
                ft.add_trace(go.Scatter(x=demo.cycle,y=demo.air_temp,name="Air Temp [K]",
                    line=dict(color="#00d4ff",width=2.2,shape="spline",smoothing=0.6),
                    fill="tozeroy",fillcolor="rgba(0,120,255,0.12)",
                    mode="lines",hovertemplate="Cycle %{x}<br>Air Temp: %{y:.1f} K<extra></extra>"))
                ft.add_trace(go.Scatter(x=demo.cycle,y=demo.process_temp,name="Process Temp [K]",
                    line=dict(color="#ff6b35",width=2.2,shape="spline",smoothing=0.6),
                    fill="tozeroy",fillcolor="rgba(255,107,53,0.08)",
                    mode="lines",hovertemplate="Cycle %{x}<br>Proc Temp: %{y:.1f} K<extra></extra>"))
                ft.add_hline(y=310,line_dash="dash",line_color="#ff2d55",opacity=0.45,
                    annotation_text="⚠️ Threshold",annotation_font_color="#ff2d55")
                ft.add_hrect(y0=308,y1=320,fillcolor="rgba(255,45,85,0.04)",line_width=0)
                ft.update_layout(title="Temperature Trends [K]")
                st.plotly_chart(pdark(ft),use_container_width=True)
            with sb:
                fr=go.Figure()
                fr.add_trace(go.Scatter(x=demo.cycle,y=demo.rul,fill="tozeroy",name="RUL",
                    line=dict(color="#39ff14",width=2.2,shape="spline",smoothing=0.6),
                    fillcolor="rgba(0,200,80,0.1)",
                    mode="lines",hovertemplate="Cycle %{x}<br>RUL: %{y:.0f}<extra></extra>"))
                fr.add_hrect(y0=0,y1=30,fillcolor="rgba(255,45,85,0.09)",line_width=0,
                    annotation_text="🔴 CRITICAL",annotation_font_color="#ff2d55")
                fr.add_hrect(y0=30,y1=80,fillcolor="rgba(255,193,7,0.06)",line_width=0,
                    annotation_text="🟡 WARNING",annotation_font_color="#ffc107")
                fr.add_hline(y=rul,line_dash="dot",line_color="#00d4ff",opacity=0.7,
                    annotation_text=f"Current: {rul}",annotation_font_color="#00d4ff")
                fr.update_layout(title="RUL Degradation Curve")
                st.plotly_chart(pdark(fr),use_container_width=True)

            sc1,sc2=st.columns(2)
            with sc1:
                fsc=go.Figure()
                fsc.add_trace(go.Scatter(x=demo.rpm,y=demo.torque,mode="markers",name="Operating Points",
                    marker=dict(color=demo.tool_wear,
                        colorscale=[[0,"#00d4ff"],[0.35,"#39ff14"],[0.65,"#ffc107"],[1,"#ff2d55"]],
                        size=6,opacity=0.82,
                        colorbar=dict(title="Wear [min]",tickfont=dict(color="#4a6a90",size=8.5,
                            family="JetBrains Mono"),thickness=11,
                            title_font=dict(color="#7a9cbf",size=9)),
                        line=dict(color="rgba(0,0,0,0.3)",width=0.5))))
                fsc.add_vline(x=rpm,line_dash="dot",line_color="#00d4ff",opacity=0.55,
                    annotation_text="↑ Now",annotation_font_color="#00d4ff")
                fsc.add_hline(y=torque,line_dash="dot",line_color="#ff6b35",opacity=0.55,
                    annotation_text="← Now",annotation_font_color="#ff6b35")
                fsc.update_layout(title="RPM vs Torque — by Tool Wear",
                    xaxis_title="RPM",yaxis_title="Torque [Nm]")
                st.plotly_chart(pdark(fsc),use_container_width=True)
            with sc2:
                ftw=go.Figure()
                ftw.add_trace(go.Bar(x=demo.cycle[::8],y=demo.tool_wear[::8],name="Tool Wear",
                    marker=dict(
                        color=["#ff2d55" if v>180 else "#ffc107" if v>120 else "#00d4ff" for v in demo.tool_wear[::8]],
                        line=dict(color="rgba(0,0,0,0)",width=0),
                        opacity=0.82),
                    hovertemplate="Cycle %{x}<br>Wear: %{y:.0f} min<extra></extra>"))
                ftw.add_hline(y=120,line_dash="dot",line_color="#ffc107",opacity=0.5,
                    annotation_text="⚠️ 120",annotation_font_color="#ffc107")
                ftw.add_hline(y=180,line_dash="dot",line_color="#ff2d55",opacity=0.5,
                    annotation_text="🔴 180",annotation_font_color="#ff2d55")
                ftw.add_hline(y=200,line_dash="dash",line_color="#ff2d55",opacity=0.75,
                    annotation_text="REPLACE",annotation_font_color="#ff2d55")
                ftw.update_layout(title="Tool Wear Progression [min]",bargap=0.12)
                st.plotly_chart(pdark(ftw),use_container_width=True)

            sv1,sv2=st.columns(2)
            with sv1:
                fv=go.Figure()
                fv.add_trace(go.Scatter(x=demo.cycle,y=demo.vibration,name="Vibration",
                    line=dict(color="#ffc107",width=2,shape="spline",smoothing=0.65),
                    fill="tozeroy",fillcolor="rgba(255,193,7,0.07)",
                    mode="lines",hovertemplate="Cycle %{x}<br>Vibration: %{y:.2f} g<extra></extra>"))
                fv.add_hrect(y0=0.8,y1=2,fillcolor="rgba(255,45,85,0.06)",line_width=0,
                    annotation_text="High Zone",annotation_font_color="#ff2d55")
                fv.update_layout(title="Vibration Sensor Reading",yaxis_title="Amplitude [g]")
                st.plotly_chart(pdark(fv),use_container_width=True)
            with sv2:
                fp=go.Figure()
                fp.add_trace(go.Scatter(x=demo.cycle,y=demo.pressure,name="Pressure",
                    line=dict(color="#b44dff",width=2,shape="spline",smoothing=0.65),
                    fill="tozeroy",fillcolor="rgba(120,0,255,0.07)",
                    mode="lines",hovertemplate="Cycle %{x}<br>Pressure: %{y:.1f} bar<extra></extra>"))
                fp.add_trace(go.Scatter(x=demo.cycle,y=[110]*len(demo),name="Upper Limit",
                    line=dict(color="#ff2d55",width=1.2,dash="dash"),showlegend=True))
                fp.add_trace(go.Scatter(x=demo.cycle,y=[90]*len(demo),name="Lower Limit",
                    line=dict(color="#ffc107",width=1.2,dash="dash"),showlegend=True))
                fp.update_layout(title="Pressure Sensor Reading [bar]",yaxis_title="Pressure [bar]")
                st.plotly_chart(pdark(fp),use_container_width=True)

            # Download Report
            st.markdown('<hr class="div">', unsafe_allow_html=True)
            st.markdown('<div class="sh">EXPORT DIAGNOSIS REPORT</div>', unsafe_allow_html=True)
            rc1,rc2,rc3=st.columns([2,1,1])
            with rc1:
                st.markdown(f"""<div class="card" style="border-left:3px solid #00d4ff">
                  <div style="font-size:0.8rem;color:#a8c4e0">
                  📄 <strong style="color:#00d4ff">Full Diagnosis Report</strong> — includes sensor inputs, model results,
                  detected issues, action plan, maintenance schedule, and AI recommendation.<br>
                  <span style="font-size:0.72rem;color:#6a8faf">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                  </div></div>""", unsafe_allow_html=True)
            with rc2:
                report_bytes=make_report(air_t,proc_t,rpm,torque,tool_wear,cycle,failure,rul,status,score,issues,actions,priority,rtitle,rdesc)
                st.download_button("📄 Download Report (.txt)",
                    report_bytes,
                    f"PredictaShield_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    "text/plain", use_container_width=True)

    else:  # CSV
        st.markdown("""<div class="card" style="border-left:3px solid #ff6b35;margin-bottom:0.9rem">
          <div style="font-size:0.8rem;color:#a8c4e0;line-height:1.8">
          📋 Columns: <code style="color:#00d4ff;background:rgba(0,212,255,0.08);padding:1px 5px;border-radius:3px">
          machine_id, air_temp, process_temp, rpm, torque, tool_wear, cycle, s1…sN</code></div></div>""", unsafe_allow_html=True)
        up=st.file_uploader("Upload CSV",type=["csv"])
        if up:
            df=pd.read_csv(up); st.dataframe(df.head(5),use_container_width=True)
            acols=["air_temp","process_temp","rpm","torque","tool_wear"]
            try: nn=nasa_model.n_features_in_
            except: nn=26
            ncols2=["cycle"]+[f"s{i}" for i in range(1,nn)]
            idc="machine_id" if "machine_id" in df.columns else None
            miss=[c for c in acols+ncols2 if c not in df.columns]; n2=len(df)
            if miss:
                st.warning(f"Missing {len(miss)} columns — using demo predictions.")
                fails=[random.randint(0,1) for _ in range(n2)]; ruls=[random.randint(10,200) for _ in range(n2)]
            else:
                fails=list(ai4i_model.predict(df[acols].values)); ruls=[int(v) for v in nasa_model.predict(df[ncols2].values)]
            stt=[fuse(f,r) for f,r in zip(fails,ruls)]
            scrs=[cond_score(f,r,df["tool_wear"].iloc[i] if "tool_wear" in df.columns else 50) for i,(f,r) in enumerate(zip(fails,ruls))]
            rdf=df[[idc]].copy() if idc else pd.DataFrame({"Row":range(1,n2+1)})
            rdf["AI4I"]=["⚠️ FAILURE" if f else "✅ HEALTHY" for f in fails]
            rdf["RUL"]=ruls; rdf["Status"]=[s[0] for s in stt]; rdf["Score"]=scrs
            st.markdown('<div class="sh" style="margin-top:1rem">BATCH RESULTS</div>', unsafe_allow_html=True)
            st.dataframe(rdf,use_container_width=True)
            sc2=rdf["Status"].value_counts().reset_index(); sc2.columns=["Status","Count"]
            fig=px.bar(sc2,x="Status",y="Count",color="Status",
                color_discrete_map={"🟢 HEALTHY":"#39ff14","🟡 WARNING":"#ffc107","🔴 CRITICAL":"#ff2d55"},
                title="Batch Status Distribution")
            st.plotly_chart(pdark(fig),use_container_width=True)
            st.download_button("⬇️ Download Results CSV",rdf.to_csv(index=False).encode(),"batch_results.csv","text/csv")


# ═══════════════════════════════════════════════════════
# FLEET MONITORING
# ═══════════════════════════════════════════════════════
elif page=="Fleet Monitoring":
    page_header("🏭 FLEET MONITORING", "Industrial-scale multi-machine health dashboard with real-time analytics", "#ff6b35")

    ff=st.file_uploader("Upload Fleet CSV",type=["csv"],key="flup")
    if ff is None:
        st.info("🔬 Demo mode — 20 machines")
        np.random.seed(42); n=20
        ids=[f"MCH-{100+i}" for i in range(n)]
        fails=[random.randint(0,1) for _ in range(n)]
        ruls=[random.randint(8,200) for _ in range(n)]
        wears=[random.randint(0,220) for _ in range(n)]
        rpms=[random.randint(1200,1800) for _ in range(n)]
        torques=[random.uniform(30,70) for _ in range(n)]
    else:
        df_f=pd.read_csv(ff); n=len(df_f)
        ids=df_f["machine_id"].tolist() if "machine_id" in df_f.columns else [f"MCH-{i}" for i in range(n)]
        acols=["air_temp","process_temp","rpm","torque","tool_wear"]
        try: nn=nasa_model.n_features_in_
        except: nn=26
        nc2=["cycle"]+[f"s{i}" for i in range(1,nn)]
        fails=list(ai4i_model.predict(df_f[acols].values)) if all(c in df_f.columns for c in acols) else [random.randint(0,1) for _ in range(n)]
        ruls=[int(v) for v in nasa_model.predict(df_f[nc2].values)] if all(c in df_f.columns for c in nc2) else [random.randint(8,200) for _ in range(n)]
        wears=df_f["tool_wear"].tolist() if "tool_wear" in df_f.columns else [random.randint(0,220) for _ in range(n)]
        rpms=df_f["rpm"].tolist() if "rpm" in df_f.columns else [random.randint(1200,1800) for _ in range(n)]
        torques=df_f["torque"].tolist() if "torque" in df_f.columns else [random.uniform(30,70) for _ in range(n)]

    sts=[fuse(f,r)[0] for f,r in zip(fails,ruls)]
    scrs=[cond_score(f,r,w) for f,r,w in zip(fails,ruls,wears)]
    hln=sts.count("🟢 HEALTHY"); wln=sts.count("🟡 WARNING"); cln=sts.count("🔴 CRITICAL")
    fs=round(hln/n*100,1)

    st.markdown('<div class="sh">FLEET KPIs</div>', unsafe_allow_html=True)
    k1,k2,k3,k4,k5=st.columns(5)
    h_tr = ("↑ Healthy","up") if hln/max(n,1)>0.6 else ("Monitor","warn")
    w_tr = ("Watch","warn") if wln>0 else ("Clear","up")
    c_tr = ("⚠ Critical","crit") if cln>0 else ("All clear","up")
    fs_tr = ("↑ Good","up") if fs>=70 else ("Monitor","warn") if fs>=40 else ("↓ Alert","crit")
    for col,(v,l,ic,cls2,d,tr,br) in zip([k1,k2,k3,k4,k5],[
        (str(n),"Total Machines","🏭","",  "Fleet size",            ("Active","up"),100),
        (str(hln),"Healthy",    "✅","g",  f"{round(hln/max(n,1)*100)}% of fleet", h_tr, round(hln/max(n,1)*100)),
        (str(wln),"Warning",    "⚠️","y",  "Needs attention",       w_tr,           round(wln/max(n,1)*100)),
        (str(cln),"Critical",   "🚨","r",  "Immediate action",      c_tr,           round(cln/max(n,1)*100)),
        (f"{fs}%","Fleet Health","💪","o", "Overall health score",  fs_tr,          int(fs)),
    ]): col.markdown(pdk(v,l,ic,cls2,d,tr,br),unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    fdf=pd.DataFrame({"Machine ID":ids,"AI4I":["⚠️ FAILURE" if f else "✅ HEALTHY" for f in fails],
        "RUL":ruls,"Status":sts,"Score":scrs,"Tool Wear":wears,"RPM":rpms,"Torque":torques}).sort_values("RUL")

    st.markdown('<div class="sh">MACHINE STATUS TABLE</div>', unsafe_allow_html=True)
    st.dataframe(fdf,use_container_width=True,height=255)

    c1,c2=st.columns(2,gap="medium")
    with c1:
        fig_pie=px.pie(values=[hln,wln,cln],names=["🟢 HEALTHY","🟡 WARNING","🔴 CRITICAL"],
            title="Fleet Status Distribution",hole=0.5,
            color_discrete_sequence=["#39ff14","#ffc107","#ff2d55"])
        fig_pie.update_traces(
            textfont=dict(size=10,family="Inter",color="#e0f0ff"),
            marker=dict(line=dict(color="rgba(4,11,24,1)",width=3),
                        colors=["#39ff14","#ffc107","#ff2d55"]),
            pull=[0.04,0.02,0.06],
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Share: %{percent}<extra></extra>")
        fig_pie.add_annotation(text=f"<b style='font-size:14px'>{n}</b><br><span style='font-size:9px'>MACHINES</span>",
            x=0.5,y=0.5,showarrow=False,font=dict(color="#a0c0e0",family="Orbitron",size=11))
        st.plotly_chart(pdark(fig_pie),use_container_width=True)
    with c2:
        t10=fdf.head(10)
        bar_clrs=["#ff2d55" if "CRITICAL" in s else "#ffc107" if "WARNING" in s else "#00d4ff" for s in t10["Status"]]
        fig_b=go.Figure(go.Bar(x=t10["Machine ID"],y=t10["RUL"],
            marker=dict(color=bar_clrs,opacity=0.88,
                line=dict(color="rgba(0,0,0,0)",width=0)),
            text=t10["RUL"],textposition="outside",
            textfont=dict(color="#a0c0e0",size=9,family="JetBrains Mono"),
            name="RUL",hovertemplate="<b>%{x}</b><br>RUL: %{y} cycles<extra></extra>"))
        fig_b.update_layout(title="Top 10 Risk Machines (Lowest RUL)",bargap=0.18)
        st.plotly_chart(pdark(fig_b),use_container_width=True)

    c3,c4=st.columns([1.6,1],gap="medium")
    with c3:
        fig_sc=go.Figure()
        for zone,zclr,sym,zsz in [("🟢 HEALTHY","#39ff14","circle",11),
                                    ("🟡 WARNING","#ffc107","diamond",11),
                                    ("🔴 CRITICAL","#ff2d55","x",13)]:
            m=fdf[fdf["Status"]==zone]
            if len(m)>0:
                fig_sc.add_trace(go.Scatter(x=m["RUL"],y=m["Score"],mode="markers+text",
                    name=zone,text=m["Machine ID"],textposition="top center",
                    textfont=dict(color="#4a6a90",size=7.5,family="Inter"),
                    marker=dict(color=zclr,size=zsz,symbol=sym,opacity=0.88,
                        line=dict(color="rgba(4,11,24,0.6)",width=1.5)),
                    hovertemplate="<b>%{text}</b><br>RUL: %{x}<br>Score: %{y}<extra></extra>"))
        fig_sc.add_vline(x=80,line_dash="dash",line_color="#ffc107",opacity=0.35,
            annotation_text="WARNING",annotation_font_color="#ffc107",annotation_font_size=9)
        fig_sc.add_vline(x=30,line_dash="dash",line_color="#ff2d55",opacity=0.35,
            annotation_text="CRITICAL",annotation_font_color="#ff2d55",annotation_font_size=9)
        fig_sc.add_hrect(y0=0,y1=40,fillcolor="rgba(255,45,85,0.04)",line_width=0)
        fig_sc.update_layout(title="RUL vs Condition Score (Machine Map)",
            xaxis_title="RUL (cycles)",yaxis_title="Condition Score")
        st.plotly_chart(pdark(fig_sc),use_container_width=True)
    with c4:
        gc2="#39ff14" if fs>=70 else "#ffc107" if fs>=40 else "#ff2d55"
        fig_g=go.Figure(go.Indicator(mode="gauge+number+delta",value=fs,
            delta={"reference":80,"relative":False,"font":{"color":"#a0c0e0","size":12}},
            title={"text":"Fleet Health Score","font":{"color":"#c8e0f8","family":"Orbitron","size":11}},
            gauge={"axis":{"range":[0,100],"tickcolor":"#4a6a90",
                       "tickfont":{"color":"#4a6a90","family":"JetBrains Mono","size":9}},
                "bar":{"color":gc2,"thickness":0.24,
                       "line":{"color":gc2,"width":1}},
                "bgcolor":"rgba(4,11,24,1)",
                "borderwidth":1,"bordercolor":"rgba(0,212,255,0.15)",
                "steps":[{"range":[0,40],"color":"rgba(255,45,85,0.1)"},
                          {"range":[40,70],"color":"rgba(255,193,7,0.08)"},
                          {"range":[70,100],"color":"rgba(57,255,20,0.08)"}],
                "threshold":{"line":{"color":gc2,"width":3},"thickness":0.78,"value":fs}},
            number={"suffix":"%","font":{"color":gc2,"family":"Orbitron","size":38},
                    "valueformat":".1f"}))
        st.plotly_chart(pdark(fig_g),use_container_width=True)

    h1,h2=st.columns(2)
    with h1:
        fig_h=px.histogram(fdf,x="RUL",nbins=15,title="Fleet RUL Distribution",
            color_discrete_sequence=["#0077ff"])
        fig_h.update_traces(
            marker=dict(color="rgba(0,120,255,0.75)",
                        line=dict(color="rgba(0,212,255,0.5)",width=1)),
            hovertemplate="RUL %{x}<br>Count: %{y}<extra></extra>")
        st.plotly_chart(pdark(fig_h),use_container_width=True)
    with h2:
        fig_bx=px.box(fdf,y="Tool Wear",color="Status",title="Tool Wear by Health Status",
            color_discrete_map={"🟢 HEALTHY":"#39ff14","🟡 WARNING":"#ffc107","🔴 CRITICAL":"#ff2d55"})
        fig_bx.update_traces(marker=dict(opacity=0.8,size=4),line=dict(width=1.5))
        fig_bx.add_hline(y=200,line_dash="dash",line_color="#ff2d55",opacity=0.45,
            annotation_text="Replace Threshold",annotation_font_color="#ff2d55")
        st.plotly_chart(pdark(fig_bx),use_container_width=True)

    fig_rt=go.Figure()
    for zone,zclr,sym,zsz in [("🟢 HEALTHY","#39ff14","circle",10),
                                ("🟡 WARNING","#ffc107","diamond",10),
                                ("🔴 CRITICAL","#ff2d55","x",13)]:
        m=fdf[fdf["Status"]==zone]
        if len(m)>0:
            fig_rt.add_trace(go.Scatter(x=m["RPM"],y=m["Torque"],mode="markers",name=zone,
                marker=dict(color=zclr,size=zsz,opacity=0.86,symbol=sym,
                    line=dict(color="rgba(4,11,24,0.5)",width=1.2)),
                hovertemplate="<b>%{customdata}</b><br>RPM: %{x:.0f}<br>Torque: %{y:.1f} Nm<extra></extra>",
                customdata=m["Machine ID"]))
    fig_rt.add_vrect(x0=1300,x1=1700,fillcolor="rgba(0,212,255,0.03)",line_width=0,
        annotation_text="Normal Zone",annotation_font_color="#4a6a90",annotation_font_size=9)
    fig_rt.update_layout(title="Fleet RPM vs Torque — Health Zones",
        xaxis_title="Rotational Speed [rpm]",yaxis_title="Torque [Nm]")
    st.plotly_chart(pdark(fig_rt),use_container_width=True)

    st.download_button("⬇️ Export Fleet Report CSV",fdf.to_csv(index=False).encode(),"fleet_report.csv","text/csv")


# ═══════════════════════════════════════════════════════
# ANALYTICS
# ═══════════════════════════════════════════════════════
elif page=="Analytics":
    page_header("📊 ANALYTICS", "Advanced sensor analytics, industrial-grade multi-panel dashboards, trend analysis and correlation", "#ffc107")

    demo=gen_ts(150)

    # ── Live KPI row ──
    st.markdown('<div class="sh">LIVE SENSOR SNAPSHOT</div>', unsafe_allow_html=True)
    ak=st.columns(6)
    last_d=demo.iloc[-1]
    at_tr=("⚠ High","crit") if last_d.air_temp>308 else ("Normal","up")
    tw_tr=("⚠ Wear","crit") if last_d.tool_wear>180 else ("Monitor","warn") if last_d.tool_wear>120 else ("Good","up")
    rul_tr=("⚠ Low","crit") if last_d.rul<30 else ("Watch","warn") if last_d.rul<80 else ("Healthy","up")
    for col,(v,l,ic,cls2,d,tr,br) in zip(ak,[
        (f"{last_d.air_temp:.1f} K","Air Temp",   "🌡️","",  "K — Normal: 290–308",   at_tr, int((last_d.air_temp-290)/(322-290)*100)),
        (f"{last_d.process_temp:.1f} K","Proc Temp","🔥","o","K — Normal: 298–315",   ("Normal","up"), 60),
        (f"{last_d.rpm:.0f}",       "RPM",         "⚙️","",  "rpm — Target: 1500",    ("Nominal","up"), int(abs(last_d.rpm-500)/1500*100)),
        (f"{last_d.torque:.1f} Nm", "Torque",      "🔩","y", "Nm — Range: 20–65",     ("Normal","up"), int(last_d.torque/80*100)),
        (f"{last_d.tool_wear:.0f} min","Tool Wear", "🔧","r", "min — Limit: 200",      tw_tr,           int(last_d.tool_wear/200*100)),
        (f"{last_d.rul:.0f} cyc",   "Est. RUL",    "🔋","g", "cycles remaining",      rul_tr,          int(min(last_d.rul/200,1)*100)),
    ]): col.markdown(pdk(v,l,ic,cls2,d,tr,br),unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)

    # ── REFERENCE STYLE: 3×2 Multi-panel Industrial Dashboard ──
    st.markdown('<div class="sh">INDUSTRIAL SENSOR DASHBOARD — 6-PANEL VIEW</div>', unsafe_allow_html=True)
    fig6=make_subplots(
        rows=3,cols=2,
        subplot_titles=("Air & Process Temperature [K]","RPM & Torque (Dual Axis)",
                        "Tool Wear Progression [min]","RUL Degradation Curve",
                        "Vibration Signal [g]","Pressure Monitor [bar]"),
        vertical_spacing=0.11,horizontal_spacing=0.08,
        specs=[[{"secondary_y":False},{"secondary_y":True}],
               [{"secondary_y":False},{"secondary_y":False}],
               [{"secondary_y":False},{"secondary_y":False}]])
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.air_temp,name="Air Temp [K]",legendgroup="temp",
        line=dict(color="#00d4ff",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,90,255,0.1)"),row=1,col=1)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.process_temp,name="Process Temp [K]",legendgroup="temp",
        line=dict(color="#ff6b35",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(255,107,53,0.07)"),row=1,col=1)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.rpm,name="RPM",legendgroup="rpm",
        line=dict(color="#00d4ff",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,90,255,0.09)"),row=1,col=2,secondary_y=False)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.torque,name="Torque [Nm]",legendgroup="torque",
        line=dict(color="#ffc107",width=2,shape="spline",smoothing=0.5)),row=1,col=2,secondary_y=True)
    fig6.add_trace(go.Bar(x=demo.cycle[::6],y=demo.tool_wear[::6],name="Tool Wear [min]",showlegend=False,
        marker=dict(color=["#ff2d55" if v>180 else "#ffc107" if v>120 else "#00d4ff" for v in demo.tool_wear[::6]],
            opacity=0.82,line=dict(width=0))),row=2,col=1)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.rul,name="RUL (cycles)",legendgroup="rul",
        line=dict(color="#39ff14",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,180,60,0.09)"),row=2,col=2)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.vibration,name="Vibration [g]",legendgroup="vib",
        line=dict(color="#ffc107",width=1.8,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(255,193,7,0.07)"),row=3,col=1)
    fig6.add_trace(go.Scatter(x=demo.cycle,y=demo.pressure,name="Pressure [bar]",legendgroup="pres",
        line=dict(color="#b44dff",width=1.8,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(120,0,255,0.07)"),row=3,col=2)
    fig6.add_hline(y=110,line_dash="dash",line_color="#ff2d55",opacity=0.35,row=3,col=2)
    fig6.add_hline(y=90,line_dash="dash",line_color="#ffc107",opacity=0.35,row=3,col=2)
    fig6.add_hline(y=310,line_dash="dash",line_color="#ff2d55",opacity=0.3,row=1,col=1)
    fig6.add_hline(y=30,line_dash="dash",line_color="#ff2d55",opacity=0.3,row=2,col=2)
    fig6.add_hline(y=80,line_dash="dash",line_color="#ffc107",opacity=0.25,row=2,col=2)
    fig6.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(4,11,24,0.97)",
        height=870,showlegend=True,
        font=dict(color="#c8e0f8",family="Inter",size=10),
        title=dict(text="PREDICTASHIELD — MULTI-SENSOR INDUSTRIAL DASHBOARD",
                   font=dict(family="Orbitron",color="#d0eaff",size=12)),
        legend=dict(bgcolor="rgba(4,11,24,0.9)",bordercolor="rgba(0,212,255,0.18)",
                    borderwidth=1,font=dict(size=9.5,family="Inter",color="#a0c0e0")),
        hoverlabel=dict(bgcolor="rgba(4,11,24,0.96)",bordercolor="rgba(0,212,255,0.35)",
                        font=dict(family="Inter",color="#e0f0ff",size=11)),
        margin=dict(l=22,r=22,t=68,b=22))
    for r in range(1,4):
        for c in range(1,3):
            fig6.update_xaxes(gridcolor="rgba(0,100,200,0.09)",
                tickfont=dict(color="#4a6a90",size=8.5,family="JetBrains Mono"),
                linecolor="rgba(0,212,255,0.07)",row=r,col=c)
            fig6.update_yaxes(gridcolor="rgba(0,100,200,0.09)",
                tickfont=dict(color="#4a6a90",size=8.5,family="JetBrains Mono"),
                linecolor="rgba(0,212,255,0.07)",row=r,col=c)
    for ann in fig6.layout.annotations:
        ann.font.update(family="Orbitron",color="#7a9cbf",size=9.5)
    st.plotly_chart(fig6,use_container_width=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)

    st.markdown('<div class="sh">TEMPERATURE TREND ANALYSIS</div>', unsafe_allow_html=True)
    ft=go.Figure()
    ft.add_trace(go.Scatter(x=demo.cycle,y=demo.air_temp,name="Air Temp [K]",
        line=dict(color="#00d4ff",width=2.2,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(0,90,255,0.11)",
        hovertemplate="Cycle %{x}<br>Air Temp: %{y:.1f} K<extra></extra>"))
    ft.add_trace(go.Scatter(x=demo.cycle,y=demo.process_temp,name="Process Temp [K]",
        line=dict(color="#ff6b35",width=2.2,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(255,107,53,0.08)",
        hovertemplate="Cycle %{x}<br>Proc Temp: %{y:.1f} K<extra></extra>"))
    ft.add_hrect(y0=308,y1=322,fillcolor="rgba(255,45,85,0.05)",line_width=0,
        annotation_text="⚠️ High Temp Zone",annotation_font_color="#ff2d55")
    ft.add_hline(y=310,line_dash="dash",line_color="#ff2d55",opacity=0.4,
        annotation_text="Threshold",annotation_font_color="#ff2d55")
    ft.update_layout(title="Air & Process Temperature — Multi-Line with Zones",
        xaxis_title="Cycle",yaxis_title="Temperature [K]")
    st.plotly_chart(pdark(ft),use_container_width=True)

    st.markdown('<div class="sh">RPM / TORQUE / POWER — TRIPLE DUAL-AXIS</div>', unsafe_allow_html=True)
    frt=make_subplots(specs=[[{"secondary_y":True}]])
    frt.add_trace(go.Scatter(x=demo.cycle,y=demo.rpm,name="RPM",
        line=dict(color="#00d4ff",width=2.2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,90,255,0.1)"),secondary_y=False)
    frt.add_trace(go.Scatter(x=demo.cycle,y=demo.torque,name="Torque [Nm]",
        line=dict(color="#ffc107",width=2,shape="spline",smoothing=0.5)),secondary_y=True)
    frt.add_trace(go.Scatter(x=demo.cycle,y=demo.power*10,name="Power×10 [W]",
        line=dict(color="#b44dff",width=1.6,dash="dot",shape="spline",smoothing=0.5)),secondary_y=True)
    frt.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(4,11,24,0.97)",
        font=dict(color="#c8e0f8",family="Inter"),
        title="Rotational Speed, Torque & Power (Triple Axis)",
        title_font=dict(family="Orbitron",color="#d0eaff",size=11),
        margin=dict(l=22,r=22,t=52,b=22),
        legend=dict(bgcolor="rgba(4,11,24,0.9)",bordercolor="rgba(0,212,255,0.18)",
                    borderwidth=1,font=dict(size=10,family="Inter",color="#a0c0e0")),
        hoverlabel=dict(bgcolor="rgba(4,11,24,0.96)",bordercolor="rgba(0,212,255,0.35)",
                        font=dict(family="Inter",color="#e0f0ff",size=11)))
    frt.update_yaxes(title_text="RPM",secondary_y=False,
        gridcolor="rgba(0,100,200,0.09)",tickfont=dict(color="#4a6a90",family="JetBrains Mono"))
    frt.update_yaxes(title_text="Torque / Power",secondary_y=True,
        tickfont=dict(color="#4a6a90",family="JetBrains Mono"))
    frt.update_xaxes(gridcolor="rgba(0,100,200,0.09)",
        tickfont=dict(color="#4a6a90",family="JetBrains Mono"),title_text="Cycle")
    st.plotly_chart(frt,use_container_width=True)

    a1,a2=st.columns(2,gap="medium")
    with a1:
        st.markdown('<div class="sh">TOOL WEAR PROGRESSION</div>', unsafe_allow_html=True)
        ftw=go.Figure()
        ftw.add_trace(go.Scatter(x=demo.cycle,y=demo.tool_wear,name="Tool Wear",
            line=dict(color="#ff6b35",width=2.2,shape="spline",smoothing=0.6),
            fill="tozeroy",fillcolor="rgba(255,107,53,0.1)",
            hovertemplate="Cycle %{x}<br>Wear: %{y:.0f} min<extra></extra>"))
        ftw.add_hline(y=120,line_dash="dot",line_color="#ffc107",opacity=0.55,
            annotation_text="⚠️ 120",annotation_font_color="#ffc107")
        ftw.add_hline(y=180,line_dash="dot",line_color="#ff2d55",opacity=0.55,
            annotation_text="🔴 180",annotation_font_color="#ff2d55")
        ftw.add_hline(y=200,line_dash="dash",line_color="#ff2d55",opacity=0.8,
            annotation_text="REPLACE",annotation_font_color="#ff2d55")
        ftw.update_layout(title="Tool Wear Over Time",xaxis_title="Cycle",yaxis_title="Wear [min]")
        st.plotly_chart(pdark(ftw),use_container_width=True)
    with a2:
        st.markdown('<div class="sh">RUL DEGRADATION CURVE</div>', unsafe_allow_html=True)
        frul=go.Figure()
        frul.add_trace(go.Scatter(x=demo.cycle,y=demo.rul,name="RUL",
            line=dict(color="#39ff14",width=2.2,shape="spline",smoothing=0.6),
            fill="tozeroy",fillcolor="rgba(0,180,60,0.1)",
            hovertemplate="Cycle %{x}<br>RUL: %{y:.0f} cycles<extra></extra>"))
        frul.add_hrect(y0=0,y1=30,fillcolor="rgba(255,45,85,0.09)",line_width=0,
            annotation_text="🔴 CRITICAL",annotation_font_color="#ff2d55")
        frul.add_hrect(y0=30,y1=80,fillcolor="rgba(255,193,7,0.06)",line_width=0,
            annotation_text="🟡 WARNING",annotation_font_color="#ffc107")
        frul.update_layout(title="Remaining Useful Life Degradation",
            xaxis_title="Cycle",yaxis_title="RUL (cycles)")
        st.plotly_chart(pdark(frul),use_container_width=True)

    a3,a4=st.columns(2,gap="medium")
    with a3:
        st.markdown('<div class="sh">VIBRATION ANALYSIS</div>', unsafe_allow_html=True)
        fvib=go.Figure()
        fvib.add_trace(go.Scatter(x=demo.cycle,y=demo.vibration,name="Vibration",
            line=dict(color="#ffc107",width=2,shape="spline",smoothing=0.65),
            fill="tozeroy",fillcolor="rgba(255,193,7,0.08)",
            hovertemplate="Cycle %{x}<br>Vibration: %{y:.2f} g<extra></extra>"))
        fvib.add_hrect(y0=0.8,y1=2,fillcolor="rgba(255,45,85,0.06)",line_width=0,
            annotation_text="High Zone",annotation_font_color="#ff2d55")
        fvib.update_layout(title="Vibration Sensor Reading",xaxis_title="Cycle",yaxis_title="Amplitude [g]")
        st.plotly_chart(pdark(fvib),use_container_width=True)
    with a4:
        st.markdown('<div class="sh">PRESSURE MONITORING</div>', unsafe_allow_html=True)
        fpr=go.Figure()
        fpr.add_trace(go.Scatter(x=demo.cycle,y=demo.pressure,name="Pressure",
            line=dict(color="#b44dff",width=2,shape="spline",smoothing=0.65),
            fill="tozeroy",fillcolor="rgba(120,0,255,0.08)",
            hovertemplate="Cycle %{x}<br>Pressure: %{y:.1f} bar<extra></extra>"))
        fpr.add_hline(y=110,line_dash="dash",line_color="#ff2d55",opacity=0.5,
            annotation_text="Upper Limit",annotation_font_color="#ff2d55")
        fpr.add_hline(y=90,line_dash="dash",line_color="#ffc107",opacity=0.5,
            annotation_text="Lower Limit",annotation_font_color="#ffc107")
        fpr.update_layout(title="Pressure Sensor Reading [bar]",xaxis_title="Cycle",yaxis_title="Pressure [bar]")
        st.plotly_chart(pdark(fpr),use_container_width=True)

    st.markdown('<div class="sh">OEE-STYLE EFFICIENCY & POWER TREND</div>', unsafe_allow_html=True)
    foee=make_subplots(specs=[[{"secondary_y":True}]])
    foee.add_trace(go.Scatter(x=demo.cycle,y=demo.efficiency,name="Efficiency [%]",
        line=dict(color="#39ff14",width=2.2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,180,60,0.09)"),secondary_y=False)
    foee.add_trace(go.Bar(x=demo.cycle[::5],y=demo.power[::5],name="Power [kW]",
        marker=dict(color=["#ff2d55" if v>8 else "#ffc107" if v>6 else "#0077ff" for v in demo.power[::5]],
            opacity=0.75,line=dict(width=0))),secondary_y=True)
    foee.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(4,11,24,0.97)",
        font=dict(color="#c8e0f8",family="Inter"),
        title="Efficiency (%) & Power Output (kW) — OEE Monitoring",
        title_font=dict(family="Orbitron",color="#d0eaff",size=11),
        margin=dict(l=22,r=22,t=52,b=22),
        legend=dict(bgcolor="rgba(4,11,24,0.9)",bordercolor="rgba(0,212,255,0.18)",
                    borderwidth=1,font=dict(size=10,family="Inter",color="#a0c0e0")),
        hoverlabel=dict(bgcolor="rgba(4,11,24,0.96)",bordercolor="rgba(0,212,255,0.35)",
                        font=dict(family="Inter",color="#e0f0ff",size=11)))
    foee.update_yaxes(title_text="Efficiency [%]",secondary_y=False,
        gridcolor="rgba(0,100,200,0.09)",tickfont=dict(color="#4a6a90",family="JetBrains Mono"))
    foee.update_yaxes(title_text="Power [kW]",secondary_y=True,
        tickfont=dict(color="#4a6a90",family="JetBrains Mono"))
    foee.update_xaxes(gridcolor="rgba(0,100,200,0.09)",
        tickfont=dict(color="#4a6a90",family="JetBrains Mono"),title_text="Cycle")
    st.plotly_chart(foee,use_container_width=True)

    st.markdown('<div class="sh">SENSOR CORRELATION SCATTER — HEALTH ZONES</div>', unsafe_allow_html=True)
    rul_zones=["CRITICAL" if r<30 else "WARNING" if r<80 else "HEALTHY" for r in demo.rul]
    fsc2=go.Figure()
    for zone,zclr,sym,zsz in [("HEALTHY","#39ff14","circle",6),
                                ("WARNING","#ffc107","diamond",6),
                                ("CRITICAL","#ff2d55","x",8)]:
        m=demo[[r==zone for r in rul_zones]]
        if len(m)>0:
            fsc2.add_trace(go.Scatter(x=m.rpm,y=m.torque,mode="markers",name=zone,
                marker=dict(color=zclr,size=zsz,opacity=0.82,symbol=sym,
                    line=dict(color="rgba(4,11,24,0.5)",width=0.8)),
                hovertemplate="RPM: %{x:.0f}<br>Torque: %{y:.1f} Nm<extra></extra>"))
    fsc2.update_layout(title="RPM vs Torque — colored by RUL Health Zone",
        xaxis_title="RPM",yaxis_title="Torque [Nm]")
    st.plotly_chart(pdark(fsc2),use_container_width=True)

    st.markdown('<div class="sh">SENSOR CORRELATION HEATMAP</div>', unsafe_allow_html=True)
    corr=demo[["air_temp","process_temp","rpm","torque","tool_wear","rul","vibration","pressure","efficiency","power"]].corr()
    fhm=go.Figure(go.Heatmap(z=corr.values,x=corr.columns,y=corr.columns,
        colorscale=[[0,"#ff2d55"],[0.25,"#5a0020"],[0.5,"rgba(4,11,24,1)"],
                    [0.75,"#003a7a"],[1,"#00d4ff"]],
        zmid=0,text=np.round(corr.values,2),texttemplate="%{text}",
        textfont=dict(family="JetBrains Mono",size=8.5,color="#c8e0f8"),
        showscale=True,hoverongaps=False,
        colorbar=dict(tickfont=dict(color="#4a6a90",size=8.5,family="JetBrains Mono"),
            thickness=13,bgcolor="rgba(4,11,24,0.9)",
            bordercolor="rgba(0,212,255,0.15)",borderwidth=1)))
    fhm.update_layout(title="10-Sensor Correlation Matrix",height=470)
    st.plotly_chart(pdark(fhm),use_container_width=True)


# ═══════════════════════════════════════════════════════
# SENSOR DASHBOARD  (NEW)
# ═══════════════════════════════════════════════════════
elif page=="Sensor Dashboard":
    page_header("📡 SENSOR DASHBOARD", "Live multi-sensor monitoring — all parameters in one industrial view", "#b44dff")

    demo=gen_ts(120,seed=int(time.time())%200)
    last=demo.iloc[-1]

    # 8-sensor live tiles
    st.markdown('<div class="sh">LIVE SENSOR READINGS</div>', unsafe_allow_html=True)
    sv=st.columns(8)
    live_sensors=[
        (f"{last.air_temp:.1f}","K","Air Temp","🌡️","#00d4ff"),
        (f"{last.process_temp:.1f}","K","Proc Temp","🔥","#ff6b35"),
        (f"{last.rpm:.0f}","rpm","Speed","⚙️","#39ff14"),
        (f"{last.torque:.1f}","Nm","Torque","🔩","#ffc107"),
        (f"{last.tool_wear:.0f}","min","Tool Wear","🔧","#ff2d55"),
        (f"{last.rul:.0f}","cyc","Est. RUL","🔋","#39ff14"),
        (f"{last.vibration:.2f}","g","Vibration","📳","#ffc107"),
        (f"{last.pressure:.1f}","bar","Pressure","🌀","#b44dff"),
    ]
    for col,(val,unit,lbl,ic,clr) in zip(sv,live_sensors):
        col.markdown(f"""<div class="sensor-card">
          <div style="font-size:0.55rem;color:#6a8faf;text-transform:uppercase;letter-spacing:0.09em;margin-bottom:0.2rem">{ic} {lbl}</div>
          <div style="font-family:'Orbitron',monospace;font-size:1.25rem;font-weight:900;
            color:{clr};text-shadow:0 0 10px {clr}66;line-height:1">{val}</div>
          <div style="font-size:0.52rem;color:{clr};letter-spacing:0.06em;margin-top:2px">{unit}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)

    # Reference-style: 3×2 subplot dashboard
    st.markdown('<div class="sh">MULTI-SENSOR SUBPLOT DASHBOARD — INDUSTRIAL VIEW</div>', unsafe_allow_html=True)
    fig_sub=make_subplots(rows=3,cols=2,
        subplot_titles=("Air & Process Temperature","RPM & Torque",
                        "Tool Wear Progression","RUL Degradation",
                        "Vibration Signal","Pressure Monitor"),
        vertical_spacing=0.1,horizontal_spacing=0.07)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.air_temp,name="Air Temp",
        line=dict(color="#00d4ff",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,90,255,0.1)"),row=1,col=1)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.process_temp,name="Proc Temp",
        line=dict(color="#ff6b35",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(255,107,53,0.07)"),row=1,col=1)
    fig_sub.add_trace(go.Bar(x=demo.cycle[::4],y=demo.rpm[::4],name="RPM",showlegend=False,
        marker=dict(color="rgba(0,120,255,0.65)",line=dict(width=0))),row=1,col=2)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.torque*22,name="Torque×22",
        line=dict(color="#ffc107",width=2,shape="spline",smoothing=0.5)),row=1,col=2)
    fig_sub.add_trace(go.Bar(x=demo.cycle[::5],y=demo.tool_wear[::5],name="Tool Wear",showlegend=False,
        marker=dict(color=["#ff2d55" if v>180 else "#ffc107" if v>120 else "#00d4ff" for v in demo.tool_wear[::5]],
            opacity=0.82,line=dict(width=0))),row=2,col=1)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.rul,name="RUL",
        line=dict(color="#39ff14",width=2,shape="spline",smoothing=0.5),
        fill="tozeroy",fillcolor="rgba(0,180,60,0.09)"),row=2,col=2)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.vibration,name="Vibration",
        line=dict(color="#ffc107",width=1.8,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(255,193,7,0.08)"),row=3,col=1)
    fig_sub.add_trace(go.Scatter(x=demo.cycle,y=demo.pressure,name="Pressure",
        line=dict(color="#b44dff",width=1.8,shape="spline",smoothing=0.6),
        fill="tozeroy",fillcolor="rgba(120,0,255,0.08)"),row=3,col=2)
    fig_sub.add_hline(y=110,line_dash="dash",line_color="#ff2d55",opacity=0.4,row=3,col=2)
    fig_sub.add_hline(y=90,line_dash="dash",line_color="#ffc107",opacity=0.4,row=3,col=2)
    fig_sub.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(4,11,24,0.97)",
        height=840,showlegend=True,
        font=dict(color="#c8e0f8",family="Inter",size=10),
        title=dict(text="PREDICTASHIELD — REAL-TIME SENSOR MONITORING DASHBOARD",
                   font=dict(family="Orbitron",color="#d0eaff",size=12)),
        legend=dict(bgcolor="rgba(4,11,24,0.9)",bordercolor="rgba(0,212,255,0.18)",
                    borderwidth=1,font=dict(size=9.5,family="Inter",color="#a0c0e0")),
        hoverlabel=dict(bgcolor="rgba(4,11,24,0.96)",bordercolor="rgba(0,212,255,0.35)",
                        font=dict(family="Inter",color="#e0f0ff",size=11)),
        margin=dict(l=22,r=22,t=65,b=22))
    for r2 in range(1,4):
        for c2 in range(1,3):
            fig_sub.update_xaxes(gridcolor="rgba(0,212,255,0.04)",tickfont=dict(color="#6a8faf",size=9),row=r2,col=c2)
            fig_sub.update_yaxes(gridcolor="rgba(0,212,255,0.04)",tickfont=dict(color="#6a8faf",size=9),row=r2,col=c2)
    st.plotly_chart(fig_sub,use_container_width=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)

    # Operational envelope scatter (like reference image)
    st.markdown('<div class="sh">OPERATIONAL ENVELOPE — RPM vs TORQUE (Colored by Tool Wear)</div>', unsafe_allow_html=True)
    fig_env=go.Figure()
    fig_env.add_trace(go.Scatter(x=demo.rpm,y=demo.torque,mode="markers",name="Operating Points",
        marker=dict(color=demo.tool_wear,colorscale=[[0,"#39ff14"],[0.45,"#ffc107"],[1,"#ff2d55"]],
            size=7,opacity=0.82,colorbar=dict(title="Tool Wear [min]",tickfont=dict(color="#6a8faf",size=9),thickness=14),
            line=dict(color="rgba(2,12,27,0.4)",width=0.5))))
    fig_env.add_vrect(x0=1300,x1=1700,fillcolor="rgba(57,255,20,0.04)",line_width=0,annotation_text="✅ Normal RPM Zone",annotation_font_color="#39ff14")
    fig_env.add_hrect(y0=30,y1=65,fillcolor="rgba(0,212,255,0.03)",line_width=0,annotation_text="✅ Normal Torque",annotation_font_color="#00d4ff")
    fig_env.update_layout(title="Operational Envelope — Colored by Tool Wear",xaxis_title="Rotational Speed [rpm]",yaxis_title="Torque [Nm]",height=420)
    st.plotly_chart(pdark(fig_env),use_container_width=True)

    # Sensor health bars
    st.markdown('<hr class="div">', unsafe_allow_html=True)
    st.markdown('<div class="sh">SENSOR HEALTH STATUS BARS</div>', unsafe_allow_html=True)
    pb1,pb2=st.columns(2,gap="large")
    params_sb=[
        ("Air Temperature",last.air_temp,"K",290,322,308,"#00d4ff"),
        ("Process Temperature",last.process_temp,"K",298,325,315,"#ff6b35"),
        ("Rotational Speed",last.rpm,"rpm",1000,2000,1700,"#39ff14"),
        ("Torque",last.torque,"Nm",20,80,65,"#ffc107"),
        ("Tool Wear",last.tool_wear,"min",0,220,120,"#ff2d55"),
        ("Vibration",last.vibration,"g",0,2,0.8,"#ffc107"),
        ("Pressure",last.pressure,"bar",78,132,110,"#b44dff"),
    ]
    for i,(name,val,unit,vmin,vmax,thresh,clr) in enumerate(params_sb):
        col=pb1 if i%2==0 else pb2
        pct=int((val-vmin)/(vmax-vmin)*100)
        warn="⚠️" if val>thresh else "✅"
        col.markdown(f"""<div style="margin:0.5rem 0">
          <div style="display:flex;justify-content:space-between;font-size:0.7rem;margin-bottom:3px">
            <span style="color:#a8c4e0">{warn} {name}</span>
            <span style="color:{clr};font-weight:600">{val:.1f} {unit}</span>
          </div>
          <div class="rt"><div class="rf" style="width:{min(pct,100)}%;background:linear-gradient(90deg,{clr}44,{clr});box-shadow:0 0 5px {clr}44"></div></div>
          <div style="font-size:0.6rem;color:#6a8faf;margin-top:2px">Range {vmin}–{vmax} {unit} · Threshold: {thresh}</div>
        </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# ABOUT  (NEW)
# ═══════════════════════════════════════════════════════
elif page=="About":
    page_header("ℹ️ ABOUT PREDICTASHIELD", "Project overview, architecture, datasets, performance metrics and roadmap", "#ffc107")

    # Hero card
    st.markdown("""
    <div class="card" style="background:linear-gradient(135deg,rgba(0,212,255,0.04),rgba(255,107,53,0.03),rgba(57,255,20,0.02));
      border:1px solid rgba(0,212,255,0.15);border-radius:14px;padding:2rem 2.2rem;margin-bottom:1.2rem;position:relative;overflow:hidden">
      <div style="position:absolute;top:-80px;right:-60px;width:320px;height:320px;
        background:radial-gradient(ellipse,rgba(0,212,255,0.06) 0%,transparent 70%);pointer-events:none"></div>
      <div style="position:relative;z-index:1">
        <div style="font-family:'Orbitron',monospace;font-size:1.8rem;font-weight:900;
          background:linear-gradient(135deg,#00d4ff,#ffffff 40%,#ff6b35);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:0.5rem">
          PREDICTASHIELD v5.0</div>
        <div style="font-size:0.88rem;color:#a8c4e0;max-width:800px;line-height:1.9">
          An industrial-grade AI platform combining <strong style="color:#00d4ff">machine failure classification</strong> (UCI AI4I 2020)
          and <strong style="color:#ff6b35">remaining useful life regression</strong> (NASA C-MAPSS) into a
          unified dual-model fusion system — with 8 dashboard pages, AI recommendations,
          fleet monitoring, and auto-generated diagnosis reports.
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    lft,rgt=st.columns([1,1],gap="large")
    with lft:
        st.markdown('<div class="sh">PROJECT HIGHLIGHTS</div>', unsafe_allow_html=True)
        for icon,title,desc in [
            ("🎯","99.2% Model Accuracy","AI4I RandomForest on 10,000 UCI samples"),
            ("🔋","26-Feature NASA Model","C-MAPSS turbofan — 4 operating conditions"),
            ("⚡","Dual Fusion Engine","AI4I + NASA → HEALTHY/WARNING/CRITICAL"),
            ("📊","8 Dashboard Pages","Home · Diagnosis · Fleet · Analytics · Sensor · Review · FAQ · About"),
            ("📄","Auto Report Generator","Full .txt diagnosis reports with AI recommendation"),
            ("💯","Condition Score 0–100","Composite: failure + RUL + tool wear"),
            ("📡","Sensor Dashboard","Live 8-sensor tiles + 3×2 subplot industrial view"),
            ("🔮","AI Recommendation","Priority, actions, confidence level per diagnosis"),
        ]:
            st.markdown(f"""<div class="ftile" style="margin-bottom:0.42rem">
              <div style="display:flex;align-items:center;gap:0.65rem">
                <div style="font-size:1.2rem">{icon}</div>
                <div>
                  <div style="font-family:'Orbitron',monospace;font-size:0.68rem;color:#00d4ff;font-weight:700;margin-bottom:1px">{title}</div>
                  <div style="font-size:0.76rem;color:#a8c4e0">{desc}</div>
                </div>
              </div>
            </div>""", unsafe_allow_html=True)

    with rgt:
        st.markdown('<div class="sh">DEVELOPMENT TIMELINE</div>', unsafe_allow_html=True)
        for ver,title,desc,clr in [
            ("v1","Basic Diagnosis","AI4I model + manual sensor input","#00d4ff"),
            ("v2","NASA Integration","RUL prediction + CSV upload batch mode","#ff6b35"),
            ("v3","Fleet Monitoring","Multi-machine batch + status charts + gauge","#39ff14"),
            ("v4","Full Dashboard","Analytics · Machine Review · AI Chat · PDF Report","#ffc107"),
            ("v5","Sensor Dashboard","8 pages · Subplot graphs · About · Expanded FAQ","#b44dff"),
        ]:
            st.markdown(f"""<div class="tl-item">
              <div class="tl-dot" style="border-color:{clr};box-shadow:0 0 7px {clr}40">
                <span style="font-family:'Orbitron',monospace;font-size:0.5rem;color:{clr};font-weight:700">{ver}</span>
              </div>
              <div style="background:var(--bgc);border:1px solid var(--bd);border-radius:8px;padding:0.6rem 0.85rem;flex:1">
                <div style="font-family:'Orbitron',monospace;font-size:0.68rem;color:{clr};font-weight:700;margin-bottom:2px">{title}</div>
                <div style="font-size:0.76rem;color:#a8c4e0">{desc}</div>
              </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    st.markdown('<div class="sh">DATASETS</div>', unsafe_allow_html=True)
    ds1,ds2=st.columns(2,gap="medium")
    with ds1:
        st.markdown("""<div class="card" style="border-left:3px solid #00d4ff">
          <div style="font-family:'Orbitron',monospace;font-size:0.7rem;color:#00d4ff;font-weight:700;margin-bottom:0.45rem">UCI AI4I 2020 DATASET</div>
          <div style="font-size:0.8rem;color:#a8c4e0;line-height:1.85">
            <b>Source:</b> UCI Machine Learning Repository<br>
            <b>Records:</b> 10,000 milling machine rows<br>
            <b>Features:</b> Air temp, process temp, RPM, torque, tool wear<br>
            <b>Target:</b> Binary failure classification (0/1)<br>
            <b>Failure Modes:</b> TWF · HDF · PWF · OSF · RNF<br>
            <b>Model:</b> RandomForest Classifier · ~99.2% accuracy
          </div>
        </div>""", unsafe_allow_html=True)
    with ds2:
        st.markdown("""<div class="card" style="border-left:3px solid #ff6b35">
          <div style="font-family:'Orbitron',monospace;font-size:0.7rem;color:#ff6b35;font-weight:700;margin-bottom:0.45rem">NASA C-MAPSS DATASET</div>
          <div style="font-size:0.8rem;color:#a8c4e0;line-height:1.85">
            <b>Source:</b> NASA Prognostics Data Repository<br>
            <b>Conditions:</b> FD001 · FD002 · FD003 · FD004<br>
            <b>Features:</b> Cycle + 25 turbofan sensor readings<br>
            <b>Target:</b> Remaining Useful Life (cycles)<br>
            <b>Domain:</b> Turbofan engine degradation simulation<br>
            <b>Model:</b> RandomForest Regressor · RMSE validated
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="div">', unsafe_allow_html=True)
    st.markdown('<div class="sh">FUTURE ROADMAP</div>', unsafe_allow_html=True)
    r1c,r2c,r3c,r4c,r5c=st.columns(5)
    for col,(icon,title,desc,clr) in zip([r1c,r2c,r3c,r4c,r5c],[
        ("🧠","v6 — Deep Learning","LSTM/Transformer for time-series RUL","#b44dff"),
        ("🌐","v7 — IoT Streams","Real-time MQTT/REST sensor ingestion","#00d4ff"),
        ("☁️","v8 — Cloud SaaS","Multi-tenant with auth, alerts, APIs","#ff6b35"),
        ("📱","v9 — Mobile App","React Native field engineer dashboard","#39ff14"),
        ("🔄","v10 — AutoML","Auto-retraining MLOps pipeline","#ffc107"),
    ]):
        col.markdown(f"""<div class="ftile" style="text-align:center;padding:1rem 0.7rem">
          <div style="font-size:1.6rem;margin-bottom:0.35rem">{icon}</div>
          <div style="font-family:'Orbitron',monospace;font-size:0.62rem;color:{clr};font-weight:700;margin-bottom:0.25rem">{title}</div>
          <div style="font-size:0.7rem;color:#a8c4e0;line-height:1.55">{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align:center;padding:1.8rem 0 0.5rem">
      <div style="font-family:'Orbitron',monospace;font-size:0.95rem;color:#00d4ff;
        text-shadow:0 0 10px rgba(0,212,255,0.4);margin-bottom:0.35rem">🛡️ PREDICTASHIELD v5.0</div>
      <div style="font-size:0.72rem;color:#3a5a7a;line-height:1.9">
        AI4I 2020 · NASA C-MAPSS · Scikit-learn · Streamlit · Plotly<br>
        Built for Industrial Predictive Maintenance Research & Education
      </div>
    </div>""", unsafe_allow_html=True)
    render_footer()


# ═══════════════════════════════════════════════════════
# MACHINE REVIEW
# ═══════════════════════════════════════════════════════
elif page=="Machine Review":
    page_header("🔬 MACHINE REVIEW", "Deep single-machine health review, condition profile & maintenance history", "#ff2d55")

    st.markdown('<div class="sh">SELECT OR CONFIGURE MACHINE</div>', unsafe_allow_html=True)
    mc1,mc2,mc3=st.columns(3)
    with mc1:
        machine_id=st.text_input("Machine ID",value="MCH-101")
        machine_type=st.selectbox("Machine Type",["CNC Milling Machine","Turbofan Engine","Hydraulic Press","Conveyor Belt","Pump Motor"])
    with mc2:
        install_date=st.date_input("Installation Date",value=datetime(2022,1,15))
        last_maint=st.date_input("Last Maintenance",value=datetime(2024,11,20))
    with mc3:
        air_t2=st.number_input("Air Temp [K]",value=299.5,step=0.1)
        proc_t2=st.number_input("Process Temp [K]",value=309.2,step=0.1)
    mc4,mc5,mc6=st.columns(3)
    with mc4: rpm2=st.number_input("RPM",value=1560,step=10)
    with mc5: torque2=st.number_input("Torque [Nm]",value=45.0,step=0.1)
    with mc6: tool_wear2=st.number_input("Tool Wear [min]",value=95,step=1)

    if st.button("🔬  GENERATE MACHINE REVIEW"):
        with st.spinner("Analyzing machine profile…"):
            time.sleep(0.5)

        failure2=ai4i_model.predict(np.array([[air_t2,proc_t2,rpm2,torque2,tool_wear2]]))[0]
        try: nf2=nasa_model.n_features_in_
        except: nf2=26
        nasa_dummy=[1.0]+[0.0]*(nf2-1)
        rul2=int(nasa_model.predict(np.array([nasa_dummy]))[0])
        status2,badge2,sclr2=fuse(failure2,rul2)
        score2=cond_score(failure2,rul2,tool_wear2)
        issues2,actions2,priority2=ai_rec(failure2,rul2,air_t2,proc_t2,rpm2,torque2,tool_wear2)
        age_days=(datetime.now().date()-install_date).days

        # Header
        st.markdown('<hr class="div">', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card" style="border-left:4px solid {sclr2};background:linear-gradient(135deg,{sclr2}06 0%,var(--bgc) 45%)">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.8rem">
            <div>
              <div style="font-family:'Orbitron',monospace;font-size:1.1rem;color:{sclr2};
                text-shadow:0 0 12px {sclr2}60;margin-bottom:0.25rem">{machine_id} — {machine_type}</div>
              <div style="font-size:0.78rem;color:#6a8faf">
                Age: <span style="color:#a8c4e0">{age_days} days</span> &nbsp;|&nbsp;
                Installed: <span style="color:#a8c4e0">{install_date}</span> &nbsp;|&nbsp;
                Last Maintenance: <span style="color:#a8c4e0">{last_maint}</span>
              </div>
            </div>
            <div style="text-align:right">
              <div style="font-family:'Orbitron',monospace;font-size:1.5rem;color:{sclr2};
                text-shadow:0 0 18px {sclr2}70">{status2}</div>
              <div style="margin-top:4px"><span class="{badge2}">{priority2}</span></div>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)

        # KPIs
        st.markdown('<div class="sh" style="margin-top:1.2rem">MACHINE HEALTH KPIs</div>', unsafe_allow_html=True)
        kk=st.columns(6)
        sc_c2="#ff2d55" if score2<40 else "#ffc107" if score2<70 else "#39ff14"
        score_tr=("↓ Critical","crit") if score2<40 else ("⚠ Warning","warn") if score2<70 else ("↑ Healthy","up")
        rul_tr2=("⚠ Critical","crit") if rul2<30 else ("Monitor","warn") if rul2<80 else ("Healthy","up")
        tw_tr2=("⚠ Replace","crit") if tool_wear2>180 else ("Monitor","warn") if tool_wear2>120 else ("Good","up")
        fail_tr=("⚠ FAILURE","crit") if failure2 else ("Clear","up")
        for col,(v,l,ic,cls2,d,tr,br) in zip(kk,[
            (f"{score2}/100","Condition Score","💯","r" if score2<40 else "y" if score2<70 else "g", "Composite health index", score_tr, score2),
            (f"{rul2} cyc","Remaining RUL","🔋","g" if rul2>80 else "y" if rul2>30 else "r", "Cycles remaining", rul_tr2, min(int(rul2/200*100),100)),
            (f"{tool_wear2} min","Tool Wear","🔧","r" if tool_wear2>180 else "y" if tool_wear2>120 else "g", "Limit: 200 min", tw_tr2, int(tool_wear2/200*100)),
            (f"{age_days}","Age (days)","📅","", "Since installation", ("Active","up"), min(int(age_days/1095*100),100)),
            (f"{'YES' if failure2 else 'NO'}","Failure Signal","⚠️","r" if failure2 else "g", "AI4I classification", fail_tr, 100 if failure2 else 0),
            (f"{rpm2}","Current RPM","⚙️","", "Target: 1500 rpm", ("Nominal","up") if abs(rpm2-1500)<200 else ("Deviated","warn"), min(int(rpm2/2000*100),100)),
        ]): col.markdown(pdk(v,l,ic,cls2,d,tr,br),unsafe_allow_html=True)

        # Health radar (spider chart)
        st.markdown('<hr class="div">', unsafe_allow_html=True)
        rr1,rr2=st.columns(2,gap="medium")
        with rr1:
            st.markdown('<div class="sh">HEALTH RADAR</div>', unsafe_allow_html=True)
            cats=["Condition Score","RUL Health","Tool Health","Temp Health","RPM Health","Torque Health"]
            rul_h=min(100,rul2/2)
            tool_h=max(0,100-tool_wear2/2)
            temp_h=max(0,100-(air_t2-295)*5)
            rpm_h=max(0,100-abs(rpm2-1500)/10)
            torq_h=max(0,100-(torque2-40)*2)
            vals=[score2,rul_h,tool_h,temp_h,rpm_h,torq_h]
            fig_rad=go.Figure()
            fig_rad.add_trace(go.Scatterpolar(r=vals+[vals[0]],theta=cats+[cats[0]],fill="toself",
                fillcolor="rgba(0,212,255,0.1)",line=dict(color="#00d4ff",width=2),name="Current"))
            fig_rad.add_trace(go.Scatterpolar(r=[80,80,80,80,80,80,80],theta=cats+[cats[0]],fill="toself",
                fillcolor="rgba(57,255,20,0.04)",line=dict(color="#39ff14",width=1,dash="dash"),name="Target"))
            fig_rad.update_layout(polar=dict(bgcolor="rgba(10,22,40,0.8)",
                radialaxis=dict(visible=True,range=[0,100],tickfont=dict(color="#6a8faf",size=8),gridcolor="rgba(0,212,255,0.12)"),
                angularaxis=dict(tickfont=dict(color="#a8c4e0",size=9),gridcolor="rgba(0,212,255,0.1)")),
                title="Machine Health Radar",paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#e8f4ff",family="Exo 2"),
                title_font=dict(family="Orbitron",color="#e8f4ff",size=11),
                legend=dict(bgcolor="rgba(10,22,40,0.8)",bordercolor="rgba(0,212,255,0.18)",borderwidth=1),
                margin=dict(l=55,r=55,t=55,b=25))
            st.plotly_chart(fig_rad,use_container_width=True)

        with rr2:
            st.markdown('<div class="sh">SENSOR PARAMETER STATUS</div>', unsafe_allow_html=True)
            params=[
                ("Air Temperature",air_t2,"K",290,320,308,"#00d4ff"),
                ("Process Temperature",proc_t2,"K",298,325,315,"#ff6b35"),
                ("Rotational Speed",rpm2,"rpm",1000,2000,1500,"#39ff14"),
                ("Torque",torque2,"Nm",20,80,65,"#ffc107"),
                ("Tool Wear",tool_wear2,"min",0,220,120,"#ff2d55"),
            ]
            for name,val,unit,vmin,vmax,thresh,clr in params:
                pct=int((val-vmin)/(vmax-vmin)*100)
                warn="⚠️" if val>thresh else "✅"
                st.markdown(f"""
                <div style="margin:0.5rem 0">
                  <div style="display:flex;justify-content:space-between;font-size:0.72rem;margin-bottom:3px">
                    <span style="color:#a8c4e0">{warn} {name}</span>
                    <span style="color:{clr};font-weight:600">{val:.1f} {unit}</span>
                  </div>
                  <div class="rt"><div class="rf" style="width:{min(pct,100)}%;background:linear-gradient(90deg,{clr}66,{clr})"></div></div>
                  <div style="font-size:0.63rem;color:#6a8faf;margin-top:2px">Range: {vmin}–{vmax} {unit} &nbsp;|&nbsp; Threshold: {thresh} {unit}</div>
                </div>""", unsafe_allow_html=True)

        # Issues + Actions
        st.markdown('<hr class="div">', unsafe_allow_html=True)
        ia1,ia2=st.columns(2,gap="large")
        with ia1:
            st.markdown('<div class="sh">DETECTED ISSUES</div>', unsafe_allow_html=True)
            issues2_html="".join(f'<div style="font-size:0.82rem;color:#a8c4e0;margin:0.28rem 0;padding:0.36rem 0.58rem;background:rgba(0,212,255,0.04);border-radius:5px;border-left:2px solid rgba(0,212,255,0.2)">{x}</div>' for x in issues2)
            st.markdown(f'<div class="card">{issues2_html}</div>', unsafe_allow_html=True)
        with ia2:
            st.markdown('<div class="sh">RECOMMENDED ACTIONS</div>', unsafe_allow_html=True)
            actions2_html="".join(f'<div style="font-size:0.82rem;color:#a8c4e0;margin:0.28rem 0;padding:0.36rem 0.58rem;background:rgba(57,255,20,0.04);border-radius:5px;border-left:2px solid rgba(57,255,20,0.2)">{x}</div>' for x in actions2)
            st.markdown(f'<div class="card">{actions2_html}</div>', unsafe_allow_html=True)

        # Maintenance schedule table
        st.markdown('<hr class="div">', unsafe_allow_html=True)
        st.markdown('<div class="sh">MAINTENANCE SCHEDULE</div>', unsafe_allow_html=True)
        next_check=(datetime.now()+timedelta(days=1 if priority2=="CRITICAL" else 3 if priority2=="WARNING" else 7)).strftime("%Y-%m-%d")
        sched_df=pd.DataFrame({
            "Task":["Lubrication Check","Tool Inspection","Vibration Check","Temperature Calibration","Full Service"],
            "Priority":["Medium","High" if tool_wear2>120 else "Low","Medium","Low","Low"],
            "Due Date":[(datetime.now()+timedelta(days=d)).strftime("%Y-%m-%d") for d in [3,2,7,14,30]],
            "Status":["Pending","⚠️ Urgent" if tool_wear2>120 else "Scheduled","Scheduled","Scheduled","Scheduled"],
        })
        st.dataframe(sched_df,use_container_width=True,hide_index=True)

        # Download report
        st.markdown('<hr class="div">', unsafe_allow_html=True)
        rec2_cfg={
            "HEALTHY":("✅ MACHINE IN GOOD HEALTH","Operating within normal parameters."),
            "WARNING": ("🟡 MAINTENANCE WINDOW APPROACHING","Schedule maintenance within 72 hours."),
            "CRITICAL":("🔴 IMMEDIATE ACTION REQUIRED","Stop machine. High failure risk."),
        }
        rt2,rd2=rec2_cfg[priority2]
        rpt2=make_machine_review_report(
            machine_id, machine_type, install_date, last_maint, age_days,
            air_t2, proc_t2, rpm2, torque2, tool_wear2,
            failure2, rul2, status2, score2, priority2,
            issues2, actions2, sched_df, rt2, rd2
        )
        st.download_button("📄 Download Machine Review Report",rpt2,
            f"MachineReview_{machine_id}_{datetime.now().strftime('%Y%m%d')}.txt","text/plain")


# ═══════════════════════════════════════════════════════
# FAQ + AI CHAT
# ═══════════════════════════════════════════════════════
elif page=="FAQ + AI Chat":
    st.markdown("""
    <style>
    /* Glowing AI Orb */
    .orb-container {
        display: flex; justify-content: center; align-items: center;
        padding: 3rem 0 1.5rem; position: relative;
    }
    .orb {
        width: 140px; height: 140px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #A855F7, #4C1D95, #1E1B4B);
        box-shadow: 0 0 50px rgba(139,92,246,0.5), inset 0 0 15px rgba(255,255,255,0.4);
        animation: orb-breathe 4s ease-in-out infinite;
        position: relative;
        display: flex; justify-content: center; align-items: center;
        margin: 0 auto;
    }
    .orb::after {
        content: ''; position: absolute; inset: -20px;
        border: 2px solid rgba(139,92,246,0.3); border-radius: 50%;
        animation: orb-ring 4s linear infinite;
    }
    @keyframes orb-breathe {
        0%, 100% { transform: scale(1); box-shadow: 0 0 50px rgba(139,92,246,0.5); }
        50% { transform: scale(1.05); box-shadow: 0 0 80px rgba(139,92,246,0.8); }
    }
    @keyframes orb-ring {
        0% { transform: scale(0.8); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: scale(1.3); opacity: 0; }
    }
    .orb-status {
        position: absolute; bottom: 8px; right: 18px;
        width: 18px; height: 18px; border-radius: 50%;
        background: #00D4FF; box-shadow: 0 0 15px #00D4FF;
        border: 2px solid #050B14;
    }

    /* Glassmorphism Chat Bubbles */
    .cb, .cu {
        padding: 1.2rem 1.4rem; border-radius: 20px; margin: 0.8rem 0;
        font-family: 'Inter', sans-serif; font-size: 0.95rem; line-height: 1.6;
        max-width: 85%; position: relative;
    }
    .cb {
        background: rgba(15,10,30,0.7); border: 1px solid rgba(139,92,246,0.4);
        color: #E0E7FF; border-bottom-left-radius: 4px; margin-right: auto;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }
    .cu {
        background: linear-gradient(135deg, #7C3AED, #4F46E5);
        color: #FFFFFF; border-bottom-right-radius: 4px; margin-left: auto;
        box-shadow: 0 8px 32px rgba(124,58,237,0.3);
    }
    .cb-icon { font-size: 1.2rem; margin-right: 10px; }

    /* Pill-Shaped Glowing Chat Input Override */
    div[data-testid="stChatInput"] {
        padding-bottom: 1.5rem !important; 
    }
    div[data-testid="stChatInput"] > div {
        border-radius: 50px !important;
        background: rgba(10, 15, 30, 0.75) !important;
        backdrop-filter: blur(15px) !important;
        border: 2px solid rgba(0, 212, 255, 0.4) !important;
        box-shadow: 0 0 35px rgba(0, 212, 255, 0.15), inset 0 0 15px rgba(0, 212, 255, 0.1) !important;
        transition: all 0.3s ease !important;
        padding: 0.2rem 1rem !important;
    }
    div[data-testid="stChatInput"] > div:focus-within {
        border-color: rgba(0, 212, 255, 0.9) !important;
        box-shadow: 0 0 50px rgba(0, 212, 255, 0.4), inset 0 0 20px rgba(0, 212, 255, 0.25) !important;
    }
    div[data-testid="stChatInput"] textarea {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
    }
    div[data-testid="stChatInput"] button {
        color: #00D4FF !important;
        background: transparent !important;
    }
    div[data-testid="stChatInput"] button:hover {
        color: #FFFFFF !important;
        text-shadow: 0 0 12px #00D4FF !important;
        transform: scale(1.1) !important;
    }

    /* Floating Suggested Prompts Chips */
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 30px !important;
        background: rgba(139,92,246,0.15) !important;
        border: 1px solid rgba(139,92,246,0.4) !important;
        color: #E0E7FF !important;
        transition: all 0.3s ease !important;
        padding: 0.4rem 1rem !important;
        font-size: 0.85rem !important;
    }
    div[data-testid="stHorizontalBlock"] button:hover {
        background: rgba(139,92,246,0.3) !important;
        border-color: #A855F7 !important;
        box-shadow: 0 0 20px rgba(139,92,246,0.5) !important;
        transform: translateY(-2px) !important;
        color: #FFFFFF !important;
    }
    
    /* Voice / Status Bar */
    .voice-bar {
        height: 2px; background: linear-gradient(90deg, transparent, #00D4FF, transparent);
        margin: 2rem 0; opacity: 0.6; animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 0.9; box-shadow: 0 0 15px #00D4FF; } }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="orb-container">
        <div class="orb">
            <span style="font-size:2.8rem;">🎙️</span>
            <div class="orb-status"></div>
        </div>
    </div>
    <div style="text-align:center; font-family:'Orbitron', monospace; font-size:2rem; font-weight:900; color:#E0E7FF; text-shadow:0 0 25px rgba(0,212,255,0.7); margin-bottom:0.3rem;">AURA AI</div>
    <div style="text-align:center; color:#00D4FF; font-size:0.95rem; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:1.5rem;">Intelligent Diagnostic Assistant</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="voice-bar"></div>', unsafe_allow_html=True)

    KB={
    "predictive maintenance":"🏭 **Predictive Maintenance** — AI + sensor data are used to predict failures before breakdown happens. Reduces downtime, maintenance cost, and unexpected production stoppage.",

    "how system works":"⚙️ **System Workflow** — Sensor data → AI4I Failure Model + NASA RUL Model → Fusion Engine → Final Machine Status (🟢 Healthy / 🟡 Warning / 🔴 Critical).",

    "rul":"🔋 **RUL (Remaining Useful Life)** — NASA C-MAPSS model predicts cycles remaining before failure. <30 = 🔴 CRITICAL (stop machine), 30–80 = 🟡 WARNING (schedule maintenance in 72h), >80 = 🟢 HEALTHY (continue operating).",

    "failure":"⚠️ **AI4I Failure Model** — RandomForest classifier, 5 sensor inputs. Output 1 = failure, 0 = healthy. Failure modes: TWF (tool wear), HDF (heat dissipation), PWF (power), OSF (overstrain), RNF (random). ~99.2% accuracy.",

    "fusion":"⚡ **Fusion Decision Engine** — merges AI4I + NASA → 🟢 HEALTHY / 🟡 WARNING / 🔴 CRITICAL. Machine is CRITICAL if either model flags danger. Dual-model approach reduces false negatives.",

    "csv":"📁 **CSV Format** — Supported columns: machine_id, air_temp, process_temp, rpm, torque, tool_wear, cycle, sensor values. Each row = one machine snapshot.",

    "upload":"📤 **CSV Upload** — Users can upload single-machine or fleet CSV files directly from Smart Diagnosis or Fleet Monitoring pages.",

    "dataset":"📊 **Datasets Used** — UCI AI4I 2020 (10,000 milling records, 5 failure modes) + NASA C-MAPSS turbofan degradation dataset.",

    "maintenance":"🏭 **Why Predictive Maintenance Matters** — Reduces maintenance cost ~30% and downtime ~40% compared to reactive maintenance.",

    "model":"🤖 **Models Used** — RandomForest Classifier (AI4I failure prediction) + RandomForest Regressor (NASA RUL prediction). Saved as .pkl files.",

    "accuracy":"🎯 **Model Accuracy** — AI4I model achieves ~99% classification accuracy. NASA model validated using MAE and R² metrics.",

    "critical":"🔴 **CRITICAL Status** — Failure detected OR RUL <30 cycles. Immediate maintenance required. Machine should be stopped to avoid catastrophic damage.",

    "warning":"🟡 **WARNING Status** — No immediate failure but degradation detected. Schedule maintenance within 72 hours.",

    "healthy":"🟢 **HEALTHY Status** — Machine operating normally. No failure risk and RUL >80 cycles.",

    "fleet":"🏭 **Fleet Monitoring** — Upload one CSV containing multiple machines. Dashboard shows KPI cards, machine table, charts, and overall fleet health.",

    "score":"💯 **Condition Score** — Composite health score from 0–100 calculated using failure probability, RUL, and sensor condition.",

    "analytics":"📊 **Analytics Dashboard** — Includes temperature trends, RPM-torque analysis, RUL degradation, correlation heatmap, and fleet risk charts.",

    "pdf":"📄 **Report Download** — Users can download diagnosis reports containing machine inputs, predictions, issues, and maintenance recommendations.",

    "review":"🔬 **Machine Review Page** — Advanced single-machine analysis with radar chart, sensor health bars, issue summary, and maintenance schedule.",

    "radar":"📡 **Health Radar Chart** — Displays Condition Score, Temperature Health, RPM Health, Torque Health, Tool Wear Health, and RUL Health.",

    "sensor":"📡 **Sensors Used** — NASA dataset contains turbofan sensor readings. AI4I uses milling machine process parameters like RPM, torque, and wear.",

    "iot":"🌐 **IoT Integration** — Real-time sensor streaming can be connected using MQTT, REST APIs, or industrial IoT platforms.",

    "cloud":"☁️ **Cloud Deployment** — Can be deployed on Streamlit Cloud, AWS, Azure, GCP, or Docker environments.",

    "deep":"🧠 **Deep Learning Upgrade** — Future versions can use LSTM, GRU, or Transformer models for better time-series degradation prediction.",

    "twf":"🔧 **TWF (Tool Wear Failure)** — Failure due to excessive tool wear. High wear causes reduced machining accuracy and breakdown risk.",

    "hdf":"🌡️ **HDF (Heat Dissipation Failure)** — Happens when cooling system fails and temperature rises above safe operating limit.",

    "pwf":"⚡ **PWF (Power Failure)** — Caused by abnormal torque × RPM power conditions outside safe operational limits.",

    "osf":"⚙️ **OSF (Overstrain Failure)** — Occurs when machine operates under excessive mechanical stress or overload conditions.",

    "rnf":"🎲 **RNF (Random Failure)** — Unexpected failure not directly linked to wear or temperature; may occur due to random defects.",

    "industry":"⚙️ **Industries Using This System** — Manufacturing, aviation, automotive, energy, oil & gas, heavy machinery, and smart factories.",

    "schedule":"📅 **Maintenance Schedule** — System generates maintenance tasks with due dates and priorities based on sensor condition.",

    "recommend":"💡 **AI Recommendation Engine** — Generates maintenance suggestions, risk summary, and action plan after diagnosis.",

    "report":"📄 **Full Report Includes** — Sensor inputs, AI predictions, fusion status, issues detected, condition score, and maintenance plan.",

    "failure prediction":"⚠️ **Failure Prediction** — Predicts whether a machine is likely to fail based on sensor data patterns.",

    "real time":"⏱️ **Real-Time Monitoring** — System can simulate or process real-time sensor streams for continuous health monitoring.",

    "single machine":"🛠️ **Single Machine Diagnosis** — Users can manually enter sensor values or upload one machine CSV for prediction.",

    "multiple machines":"🏭 **Multiple Machine Prediction** — Fleet mode processes hundreds of machines together using batch CSV upload.",

    "fleet health":"💚 **Fleet Health Score** — Percentage showing overall health condition of all machines combined.",

    "download":"📥 **Export Results** — Prediction tables and analytics can be downloaded as CSV or text reports.",

    "chatbot":"💬 **AI Chatbot** — Interactive assistant that answers questions related to predictive maintenance, RUL, failures, and system features.",

    "chatbot explanation":"🤖 **Chatbot Purpose** — Helps users understand model outputs, machine conditions, and maintenance recommendations.",

    "portfolio":"📁 **Portfolio Project** — This system demonstrates AI, machine learning, data analytics, dashboarding, and industrial monitoring skills.",

    "future":"🚀 **Future Improvements** — Planned features include deep learning, live IoT streaming, cloud analytics, and anomaly detection.",

    "deep learning":"🧠 **Deep Learning Models** — LSTM and GRU are suitable for sequential degradation analysis and advanced RUL prediction.",

    "classification":"📌 **Classification Model** — AI4I failure prediction is a binary classification problem (0 = healthy, 1 = failure).",

    "regression":"📈 **Regression Model** — NASA RUL prediction estimates continuous remaining life cycles using regression algorithms.",

    "condition":"📊 **Machine Condition Levels** — Machines are categorized as Healthy, Warning, or Critical based on AI fusion results.",

    "kpi":"📉 **KPI Cards** — Dashboard displays total machines, healthy count, critical alerts, fleet score, and average RUL.",

    "dashboard":"🖥️ **Dashboard Features** — Interactive charts, machine tables, health indicators, and downloadable reports.",

    "downtime":"⛔ **Downtime Reduction** — Early failure prediction helps industries avoid sudden machine stoppage.",

    "sensor upload":"📡 **Sensor Data Upload** — CSV uploads allow users to test models using custom machine sensor data.",

    "industrial ai":"🏭 **Industrial AI** — Combines machine learning with industrial sensor systems to optimize operations and maintenance.",

    "machine learning":"🤖 **Machine Learning** — Algorithms learn patterns from historical machine data to predict future failures.",

    "why rul":"🔋 **Why RUL is Important** — RUL helps maintenance teams know how long a machine can safely operate before servicing.",

    "why fusion":"⚡ **Why Fusion Engine Matters** — Combining two AI models improves reliability and reduces false predictions.",

    "sensor monitoring":"📡 **Sensor Monitoring** — Tracks temperature, RPM, torque, pressure, and wear continuously for anomaly detection.",

    "anomaly":"🚨 **Anomaly Detection** — Identifies unusual sensor behavior before a major failure occurs.",

    "time series":"📈 **Time-Series Data** — NASA dataset contains sequential cycle-based degradation data useful for RUL modeling.",

    "ai4i":"⚙️ **AI4I Dataset** — Predictive maintenance dataset with milling machine process parameters and labeled failure modes.",

    "nasa":"🚀 **NASA Dataset** — Turbofan engine degradation simulation dataset widely used for Remaining Useful Life prediction.",

    "streamlit":"🖥️ **Streamlit Web App** — User-friendly Python framework used to build the predictive maintenance dashboard.",

    "scalability":"📦 **Scalability** — System can scale from single-machine diagnosis to enterprise-level fleet monitoring.",

    "local deployment":"💻 **Local Deployment** — App can run offline on local machine after setup.",

    "emergency":"🚨 **Emergency Maintenance** — Critical machines require immediate shutdown and inspection to prevent severe damage.",

    "tool wear":"🔧 **Tool Wear** — Measures degradation of cutting tool over time. High wear increases failure probability.",

    "rpm":"⚙️ **RPM (Rotational Speed)** — Measures machine rotational speed. Extremely low/high RPM may indicate abnormal behavior.",

    "torque":"🔩 **Torque** — Indicates rotational force applied by the machine. Excessive torque increases mechanical stress.",

    "temperature":"🌡️ **Temperature Monitoring** — High air/process temperature often signals cooling or operational problems.",

    "random forest":"🌲 **Random Forest** — Ensemble machine learning algorithm using multiple decision trees for robust prediction.",

    "maintenance plan":"📅 **Maintenance Plan** — System suggests inspection, lubrication, replacement, and emergency servicing tasks.",

    "industrial dashboard":"📊 **Industrial Dashboard** — Provides visual monitoring of machine health, risks, and operational insights.",

    "why this project":"⭐ **Why This Project is Special** — Combines failure prediction, RUL estimation, fusion logic, fleet monitoring, analytics, and AI chatbot into one professional platform.",

    "what is rul": "ℹ️ Rul refers to an important concept in predictive maintenance and machine monitoring.",
        "how does rul work": "⚙️ Rul works using AI models, sensor analytics, and predictive logic.",
        "why is rul important": "⭐ Rul is important for improving machine reliability and reducing downtime.",
        "can the system handle rul": "✅ Yes, the system supports Rul with industrial-scale monitoring.",
        "advantages of rul": "📈 Rul improves operational efficiency and maintenance planning.",
        "limitations of rul": "⚠️ Rul depends on sensor quality, operating conditions, and training data.",
        "future of rul": "🚀 Future upgrades of Rul include deep learning and real-time IoT integration.",
        "use cases of rul": "🏭 Rul is widely used in industrial monitoring and predictive maintenance.",
        "benefits of rul": "💡 Rul helps optimize maintenance schedules and reduce breakdown risk.",
        "what is failure": "ℹ️ Failure refers to an important concept in predictive maintenance and machine monitoring.",
        "how does failure work": "⚙️ Failure works using AI models, sensor analytics, and predictive logic.",
        "why is failure important": "⭐ Failure is important for improving machine reliability and reducing downtime.",
        "can the system handle failure": "✅ Yes, the system supports Failure with industrial-scale monitoring.",
        "advantages of failure": "📈 Failure improves operational efficiency and maintenance planning.",
        "limitations of failure": "⚠️ Failure depends on sensor quality, operating conditions, and training data.",
        "future of failure": "🚀 Future upgrades of Failure include deep learning and real-time IoT integration.",
        "use cases of failure": "🏭 Failure is widely used in industrial monitoring and predictive maintenance.",
        "benefits of failure": "💡 Failure helps optimize maintenance schedules and reduce breakdown risk.",
        "what is fusion": "ℹ️ Fusion refers to an important concept in predictive maintenance and machine monitoring.",
        "how does fusion work": "⚙️ Fusion works using AI models, sensor analytics, and predictive logic.",
        "why is fusion important": "⭐ Fusion is important for improving machine reliability and reducing downtime.",
        "can the system handle fusion": "✅ Yes, the system supports Fusion with industrial-scale monitoring.",
        "advantages of fusion": "📈 Fusion improves operational efficiency and maintenance planning.",
        "limitations of fusion": "⚠️ Fusion depends on sensor quality, operating conditions, and training data.",
        "future of fusion": "🚀 Future upgrades of Fusion include deep learning and real-time IoT integration.",
        "use cases of fusion": "🏭 Fusion is widely used in industrial monitoring and predictive maintenance.",
        "benefits of fusion": "💡 Fusion helps optimize maintenance schedules and reduce breakdown risk.",
        "what is csv": "ℹ️ Csv refers to an important concept in predictive maintenance and machine monitoring.",
        "how does csv work": "⚙️ Csv works using AI models, sensor analytics, and predictive logic.",
        "why is csv important": "⭐ Csv is important for improving machine reliability and reducing downtime.",
        "can the system handle csv": "✅ Yes, the system supports Csv with industrial-scale monitoring.",
        "advantages of csv": "📈 Csv improves operational efficiency and maintenance planning.",
        "limitations of csv": "⚠️ Csv depends on sensor quality, operating conditions, and training data.",
        "future of csv": "🚀 Future upgrades of Csv include deep learning and real-time IoT integration.",
        "use cases of csv": "🏭 Csv is widely used in industrial monitoring and predictive maintenance.",
        "benefits of csv": "💡 Csv helps optimize maintenance schedules and reduce breakdown risk.",
        "what is dataset": "ℹ️ Dataset refers to an important concept in predictive maintenance and machine monitoring.",
        "how does dataset work": "⚙️ Dataset works using AI models, sensor analytics, and predictive logic.",
        "why is dataset important": "⭐ Dataset is important for improving machine reliability and reducing downtime.",
        "can the system handle dataset": "✅ Yes, the system supports Dataset with industrial-scale monitoring.",
        "advantages of dataset": "📈 Dataset improves operational efficiency and maintenance planning.",
        "limitations of dataset": "⚠️ Dataset depends on sensor quality, operating conditions, and training data.",
        "future of dataset": "🚀 Future upgrades of Dataset include deep learning and real-time IoT integration.",
        "use cases of dataset": "🏭 Dataset is widely used in industrial monitoring and predictive maintenance.",
        "benefits of dataset": "💡 Dataset helps optimize maintenance schedules and reduce breakdown risk.",
        "what is maintenance": "ℹ️ Maintenance refers to an important concept in predictive maintenance and machine monitoring.",
        "how does maintenance work": "⚙️ Maintenance works using AI models, sensor analytics, and predictive logic.",
        "why is maintenance important": "⭐ Maintenance is important for improving machine reliability and reducing downtime.",
        "can the system handle maintenance": "✅ Yes, the system supports Maintenance with industrial-scale monitoring.",
        "advantages of maintenance": "📈 Maintenance improves operational efficiency and maintenance planning.",
        "limitations of maintenance": "⚠️ Maintenance depends on sensor quality, operating conditions, and training data.",
        "future of maintenance": "🚀 Future upgrades of Maintenance include deep learning and real-time IoT integration.",
        "use cases of maintenance": "🏭 Maintenance is widely used in industrial monitoring and predictive maintenance.",
        "benefits of maintenance": "💡 Maintenance helps optimize maintenance schedules and reduce breakdown risk.",
        "what is model": "ℹ️ Model refers to an important concept in predictive maintenance and machine monitoring.",
        "how does model work": "⚙️ Model works using AI models, sensor analytics, and predictive logic.",
        "why is model important": "⭐ Model is important for improving machine reliability and reducing downtime.",
        "can the system handle model": "✅ Yes, the system supports Model with industrial-scale monitoring.",
        "advantages of model": "📈 Model improves operational efficiency and maintenance planning.",
        "limitations of model": "⚠️ Model depends on sensor quality, operating conditions, and training data.",
        "future of model": "🚀 Future upgrades of Model include deep learning and real-time IoT integration.",
        "use cases of model": "🏭 Model is widely used in industrial monitoring and predictive maintenance.",
        "benefits of model": "💡 Model helps optimize maintenance schedules and reduce breakdown risk.",
        "what is accuracy": "ℹ️ Accuracy refers to an important concept in predictive maintenance and machine monitoring.",
        "how does accuracy work": "⚙️ Accuracy works using AI models, sensor analytics, and predictive logic.",
        "why is accuracy important": "⭐ Accuracy is important for improving machine reliability and reducing downtime.",
        "can the system handle accuracy": "✅ Yes, the system supports Accuracy with industrial-scale monitoring.",
        "advantages of accuracy": "📈 Accuracy improves operational efficiency and maintenance planning.",
        "limitations of accuracy": "⚠️ Accuracy depends on sensor quality, operating conditions, and training data.",
        "future of accuracy": "🚀 Future upgrades of Accuracy include deep learning and real-time IoT integration.",
        "use cases of accuracy": "🏭 Accuracy is widely used in industrial monitoring and predictive maintenance.",
        "benefits of accuracy": "💡 Accuracy helps optimize maintenance schedules and reduce breakdown risk.",
        "what is critical": "ℹ️ Critical refers to an important concept in predictive maintenance and machine monitoring.",
        "how does critical work": "⚙️ Critical works using AI models, sensor analytics, and predictive logic.",
        "why is critical important": "⭐ Critical is important for improving machine reliability and reducing downtime.",
        "can the system handle critical": "✅ Yes, the system supports Critical with industrial-scale monitoring.",
        "advantages of critical": "📈 Critical improves operational efficiency and maintenance planning.",
        "limitations of critical": "⚠️ Critical depends on sensor quality, operating conditions, and training data.",
        "future of critical": "🚀 Future upgrades of Critical include deep learning and real-time IoT integration.",
        "use cases of critical": "🏭 Critical is widely used in industrial monitoring and predictive maintenance.",
        "benefits of critical": "💡 Critical helps optimize maintenance schedules and reduce breakdown risk.",
        "what is warning": "ℹ️ Warning refers to an important concept in predictive maintenance and machine monitoring.",
        "how does warning work": "⚙️ Warning works using AI models, sensor analytics, and predictive logic.",
        "why is warning important": "⭐ Warning is important for improving machine reliability and reducing downtime.",
        "can the system handle warning": "✅ Yes, the system supports Warning with industrial-scale monitoring.",
        "advantages of warning": "📈 Warning improves operational efficiency and maintenance planning.",
        "limitations of warning": "⚠️ Warning depends on sensor quality, operating conditions, and training data.",
        "future of warning": "🚀 Future upgrades of Warning include deep learning and real-time IoT integration.",
        "use cases of warning": "🏭 Warning is widely used in industrial monitoring and predictive maintenance.",
        "benefits of warning": "💡 Warning helps optimize maintenance schedules and reduce breakdown risk.",
        "what is healthy": "ℹ️ Healthy refers to an important concept in predictive maintenance and machine monitoring.",
        "how does healthy work": "⚙️ Healthy works using AI models, sensor analytics, and predictive logic.",
        "why is healthy important": "⭐ Healthy is important for improving machine reliability and reducing downtime.",
        "can the system handle healthy": "✅ Yes, the system supports Healthy with industrial-scale monitoring.",
        "advantages of healthy": "📈 Healthy improves operational efficiency and maintenance planning.",
        "limitations of healthy": "⚠️ Healthy depends on sensor quality, operating conditions, and training data.",
        "future of healthy": "🚀 Future upgrades of Healthy include deep learning and real-time IoT integration.",
        "use cases of healthy": "🏭 Healthy is widely used in industrial monitoring and predictive maintenance.",
        "benefits of healthy": "💡 Healthy helps optimize maintenance schedules and reduce breakdown risk.",
        "what is fleet": "ℹ️ Fleet refers to an important concept in predictive maintenance and machine monitoring.",
        "how does fleet work": "⚙️ Fleet works using AI models, sensor analytics, and predictive logic.",
        "why is fleet important": "⭐ Fleet is important for improving machine reliability and reducing downtime.",
        "can the system handle fleet": "✅ Yes, the system supports Fleet with industrial-scale monitoring.",
        "advantages of fleet": "📈 Fleet improves operational efficiency and maintenance planning.",
        "limitations of fleet": "⚠️ Fleet depends on sensor quality, operating conditions, and training data.",
        "future of fleet": "🚀 Future upgrades of Fleet include deep learning and real-time IoT integration.",
        "use cases of fleet": "🏭 Fleet is widely used in industrial monitoring and predictive maintenance.",
        "benefits of fleet": "💡 Fleet helps optimize maintenance schedules and reduce breakdown risk.",
        "what is score": "ℹ️ Score refers to an important concept in predictive maintenance and machine monitoring.",
        "how does score work": "⚙️ Score works using AI models, sensor analytics, and predictive logic.",
        "why is score important": "⭐ Score is important for improving machine reliability and reducing downtime.",
        "can the system handle score": "✅ Yes, the system supports Score with industrial-scale monitoring.",
        "advantages of score": "📈 Score improves operational efficiency and maintenance planning.",
        "limitations of score": "⚠️ Score depends on sensor quality, operating conditions, and training data.",
        "future of score": "🚀 Future upgrades of Score include deep learning and real-time IoT integration.",
        "use cases of score": "🏭 Score is widely used in industrial monitoring and predictive maintenance.",
        "benefits of score": "💡 Score helps optimize maintenance schedules and reduce breakdown risk.",
        "what is analytics": "ℹ️ Analytics refers to an important concept in predictive maintenance and machine monitoring.",
        "how does analytics work": "⚙️ Analytics works using AI models, sensor analytics, and predictive logic.",
        "why is analytics important": "⭐ Analytics is important for improving machine reliability and reducing downtime.",
        "can the system handle analytics": "✅ Yes, the system supports Analytics with industrial-scale monitoring.",
        "advantages of analytics": "📈 Analytics improves operational efficiency and maintenance planning.",
        "limitations of analytics": "⚠️ Analytics depends on sensor quality, operating conditions, and training data.",
        "future of analytics": "🚀 Future upgrades of Analytics include deep learning and real-time IoT integration.",
        "use cases of analytics": "🏭 Analytics is widely used in industrial monitoring and predictive maintenance.",
        "benefits of analytics": "💡 Analytics helps optimize maintenance schedules and reduce breakdown risk.",
        "what is pdf": "ℹ️ Pdf refers to an important concept in predictive maintenance and machine monitoring.",
        "how does pdf work": "⚙️ Pdf works using AI models, sensor analytics, and predictive logic.",
        "why is pdf important": "⭐ Pdf is important for improving machine reliability and reducing downtime.",
        "can the system handle pdf": "✅ Yes, the system supports Pdf with industrial-scale monitoring.",
        "advantages of pdf": "📈 Pdf improves operational efficiency and maintenance planning.",
        "limitations of pdf": "⚠️ Pdf depends on sensor quality, operating conditions, and training data.",
        "future of pdf": "🚀 Future upgrades of Pdf include deep learning and real-time IoT integration.",
        "use cases of pdf": "🏭 Pdf is widely used in industrial monitoring and predictive maintenance.",
        "benefits of pdf": "💡 Pdf helps optimize maintenance schedules and reduce breakdown risk.",
        "what is review": "ℹ️ Review refers to an important concept in predictive maintenance and machine monitoring.",
        "how does review work": "⚙️ Review works using AI models, sensor analytics, and predictive logic.",
        "why is review important": "⭐ Review is important for improving machine reliability and reducing downtime.",
        "can the system handle review": "✅ Yes, the system supports Review with industrial-scale monitoring.",
        "advantages of review": "📈 Review improves operational efficiency and maintenance planning.",
        "limitations of review": "⚠️ Review depends on sensor quality, operating conditions, and training data.",
        "future of review": "🚀 Future upgrades of Review include deep learning and real-time IoT integration.",
        "use cases of review": "🏭 Review is widely used in industrial monitoring and predictive maintenance.",
        "benefits of review": "💡 Review helps optimize maintenance schedules and reduce breakdown risk.",
        "what is radar": "ℹ️ Radar refers to an important concept in predictive maintenance and machine monitoring.",
        "how does radar work": "⚙️ Radar works using AI models, sensor analytics, and predictive logic.",
        "why is radar important": "⭐ Radar is important for improving machine reliability and reducing downtime.",
        "can the system handle radar": "✅ Yes, the system supports Radar with industrial-scale monitoring.",
        "advantages of radar": "📈 Radar improves operational efficiency and maintenance planning.",
        "limitations of radar": "⚠️ Radar depends on sensor quality, operating conditions, and training data.",
        "future of radar": "🚀 Future upgrades of Radar include deep learning and real-time IoT integration.",
        "use cases of radar": "🏭 Radar is widely used in industrial monitoring and predictive maintenance.",
        "benefits of radar": "💡 Radar helps optimize maintenance schedules and reduce breakdown risk.",
        "what is sensor": "ℹ️ Sensor refers to an important concept in predictive maintenance and machine monitoring.",
        "how does sensor work": "⚙️ Sensor works using AI models, sensor analytics, and predictive logic.",
        "why is sensor important": "⭐ Sensor is important for improving machine reliability and reducing downtime.",
        "can the system handle sensor": "✅ Yes, the system supports Sensor with industrial-scale monitoring.",
        "advantages of sensor": "📈 Sensor improves operational efficiency and maintenance planning.",
        "limitations of sensor": "⚠️ Sensor depends on sensor quality, operating conditions, and training data.",
        "future of sensor": "🚀 Future upgrades of Sensor include deep learning and real-time IoT integration.",
        "use cases of sensor": "🏭 Sensor is widely used in industrial monitoring and predictive maintenance.",
        "benefits of sensor": "💡 Sensor helps optimize maintenance schedules and reduce breakdown risk.",
        "what is iot": "ℹ️ Iot refers to an important concept in predictive maintenance and machine monitoring.",
        "how does iot work": "⚙️ Iot works using AI models, sensor analytics, and predictive logic.",
        "why is iot important": "⭐ Iot is important for improving machine reliability and reducing downtime.",
        "can the system handle iot": "✅ Yes, the system supports Iot with industrial-scale monitoring.",
        "advantages of iot": "📈 Iot improves operational efficiency and maintenance planning.",
        "limitations of iot": "⚠️ Iot depends on sensor quality, operating conditions, and training data.",
        "future of iot": "🚀 Future upgrades of Iot include deep learning and real-time IoT integration.",
        "use cases of iot": "🏭 Iot is widely used in industrial monitoring and predictive maintenance.",
        "benefits of iot": "💡 Iot helps optimize maintenance schedules and reduce breakdown risk.",
        "what is cloud": "ℹ️ Cloud refers to an important concept in predictive maintenance and machine monitoring.",
        "how does cloud work": "⚙️ Cloud works using AI models, sensor analytics, and predictive logic.",
        "why is cloud important": "⭐ Cloud is important for improving machine reliability and reducing downtime.",
        "can the system handle cloud": "✅ Yes, the system supports Cloud with industrial-scale monitoring.",
        "advantages of cloud": "📈 Cloud improves operational efficiency and maintenance planning.",
        "limitations of cloud": "⚠️ Cloud depends on sensor quality, operating conditions, and training data.",
        "future of cloud": "🚀 Future upgrades of Cloud include deep learning and real-time IoT integration.",
        "use cases of cloud": "🏭 Cloud is widely used in industrial monitoring and predictive maintenance.",
        "benefits of cloud": "💡 Cloud helps optimize maintenance schedules and reduce breakdown risk.",
        "what is deep learning": "ℹ️ Deep Learning refers to an important concept in predictive maintenance and machine monitoring.",
        "how does deep learning work": "⚙️ Deep Learning works using AI models, sensor analytics, and predictive logic.",
        "why is deep learning important": "⭐ Deep Learning is important for improving machine reliability and reducing downtime.",
        "can the system handle deep learning": "✅ Yes, the system supports Deep Learning with industrial-scale monitoring.",
        "advantages of deep learning": "📈 Deep Learning improves operational efficiency and maintenance planning.",
        "limitations of deep learning": "⚠️ Deep Learning depends on sensor quality, operating conditions, and training data.",
        "future of deep learning": "🚀 Future upgrades of Deep Learning include deep learning and real-time IoT integration.",
        "use cases of deep learning": "🏭 Deep Learning is widely used in industrial monitoring and predictive maintenance.",
        "benefits of deep learning": "💡 Deep Learning helps optimize maintenance schedules and reduce breakdown risk.",
        "what is twf": "ℹ️ Twf refers to an important concept in predictive maintenance and machine monitoring.",
        "how does twf work": "⚙️ Twf works using AI models, sensor analytics, and predictive logic.",
        "why is twf important": "⭐ Twf is important for improving machine reliability and reducing downtime.",
        "can the system handle twf": "✅ Yes, the system supports Twf with industrial-scale monitoring.",
        "advantages of twf": "📈 Twf improves operational efficiency and maintenance planning.",
        "limitations of twf": "⚠️ Twf depends on sensor quality, operating conditions, and training data.",
        "future of twf": "🚀 Future upgrades of Twf include deep learning and real-time IoT integration.",
        "use cases of twf": "🏭 Twf is widely used in industrial monitoring and predictive maintenance.",
        "benefits of twf": "💡 Twf helps optimize maintenance schedules and reduce breakdown risk.",
        "what is hdf": "ℹ️ Hdf refers to an important concept in predictive maintenance and machine monitoring.",
        "how does hdf work": "⚙️ Hdf works using AI models, sensor analytics, and predictive logic.",
        "why is hdf important": "⭐ Hdf is important for improving machine reliability and reducing downtime.",
        "can the system handle hdf": "✅ Yes, the system supports Hdf with industrial-scale monitoring.",
        "advantages of hdf": "📈 Hdf improves operational efficiency and maintenance planning.",
        "limitations of hdf": "⚠️ Hdf depends on sensor quality, operating conditions, and training data.",
        "future of hdf": "🚀 Future upgrades of Hdf include deep learning and real-time IoT integration.",
        "use cases of hdf": "🏭 Hdf is widely used in industrial monitoring and predictive maintenance.",
        "benefits of hdf": "💡 Hdf helps optimize maintenance schedules and reduce breakdown risk.",
        "what is pwf": "ℹ️ Pwf refers to an important concept in predictive maintenance and machine monitoring.",
        "how does pwf work": "⚙️ Pwf works using AI models, sensor analytics, and predictive logic.",
        "why is pwf important": "⭐ Pwf is important for improving machine reliability and reducing downtime.",
        "can the system handle pwf": "✅ Yes, the system supports Pwf with industrial-scale monitoring.",
        "advantages of pwf": "📈 Pwf improves operational efficiency and maintenance planning.",
        "limitations of pwf": "⚠️ Pwf depends on sensor quality, operating conditions, and training data.",
        "future of pwf": "🚀 Future upgrades of Pwf include deep learning and real-time IoT integration.",
        "use cases of pwf": "🏭 Pwf is widely used in industrial monitoring and predictive maintenance.",
        "benefits of pwf": "💡 Pwf helps optimize maintenance schedules and reduce breakdown risk.",
        "what is industry": "ℹ️ Industry refers to an important concept in predictive maintenance and machine monitoring.",
        "how does industry work": "⚙️ Industry works using AI models, sensor analytics, and predictive logic.",
        "why is industry important": "⭐ Industry is important for improving machine reliability and reducing downtime.",
        "can the system handle industry": "✅ Yes, the system supports Industry with industrial-scale monitoring.",
        "advantages of industry": "📈 Industry improves operational efficiency and maintenance planning.",
        "limitations of industry": "⚠️ Industry depends on sensor quality, operating conditions, and training data.",
        "future of industry": "🚀 Future upgrades of Industry include deep learning and real-time IoT integration.",
        "use cases of industry": "🏭 Industry is widely used in industrial monitoring and predictive maintenance.",
        "benefits of industry": "💡 Industry helps optimize maintenance schedules and reduce breakdown risk.",
        "what is schedule": "ℹ️ Schedule refers to an important concept in predictive maintenance and machine monitoring.",
        "how does schedule work": "⚙️ Schedule works using AI models, sensor analytics, and predictive logic.",
        "why is schedule important": "⭐ Schedule is important for improving machine reliability and reducing downtime.",
        "can the system handle schedule": "✅ Yes, the system supports Schedule with industrial-scale monitoring.",
        "advantages of schedule": "📈 Schedule improves operational efficiency and maintenance planning.",
        "limitations of schedule": "⚠️ Schedule depends on sensor quality, operating conditions, and training data.",
        "future of schedule": "🚀 Future upgrades of Schedule include deep learning and real-time IoT integration.",
        "use cases of schedule": "🏭 Schedule is widely used in industrial monitoring and predictive maintenance.",
        "benefits of schedule": "💡 Schedule helps optimize maintenance schedules and reduce breakdown risk.",
        "what is recommendation": "ℹ️ Recommendation refers to an important concept in predictive maintenance and machine monitoring.",
        "how does recommendation work": "⚙️ Recommendation works using AI models, sensor analytics, and predictive logic.",
        "why is recommendation important": "⭐ Recommendation is important for improving machine reliability and reducing downtime.",
        "can the system handle recommendation": "✅ Yes, the system supports Recommendation with industrial-scale monitoring.",
        "advantages of recommendation": "📈 Recommendation improves operational efficiency and maintenance planning.",
        "limitations of recommendation": "⚠️ Recommendation depends on sensor quality, operating conditions, and training data.",
        "future of recommendation": "🚀 Future upgrades of Recommendation include deep learning and real-time IoT integration.",
        "use cases of recommendation": "🏭 Recommendation is widely used in industrial monitoring and predictive maintenance.",
        "benefits of recommendation": "💡 Recommendation helps optimize maintenance schedules and reduce breakdown risk.",
        "what is report": "ℹ️ Report refers to an important concept in predictive maintenance and machine monitoring.",
        "how does report work": "⚙️ Report works using AI models, sensor analytics, and predictive logic.",
        "why is report important": "⭐ Report is important for improving machine reliability and reducing downtime.",
        "can the system handle report": "✅ Yes, the system supports Report with industrial-scale monitoring.",
        "advantages of report": "📈 Report improves operational efficiency and maintenance planning.",
        "limitations of report": "⚠️ Report depends on sensor quality, operating conditions, and training data.",
        "future of report": "🚀 Future upgrades of Report include deep learning and real-time IoT integration.",
        "use cases of report": "🏭 Report is widely used in industrial monitoring and predictive maintenance.",
        "benefits of report": "💡 Report helps optimize maintenance schedules and reduce breakdown risk.",
        "what is rpm": "ℹ️ Rpm refers to an important concept in predictive maintenance and machine monitoring.",
        "how does rpm work": "⚙️ Rpm works using AI models, sensor analytics, and predictive logic.",
        "why is rpm important": "⭐ Rpm is important for improving machine reliability and reducing downtime.",
        "can the system handle rpm": "✅ Yes, the system supports Rpm with industrial-scale monitoring.",
        "advantages of rpm": "📈 Rpm improves operational efficiency and maintenance planning.",
        "limitations of rpm": "⚠️ Rpm depends on sensor quality, operating conditions, and training data.",
        "future of rpm": "🚀 Future upgrades of Rpm include deep learning and real-time IoT integration.",
        "use cases of rpm": "🏭 Rpm is widely used in industrial monitoring and predictive maintenance.",
        "benefits of rpm": "💡 Rpm helps optimize maintenance schedules and reduce breakdown risk.",
        "what is torque": "ℹ️ Torque refers to an important concept in predictive maintenance and machine monitoring.",
        "how does torque work": "⚙️ Torque works using AI models, sensor analytics, and predictive logic.",
        "why is torque important": "⭐ Torque is important for improving machine reliability and reducing downtime.",
        "can the system handle torque": "✅ Yes, the system supports Torque with industrial-scale monitoring.",
        "advantages of torque": "📈 Torque improves operational efficiency and maintenance planning.",
        "limitations of torque": "⚠️ Torque depends on sensor quality, operating conditions, and training data.",
        "future of torque": "🚀 Future upgrades of Torque include deep learning and real-time IoT integration.",
        "use cases of torque": "🏭 Torque is widely used in industrial monitoring and predictive maintenance.",
        "benefits of torque": "💡 Torque helps optimize maintenance schedules and reduce breakdown risk.",
        "what is temperature": "ℹ️ Temperature refers to an important concept in predictive maintenance and machine monitoring.",
        "how does temperature work": "⚙️ Temperature works using AI models, sensor analytics, and predictive logic.",
        "why is temperature important": "⭐ Temperature is important for improving machine reliability and reducing downtime.",
        "can the system handle temperature": "✅ Yes, the system supports Temperature with industrial-scale monitoring.",
        "advantages of temperature": "📈 Temperature improves operational efficiency and maintenance planning.",
        "limitations of temperature": "⚠️ Temperature depends on sensor quality, operating conditions, and training data.",
        "future of temperature": "🚀 Future upgrades of Temperature include deep learning and real-time IoT integration.",
        "use cases of temperature": "🏭 Temperature is widely used in industrial monitoring and predictive maintenance.",
        "benefits of temperature": "💡 Temperature helps optimize maintenance schedules and reduce breakdown risk.",
        "what is random forest": "ℹ️ Random Forest refers to an important concept in predictive maintenance and machine monitoring.",
        "how does random forest work": "⚙️ Random Forest works using AI models, sensor analytics, and predictive logic.",
        "why is random forest important": "⭐ Random Forest is important for improving machine reliability and reducing downtime.",
        "can the system handle random forest": "✅ Yes, the system supports Random Forest with industrial-scale monitoring.",
        "advantages of random forest": "📈 Random Forest improves operational efficiency and maintenance planning.",
        "limitations of random forest": "⚠️ Random Forest depends on sensor quality, operating conditions, and training data.",
        "future of random forest": "🚀 Future upgrades of Random Forest include deep learning and real-time IoT integration.",
        "use cases of random forest": "🏭 Random Forest is widely used in industrial monitoring and predictive maintenance.",
        "benefits of random forest": "💡 Random Forest helps optimize maintenance schedules and reduce breakdown risk.",
        "predictive maintenance faq 1": "🤖 Predictive maintenance FAQ answer #1: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 2": "🤖 Predictive maintenance FAQ answer #2: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 3": "🤖 Predictive maintenance FAQ answer #3: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 4": "🤖 Predictive maintenance FAQ answer #4: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 5": "🤖 Predictive maintenance FAQ answer #5: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 6": "🤖 Predictive maintenance FAQ answer #6: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 7": "🤖 Predictive maintenance FAQ answer #7: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 8": "🤖 Predictive maintenance FAQ answer #8: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 9": "🤖 Predictive maintenance FAQ answer #9: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 10": "🤖 Predictive maintenance FAQ answer #10: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 11": "🤖 Predictive maintenance FAQ answer #11: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 12": "🤖 Predictive maintenance FAQ answer #12: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 13": "🤖 Predictive maintenance FAQ answer #13: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 14": "🤖 Predictive maintenance FAQ answer #14: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 15": "🤖 Predictive maintenance FAQ answer #15: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 16": "🤖 Predictive maintenance FAQ answer #16: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 17": "🤖 Predictive maintenance FAQ answer #17: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 18": "🤖 Predictive maintenance FAQ answer #18: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 19": "🤖 Predictive maintenance FAQ answer #19: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 20": "🤖 Predictive maintenance FAQ answer #20: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 21": "🤖 Predictive maintenance FAQ answer #21: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 22": "🤖 Predictive maintenance FAQ answer #22: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 23": "🤖 Predictive maintenance FAQ answer #23: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 24": "🤖 Predictive maintenance FAQ answer #24: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 25": "🤖 Predictive maintenance FAQ answer #25: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 26": "🤖 Predictive maintenance FAQ answer #26: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 27": "🤖 Predictive maintenance FAQ answer #27: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 28": "🤖 Predictive maintenance FAQ answer #28: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 29": "🤖 Predictive maintenance FAQ answer #29: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 30": "🤖 Predictive maintenance FAQ answer #30: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 31": "🤖 Predictive maintenance FAQ answer #31: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 32": "🤖 Predictive maintenance FAQ answer #32: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 33": "🤖 Predictive maintenance FAQ answer #33: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 34": "🤖 Predictive maintenance FAQ answer #34: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 35": "🤖 Predictive maintenance FAQ answer #35: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 36": "🤖 Predictive maintenance FAQ answer #36: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 37": "🤖 Predictive maintenance FAQ answer #37: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 38": "🤖 Predictive maintenance FAQ answer #38: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 39": "🤖 Predictive maintenance FAQ answer #39: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 40": "🤖 Predictive maintenance FAQ answer #40: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 41": "🤖 Predictive maintenance FAQ answer #41: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 42": "🤖 Predictive maintenance FAQ answer #42: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 43": "🤖 Predictive maintenance FAQ answer #43: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 44": "🤖 Predictive maintenance FAQ answer #44: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 45": "🤖 Predictive maintenance FAQ answer #45: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 46": "🤖 Predictive maintenance FAQ answer #46: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 47": "🤖 Predictive maintenance FAQ answer #47: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 48": "🤖 Predictive maintenance FAQ answer #48: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 49": "🤖 Predictive maintenance FAQ answer #49: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 50": "🤖 Predictive maintenance FAQ answer #50: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 51": "🤖 Predictive maintenance FAQ answer #51: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 52": "🤖 Predictive maintenance FAQ answer #52: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 53": "🤖 Predictive maintenance FAQ answer #53: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 54": "🤖 Predictive maintenance FAQ answer #54: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 55": "🤖 Predictive maintenance FAQ answer #55: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 56": "🤖 Predictive maintenance FAQ answer #56: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 57": "🤖 Predictive maintenance FAQ answer #57: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 58": "🤖 Predictive maintenance FAQ answer #58: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 59": "🤖 Predictive maintenance FAQ answer #59: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 60": "🤖 Predictive maintenance FAQ answer #60: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 61": "🤖 Predictive maintenance FAQ answer #61: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 62": "🤖 Predictive maintenance FAQ answer #62: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 63": "🤖 Predictive maintenance FAQ answer #63: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 64": "🤖 Predictive maintenance FAQ answer #64: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 65": "🤖 Predictive maintenance FAQ answer #65: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 66": "🤖 Predictive maintenance FAQ answer #66: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 67": "🤖 Predictive maintenance FAQ answer #67: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 68": "🤖 Predictive maintenance FAQ answer #68: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 69": "🤖 Predictive maintenance FAQ answer #69: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 70": "🤖 Predictive maintenance FAQ answer #70: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 71": "🤖 Predictive maintenance FAQ answer #71: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 72": "🤖 Predictive maintenance FAQ answer #72: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 73": "🤖 Predictive maintenance FAQ answer #73: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 74": "🤖 Predictive maintenance FAQ answer #74: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 75": "🤖 Predictive maintenance FAQ answer #75: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 76": "🤖 Predictive maintenance FAQ answer #76: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 77": "🤖 Predictive maintenance FAQ answer #77: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 78": "🤖 Predictive maintenance FAQ answer #78: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 79": "🤖 Predictive maintenance FAQ answer #79: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 80": "🤖 Predictive maintenance FAQ answer #80: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 81": "🤖 Predictive maintenance FAQ answer #81: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 82": "🤖 Predictive maintenance FAQ answer #82: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 83": "🤖 Predictive maintenance FAQ answer #83: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 84": "🤖 Predictive maintenance FAQ answer #84: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 85": "🤖 Predictive maintenance FAQ answer #85: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 86": "🤖 Predictive maintenance FAQ answer #86: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 87": "🤖 Predictive maintenance FAQ answer #87: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 88": "🤖 Predictive maintenance FAQ answer #88: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 89": "🤖 Predictive maintenance FAQ answer #89: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 90": "🤖 Predictive maintenance FAQ answer #90: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 91": "🤖 Predictive maintenance FAQ answer #91: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 92": "🤖 Predictive maintenance FAQ answer #92: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 93": "🤖 Predictive maintenance FAQ answer #93: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 94": "🤖 Predictive maintenance FAQ answer #94: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 95": "🤖 Predictive maintenance FAQ answer #95: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 96": "🤖 Predictive maintenance FAQ answer #96: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 97": "🤖 Predictive maintenance FAQ answer #97: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 98": "🤖 Predictive maintenance FAQ answer #98: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 99": "🤖 Predictive maintenance FAQ answer #99: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 100": "🤖 Predictive maintenance FAQ answer #100: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 101": "🤖 Predictive maintenance FAQ answer #101: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 102": "🤖 Predictive maintenance FAQ answer #102: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 103": "🤖 Predictive maintenance FAQ answer #103: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 104": "🤖 Predictive maintenance FAQ answer #104: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 105": "🤖 Predictive maintenance FAQ answer #105: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 106": "🤖 Predictive maintenance FAQ answer #106: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 107": "🤖 Predictive maintenance FAQ answer #107: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 108": "🤖 Predictive maintenance FAQ answer #108: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 109": "🤖 Predictive maintenance FAQ answer #109: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 110": "🤖 Predictive maintenance FAQ answer #110: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 111": "🤖 Predictive maintenance FAQ answer #111: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 112": "🤖 Predictive maintenance FAQ answer #112: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 113": "🤖 Predictive maintenance FAQ answer #113: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 114": "🤖 Predictive maintenance FAQ answer #114: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 115": "🤖 Predictive maintenance FAQ answer #115: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 116": "🤖 Predictive maintenance FAQ answer #116: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 117": "🤖 Predictive maintenance FAQ answer #117: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 118": "🤖 Predictive maintenance FAQ answer #118: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 119": "🤖 Predictive maintenance FAQ answer #119: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 120": "🤖 Predictive maintenance FAQ answer #120: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 121": "🤖 Predictive maintenance FAQ answer #121: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 122": "🤖 Predictive maintenance FAQ answer #122: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 123": "🤖 Predictive maintenance FAQ answer #123: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 124": "🤖 Predictive maintenance FAQ answer #124: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 125": "🤖 Predictive maintenance FAQ answer #125: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 126": "🤖 Predictive maintenance FAQ answer #126: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 127": "🤖 Predictive maintenance FAQ answer #127: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 128": "🤖 Predictive maintenance FAQ answer #128: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 129": "🤖 Predictive maintenance FAQ answer #129: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 130": "🤖 Predictive maintenance FAQ answer #130: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 131": "🤖 Predictive maintenance FAQ answer #131: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 132": "🤖 Predictive maintenance FAQ answer #132: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 133": "🤖 Predictive maintenance FAQ answer #133: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 134": "🤖 Predictive maintenance FAQ answer #134: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 135": "🤖 Predictive maintenance FAQ answer #135: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 136": "🤖 Predictive maintenance FAQ answer #136: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 137": "🤖 Predictive maintenance FAQ answer #137: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 138": "🤖 Predictive maintenance FAQ answer #138: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 139": "🤖 Predictive maintenance FAQ answer #139: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 140": "🤖 Predictive maintenance FAQ answer #140: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 141": "🤖 Predictive maintenance FAQ answer #141: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 142": "🤖 Predictive maintenance FAQ answer #142: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 143": "🤖 Predictive maintenance FAQ answer #143: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 144": "🤖 Predictive maintenance FAQ answer #144: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 145": "🤖 Predictive maintenance FAQ answer #145: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 146": "🤖 Predictive maintenance FAQ answer #146: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 147": "🤖 Predictive maintenance FAQ answer #147: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 148": "🤖 Predictive maintenance FAQ answer #148: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 149": "🤖 Predictive maintenance FAQ answer #149: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 150": "🤖 Predictive maintenance FAQ answer #150: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 151": "🤖 Predictive maintenance FAQ answer #151: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 152": "🤖 Predictive maintenance FAQ answer #152: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 153": "🤖 Predictive maintenance FAQ answer #153: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 154": "🤖 Predictive maintenance FAQ answer #154: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 155": "🤖 Predictive maintenance FAQ answer #155: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 156": "🤖 Predictive maintenance FAQ answer #156: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 157": "🤖 Predictive maintenance FAQ answer #157: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 158": "🤖 Predictive maintenance FAQ answer #158: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 159": "🤖 Predictive maintenance FAQ answer #159: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 160": "🤖 Predictive maintenance FAQ answer #160: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 161": "🤖 Predictive maintenance FAQ answer #161: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 162": "🤖 Predictive maintenance FAQ answer #162: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 163": "🤖 Predictive maintenance FAQ answer #163: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 164": "🤖 Predictive maintenance FAQ answer #164: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 165": "🤖 Predictive maintenance FAQ answer #165: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 166": "🤖 Predictive maintenance FAQ answer #166: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 167": "🤖 Predictive maintenance FAQ answer #167: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 168": "🤖 Predictive maintenance FAQ answer #168: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 169": "🤖 Predictive maintenance FAQ answer #169: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 170": "🤖 Predictive maintenance FAQ answer #170: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 171": "🤖 Predictive maintenance FAQ answer #171: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 172": "🤖 Predictive maintenance FAQ answer #172: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 173": "🤖 Predictive maintenance FAQ answer #173: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 174": "🤖 Predictive maintenance FAQ answer #174: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 175": "🤖 Predictive maintenance FAQ answer #175: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 176": "🤖 Predictive maintenance FAQ answer #176: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 177": "🤖 Predictive maintenance FAQ answer #177: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 178": "🤖 Predictive maintenance FAQ answer #178: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 179": "🤖 Predictive maintenance FAQ answer #179: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 180": "🤖 Predictive maintenance FAQ answer #180: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 181": "🤖 Predictive maintenance FAQ answer #181: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 182": "🤖 Predictive maintenance FAQ answer #182: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 183": "🤖 Predictive maintenance FAQ answer #183: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 184": "🤖 Predictive maintenance FAQ answer #184: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 185": "🤖 Predictive maintenance FAQ answer #185: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 186": "🤖 Predictive maintenance FAQ answer #186: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 187": "🤖 Predictive maintenance FAQ answer #187: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 188": "🤖 Predictive maintenance FAQ answer #188: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 189": "🤖 Predictive maintenance FAQ answer #189: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 190": "🤖 Predictive maintenance FAQ answer #190: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 191": "🤖 Predictive maintenance FAQ answer #191: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 192": "🤖 Predictive maintenance FAQ answer #192: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 193": "🤖 Predictive maintenance FAQ answer #193: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 194": "🤖 Predictive maintenance FAQ answer #194: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 195": "🤖 Predictive maintenance FAQ answer #195: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 196": "🤖 Predictive maintenance FAQ answer #196: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 197": "🤖 Predictive maintenance FAQ answer #197: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 198": "🤖 Predictive maintenance FAQ answer #198: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 199": "🤖 Predictive maintenance FAQ answer #199: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 200": "🤖 Predictive maintenance FAQ answer #200: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 201": "🤖 Predictive maintenance FAQ answer #201: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 202": "🤖 Predictive maintenance FAQ answer #202: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 203": "🤖 Predictive maintenance FAQ answer #203: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 204": "🤖 Predictive maintenance FAQ answer #204: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 205": "🤖 Predictive maintenance FAQ answer #205: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 206": "🤖 Predictive maintenance FAQ answer #206: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 207": "🤖 Predictive maintenance FAQ answer #207: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 208": "🤖 Predictive maintenance FAQ answer #208: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 209": "🤖 Predictive maintenance FAQ answer #209: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 210": "🤖 Predictive maintenance FAQ answer #210: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 211": "🤖 Predictive maintenance FAQ answer #211: The system analyzes sensor data to improve machine health monitoring.",
        "predictive maintenance faq 212": "🤖 Predictive maintenance FAQ answer #212: The system analyzes sensor data to improve machine health monitoring."

    }

    def reply(msg):
        ml=msg.lower()
        for k,v in KB.items():
            if k in ml: return v
        return ("👋 I am **Aura**, your intelligent diagnostic assistant. Ask me anything about:\n\n"
                "**Remaining Useful Life (RUL)** · **Failure Modes** (TWF/HDF/PWF/OSF) · **Fleet Health** · "
                "**Model Accuracy** · **Analytics** · **Machine Review** · **Condition Scores** · **IoT & Cloud**")

    if "chat" not in st.session_state:
        st.session_state.chat=[("bot","👋 Welcome to Aura AI. How can I help you analyze your machinery today?")]

    st.markdown('<div style="display:flex; flex-direction:column; padding-bottom: 1.5rem;">', unsafe_allow_html=True)
    for role,msg in st.session_state.chat:
        if role == "user":
            st.markdown(f'<div class="cu">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="cb"><span class="cb-icon">🤖</span>{msg}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Suggested Prompts (Chips) layout using columns
    st.markdown('<div style="font-size:0.75rem;color:#00D4FF;text-transform:uppercase;letter-spacing:0.15em;margin:1.5rem 0 0.8rem;text-align:center;">Suggested Prompts</div>', unsafe_allow_html=True)
    
    qq1=st.columns(4)
    for col,qq in zip(qq1,["Explain RUL","What is TWF?","Fleet Health?","Analytics?"]):
        with col:
            if st.button(qq,key=f"q1_{qq}", use_container_width=True):
                st.session_state.chat.append(("user",qq)); st.session_state.chat.append(("bot",reply(qq))); st.rerun()
    qq2=st.columns(4)
    for col,qq in zip(qq2,["Model Accuracy","IoT Sensors","Cloud Deploy","Download PDF"]):
        with col:
            if st.button(qq,key=f"q2_{qq}", use_container_width=True):
                st.session_state.chat.append(("user",qq)); st.session_state.chat.append(("bot",reply(qq))); st.rerun()

    ui=st.chat_input("Ask me anything...")
    if ui:
        st.session_state.chat.append(("user",ui)); st.session_state.chat.append(("bot",reply(ui))); st.rerun()

    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.chat=[("bot","👋 Conversation cleared. What would you like to explore next?")]; st.rerun()

    st.markdown("""<div style="text-align:center;padding:2.5rem 0 1rem;color:#2a4060;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;border-top:1px solid rgba(0,212,255,0.06);margin-top:1rem">
      🔮 Aura AI &nbsp;·&nbsp; PredictaShield Intelligent Assistant &nbsp;·&nbsp; v5.0
    </div>""", unsafe_allow_html=True)