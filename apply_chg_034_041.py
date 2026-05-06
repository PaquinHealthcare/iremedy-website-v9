#!/usr/bin/env python3
"""Apply CHG-034 through CHG-041 design refinements to index.html"""

with open('/Users/berniemac/projects/iremedy-website-v9/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# ==============================================================================
# 1. Add comprehensive CSS block before closing </style>
# ==============================================================================

css_block = """
    /* ══ CHG-034 through CHG-041: DESIGN REFINEMENTS ══ */

    /* --- TradeSpy: convert ts-dark-section and ts-gov-section to deep dark --- */
    .ts-section.ts-dark-section { background: #212E3E !important; }
    .ts-section.ts-gov-section  { background: #212E3E !important; }

    /* Text in converted dark ts sections */
    .ts-dark-section .ts-sec-title,
    .ts-gov-section  .ts-sec-title          { color: #FFFFFF !important; }
    .ts-dark-section .ts-sec-title em,
    .ts-gov-section  .ts-sec-title em       { color: #00ACE6 !important; }
    .ts-dark-section .ts-body,
    .ts-gov-section  .ts-body               { color: #C8CDD3 !important; }
    .ts-dark-section .ts-list li,
    .ts-gov-section  .ts-list li            { color: #C8CDD3 !important; }
    .ts-dark-section .ts-list li::before,
    .ts-gov-section  .ts-list li::before    { color: #00ACE6 !important; }
    .ts-dark-section .ts-section-label,
    .ts-gov-section  .ts-section-label      { color: #00ACE6 !important; }
    .ts-dark-section .ts-layer-num,
    .ts-gov-section  .ts-layer-num          { color: #00ACE6 !important; }
    .ts-dark-section .ts-layer-name,
    .ts-gov-section  .ts-layer-name         { color: #FFFFFF !important; font-weight: 700 !important; }
    .ts-dark-section .ts-layer-card p,
    .ts-gov-section  .ts-layer-card p       { color: #C8CDD3 !important; }
    .ts-dark-section .ts-layer-card,
    .ts-gov-section  .ts-layer-card         { background: rgba(255,255,255,0.04) !important; }
    .ts-dark-section .ts-callout,
    .ts-gov-section  .ts-callout            { background: rgba(0,172,230,0.08) !important; border-color: rgba(0,172,230,0.4) !important; }
    .ts-dark-section .ts-callout-label,
    .ts-gov-section  .ts-callout-label      { color: #00ACE6 !important; }
    /* Roadmap rows on dark */
    .ts-dark-section .ts-roadmap            { border-color: rgba(255,255,255,0.12) !important; }
    .ts-dark-section .ts-rm-row             { border-color: rgba(255,255,255,0.08) !important; }
    .ts-dark-section .ts-rm-item            { color: #C8CDD3 !important; }
    .ts-dark-section .ts-rm-row.active .ts-rm-item { color: #FFFFFF !important; font-weight: 500 !important; }

    /* --- TradeSpy "The Doctrine" section: handled via inline style in HTML --- */

    /* --- TradeSpy global size floors --- */
    .ts-body      { font-size: 1rem; }
    .ts-std-name  { font-size: 1.125rem !important; font-weight: 700 !important; }
    .ts-standard-card p { font-size: 0.9375rem !important; }
    .ts-arch-item p     { font-size: 0.9375rem !important; }
    .ts-list li         { font-size: 0.9375rem !important; }

    /* --- Press releases --- */
    .pr-date  { font-size: 0.8125rem !important; }
    .pr-title { font-size: 0.9375rem !important; }
    .pr-tag   { font-size: 0.6875rem !important; }
    .pr-row   { padding-top: 0.75rem !important; padding-bottom: 0.75rem !important; }

    /* --- Leadership page cards --- */
    .ldp-name  { font-size: 1.15rem !important; font-weight: 700 !important; }
    .ldp-bio   { font-size: 0.875rem !important; line-height: 1.7 !important; }
    .ldp-title { font-size: 0.8rem !important; }

    /* --- cap-list items (Providers iRemedy Direct section) --- */
    .cap-title { font-size: 1.125rem !important; font-weight: 700 !important; }
    .cap-body  { font-size: 0.9375rem !important; }

    /* --- FAQ min sizes (providers/pharmacies) --- */
    .callout p { font-size: 1.125rem !important; }

    /* --- blist sizing --- */
    .blist li  { font-size: 1rem !important; }

    /* --- sec-body global floor --- */
    .sec-body  { font-size: 1rem !important; }

    /* --- Form --- */
    .form-group label { font-size: 0.75rem !important; }
    .form-group input,
    .form-group select,
    .form-group textarea { font-size: 1rem !important; }
"""

old_style_close = '  </style>'
content = content.replace(old_style_close, css_block + old_style_close, 1)
changes.append('Added CHG CSS block')

# ==============================================================================
# 2. CHG-034 — PROVIDERS PAGE
# ==============================================================================

# Hero italic subheadline: rgba(242,237,228,0.62) → #C8CDD3
r = 'color:rgba(242,237,228,0.62);max-width:680px;margin-bottom:2rem;line-height:1.7;font-weight:300;">Pharmaceuticals, biologics, medical devices, and supplies - direct from the manufacturer'
n = 'color:#C8CDD3;max-width:680px;margin-bottom:2rem;line-height:1.7;font-weight:300;">Pharmaceuticals, biologics, medical devices, and supplies - direct from the manufacturer'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers hero subheadline color')

# Hero credential strip: size + color
r = 'font-size:0.8rem;letter-spacing:0.14em;text-transform:uppercase;color:rgba(242,237,228,0.4);margin-bottom:2.5rem;">50-State Licensed \u00b7 DEA Authorized \u00b7 DSCSA Compliant \u00b7 NABP Accredited \u00b7 UPS Healthcare Logistics'
n = 'font-size:0.875rem;letter-spacing:0.14em;text-transform:uppercase;color:#9CA3AF;margin-bottom:2.5rem;">50-State Licensed \u00b7 DEA Authorized \u00b7 DSCSA Compliant \u00b7 NABP Accredited \u00b7 UPS Healthcare Logistics'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers hero cred strip')

# Section 06 GPO Question: padding 5rem → 7rem
r = '<!-- SECTION 06 - THE GPO QUESTION -->\n  <div style="background:var(--bg);padding:5rem 6vw;border-bottom:1px solid var(--rule);">'
n = '<!-- SECTION 06 - THE GPO QUESTION -->\n  <div style="background:var(--bg);padding:7rem 6vw;border-bottom:1px solid var(--rule);">'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S06 padding')

# Section 06: headline clamp min → 2rem
r = 'font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:900;line-height:1.1;letter-spacing:-0.02em;color:var(--ink);max-width:760px;margin-bottom:2.5rem;">You don\'t have to leave your GPO.'
n = 'font-size:clamp(2rem,3.5vw,2.8rem);font-weight:900;line-height:1.1;letter-spacing:-0.02em;color:var(--ink);max-width:760px;margin-bottom:2.5rem;">You don\'t have to leave your GPO.'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S06 headline clamp')

# Section 07 Fulfillment: bg-3 → #EDF1F5
r = '<!-- SECTION 07 - FULFILLMENT (bg-3 / off-white) -->\n  <div style="background:var(--bg-3);padding:5rem 6vw;border-bottom:1px solid var(--rule);">'
n = '<!-- SECTION 07 - FULFILLMENT (bg-3 / off-white) -->\n  <div style="background:#EDF1F5;padding:5rem 6vw;border-bottom:1px solid var(--rule);">'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S07 background')

# Section 08 logo min-height 64px → 80px
r = 'background:var(--bg-2);padding:1.25rem;display:flex;align-items:center;justify-content:center;min-height:64px;'
n = 'background:var(--bg-2);padding:1.25rem;display:flex;align-items:center;justify-content:center;min-height:80px;'
# Replace all occurrences (there are 4 logo placeholders)
old_count = content.count(r)
content = content.replace(r, n)
changes.append(f'CHG-034: Providers S08 logo min-height ({old_count} instances)')

# Section 08 testimonial quote: 1.1rem → 1.125rem
r = 'font-size:1.1rem;font-style:italic;line-height:1.65;color:var(--ink);margin-bottom:1rem;">&ldquo;[Testimonial quote from a provider/buyer client - to be provided]&rdquo;</div>'
n = 'font-size:1.125rem;font-style:italic;line-height:1.65;color:var(--ink);margin-bottom:1rem;">&ldquo;[Testimonial quote from a provider/buyer client - to be provided]&rdquo;</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S08 testimonial size')

