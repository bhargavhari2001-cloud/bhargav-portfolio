#!/usr/bin/env python3
# Builds the two-page resume.pdf served by the site's Résumé button.
# Page 1: summary · experience · education — Page 2: projects · skills.
# Every project figure is verified against the underlying coursework/notebook files.
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, ListFlowable, ListItem, PageBreak)
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

link = '<a href="{u}" color="#0F62FE">{t}</a>'

# ================================ PAGE 1 ================================

story.append(Paragraph("Bhargav Hari", name))
story.append(Paragraph("Business Analytics &nbsp;·&nbsp; Finance &nbsp;·&nbsp; Applied AI", tagline))
story.append(Paragraph(
    "Bengaluru, India &nbsp;·&nbsp; +1 (585) 633-6600 &nbsp;·&nbsp; bhargavhari2001@gmail.com &nbsp;·&nbsp; "
    "linkedin.com/in/bhargavhari &nbsp;·&nbsp; github.com/bhargavhari2001-cloud &nbsp;·&nbsp; "
    "bhargav-portfolio-lake.vercel.app", contact))
story.append(Spacer(1, 4))

section("Summary")
story.append(Paragraph(
    "Analyst with three years of enterprise pre-sales behind an M.S. in Business Analytics (GPA 3.89) and a "
    "finance degree. At Impelsys I owned proposals worth over $1M a year and saw first-hand where deals, "
    "pricing, and data break; at RIT I built the technical depth to fix them — volatility models, credit-risk "
    "rankings, survival analysis. Along the way I shipped three working AI products, alone, end to end. "
    "Equally at home in a client meeting, a financial model, or a codebase — and looking for analyst roles "
    "that use all three.", body))

section("Experience")

header_row("Student Research Intern — Accounting Analytics",
           "Rochester Institute of Technology, Rochester, NY &nbsp;·&nbsp; Graduate Assistant (Jan–May) → Research Intern (May–Aug)",
           "Jan 2026 – Aug 2026")
bullets([
    "Ran the literature side of a faculty research program on AI and ESG: read, screened, and tagged 49+ papers "
    "across 12 leading information-systems journals (MIS Quarterly, ISR, JMIS), building the organized, searchable "
    "library the research is written from.",
    "Converted 70+ academic references into EndNote import files and prepared manuscripts to journal submission "
    "standards — removing the manual bottleneck in the lab's writing workflow.",
    "Graded and gave structured feedback across accounting-analytics cohorts of 25+ students; built seminar "
    "presentations on AI in accounting information systems and AI for SME growth.",
])
story.append(Spacer(1, 3))

header_row("Graduate Assistant — Financial Analysis",
           "Rochester Institute of Technology, Rochester, NY", "Sep 2024 – May 2025")
bullets([
    "Analyzed the fundamentals of 50+ public companies with time-series regression in R and Python, surfacing "
    "sector trends the faculty used for risk-management research.",
    "Built forecasting models across 10,000+ observations — EV-loan repossession risk and S&amp;P 500 volatility "
    "(ARIMA + GARCH) — cutting forecast error by 18% against the standing baseline.",
    "Maintained an Excel dashboard tracking $500M+ in financial-restatement events, the working dataset for "
    "faculty research on earnings manipulation and governance failure.",
    "Modeled credit default with XGBoost and SHAP (0.98 AUC) for instructor-led case studies.",
])
story.append(Spacer(1, 3))

header_row("Business Analyst", "Impelsys Pvt Ltd, Bangalore, India", "Jul 2022 – Jul 2024")
bullets([
    "Owned proposal responses for $1M+ a year in enterprise publishing and edtech deals (Wiley, Pearson, "
    "McGraw-Hill); the win rate rose 25% on the strength of sharper, evidence-led positioning.",
    "Wrote and quality-checked 80+ RFP responses end to end — scope, pricing, compliance mapping, executive "
    "narrative — and cut turnaround 30% by building the team's standard response playbook.",
    "Built the Excel pricing models behind multi-product bids: FTE cost allocation, margin floors, and vendor "
    "benchmarks that kept bids competitive without giving away the margin.",
    "Studied win/loss patterns across 200+ proposals in Python; the pricing and messaging gaps it exposed "
    "reshaped the go-to-market playbook.",
    "Led discovery calls and C-suite presentations, turning loosely-defined transformation asks into clean "
    "solution blueprints — 100% compliance on $500K+ contracts.",
])

section("Education")
header_row("M.S. Business Analytics (STEM)",
           "Rochester Institute of Technology — Saunders College of Business (AACSB) · GPA 3.89/4.0",
           "Aug 2024 – May 2026")
