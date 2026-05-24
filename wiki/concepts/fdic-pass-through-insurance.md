---
type: concept
slug: fdic-pass-through-insurance
canonical_name: FDIC Pass-Through Insurance
domains:
  - condo-software
---

# FDIC Pass-Through Insurance

## Summary

FDIC pass-through insurance is the mechanism by which a single customer's deposit, placed via an intermediary into multiple FDIC-insured banks, retains insurance coverage at each underlying bank up to the standard $250,000 per-bank maximum rather than being capped at $250,000 in aggregate [[sources/web-2008-01-01-0ad]]. The per-bank maximum is referred to in network-deposit disclosures as the Standard Maximum Deposit Insurance Amount (SMDIA) [[sources/web-2026-01-01-21d]].

## Key claims

- The standard FDIC insurance maximum is $250,000 per insured bank [[sources/web-2008-01-01-0ad]], referred to in IntraFi-network disclosures as the SMDIA [[sources/web-2026-01-01-21d]].
- When a large customer deposit is placed through a network service such as ICS or CDARS, the deposit is divided into amounts under $250,000 and placed in accounts at multiple participating banks so that each tranche stays within the per-bank insurance limit [[sources/web-2008-01-01-0ad]].
- Pass-through coverage is not automatic; certain conditions must be satisfied for pass-through FDIC deposit insurance to apply [[sources/web-2008-01-01-0ad]].
- The intermediary service operator (e.g., IntraFi) is not itself an FDIC-insured bank; insurance covers failure of the underlying network banks where funds are actually held [[sources/web-2008-01-01-0ad]].
- Pass-through structures allow depositors to access millions of dollars of aggregate FDIC insurance while maintaining a single customer-facing institutional relationship [[sources/web-2008-01-01-0ad]].
- A depositor's balances at the institution that places network deposits may exceed the SMDIA before settlement for deposits or after settlement for withdrawals, creating a transient uninsured window at the placing institution itself [[sources/web-2026-01-01-21d]].
- If the placing institution is not itself an FDIC-insured bank, balances held there may be entirely uninsured; the depositor must make any necessary arrangements to protect such balances consistent with applicable law [[sources/web-2026-01-01-21d]].
- The depositor is also responsible for determining whether placement through CDARS or ICS satisfies any legal restrictions on its own deposits [[sources/web-2026-01-01-21d]].

## Sources

- [[sources/web-2008-01-01-0ad]] — IntraFi product page describing ICS and CDARS
- [[sources/web-2026-01-01-21d]] — Alliance Association Bank HOA ICS and CDARS product page

## Related

- [[entities/intrafi]]
- [[entities/ics-intrafi-cash-service]]
- [[entities/cdars]]
- [[entities/alliance-association-bank]]
- [[concepts/network-deposit-placement]]
- [[concepts/reciprocal-deposits]]