# Section 10 CTA body text
r = 'color:rgba(242,237,228,0.62);max-width:540px;margin:0 auto 2.5rem;">Tell us what you\'re buying today'
n = 'color:#C8CDD3;max-width:540px;margin:0 auto 2.5rem;">Tell us what you\'re buying today'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S10 CTA body')

# Section 10 CTA contact line
r = 'font-size:0.8rem;letter-spacing:0.1em;color:rgba(242,237,228,0.35);">Or contact our team directly - sales@iremedy.com'
n = 'font-size:0.875rem;letter-spacing:0.1em;color:#C8CDD3;">Or contact our team directly - sales@iremedy.com'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-034: Providers S10 contact line')

# ==============================================================================
# 3. CHG-035 — PHARMACIES PAGE
# ==============================================================================

# Hero subheadline
r = 'color:rgba(242,237,228,0.62);max-width:720px;margin-bottom:2rem;line-height:1.7;font-weight:300;">Pharmaceuticals, bulk APIs, peptides, GLP-1 agonists, biologics, controlled substances, and supplies'
n = 'color:#C8CDD3;max-width:720px;margin-bottom:2rem;line-height:1.7;font-weight:300;">Pharmaceuticals, bulk APIs, peptides, GLP-1 agonists, biologics, controlled substances, and supplies'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies hero subheadline')

