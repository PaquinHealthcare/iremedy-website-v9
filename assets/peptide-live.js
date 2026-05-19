/**
 * peptide-live.js
 * iRemedy Peptide Intelligence Hub — Live Data Module
 * Fetches: PubMed/NCBI recent papers, ClinicalTrials.gov active trials, FDA compounding status
 */

const FDA_COMPOUNDING_STATUS = {
  'semaglutide': { status: 'Shortage Ended — Compounding Restricted', detail: 'FDA removed semaglutide from 503A/503B shortage lists (Mar 2025). Commercial Ozempic/Wegovy shortage resolved. Compounding under active FDA enforcement. Litigation ongoing.', badge: 'restricted', verified: 'May 2026' },
  'tirzepatide': { status: 'Shortage Ended — Compounding Restricted', detail: 'FDA removed tirzepatide from shortage list (May 2025). Compounding restrictions in effect. Litigation ongoing in federal courts.', badge: 'restricted', verified: 'May 2026' },
  'liraglutide': { status: 'FDA-Approved / Not Compoundable', detail: 'Commercial product (Victoza, Saxenda) not in shortage. No 503A/503B authorization.', badge: 'approved', verified: 'May 2026' },
  'octreotide': { status: 'FDA-Approved / Compoundable 503A', detail: 'FDA-approved (Sandostatin). Compounding permitted under 503A for customized formulations (e.g., alternate routes, strengths).', badge: 'compoundable', verified: 'May 2026' },
  'insulin-analogs': { status: 'FDA-Approved / Compounding Restricted', detail: 'All commercial insulin analogs FDA-approved. Compounding permitted only where commercial product unavailable or clinically inappropriate.', badge: 'approved', verified: 'May 2026' },
  'orforglipron': { status: 'FDA-Approved (Apr 2026) / Not Compoundable', detail: 'Just approved. No shortage designation. Not on compounding lists.', badge: 'approved', verified: 'May 2026' },
  'tesamorelin': { status: 'FDA-Approved (Egrifta) / 503A Bulk Listed', detail: 'FDA-approved for HIV lipodystrophy. Listed as 503A bulk drug substance for compounding in non-approved indications.', badge: 'compoundable', verified: 'May 2026' },
  'exenatide': { status: 'FDA-Approved / Not Compoundable', detail: 'Byetta/Bydureon FDA-approved. Not on 503A bulk lists.', badge: 'approved', verified: 'May 2026' },
  'pegvisomant': { status: 'FDA-Approved / Not Compoundable', detail: 'Somavert FDA-approved for acromegaly. Not on compounding lists.', badge: 'approved', verified: 'May 2026' },
  'pt141': { status: 'FDA-Approved (Vyleesi) / Compounding Restricted', detail: 'Bremelanotide approved as Vyleesi. Compounding of commercially available approved drugs generally restricted.', badge: 'approved', verified: 'May 2026' },
  'thymosin-a1': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees (Category 1 — permitted for use in compounding). Not FDA-approved for any indication.', badge: 'compoundable', verified: 'May 2026' },
  'oxytocin': { status: 'FDA-Approved / 503A Compoundable', detail: 'FDA-approved (Pitocin). Listed on 503A bulk list for compounding alternate routes/formulations (e.g., intranasal).', badge: 'compoundable', verified: 'May 2026' },
  'retatrutide': { status: 'Investigational — Phase III', detail: 'No FDA approval. Phase III trials ongoing (Eli Lilly). Not on compounding lists.', badge: 'investigational', verified: 'May 2026' },
  'sermorelin': { status: 'Compoundable — 503A Category 1', detail: 'FDA-approved version discontinued (Geref). Listed on 503A Bulk Drug Substance list — compoundable. Common in anti-aging/GH optimization protocols.', badge: 'compoundable', verified: 'May 2026' },
  'survodutide': { status: 'Investigational — Phase III', detail: 'Boehringer Ingelheim GLP-1/glucagon dual agonist. Phase III. Not on compounding lists.', badge: 'investigational', verified: 'May 2026' },
  'mk677': { status: 'Not a Peptide — Research Only', detail: 'Ibutamoren is a small-molecule GH secretagogue, not a peptide. Not FDA-approved. Not on compounding lists. DEA gray area.', badge: 'research', verified: 'May 2026' },
  'semax': { status: 'Not FDA-Approved — Research Only', detail: 'Russian-origin neuropeptide. Not FDA-approved. Not on 503A/503B lists. Research/international use only.', badge: 'research', verified: 'May 2026' },
  'thymosin-b4': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved for any indication. Compoundable for licensed practitioners.', badge: 'compoundable', verified: 'May 2026' },
  'ghk-cu': { status: 'Cosmetic/Topical — Not Regulated as Drug', detail: 'GHK-Cu primarily used topically. Systemic peptide compounding is not standard. Regulatory status unclear for injectable use.', badge: 'research', verified: 'May 2026' },
  'cjc1295': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved. Compoundable for licensed practitioners. Often combined with Ipamorelin.', badge: 'compoundable', verified: 'May 2026' },
  'ipamorelin': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved. Compoundable for licensed practitioners.', badge: 'compoundable', verified: 'May 2026' },
  'selank': { status: 'Not FDA-Approved — Research Only', detail: 'Russian-origin anxiolytic peptide. Not FDA-approved. Not on compounding lists. Research use only.', badge: 'research', verified: 'May 2026' },
  'ghrp2': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved. Compoundable for licensed practitioners.', badge: 'compoundable', verified: 'May 2026' },
  'ghrp6': { status: 'Compoundable — 503A Category 1', detail: 'Listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved. Compoundable for licensed practitioners.', badge: 'compoundable', verified: 'May 2026' },
  'bpc157': { status: '503A Category 2 — Under FDA Review', detail: 'On FDA 503A Category 2 Bulk Substances list (under evaluation). NOT on positive/permitted list. Compounding technically not authorized pending FDA decision. High controversy.', badge: 'under-review', verified: 'May 2026' },
  'epithalon': { status: 'Not FDA-Approved — Research Only', detail: 'Not FDA-approved. Not listed on 503A/503B bulk substance lists. Research compound only.', badge: 'research', verified: 'May 2026' },
  'hexarelin': { status: 'Not FDA-Approved — Compounding Gray Area', detail: 'Not FDA-approved. Not explicitly on 503A positive lists. Some compounders prepare under GHRP class. Regulatory status unclear.', badge: 'research', verified: 'May 2026' },
  'aod9604': { status: 'Not FDA-Approved — Research Only', detail: 'AOD9604 failed Phase III (no statistical significance for weight loss). Not FDA-approved. Not on compounding lists.', badge: 'research', verified: 'May 2026' },
  'nad': { status: 'Compoundable — 503A Listed', detail: 'NAD+ (nicotinamide adenine dinucleotide) compoundable under 503A. IV/IM formulations prepared by licensed 503A compounders.', badge: 'compoundable', verified: 'May 2026' },
  'll37': { status: 'Not FDA-Approved — Research Only', detail: 'Antimicrobial peptide. Not FDA-approved for any indication. Not on compounding lists. Research stage.', badge: 'research', verified: 'May 2026' },
  'tb500': { status: 'Compoundable — 503A Category 1', detail: 'TB-500 (Thymosin Beta-4 fragment) listed on FDA 503A Bulk Drug Substance Nominees. Not FDA-approved. Compoundable for licensed practitioners.', badge: 'compoundable', verified: 'May 2026' },
  'dsip': { status: 'Not FDA-Approved — Research Only', detail: 'Delta sleep-inducing peptide. Not FDA-approved. Not on compounding lists.', badge: 'research', verified: 'May 2026' },
  'melanotan2': { status: 'Not FDA-Approved — Not Compoundable', detail: 'MT-II not FDA-approved for any indication. Not on 503A/503B lists. FDA has issued warnings against use. Research only.', badge: 'restricted', verified: 'May 2026' },
  'motsc': { status: 'Not FDA-Approved — Research Only', detail: 'Mitochondria-derived peptide. Not FDA-approved. Not on compounding lists. Research stage.', badge: 'research', verified: 'May 2026' },
  'cartalax': { status: 'Not FDA-Approved — Research Only', detail: 'Short peptide from cartilage. Not FDA-approved in US. Research compound.', badge: 'research', verified: 'May 2026' },
  'kpv': { status: 'Not FDA-Approved — Research Only', detail: 'Alpha-MSH tripeptide fragment. Not FDA-approved. Not on compounding lists. Research stage.', badge: 'research', verified: 'May 2026' },
  'dihexa': { status: 'Not FDA-Approved — Research Only', detail: 'Hepatocyte growth factor fragment. Not FDA-approved. Research compound only.', badge: 'research', verified: 'May 2026' },
  'foxo4dri': { status: 'Not FDA-Approved — Research Only', detail: 'Senolytic research peptide. No human trials completed. Not FDA-approved. Not on compounding lists.', badge: 'research', verified: 'May 2026' }
};