story.append(Spacer(1, 2))
header_row("B.B.A. Finance &amp; International Business",
           "CHRIST University, Bangalore (NAAC A+) · CGPA 8.97/10", "Jun 2019 – May 2022")
story.append(Spacer(1, 2))
header_row("Advanced Certificate, Business &amp; Data Analytics",
           "Indian Institute of Management Udaipur (AACSB)", "May – Jul 2025")

# ================================ PAGE 2 ================================
story.append(PageBreak())

section("Selected Projects — Built Solo, End To End")
story.append(Paragraph(
    "Three are live products; the rest are full studies. Every number below comes from the underlying code and "
    "reports — deeper write-ups, dashboards, and source at "
    + link.format(u="https://bhargav-portfolio-lake.vercel.app", t="bhargav-portfolio-lake.vercel.app") + ".", body))
story.append(Spacer(1, 4))
bullets([
    "<b>BidCraft — AI RFP automation</b> (live): turns the 40–60-hour RFP grind into a grounded, "
    "confidence-scored first draft. Reads the RFP, retrieves your strongest past answers by meaning "
    "(240-answer knowledge base, 512-dim embeddings, pgvector), and drafts the response with citations. "
    "Born from running 20+ enterprise proposals a year at Impelsys. Next.js 16 · Claude · Voyage AI · "
    "Supabase. &nbsp;" + link.format(u="https://bid-craft-beta.vercel.app/", t="bid-craft-beta.vercel.app"),

    "<b>S&amp;P 500 volatility forecasting:</b> ARIMA + GARCH pipeline that called the market's volatility "
    "state correctly 81.5% of the time vs a 70.5% rolling baseline across 1,765 walk-forward forecasts — "
    "14.7% lower RMSE, 0.88 correlation with the VIX, and it reacted to the COVID crash days before the "
    "baseline did.",

    "<b>Customer churn &amp; survival analysis:</b> predicts not just who will leave but when — XGBoost for "
    "the who (0.981 AUC, 0.84 F1), a Cox survival model for the when, SHAP for the why, on ~5,600 real "
    "e-commerce customers.",

    "<b>Amex credit-default prediction:</b> engineered 1,085 features from raw statement history; LightGBM "
    "ranked defaulters at 0.948 ROC-AUC — the riskiest decile it flagged was 94% actual defaulters, and the "
    "top three deciles caught 85% of all defaults.",

    "<b>Options trading bot</b> (live): a vol-gated SPY options strategy that stands aside when the VIX term "
    "structure says panic — lifting Sharpe from 1.21 to 1.66 and cutting max drawdown 87% in an 8-year "
    "backtest; runs live on Alpaca paper trading. &nbsp;"
    + link.format(u="https://trading-bot-dashboard-five.vercel.app", t="trading-bot-dashboard-five.vercel.app"),

    "<b>Precision Retail Pro</b> (live): turns two CSVs — inventory and sales — into demand forecasts and "
    "ABC/dead-stock alerts, giving small retailers the inventory intelligence that enterprise systems price "
    "out of reach. &nbsp;" + link.format(u="https://precision-retail-pro.vercel.app/", t="precision-retail-pro.vercel.app"),

    "<b>Financial-restatement risk:</b> Fraud-Triangle-based screens over 1,000+ firms showing that a 20% "
    "drop in net income raises restatement odds roughly 3.5× — pressure, not complexity, is the tell.",

    "<b>Also on the portfolio:</b> hospital-stay triage on 113K patients (Heritage Health Prize), NYC taxi "
    "trip-duration prediction, real-vs-fake-news NLP on 22K headlines, healthcare database in Oracle APEX, "
    "and market-basket analysis in R.",
])

section("Skills")
story.append(Paragraph("<b>Languages &amp; Data:</b> Python (pandas, scikit-learn, XGBoost, LightGBM, SHAP), R (tidyverse, survival, caret, tidytext), SQL (Oracle, PostgreSQL, PL/SQL), TypeScript / JavaScript", skill))
story.append(Paragraph("<b>AI &amp; Analytics:</b> Machine learning, survival analysis, NLP; time-series forecasting (ARIMA, GARCH, Prophet); RAG &amp; vector search (pgvector); LLM integration (Claude API)", skill))
story.append(Paragraph("<b>Business:</b> Financial modeling &amp; pricing; RFP management &amp; pre-sales solutioning; win/loss analysis; client discovery &amp; C-suite communication; research design", skill))
story.append(Paragraph("<b>Tools &amp; Platforms:</b> Tableau, Power BI, Advanced Excel; Next.js, React, Supabase; Git, Jupyter, Oracle APEX, EndNote, Alpaca API, Vercel", skill))
story.append(Paragraph("<b>Spoken:</b> English · Kannada · Hindi · Tamil", skill))

doc.build(story)
print("WROTE", OUT)