# Hero credential strip
r = 'font-size:0.8rem;letter-spacing:0.14em;text-transform:uppercase;color:rgba(242,237,228,0.4);margin-bottom:2.5rem;">50-State Licensed \u00b7 DEA Authorized \u00b7 NABP Accredited \u00b7 DSCSA Compliant \u00b7 FDA Green List API Sources \u00b7 UPS Healthcare Cold Chain'
n = 'font-size:0.875rem;letter-spacing:0.14em;text-transform:uppercase;color:#9CA3AF;margin-bottom:2.5rem;">50-State Licensed \u00b7 DEA Authorized \u00b7 NABP Accredited \u00b7 DSCSA Compliant \u00b7 FDA Green List API Sources \u00b7 UPS Healthcare Cold Chain'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies hero cred strip')

# Section 03 HIGH DEMAND badge → red
r = 'position:absolute;top:1.25rem;right:1.25rem;font-family:var(--mono);font-size:0.8rem;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;background:var(--teal);color:#fff;padding:3px 8px;">HIGH DEMAND</div>'
n = 'position:absolute;top:1.25rem;right:1.25rem;font-family:var(--mono);font-size:0.75rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;background:#E53E3E;color:#FFFFFF;padding:0.25rem 0.6rem;border-radius:3px;">HIGH DEMAND</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: HIGH DEMAND badge red')

# Section 03 molecule name lines → teal color, 0.9375rem
molecule_lines = [
    'Tirzepatide \u00b7 Semaglutide \u00b7 Retatrutide (pipeline)',
    'Sermorelin \u00b7 Gonadorelin \u00b7 BPC-157 \u00b7 Ipamorelin \u00b7 Thymosin Alpha-1 \u00b7 NAD+',
    'Progesterone \u00b7 Estradiol \u00b7 Estriol \u00b7 DHEA \u00b7 Testosterone Cypionate/Enanthate',
    'Tadalafil \u00b7 Sildenafil \u00b7 Testosterone \u00b7 Anastrozole',
    'Ketamine \u00b7 Low-Dose Naltrexone \u00b7 Oxytocin \u00b7 Naloxone',
    'Branded, generic &amp; specialty pharmaceuticals \u00b7 Biologics including IVIG \u00b7 Medical supplies \u00b7 Controlled substances (DEA Schedule II-V)',
]
for mol in molecule_lines:
    r = f'font-size:1rem;color:var(--ink);font-weight:500;margin-bottom:0.75rem;line-height:1.5;">{mol}</div>'
    n = f'font-size:0.9375rem;color:var(--teal);font-weight:600;margin-bottom:0.75rem;line-height:1.5;font-style:italic;">{mol}</div>'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-035: molecule name "{mol[:20]}..."')