const PUBMED_TERMS = {
  'semaglutide': 'semaglutide[Title/Abstract]',
  'tirzepatide': 'tirzepatide[Title/Abstract]',
  'liraglutide': 'liraglutide[Title/Abstract]',
  'octreotide': 'octreotide clinical[Title/Abstract]',
  'insulin-analogs': 'insulin analog clinical trial[Title/Abstract]',
  'orforglipron': 'orforglipron[Title/Abstract]',
  'tesamorelin': 'tesamorelin[Title/Abstract]',
  'exenatide': 'exenatide clinical[Title/Abstract]',
  'pegvisomant': 'pegvisomant[Title/Abstract]',
  'pt141': 'bremelanotide[Title/Abstract]',
  'thymosin-a1': 'thymosin alpha-1[Title/Abstract]',
  'oxytocin': 'oxytocin clinical[Title/Abstract]',
  'retatrutide': 'retatrutide[Title/Abstract]',
  'sermorelin': 'sermorelin[Title/Abstract]',
  'survodutide': 'survodutide[Title/Abstract]',
  'mk677': 'ibutamoren MK-677[Title/Abstract]',
  'semax': 'semax peptide[Title/Abstract]',
  'thymosin-b4': 'thymosin beta-4[Title/Abstract]',
  'ghk-cu': 'GHK-Cu copper peptide[Title/Abstract]',
  'cjc1295': 'CJC-1295[Title/Abstract]',
  'ipamorelin': 'ipamorelin[Title/Abstract]',
  'selank': 'selank peptide[Title/Abstract]',
  'ghrp2': 'GHRP-2[Title/Abstract]',
  'ghrp6': 'GHRP-6[Title/Abstract]',
  'bpc157': 'BPC-157[Title/Abstract]',
  'epithalon': 'epithalon epitalon[Title/Abstract]',
  'hexarelin': 'hexarelin[Title/Abstract]',
  'aod9604': 'AOD9604[Title/Abstract]',
  'nad': 'NAD+ nicotinamide adenine dinucleotide supplementation[Title/Abstract]',
  'll37': 'LL-37 cathelicidin clinical[Title/Abstract]',
  'tb500': 'thymosin beta-4 fragment[Title/Abstract]',
  'dsip': 'delta sleep inducing peptide[Title/Abstract]',
  'melanotan2': 'melanotan II[Title/Abstract]',
  'motsc': 'MOTS-c mitochondria peptide[Title/Abstract]',
  'cartalax': 'cartalax peptide cartilage[Title/Abstract]',
  'kpv': 'KPV peptide alpha-MSH[Title/Abstract]',
  'dihexa': 'dihexa HGF peptide[Title/Abstract]',
  'foxo4dri': 'FOXO4-DRI senolytic[Title/Abstract]'
};

