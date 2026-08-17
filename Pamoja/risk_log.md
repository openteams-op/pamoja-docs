# Risk Log

## Risk Assessment Scale

### Likelihood
| Score | Label          | Definition                         |
| ----- | -------------- | ---------------------------------- |
| 1     | Rare           | <5% chance in the project timeline |
| 2     | Unlikely       | 5-20% chance                       |
| 3     | Possible       | 20-50% chance                      |
| 4     | Likely         | 50-80% chance                      |
| 5     | Almost Certain | >80% chance                        |

### Impact
| Score | Label | Definition |
|---|---|---|
| 1 | Negligible | Minor inconvenience, easily absorbed |
| 2 | Minor | Some disruption, manageable with existing resources |
| 3 | Moderate | Significant disruption, requires dedicated effort to resolve |
| 4 | Major | Threatens timeline or budget materially |
| 5 | Critical | Threatens product viability or company reputation |

### Risk Score
**Risk Score = Likelihood × Impact**

| Score Range | Severity | Action |
|---|---|---|
| 1-4 | Low | Monitor |
| 5-9 | Medium | Plan mitigation, monitor regularly |
| 10-19 | High | Active mitigation required, escalate to stakeholders |
| 20-25 | Critical | Immediate action required, may require product pivot |

## Risk Register

### Market Risks

| ID | Risk | L | I | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
| R-001 | WhatsApp/Meta ships commerce (catalogs + payments) for Nigerian merchants before Pamoja owns the loop | 4 | 4 | 16 | Launch merchant toolkit fast (Phase 2 = launch wedge); build the closed loop (search → order → pay → receipt) WhatsApp can't offer; lean on the channel graph as the differentiator | Emphasize the unified-search + graph moat in marketing; accelerate FEAT-005 verification as the trust answer | Product Manager |
| R-002 | Cold start: early users see an empty graph and don't return | 4 | 5 | 20 | City/market-density launch (Lagos + Onitsha/Aba pilot, not national); merchant pull mechanics — each merchant onboarded with at least their top 5 customers; invite rewards | Concentrate growth spend on one market cluster until density; run "connect your trader" onboarding drives | Head of Growth |
| R-003 | A local fintech (OPay, Moniepoint, Paga) adds chat/storefronts and undercuts with an existing user base | 3 | 4 | 12 | Track competitor feature releases monthly; defend on the channel model + intent search, which none offer; move fast on merchant toolkit depth | Differentiate on graph-based commerce; explore corridor partnerships rather than head-on price wars | Product Manager |
| R-004 | Merchant tier conversion (target >10%) fails — traders won't pay ₦2,000/month | 3 | 3 | 9 | Free tier delivers real value first (20 products, basic checkout); trial upgrade for first cohort; analytics as the credit-proof hook Ada already lacks | Reduce price, add annual discount, or gate a single high-value feature (verification) as a paid-only wedge | Product Manager |

### Technical Risks

| ID | Risk | L | I | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
| R-005 | Payment idempotency failure — a replayed or retried transfer double-debits a user | 2 | 5 | 10 | Idempotency keys on every wallet mutation (per [[architecture]]); strict atomic settlement; chaos-test replay scenarios before launch | Immediate ledger reconciliation run; support refund flow; freeze affected wallet until resolution | Tech Lead |
| R-006 | Payment partner downtime, fee change, or KYC rule shift blocks money movement | 3 | 4 | 12 | Partner-rail abstraction with per-market failover to a second licensed partner; contract reviews quarterly; monitor partner SLAs | Switch traffic to fallback partner; surface degraded-mode notices in-app | Partnerships Lead |
| R-007 | Graph privacy boundary breached — a merchant sees buyer data they shouldn't, breaking the "no CRM wall" promise | 2 | 5 | 10 | Server-side visibility enforcement (never client-side); permissions model in Identity & Graph per [[architecture]]; penetration tests on visibility rules | Revoke access, notify affected users, publish incident report; tighten rules with a compliance review | Tech Lead |
| R-008 | Search relevance is poor at launch — intent classification ("buy shoes" vs "afrobeats") returns weak results | 3 | 3 | 9 | Start with deterministic keyword + name/bio matching, not ML; ship grouped results; instrument query → click metrics; iterate relevance before adding more signals | Restrict v1 search scope to high-confidence matches; ship FEAT-024 filters early to compensate | Tech Lead |
| R-009 | Data-light and offline behavior fail on cheap Android — the primary persona's device | 4 | 3 | 12 | Test on low-end device lab before launch; measure payloads in data-light mode; design offline queueing from day one per [[features]] FEAT-030 | Ship a "lite" variant or reduce media fidelity; cache aggressively; prioritize low-data fixes in post-launch sprints | Engineering Manager |

