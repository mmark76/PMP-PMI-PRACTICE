# PMP / PMBOK Practice Dashboard

Static study and reference dashboard for predictive project management concepts.

## Canonical hostname

`https://pmp-practice.markellosecosystem.com/`

## Scope

The dashboard presents a PMBOK 6 predictive foundation: Triple Constraint, 5 Process Groups, 10 Knowledge Areas, 49 processes, key documents, EVM, risk management, tools and roles. It is an independent study aid and not official PMI material.

## Dashboard shell

The interface follows the Markellos Ecosystem Project Dashboard pattern: project identity, project Assistant placeholder, GR/EN controls, ecosystem return, Light/Dark, Settings, Info, responsive layout and local-only appearance preferences.

## Validation

GitHub Actions validates the source and confirms that a production build can be generated. Deployment is intentionally separate from GitHub Actions.

## Cloudflare Pages deployment

The production origin is Cloudflare Pages, following the same deployment pattern used by other public Markellos Ecosystem applications.

Recommended Pages project configuration:

- Repository: `mmark76/PMP-PMI-PRACTICE`
- Production branch: `main`
- Framework preset: `None`
- Root directory: `/`
- Build command: `python -B scripts/validate_dashboard.py && python -B scripts/build_site.py`
- Build output directory: `_site`

Cloudflare Pages supplies `CF_PAGES_COMMIT_SHA`; the build script uses it to generate the production build identity with the real deployment commit SHA and `Europe/Nicosia` timestamp.

Production build identity format:

`vX.Y.Z_YYYYMMDD_HHMM_SHA`

After the `pages.dev` origin is healthy, add the custom domain:

`pmp-practice.markellosecosystem.com`

The Cloudflare custom-domain step should be completed only after the Pages deployment is verified.