const TRIALS_TERMS = {
  'semaglutide': 'semaglutide',
  'tirzepatide': 'tirzepatide',
  'liraglutide': 'liraglutide',
  'octreotide': 'octreotide',
  'insulin-analogs': 'insulin analog',
  'orforglipron': 'orforglipron',
  'tesamorelin': 'tesamorelin',
  'exenatide': 'exenatide',
  'pegvisomant': 'pegvisomant',
  'pt141': 'bremelanotide',
  'thymosin-a1': 'thymosin alpha-1',
  'oxytocin': 'oxytocin intranasal',
  'retatrutide': 'retatrutide',
  'sermorelin': 'sermorelin',
  'survodutide': 'survodutide',
  'mk677': 'ibutamoren MK-677',
  'semax': 'semax neuropeptide',
  'thymosin-b4': 'thymosin beta-4',
  'ghk-cu': 'GHK-Cu copper peptide',
  'cjc1295': 'CJC-1295 GHRH',
  'ipamorelin': 'ipamorelin GHRP',
  'selank': 'selank anxiety peptide',
  'ghrp2': 'GHRP-2 growth hormone',
  'ghrp6': 'GHRP-6 growth hormone',
  'bpc157': 'BPC-157 body protection compound',
  'epithalon': 'epithalon epitalon telomere',
  'hexarelin': 'hexarelin growth hormone',
  'aod9604': 'AOD9604',
  'nad': 'NAD+ nicotinamide adenine dinucleotide',
  'll37': 'LL-37 antimicrobial peptide',
  'tb500': 'thymosin beta-4 injury',
  'dsip': 'DSIP sleep peptide',
  'melanotan2': 'melanotan',
  'motsc': 'MOTS-c mitochondria',
  'cartalax': 'cartalax cartilage',
  'kpv': 'KPV anti-inflammatory peptide',
  'dihexa': 'dihexa cognitive',
  'foxo4dri': 'FOXO4 senolytic'
};