# Section 04 FDA-Credentialed headline: var(--bg) → #FFFFFF
r = 'color:var(--bg);max-width:760px;margin-bottom:1.5rem;">Green List sourced. Importer of record. Every node documented.</h2>'
n = 'color:#FFFFFF;max-width:760px;margin-bottom:1.5rem;">Green List sourced. Importer of record. Every node documented.</h2>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies S04 headline white')

# Section 04 body text: rgba(242,237,228,0.62) → #C8CDD3
for snippet in [
    '>For GLP-1 and peptide APIs, FDA Import Alert 66-80',
    '>iRemedy sources GLP-1 APIs from FDA-registered',
]:
    r = f'color:rgba(242,237,228,0.62);' + snippet.replace('>', '>')
    # Build full replacement
    r = f'color:rgba(242,237,228,0.62);">{snippet[1:]}'
    n = f'color:#C8CDD3;">{snippet[1:]}'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-035: S04 body {snippet[:30]}')

# Section 04 cred block description: rgba → #C8CDD3, size 0.875rem
cred_descs = [
    'Manufacturer FEI on file for every API',
    'Import Alert 66-80 compliance verified',
    'iRemedy named on customs documentation',
    'Certificate of analysis on every shipment',
]
for desc in cred_descs:
    r = f'font-size:0.9rem;color:rgba(242,237,228,0.5);line-height:1.6;">{desc}'
    n = f'font-size:0.875rem;color:#C8CDD3;line-height:1.6;">{desc}'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-035: S04 cred desc {desc[:20]}')

# Section 08 Peptide: callout card border
r = '<div style="background:var(--teal-dim);border:1px solid rgba(0,100,165,0.2);padding:2.5rem;width:100%;">'
n = '<div style="background:var(--teal-dim);border:2px solid var(--teal);padding:2.5rem;width:100%;">'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Peptide callout border')

# Section 08: peptides.iremedy.com bold teal
r = '<div style="font-family:var(--serif);font-size:1.5rem;font-weight:900;color:var(--ink);line-height:1.2;margin-bottom:0.75rem;">peptides.iremedy.com</div>'
n = '<div style="font-family:var(--serif);font-size:1.5rem;font-weight:700;color:var(--teal);line-height:1.2;margin-bottom:0.75rem;">peptides.iremedy.com</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: peptides.iremedy.com teal')

# Section 11 CTA headline: var(--bg) → #FFFFFF
r = 'color:var(--bg);margin-bottom:1.25rem;">Ready to source with confidence?</h2>'
n = 'color:#FFFFFF;margin-bottom:1.25rem;">Ready to source with confidence?</h2>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies CTA headline white')

# Section 11 CTA body
r = 'color:rgba(242,237,228,0.62);max-width:540px;margin:0 auto 2.5rem;">Tell us what you compound and what you need.'
n = 'color:#C8CDD3;max-width:540px;margin:0 auto 2.5rem;">Tell us what you compound and what you need.'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies CTA body')

# Section 11 CTA contact line
r = 'font-size:0.8rem;letter-spacing:0.1em;color:rgba(242,237,228,0.35);">For compounding and API inquiries: compounding@iremedy.com'
n = 'font-size:0.875rem;letter-spacing:0.1em;color:#C8CDD3;">For compounding and API inquiries: compounding@iremedy.com'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-035: Pharmacies CTA contact')

# ==============================================================================
# 4. CHG-036 — PLATFORM PAGE
# ==============================================================================

# Hero subheadline: var(--ink-2) → #C8CDD3 (INVISIBLE FIX)
r = 'color:var(--ink-2);font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:2.5rem;">MetaCommerceRx - AI-powered procurement'
n = 'color:#C8CDD3;font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:2.5rem;">MetaCommerceRx - AI-powered procurement'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Platform hero subheadline (INVISIBLE FIX)')

# Hero credential strip: var(--ink-3) → #9CA3AF
r = 'color:var(--ink-3);margin-bottom:2.5rem;border-top:1px solid rgba(242,237,228,0.15);border-bottom:1px solid rgba(242,237,228,0.15);padding:0.875rem 0;">10 Granted U.S. Patents'
n = 'color:#9CA3AF;margin-bottom:2.5rem;border-top:1px solid rgba(242,237,228,0.15);border-bottom:1px solid rgba(242,237,228,0.15);padding:0.875rem 0;">10 Granted U.S. Patents'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Platform hero cred strip (INVISIBLE FIX)')

