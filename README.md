# PMP / PMBOK Practice Dashboard

Static study and reference dashboard for predictive project management concepts.

## Canonical hostname

`https://pmp-practice.markellosecosystem.com/`

## Scope

The dashboard presents a PMBOK 6 predictive foundation: Triple Constraint, 5 Process Groups, 10 Knowledge Areas, 49 processes, key documents, EVM, risk management, tools and roles. It is an independent study aid and not official PMI material.

## Dashboard shell

The interface follows the Markellos Ecosystem Project Dashboard pattern: project identity, project Assistant placeholder, GR/EN controls, ecosystem return, Light/Dark, Settings, Info, responsive layout and local-only appearance preferences.

## Deployment

GitHub Actions validates the static source, injects a production build ID using `Europe/Nicosia` and the real Git commit SHA, builds `_site`, and deploys it to GitHub Pages.

Production build identity format:

`vX.Y.Z_YYYYMMDD_HHMM_SHA`

Cloudflare/DNS publication of the canonical hostname is a separate release step after the origin is verified.