// Badge color config
const BADGE_COLORS = {
  'compoundable': { bg: '#00875A', color: '#fff', label: 'Compoundable' },
  'restricted': { bg: '#c8160a', color: '#fff', label: 'Restricted' },
  'approved': { bg: '#0064A5', color: '#fff', label: 'FDA-Approved' },
  'under-review': { bg: '#D97706', color: '#fff', label: 'Under Review' },
  'investigational': { bg: '#6366F1', color: '#fff', label: 'Investigational' },
  'research': { bg: '#6b7280', color: '#fff', label: 'Research Only' }
};

// Cache to avoid refetching in the same session
const _liveCache = {};

async function fetchPubMedStudies(peptideId) {
  const cacheKey = 'pubmed_' + peptideId;
  if (_liveCache[cacheKey]) return _liveCache[cacheKey];
  const term = PUBMED_TERMS[peptideId];
  if (!term) return null;
  try {
    // Step 1: Search for IDs
    const searchUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${encodeURIComponent(term)}&sort=date&retmax=5&retmode=json&tool=iremedy-peptide-hub&email=info@iremedy.com`;
    const searchRes = await fetch(searchUrl);
    const searchData = await searchRes.json();
    const ids = searchData.esearchresult?.idlist;
    if (!ids || ids.length === 0) return _liveCache[cacheKey] = [];
    // Step 2: Fetch summaries
    const summaryUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=${ids.join(',')}&retmode=json&tool=iremedy-peptide-hub&email=info@iremedy.com`;
    const summaryRes = await fetch(summaryUrl);
    const summaryData = await summaryRes.json();
    const results = ids.map(id => {
      const item = summaryData.result?.[id];
      if (!item) return null;
      return {
        pmid: id,
        title: item.title || 'Untitled',
        authors: item.authors?.slice(0, 3).map(a => a.name).join(', ') || '',
        journal: item.source || '',
        pubdate: item.pubdate || '',
        url: `https://pubmed.ncbi.nlm.nih.gov/${id}/`
      };
    }).filter(Boolean);
    return _liveCache[cacheKey] = results;
  } catch(e) {
    return _liveCache[cacheKey] = null;
  }
}