# Section 03 Architecture dark: layer content text
arch_layer_content = [
    'MetaPortals.RX (B2B and B2C)',
    'Universal Medical Products Catalog',
    "iRemedy's Patented AI Meta.Agents",
    'UPS Healthcare 3PL',
]
for lc in arch_layer_content:
    r = f'<div style="font-size:0.875rem;color:var(--ink-2);font-weight:300;line-height:1.6;">{lc}'
    n = f'<div style="font-size:0.875rem;color:#C8CDD3;font-weight:300;line-height:1.6;">{lc}'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-036: Arch layer {lc[:20]}')

# Section 03 Stack note color
r = 'color:var(--ink-3);margin-top:0.5rem;">Sources: McKesson'
n = 'color:#9CA3AF;margin-top:0.5rem;">Sources: McKesson'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Arch sources line')

# Section 03 Stack box
r = '<div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);margin-bottom:0.5rem;">Stack</div>\n        <p style="font-size:0.9rem;color:var(--ink-2);font-weight:300;line-height:1.65;margin:0;">Python / FastAPI backend'
n = '<div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#00ACE6;margin-bottom:0.5rem;">Stack</div>\n        <p style="font-size:0.8125rem;color:#9CA3AF;font-weight:300;line-height:1.65;margin:0;">Python / FastAPI backend'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Arch stack box')

# Section 04 Jim Harding callout: on dark (var(--ink)) background
r = '<div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);margin-bottom:0.5rem;">Jim Harding - Co-Inventor</div>'
n = '<div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#00ACE6;margin-bottom:0.5rem;">Jim Harding - Co-Inventor</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Jim Harding label color')

r = '<p style="font-size:0.875rem;color:var(--ink-2);font-weight:300;line-height:1.65;margin:0;">Jim Harding co-invented MS-DOS'
n = '<p style="font-size:0.875rem;color:#C8CDD3;font-weight:300;line-height:1.65;margin:0;">Jim Harding co-invented MS-DOS'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Jim Harding bio color')

# ==============================================================================
# 5. CHG-037 — GOVERNMENT PAGE (CRITICAL invisible text fixes)
# ==============================================================================

# Hero subheadline: var(--ink-2) → #C8CDD3
r = '<p style="font-size:1.15rem;color:var(--ink-2);font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:2.5rem;">We detect supply chain fraud'
n = '<p style="font-size:1.15rem;color:#C8CDD3;font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:2.5rem;">We detect supply chain fraud'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov hero subheadline (INVISIBLE FIX)')

# Hero credential strip: var(--ink-3) → #9CA3AF
r = 'color:var(--ink-3);margin-bottom:2.5rem;border-top:1px solid rgba(242,237,228,0.15);border-bottom:1px solid rgba(242,237,228,0.15);padding:0.875rem 0;">Operation Warp Speed'
n = 'color:#9CA3AF;margin-bottom:2.5rem;border-top:1px solid rgba(242,237,228,0.15);border-bottom:1px solid rgba(242,237,228,0.15);padding:0.875rem 0;">Operation Warp Speed'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov hero cred strip (INVISIBLE FIX)')

# Hero: btn-ghost → btn-ghost-lt for "See the Made in America Portfolio"
r = '<button class="btn btn-ghost" onclick="document.getElementById(\'gov-mia\').scrollIntoView({behavior:\'smooth\'})">See the Made in America Portfolio \u2193</button>'
n = '<button class="btn btn-ghost-lt" onclick="document.getElementById(\'gov-mia\').scrollIntoView({behavior:\'smooth\'})">See the Made in America Portfolio \u2193</button>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov hero btn-ghost-lt')

# Section 03 TradeSpy dark: body paragraphs
gov_tradespy_paras = [
    "TradeSpy is iRemedy's autonomous supply chain intelligence platform.",
    "Federal procurement teams currently have no systematic way",
    "TradeSpy is also a fraud detection engine.",
]
for para in gov_tradespy_paras:
    r = f'<p style="font-size:1rem;color:var(--ink-2);font-weight:300;line-height:1.8;max-width:820px;margin-bottom:1.25rem;">{para}'
    n = f'<p style="font-size:1rem;color:#C8CDD3;font-weight:300;line-height:1.8;max-width:820px;margin-bottom:1.25rem;">{para}'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-037: TradeSpy para {para[:30]}')