### Operational Risks

| ID | Risk | L | I | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
| R-010 | Launch scope (16 P0s, 32 total) slips timeline | 4 | 3 | 12 | Feature freeze dates; P0-only launch scope; weekly scope review; the roadmap's module phasing isolates slippage to one module | Cut P1s from the launch window; extend timeline with stakeholder approval | Product Manager |
| R-011 | Scam/fraud epidemic (SIM swap, fake vendors) poisons trust in the network | 4 | 4 | 16 | FEAT-029 block/report from day one; merchant verification (FEAT-005) fast-tracked for high-risk categories; fraud team with partner's AML feed; educate merchants on scam patterns | Emergency freeze of flagged accounts; public trust campaign; tighten KYC via partner; expand review queue staffing | Head of Trust & Safety |
| R-012 | Key technical contributor departure stalls the build | 2 | 4 | 8 | Document architecture decisions in [[architecture]]; no single-owner knowledge; pairing and knowledge-sharing; funded team can backfill faster | Pause non-critical modules; hire/contract for critical path; re-sequence roadmap | Engineering Manager |

### Legal & Compliance Risks

| ID | Risk | L | I | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
| R-013 | CBN regulatory shift (agent banking, e-money, KYC/AML thresholds) changes the partner-first model | 3 | 4 | 12 | Partner contract includes regulatory-change clauses; monitor CBN circulars monthly; keep licensing option open for the future | Adjust to partner's revised compliance; explore licensing if the model breaks; legal review of any re-shape | Legal / Compliance |
| R-014 | Regulatory fragmentation across expansion markets (NDPR doesn't extend beyond Nigeria) | 3 | 4 | 12 | Per-market legal review before each launch; region-per-market data locality per [[architecture]]; partner handles local compliance per market | Delay a market rather than launch non-compliant; scope the first corridor (UK→NG) to two well-understood jurisdictions | Legal / Compliance |

### Financial Risks

| ID | Risk | L | I | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
| R-015 | Currency volatility erodes the multi-currency wallet's economics | 3 | 4 | 12 | Partner-managed FX with transparent spread; corridor fees (2.5%) include a volatility buffer; limit held balances in volatile currencies | Adjust corridor spread within disclosed range; pause conversion during extreme volatility; communicate clearly | CFO / Payments Lead |
| R-016 | Free P2P + low take rates delay break-even longer than funding runway | 3 | 3 | 9 | Track GMV and take-rate metrics weekly; merchant conversion target >10%; introduce advertising only after density (per [[monetization]]) | Accelerate Merchant tier adoption; raise transaction fee with notice; revisit runway with stakeholders | CFO |

## Risk Trends

| Date | Change | Risk ID | Description |
|---|---|---|---|
| 2026-08-17 | Registered | All | Initial risk assessment created from the SWOT in [[README]], informed by [[architecture]] and [[monetization]] |

## Review Cadence

- **Weekly:** Review all High and Critical risks (score ≥ 10) in team standup — currently R-001, R-002, R-003, R-005, R-006, R-007, R-009, R-010, R-011, R-013, R-014, R-015
- **Monthly:** Full risk register review with stakeholders
- **Per Milestone:** Re-assess all risks before each roadmap phase begins ([[roadmap]])
- **On Threat Events:** The moment a competitor (R-001/R-003), regulator (R-013/R-014), or fraud wave (R-011) materializes, re-score that risk same week