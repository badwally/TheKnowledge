---
type: concept
slug: network-deposit-placement
canonical_name: Network Deposit Placement
domains:
  - condo-software
---

# Network Deposit Placement

## Summary

Network deposit placement is an architecture in which a depositor's funds are placed across a network of participating banks through a single customer-facing financial institution, allowing the depositor to access FDIC insurance at multiple institutions without maintaining direct relationships with each [[sources/web-2008-01-01-0ad]].

## Key claims

- A depositor can work directly with one institution to place funds while accessing FDIC insurance through multiple banks in the network [[sources/web-2008-01-01-0ad]].
- The depositor receives an online dashboard and detailed reporting from the local bank relationship, providing visibility into where funds are held at all times [[sources/web-2008-01-01-0ad]].
- The architecture removes the need for the depositor to manage multiple bank relationships directly [[sources/web-2008-01-01-0ad]].
- IntraFi's network supports both ICS (demand deposit and money market deposit accounts) and CDARS (certificates of deposit) using the same underlying network of participating banks [[sources/web-2008-01-01-0ad]].
- The network is positioned as an alternative to collateralized deposits, letters of credit, private insurance, short-term bond funds, and money market mutual fund sweeps for cash management [[sources/web-2008-01-01-0ad]].
- The depositor retains the right to exclude specific network banks from eligibility to receive its funds, allowing for counterparty-screening overlays on top of the placement service [[sources/web-2026-01-01-21d]].
- Placement is governed by terms, conditions, and disclosures in agreements between the depositor and the placing institution, and the depositor must determine whether placement satisfies any restrictions on its deposits [[sources/web-2026-01-01-21d]].
- The network is offered to community associations through bank partners such as Alliance Association Bank, which applies the placement architecture to HOA, CID, and PUD funds [[sources/web-2026-01-01-21d]].

## Sources

- [[sources/web-2008-01-01-0ad]] — IntraFi product page describing ICS and CDARS
- [[sources/web-2026-01-01-21d]] — Alliance Association Bank HOA ICS and CDARS product page

## Related

- [[entities/intrafi]]
- [[entities/ics-intrafi-cash-service]]
- [[entities/cdars]]
- [[entities/alliance-association-bank]]
- [[concepts/fdic-pass-through-insurance]]
- [[concepts/reciprocal-deposits]]
