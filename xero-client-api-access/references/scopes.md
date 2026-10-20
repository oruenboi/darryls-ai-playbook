# Scope selection

Source: https://developer.xero.com/documentation/guides/oauth2/scopes/

Registry reviewed 2026-09-15. Verify the current portal and official documentation before new grants: scopes and app entitlements change. The script's known-scope registry is validation support, not the desired grant for every client. Extend it only from current official evidence if a needed scope is absent.

| Purpose | Scope family |
| --- | --- |
| Persistent refresh | offline_access |
| Organisation identity and settings | accounting.settings.read or accounting.settings |
| Contacts | accounting.contacts.read or accounting.contacts |
| Invoices and related documents | accounting.invoices.read or accounting.invoices |
| Payments | accounting.payments.read or accounting.payments |
| Bank transactions | accounting.banktransactions.read or accounting.banktransactions |
| Manual journals | accounting.manualjournals.read or accounting.manualjournals |
| Attachments | accounting.attachments.read or accounting.attachments |
| Files, fixed assets, projects | files.read/assets.read/projects.read or files/assets/projects |
| Budgets | accounting.budgets.read |
| Reports | accounting.reports.<report>.read |

For read-only work choose matching read variants. For explicit broad accounting write access, select management variants for the needed families, together with relevant reports and offline access. Avoid asking for redundant read variants when management already covers them. Present the real consent screen's descriptions before any required grant confirmation.

Common report suffixes: aged, balancesheet, banksummary, budgetsummary, executivesummary, profitandloss, trialbalance, taxreports. US-specific tenninetynine and payroll scopes are jurisdiction/use-case choices, not defaults for every client. Projects/assets/files may depend on available services. Budget/report access may be read-only even when the user requests maximum write access.

Do not request deprecated broad accounting.transactions or accounting.reports.read for a new granular-scope app by habit. Do not claim the general Journals API is available because manual-journal scope exists. Check current app eligibility for restricted APIs. Settings management is not equivalent to unrestricted user administration.

Verify returned token scope names after refresh and report exact gaps. Successful Organisation GET proves that endpoint and tenant identity; it does not prove every invoice, payroll, report or write operation. Later business actions use the selected tenant and their own task authorisation.