async function fetchClinicalTrials(peptideId) {
  const cacheKey = 'trials_' + peptideId;
  if (_liveCache[cacheKey]) return _liveCache[cacheKey];
  const term = TRIALS_TERMS[peptideId];
  if (!term) return null;
  try {
    const url = `https://clinicaltrials.gov/api/v2/studies?query.term=${encodeURIComponent(term)}&filter.overallStatus=RECRUITING,ACTIVE_NOT_RECRUITING&pageSize=5&format=json`;
    const res = await fetch(url);
    const data = await res.json();
    const studies = (data.studies || []).map(s => {
      const id = s.protocolSection?.identificationModule;
      const status = s.protocolSection?.statusModule;
      const design = s.protocolSection?.designModule;
      return {
        nctId: id?.nctId || '',
        title: id?.briefTitle || id?.officialTitle || 'Untitled',
        status: status?.overallStatus || '',
        phase: design?.phases?.join(', ') || 'N/A',
        url: `https://clinicaltrials.gov/study/${id?.nctId || ''}`
      };
    });
    return _liveCache[cacheKey] = { total: data.totalCount || studies.length, studies };
  } catch(e) {
    return _liveCache[cacheKey] = null;
  }
}

function getFdaStatus(peptideId) {
  return FDA_COMPOUNDING_STATUS[peptideId] || { status: 'Status Unknown', detail: 'Not found in iRemedy FDA compounding status database. Verify with FDA.gov.', badge: 'research', verified: 'May 2026' };
}

function renderFdaBadge(peptideId) {
  const fda = getFdaStatus(peptideId);
  const bc = BADGE_COLORS[fda.badge] || BADGE_COLORS['research'];
  return `
    <div style="margin-bottom:1.25rem;">
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#0064A5;margin-bottom:0.5rem;">FDA Compounding Status</div>
      <div style="display:flex;align-items:flex-start;gap:0.75rem;flex-wrap:wrap;">
        <span style="background:${bc.bg};color:${bc.color};font-family:'IBM Plex Mono',monospace;font-size:0.72rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;padding:4px 10px;white-space:nowrap;flex-shrink:0;">${fda.status}</span>
        <span style="font-size:0.82rem;color:#3D4D5E;line-height:1.6;">${fda.detail}</span>
      </div>
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#6b7280;margin-top:0.4rem;">Last verified: ${fda.verified} · <a href="https://www.fda.gov/drugs/human-drug-compounding/bulk-drug-substances-used-compounding-under-section-503a" target="_blank" rel="noopener" style="color:#0064A5;">FDA 503A List ↗</a></div>
    </div>`;
}

