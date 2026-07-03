---
title: Charging
has_children: true
parent: Legacy
grand_parent: App API
nav_order: 3
permalink: /app/legacy/charging
---

# Legacy charging (HTTP)

Wallbox management, public charging sites, completed session history, and third-party account linking. These use `POST https://rivian.com/api/gql/chrg/user/graphql`.

Live charging session state and graphs use [Parallax](/app/parallax/domains/charging) RVMs, not these endpoints.

## Endpoints

- [`getNonRivianUserSession`](/app/legacy/charging/non-rivian-user-session) — non-Rivian charging session details
- [`getNonRivianUserSession`](/app/legacy/charging/get-non-rivian-user-session) — alternate query name
- [`getWallboxStatus`](/app/legacy/charging/wallbox-status) — wallbox status
- [`updateWallbox`](/app/legacy/charging/update-wallbox) — rename wallbox
- [`getCompletedSessionSummaries`](/app/legacy/charging/get-completed-session-summaries) — past session summaries
- [`chargingSites`](/app/legacy/charging/charging-sites) — public charging map search
- [`Charging Schedule`](/app/legacy/charging/charging-schedule) — get/set charge schedule
- [`CheckByRivianId`](/app/legacy/charging/check-by-rivian-id) — third-party accounts linked to Rivian ID
- [`getLinkedEmailForRivianId`](/app/legacy/charging/get-linked-email-for-rivian-id) — emails for linked accounts
