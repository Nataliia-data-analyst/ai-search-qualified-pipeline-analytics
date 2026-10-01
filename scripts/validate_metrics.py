import csv
from pathlib import Path

DATA = Path("data/raw")

def rows(filename):
    with open(DATA / filename, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(value):
    if value is None or value.strip() == "":
        return 0.0
    return float(
        value.replace("$", "")
             .replace(",", "")
             .replace("%", "")
             .strip()
    )

# ---------------- AI PRESENCE ----------------

ai = rows("01_ai_presence.csv")

mentions = sum(num(r["Mentioned"]) for r in ai)
citations = sum(num(r["Linked_Citation"]) for r in ai)
accurate = sum(num(r["Accurate"]) for r in ai)
answers = len(ai)

brand_presence = mentions / answers if answers else 0
citation_rate = citations / answers if answers else 0
accuracy_rate = accurate / mentions if mentions else 0

# ---------------- GA4 ----------------

ga4 = rows("02_ga4_traffic.csv")

ai_sessions = 0
ai_demos = 0

for r in ga4:
    text = f'{r["Channel_Group"]} {r["Session_Source"]}'.lower()

    if any(x in text for x in [
        "chatgpt", "perplexity", "gemini", "copilot", "claude", "ai referral"
    ]):
        ai_sessions += num(r["Sessions"])
        ai_demos += num(r["Demo_Requests"])

ai_demo_cvr = ai_demos / ai_sessions if ai_sessions else 0

# ---------------- GSC ----------------

gsc = rows("03_gsc_branded.csv")

branded = [
    r for r in gsc
    if "brand" in r["Query_Type"].lower()
]

gsc_impressions = sum(num(r["Impressions"]) for r in branded)
gsc_clicks = sum(num(r["Clicks"]) for r in branded)

branded_ctr = (
    gsc_clicks / gsc_impressions
    if gsc_impressions else 0
)

# ---------------- CRM ----------------

crm = rows("04_crm_opportunities.csv")

opportunities = len({
    r["Opportunity_ID"]
    for r in crm
    if r["Opportunity_ID"]
})

qualified = sum(num(r["Qualified"]) for r in crm)

qualification_rate = (
    qualified / opportunities
    if opportunities else 0
)

# ---------------- PAID AI ----------------

paid = rows("05_ai_paid_media.csv")

spend = sum(num(r["Spend_USD"]) for r in paid)
conversions = sum(num(r["Conversions"]) for r in paid)
pipeline = sum(num(r["Attributed_Pipeline_USD"]) for r in paid)

cpa = spend / conversions if conversions else 0
pipeline_roas = pipeline / spend if spend else 0

# ---------------- OUTPUT ----------------

print("\nAI SEARCH → QUALIFIED PIPELINE")
print("SOURCE METRIC VALIDATION\n")

print(f"Brand Presence Rate       {brand_presence:.2%}")
print(f"Citation Rate             {citation_rate:.2%}")
print(f"Answer Accuracy Rate      {accuracy_rate:.2%}")
print(f"AI Referral Demo CVR      {ai_demo_cvr:.2%}")
print(f"Branded CTR               {branded_ctr:.2%}")
print(f"Qualified Opportunities   {qualified:.0f}")
print(f"Qualification Rate        {qualification_rate:.2%}")
print(f"Paid AI Spend             ${spend:,.2f}")
print(f"Paid AI Conversions       {conversions:,.0f}")
print(f"Paid AI CPA               ${cpa:,.2f}")
print(f"Attributed Pipeline       ${pipeline:,.2f}")
print(f"Pipeline ROAS             {pipeline_roas:.2f}x")