r = '<p style="font-size:1rem;color:var(--ink-2);font-weight:300;line-height:1.8;max-width:820px;margin-bottom:3rem;">TradeSpy is also a fraud detection engine.'
n = '<p style="font-size:1rem;color:#C8CDD3;font-weight:300;line-height:1.8;max-width:820px;margin-bottom:3rem;">TradeSpy is also a fraud detection engine.'
if r in content: content = content.replace(r, n, 1)

# Section 03 stat blocks: numbers white, labels #9CA3AF
stat_pairs = [
    ('129,140', 'NDCs under continuous autonomous surveillance'),
    ('412', 'CCP supply chain exposure flags in the national formulary'),
    ('24/7', 'Autonomous monitoring - no manual intervention required'),
]
for num, lbl in stat_pairs:
    r = f'<div style="font-family:var(--serif);font-size:2.5rem;font-weight:700;color:var(--teal);line-height:1;">{num}</div>\n          <div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-3);margin-top:0.5rem;line-height:1.4;">{lbl}</div>'
    n = f'<div style="font-family:var(--serif);font-size:2.5rem;font-weight:700;color:#FFFFFF;line-height:1;">{num}</div>\n          <div style="font-family:var(--mono);font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#9CA3AF;margin-top:0.5rem;line-height:1.4;">{lbl}</div>'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-037: TradeSpy stat {num}')

# Section 03: six capability block labels and descriptions
cap_nums = ['01', '02', '03', '04', '05', '06']
cap_titles = [
    'Country-of-Origin Verification',
    'CCP Exposure Mapping',
    'Geopolitical Risk Assessment',
    'Domestic Alternative Sourcing',
    'OMB M-25-22 Compliance Support',
    'Legislative &amp; Regulatory Intelligence',
]
cap_first_words = [
    'Maps the actual manufacturing location',
    'Identifies pharmaceutical products',
    'Flags supply chains transiting',
    'For every flagged product',
    'Aligns with federal Made in America',
    'Monitors congressional activity',
]
for i, (num, title, fw) in enumerate(zip(cap_nums, cap_titles, cap_first_words)):
    r = f'<div style="font-family:var(--mono);font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);margin-bottom:0.5rem;">{num} - {title}</div>\n          <p style="font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.65;margin:0;">{fw}'
    n = f'<div style="font-family:var(--mono);font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;color:#00ACE6;margin-bottom:0.5rem;">{num} - {title}</div>\n          <p style="font-size:0.9375rem;color:#C8CDD3;font-weight:300;line-height:1.65;margin:0;">{fw}'
    if r in content: content = content.replace(r, n, 1); changes.append(f'CHG-037: TradeSpy cap {num}')

# Section 09 CTA dark: body text
r = '<p style="font-size:1.05rem;color:var(--ink-2);font-weight:300;line-height:1.75;margin-bottom:2.5rem;">Whether you need supply chain intelligence'
n = '<p style="font-size:1.05rem;color:#C8CDD3;font-weight:300;line-height:1.75;margin-bottom:2.5rem;">Whether you need supply chain intelligence'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov CTA body')

# Section 09 CTA: contact line
r = '<p style="font-family:var(--mono);font-size:0.8rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-3);">Direct contact: Tony Paquin, CEO - tony@iremedy.com</p>'
n = '<p style="font-family:var(--mono);font-size:0.875rem;letter-spacing:0.08em;text-transform:uppercase;color:#9CA3AF;">Direct contact: Tony Paquin, CEO - tony@iremedy.com</p>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov CTA contact line')

# Section 09 CTA: btn-ghost → btn-ghost-lt
r = '<button class="btn btn-ghost" onclick="showPage(\'contact\')">Discuss the Made in America Portfolio \u2192</button>'
n = '<button class="btn btn-ghost-lt" onclick="showPage(\'contact\')">Discuss the Made in America Portfolio \u2192</button>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-037: Gov CTA btn-ghost-lt')

# ==============================================================================
# 6. CHG-038 — NEWSROOM PAGE
# ==============================================================================