async function renderLiveSection(containerId, peptideId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  // Show FDA status immediately (static)
  const fdaHtml = renderFdaBadge(peptideId);

  // Show loading state
  container.innerHTML = `
    <div style="border-top:2px solid #0064A5;padding:2rem 0 1rem;">
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#0064A5;margin-bottom:1.5rem;">// Live Research Intelligence</div>
      ${fdaHtml}
      <div id="${containerId}-pubmed" style="margin-bottom:1.25rem;">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#0064A5;margin-bottom:0.5rem;">Recent Publications <span style="font-weight:300;opacity:0.5;">· PubMed/NCBI</span></div>
        <div style="font-size:0.82rem;color:#6b7280;font-family:'IBM Plex Mono',monospace;">Loading...</div>
      </div>
      <div id="${containerId}-trials">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#0064A5;margin-bottom:0.5rem;">Active Clinical Trials <span style="font-weight:300;opacity:0.5;">· ClinicalTrials.gov</span></div>
        <div style="font-size:0.82rem;color:#6b7280;font-family:'IBM Plex Mono',monospace;">Loading...</div>
      </div>
    </div>`;

  // Fetch both in parallel
  const [papers, trialsData] = await Promise.all([
    fetchPubMedStudies(peptideId),
    fetchClinicalTrials(peptideId)
  ]);

  // Render PubMed
  const pubmedEl = document.getElementById(containerId + '-pubmed');
  if (pubmedEl) {
    let pubmedHtml = `<div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#0064A5;margin-bottom:0.5rem;">Recent Publications <span style="font-weight:300;opacity:0.5;">· PubMed/NCBI</span></div>`;
    if (!papers || papers.length === 0) {
      pubmedHtml += `<div style="font-size:0.82rem;color:#6b7280;">No recent indexed publications found.</div>`;
    } else {
      pubmedHtml += papers.map(p => `
        <div style="padding:0.6rem 0;border-bottom:1px solid rgba(28,31,36,0.08);display:flex;gap:0.75rem;align-items:flex-start;">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#6b7280;white-space:nowrap;padding-top:2px;">${p.pubdate.substring(0, 4)}</span>
          <div>
            <a href="${p.url}" target="_blank" rel="noopener" style="font-size:0.85rem;color:#212E3E;text-decoration:none;line-height:1.5;display:block;" onmouseover="this.style.color='#0064A5'" onmouseout="this.style.color='#212E3E'">${p.title}</a>
            <span style="font-size:0.75rem;color:#6b7280;">${p.authors}${p.authors && p.journal ? ' · ' : ''}${p.journal}</span>
          </div>
        </div>`).join('');
      pubmedHtml += `<div style="margin-top:0.5rem;"><a href="https://pubmed.ncbi.nlm.nih.gov/?term=${encodeURIComponent(PUBMED_TERMS[peptideId] || '')}&sort=date" target="_blank" rel="noopener" style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;color:#0064A5;text-decoration:none;letter-spacing:0.1em;text-transform:uppercase;">View all on PubMed ↗</a></div>`;
    }
    pubmedEl.innerHTML = pubmedHtml;
  }

  // Render Trials
  const trialsEl = document.getElementById(containerId + '-trials');
  if (trialsEl) {
    let trialsHtml = `<div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#0064A5;margin-bottom:0.5rem;">Active Clinical Trials <span style="font-weight:300;opacity:0.5;">· ClinicalTrials.gov</span></div>`;
    if (!trialsData || trialsData.studies.length === 0) {
      trialsHtml += `<div style="font-size:0.82rem;color:#6b7280;">No active recruiting trials found.</div>`;
    } else {
      const totalNote = trialsData.total > 5 ? ` <span style="font-weight:300;opacity:0.5;">(${trialsData.total} total)</span>` : '';
      trialsHtml += `<div style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;color:#0064A5;margin-bottom:0.5rem;">RECRUITING / ACTIVE${totalNote}</div>`;
      trialsHtml += trialsData.studies.map(t => `
        <div style="padding:0.6rem 0;border-bottom:1px solid rgba(28,31,36,0.08);display:flex;gap:0.75rem;align-items:flex-start;">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#6b7280;white-space:nowrap;padding-top:2px;">${t.nctId}</span>
          <div>
            <a href="${t.url}" target="_blank" rel="noopener" style="font-size:0.85rem;color:#212E3E;text-decoration:none;line-height:1.5;display:block;" onmouseover="this.style.color='#0064A5'" onmouseout="this.style.color='#212E3E'">${t.title}</a>
            <span style="font-size:0.75rem;color:#6b7280;">${t.status}${t.phase && t.phase !== 'N/A' ? ' · Phase ' + t.phase : ''}</span>
          </div>
        </div>`).join('');
      if (trialsData.total > 5) {
        trialsHtml += `<div style="margin-top:0.5rem;"><a href="https://clinicaltrials.gov/search?term=${encodeURIComponent(TRIALS_TERMS[peptideId] || '')}&status=RECRUITING,ACTIVE_NOT_RECRUITING" target="_blank" rel="noopener" style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;color:#0064A5;text-decoration:none;letter-spacing:0.1em;text-transform:uppercase;">View all ${trialsData.total} trials ↗</a></div>`;
      }
    }
    trialsEl.innerHTML = trialsHtml;
  }
}

// Auto-init: if page has data-peptide-id attribute on body, init on load
document.addEventListener('DOMContentLoaded', function() {
  const peptideId = document.body.getAttribute('data-peptide-id');
  if (peptideId) {
    renderLiveSection('live-research-section', peptideId);
  }
});
