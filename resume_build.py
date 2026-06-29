#!/usr/bin/env python3
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, ListFlowable, ListItem)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

OUT = "resume.pdf"
BLUE = colors.HexColor("#0F62FE")
INK = colors.HexColor("#1A1A1A")
MUTED = colors.HexColor("#555555")
LINE = colors.HexColor("#D9D7CF")

doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                        leftMargin=0.55*inch, rightMargin=0.55*inch,
                        topMargin=0.5*inch, bottomMargin=0.45*inch,
                        title="Bhargav Hari — Resume", author="Bhargav Hari")

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20, leading=22, textColor=BLUE, spaceAfter=2)
tagline = ParagraphStyle("tag", fontName="Helvetica", fontSize=9.5, leading=12, textColor=INK, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MUTED)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=BLUE,
                     spaceBefore=9, spaceAfter=3, tracking=1)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=INK)
org = ParagraphStyle("org", fontName="Helvetica-Oblique", fontSize=8.8, leading=11, textColor=MUTED, spaceAfter=1)
dates = ParagraphStyle("dates", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MUTED, alignment=TA_RIGHT)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=11.5, textColor=INK)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, leading=11, textColor=INK)
skill = ParagraphStyle("skill", fontName="Helvetica", fontSize=8.8, leading=11.5, textColor=INK, spaceAfter=1)

story = []

def header_row(left_role, left_org, right_dates):
    t = Table([[Paragraph(left_role, role), Paragraph(right_dates, dates)]],
              colWidths=[4.95*inch, 2.4*inch])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                           ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    story.append(t)
    if left_org:
        story.append(Paragraph(left_org, org))

def bullets(items):
    story.append(ListFlowable(
        [ListItem(Paragraph(x, bullet), value="•", leftIndent=12) for x in items],
        bulletType="bullet", start="•", leftIndent=10, bulletFontSize=7,
        spaceBefore=1, spaceAfter=2))

def section(title):
    story.append(Paragraph(title.upper(), sec))
    story.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=1, spaceAfter=4))

# ---- Header ----
story.append(Paragraph("Bhargav Hari", name))
story.append(Paragraph("Business Analytics &nbsp;·&nbsp; Finance &nbsp;·&nbsp; AI Engineering", tagline))
story.append(Paragraph(
    "Bengaluru, India &nbsp;·&nbsp; bhargavhari2001@gmail.com &nbsp;·&nbsp; "
    "linkedin.com/in/bhargav-hari-6b5428281 &nbsp;·&nbsp; github.com/bhargavhari2001-cloud &nbsp;·&nbsp; "
    "bhargav-portfolio-lake.vercel.app", contact))
story.append(Spacer(1, 4))

# ---- Summary ----
section("Summary")
story.append(Paragraph(
    "I'm a business analyst who learned to build. Three years in IT pre-sales showed me where deals and data "
    "actually break; an M.S. in Business Analytics gave me the tools to fix it. I turn problems I've lived "
    "through into working AI tools — three shipped and live, on my own — at the meeting point of finance, "
    "data, and machine learning. Looking for data and business analyst roles where I can build, not just report.",
    body))

# ---- Experience ----
section("Experience")
header_row("Student Research Intern — Accounting Analytics", "Rochester Institute of Technology, Rochester, NY", "Jan 2026 – Aug 2026")
bullets([
    "Read and tagged 49+ papers across 12 top information-systems journals (MIS Quarterly, ISR, JMIS) on AI and ESG, keeping the research library organized and searchable.",
    "Prepped manuscripts for journal submission.",
])
story.append(Spacer(1, 3))
header_row("Graduate Assistant — Financial Analysis", "Rochester Institute of Technology, Rochester, NY", "Sep 2024 – May 2025")
bullets([
    "Used R and Python to study company fundamentals and surface market trends the finance team used to manage portfolio risk.",
    "Built valuation and volatility models for ongoing corporate-finance research.",
])
story.append(Spacer(1, 3))
header_row("Business Analyst", "Impelsys Pvt Ltd, Bangalore, India", "Jul 2022 – Jul 2024")
bullets([
    "Owned the RFP/RFQ process across $250K+ in deals over my time there — wrote the proposals and pushed our win rate up 25%.",
    "Scoped and priced SaaS deals with the team, landing within 85% of final scope and margin.",
    "Ran 20–25 bids a year and demoed to C-suite buyers across education, publishing, and healthcare.",
])

# ---- Projects ----
section("Selected Projects (solo, end-to-end)")
link = '<a href="{u}" color="#0F62FE">{t}</a>'
bullets([
    "<b>BidCraft — AI RFP automation</b> (live): turns the 40–60-hour RFP grind into a grounded, confidence-scored first draft — reads an RFP, finds your strongest past answers by meaning (pgvector), and writes the response. Born from running 20+ enterprise proposals a year at Impelsys. Next.js 16 · Claude API · Voyage AI · Supabase. &nbsp;"+link.format(u="https://bid-craft-beta.vercel.app/", t="bid-craft-beta.vercel.app"),
    "<b>Customer churn &amp; survival analysis:</b> predicts not just who will churn but when — XGBoost for the who (0.981 AUC, 0.84 F1), a Cox survival model for the when, SHAP for the why. ~5,600 real e-commerce customers.",
    "<b>S&amp;P 500 options trading bot</b> (live): automates a premium-selling options strategy (IV rank, RSI, Greeks) to strip out the discretion that breaks it by hand — executed via the Alpaca API. &nbsp;"+link.format(u="https://trading-bot-dashboard-five.vercel.app", t="trading-bot-dashboard-five.vercel.app"),
    "<b>Precision Retail Pro</b> (live): turns two CSVs — inventory + sales — into demand forecasts (Prophet) and ABC stock alerts, giving small retailers the inventory intelligence that SAP/Oracle price out of reach. &nbsp;"+link.format(u="https://precision-retail-pro.vercel.app/", t="precision-retail-pro.vercel.app"),
])

# ---- Education ----
section("Education")
header_row("M.S. Business Analytics (STEM)", "Rochester Institute of Technology — Saunders College (AACSB) · GPA 3.89/4.0", "Aug 2024 – May 2026")
story.append(Spacer(1, 2))
header_row("B.B.A. Finance &amp; International Business", "CHRIST University, Bangalore (NAAC A+) · CGPA 8.97/10", "Jun 2019 – May 2022")
story.append(Spacer(1, 2))
header_row("Advanced Certificate, Business &amp; Data Analytics", "IIM Udaipur (AACSB accredited)", "May – Jul 2025")

# ---- Skills ----
section("Skills")
story.append(Paragraph("<b>Languages &amp; Data:</b> Python (pandas, scikit-learn, XGBoost, SHAP), R (tidyverse, survival, caret), SQL (Oracle, PostgreSQL, PL/SQL), TypeScript / JavaScript", skill))
story.append(Paragraph("<b>AI &amp; Analytics:</b> Machine learning, survival analysis, NLP; time-series (ARIMA, GARCH, Prophet); RAG &amp; vector search (pgvector); LLM integration (Claude API)", skill))
story.append(Paragraph("<b>Business:</b> Financial modeling &amp; variance analysis; RFP management &amp; presales solutioning; client relationships &amp; requirements gathering; stakeholder communication", skill))
story.append(Paragraph("<b>Tools &amp; Platforms:</b> Tableau, Power BI, Advanced Excel; Next.js, React, Tailwind, Supabase; Git, Jupyter, Oracle APEX, Alpaca API, Vercel", skill))

doc.build(story)
print("WROTE", OUT)