# Hero subheadline: var(--ink-2) → #C8CDD3
r = 'color:var(--ink-2);font-weight:300;line-height:1.7;max-width:680px;margin-bottom:0;">Press releases, The Supply Side podcast'
n = 'color:#C8CDD3;font-weight:300;line-height:1.7;max-width:680px;margin-bottom:0;">Press releases, The Supply Side podcast'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-038: Newsroom hero subheadline (INVISIBLE FIX)')

# Podcast callout: description on dark background
r = 'font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.65;margin:0 0 1.5rem;max-width:580px;">Healthcare supply chain policy, national security, reshoring'
n = 'font-size:0.9375rem;color:#C8CDD3;font-weight:300;line-height:1.65;margin:0 0 1.5rem;max-width:580px;">Healthcare supply chain policy, national security, reshoring'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-038: Podcast description (INVISIBLE FIX)')

# Podcast: btn-ghost on dark → btn-ghost-lt
r = '<a href="https://open.spotify.com/show/supplyside" target="_blank" class="btn btn-ghost" style="text-decoration:none;">Listen on Spotify \u2192</a>'
n = '<a href="https://open.spotify.com/show/supplyside" target="_blank" class="btn btn-ghost-lt" style="text-decoration:none;">Listen on Spotify \u2192</a>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-038: Podcast Spotify btn-ghost-lt')

# ==============================================================================
# 7. CHG-039 — ABOUT PAGE
# ==============================================================================

# Hero subheadline: var(--ink-2) → #C8CDD3
r = 'color:var(--ink-2);font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:0;">Founded in 2007.'
n = 'color:#C8CDD3;font-style:italic;font-weight:300;line-height:1.7;max-width:780px;margin-bottom:0;">Founded in 2007.'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-039: About hero subheadline (INVISIBLE FIX)')

# Anthony title: Chief AI Officer → Chief Intelligence Officer (About leadership section)
r = 'color:var(--teal);margin-bottom:1.25rem;">Chief AI Officer</div>\n          <p style="font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.75;margin-bottom:1rem;">Anthony leads iRemedy'
n = 'color:var(--teal);margin-bottom:1.25rem;">Chief Intelligence Officer</div>\n          <p style="font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.75;margin-bottom:1rem;">Anthony leads iRemedy'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-039: Anthony title → Chief Intelligence Officer (About)')

# Amanda placeholder: make italic
r = '<p style="font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.75;margin-bottom:1.25rem;">Bio to be provided.</p>'
n = '<p style="font-size:0.9375rem;color:var(--ink-2);font-style:italic;font-weight:300;line-height:1.75;margin-bottom:1.25rem;">Bio to be provided.</p>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-039: Amanda placeholder italic')

# Add Jim Harding card after Amanda — find anchor: the Board of Directors section comment
jim_harding_card = """
      <!-- Jim Harding -->
      <div style="display:grid;grid-template-columns:200px 1fr;gap:3rem;margin-bottom:4rem;align-items:start;max-width:960px;">
        <div>
          <div style="width:160px;height:160px;background:var(--ink);display:flex;align-items:center;justify-content:center;border:2px solid var(--rule);">
            <span style="font-family:var(--serif);font-size:2rem;font-weight:700;color:var(--ink-3);">JH</span>
          </div>
        </div>
        <div>
          <div style="font-family:var(--serif);font-size:1.5rem;font-weight:700;color:var(--ink);margin-bottom:0.25rem;">Jim Harding</div>
          <div style="font-family:var(--mono);font-size:0.75rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);margin-bottom:1.25rem;">Co-Inventor &amp; Technology Architect</div>
          <p style="font-size:0.9375rem;color:var(--ink-2);font-weight:300;line-height:1.75;margin-bottom:1rem;">Co-inventor of the MetaCommerceRx patent portfolio. Career spanning MS-DOS, Amazon Marketplace, and healthcare supply chain AI. Holds co-inventor credit on all 10 iRemedy granted U.S. patents.</p>
          <div style="font-family:var(--mono);font-size:0.8rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-3);line-height:2;">MS-DOS Co-Inventor &nbsp;·&nbsp; Amazon Marketplace &nbsp;·&nbsp; 10 U.S. Patents</div>
        </div>
      </div>

"""
anchor = '    </div>\n  </section>\n\n  <!-- SECTION 04 — BOARD OF DIRECTORS -->'
if anchor in content:
    content = content.replace(anchor, jim_harding_card + anchor, 1)
    changes.append('CHG-039: Added Jim Harding leadership card')

