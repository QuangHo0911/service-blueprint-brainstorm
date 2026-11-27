# Service Design Blueprint Brainstorm Skill

An open **Agent Skill** (`SKILL.md`) compatible with **Claude Code**, **OpenAI Codex**, **Cursor**, and **Antigravity** that guides structured **10-step Service Design Blueprint brainstorming** for any product or service and generates a **100% self-contained, Light-Theme-only interactive HTML Service Blueprint** (zero external CDNs — opens identically in any browser or IDE).

## Demo Output

> **Example:** Vietnamese Urban Coffee Shop — Counter-Service (Dine-in & Take-away)  
> Open or download the standalone interactive HTML: [`examples/service-blueprint-cafe-vn-en.html`](./examples/service-blueprint-cafe-vn-en.html)

![Service Design Blueprint Demo — Vietnamese Urban Coffee Shop](./docs/demo-service-blueprint-en.png)

## 10-Step Way of Thinking
1. **Business Model** (Counter-service, Take-away, Table-service, SaaS, Marketplace, Clinic, O2O...)
2. **Location & Local Context** (Vietnam, Global, HCMC, District 1, US/EU...)
3. **Actors** (Customer, Frontstage, Backstage, Support Systems & Partners)
4. **Customer Goals** (Placed directly above Customer Actions with `↓` flow)
5. **Touchpoints** (Separated `Physical Evidence` & `Digital Evidence` rows with unified neutral styling)
6. **Service Layering** (`Line of Interaction`, `Line of Visibility`, `Line of Internal Interaction`)
7. **Action Step Flows & Scenarios** (Strict sequential `Step 1 → Step 2...` with explicit `Scenario / Branch` splits)
8. **Touchpoint Durations** (Off-peak vs. Peak comparison + Bottleneck highlighting)
9. **Support Processes** (IT/POS, Supply Chain, QA, Facility, CRM, HR/SOP)
10. **Inventory Mapping** (`Actor → Action → Required Inventory Item` + searchable Inventory Explorer)

---

## Installation

### 1. Claude Code
Add this repository as a marketplace and install the plugin:
```bash
/plugin marketplace add QuangHo0911/service-blueprint-brainstorm
/plugin install service-blueprint-brainstorm@quangho-skills
```

### 2. OpenAI Codex
Install directly via Codex `$skill-installer`:
```bash
$skill-installer https://github.com/QuangHo0911/service-blueprint-brainstorm/tree/main/skills/service-blueprint-brainstorm
```

### 3. Cursor
- Open **Cursor Settings → Customize → Plugins / Skills → Add from GitHub Repository**
- Paste: `https://github.com/QuangHo0911/service-blueprint-brainstorm`

### 4. Universal CLI (`skills.sh` — Claude, Codex, Cursor, Antigravity)
```bash
npx skills add QuangHo0911/service-blueprint-brainstorm
```

### 5. Antigravity (Manual Global Install)
Copy `skills/service-blueprint-brainstorm` into `~/.gemini/config/skills/service-blueprint-brainstorm`.

---

## Example Prompt

```text
Use service-blueprint-brainstorm to co-brainstorm and build a Service Design Blueprint for:
- Product / Service: [Your product or service]
- Business Model: [e.g., Counter-service dine-in & take-away]
- Location: [e.g., District 1, Ho Chi Minh City, Vietnam]
Export the final standalone Light-Theme HTML file.
```

## License
MIT