# Also fix Chief AI Officer in ldp-card (page-leadership hidden section)
r = '<div class="ldp-title">Chief AI Officer</div>'
n = '<div class="ldp-title">Chief Intelligence Officer</div>'
count = content.count(r)
if count > 0: content = content.replace(r, n); changes.append(f'CHG-039: ldp-title Chief AI→Intelligence ({count}x)')

# ==============================================================================
# 8. CHG-040 — CONTACT PAGE
# ==============================================================================

# Hero subheadline: var(--ink-2) → #C8CDD3
r = 'color:var(--ink-2);font-weight:300;line-height:1.7;max-width:680px;margin-bottom:0;">Whether you\'re a manufacturer exploring U.S. distribution'
n = 'color:#C8CDD3;font-weight:300;line-height:1.7;max-width:680px;margin-bottom:0;">Whether you\'re a manufacturer exploring U.S. distribution'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-040: Contact hero subheadline (INVISIBLE FIX)')

# Contact sidebar: Anthony title
r = 'Anthony Paquin, Chief AI Officer'
n = 'Anthony Paquin, Chief Intelligence Officer'
count = content.count(r)
if count > 0: content = content.replace(r, n); changes.append(f'CHG-040: Contact sidebar Anthony title ({count}x)')

# ==============================================================================
# 9. CHG-041 — TRADESPY PAGE
# ==============================================================================

# "The Doctrine" section → convert to dark
r = '  <!-- THE DOCTRINE -->\n  <div class="ts-section">'
n = '  <!-- THE DOCTRINE -->\n  <div class="ts-section ts-dark-section" style="background:#212E3E;">'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-041: Doctrine section → dark')

# Pull-quote: upgrade for dark background
r = '<div class="ts-pull-quote">Where is this actually made -<br>and can we prove it?</div>'
n = '<div class="ts-pull-quote" style="font-size:1.5rem;color:#00ACE6;border-color:#00ACE6;background:rgba(0,172,230,0.08);padding:1.25rem 1.75rem;">Where is this actually made -<br>and can we prove it?</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-041: Pull-quote upgrade')

# "Three Layers" section badge: red border highlight
r = '<div class="ts-badge">\u2190 Current System Visibility Ends Here</div>'
n = '<div class="ts-badge" style="border-color:#E53E3E;color:#E53E3E;border-top:2px solid #E53E3E;margin-top:1rem;">\u2190 Current System Visibility Ends Here</div>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-041: Badge red border')

# Fraud Detection section: add red border
r = '  <!-- FRAUD DETECTION -->\n  <div class="ts-section">'
n = '  <!-- FRAUD DETECTION -->\n  <div class="ts-section" style="border-left:4px solid #E53E3E;">'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-041: Fraud section red border')

# Pharma First (Live Today) section: already ts-dark-section, will get #212E3E from CSS
# Make the data bullets monospace styled per spec
# Currently ts-list li elements - will be handled by CSS
# Roadmap label colors on dark - handled by CSS

# ==============================================================================
# 10. TRADESPY HERO STAT NUMBERS — already visible (light bg), verify styling
# ==============================================================================
# ts-stat-n.red and .teal already colored, ts-stat-n has color:var(--ink) = dark readable on light
# No change needed for hero stats

# ==============================================================================
# 11. PLATFORM: add btn-ghost-lt where btn-ghost appears on dark sections
# ==============================================================================

# Platform hero: "See the Architecture" btn-ghost → btn-ghost-lt
r = '<button class="btn btn-ghost" onclick="document.getElementById(\'platform-arch\').scrollIntoView({behavior:\'smooth\'})">See the Architecture \u2193</button>'
n = '<button class="btn btn-ghost-lt" onclick="document.getElementById(\'platform-arch\').scrollIntoView({behavior:\'smooth\'})">See the Architecture \u2193</button>'
if r in content: content = content.replace(r, n, 1); changes.append('CHG-036: Platform hero btn-ghost-lt')

# ==============================================================================
# 12. Write output
# ==============================================================================

with open('/Users/berniemac/projects/iremedy-website-v9/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"SUCCESS: Applied {len(changes)} changes:")
for c in changes:
    print(f"  ✓ {c}")
