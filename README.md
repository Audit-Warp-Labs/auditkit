# 🧪 AuditKit

**Internal repository for automation pipelines, auditing workflows, and analysis tools for Move smart contracts.**  
Includes AI-assisted and manual flows using both high-level and low-level tools. This repo is visible for transparency but intended for internal development and infrastructure R&D.

---

## 🔍 Purpose

This repository supports **AuditWarp's security automation and R&D**.  
It includes:

- 🔧 Code examples of automation and CLI tooling
- 🤖 AI model prompts and inspection logic
- 🧵 CI/CD integration patterns for smart contract security
- 🧪 Compiler toolchains and Move analyzer flows
- 📊 Risk classification, coverage metrics, and diagnostics
- 🔁 End-to-end pipelines for different types of audit inputs

---

## 📁 Supported Input Types

AuditWarp pipelines work with various data sources:

| Type | Input Format | Use Case |
|------|--------------|----------|
| A | `package_id` only | On-chain verification / bytecode introspection |
| B | `.move` file or code snippet | Static and AI-assisted review |
| C | Full folder with `Move.toml`, `sources/`, etc. | Local simulation, full static + formal audit |

---

## 🧰 Tools Used in Pipelines

| Tool | Category | Purpose |
|------|----------|---------|
| `sui move build` | Build Tool | Compile & verify syntax / test for build errors |
| `move-analyzer` | Linter / Static | Type checks, call graph, safety warnings |
| `move prove` | Formal Verifier | Prove pre/post-conditions, overflow checks |
| `move-bytecode-viewer` | Inspector | Visualize and inspect compiled bytecode |
| `move disassemble` | Bytecode Tool | Disassemble compiled modules for static diffs |
| `move doctor` | Bug Scanner | Scan for known unsafe patterns |
| `move-explain` | ABI Normalizer | Decode function signatures and module layouts |

---

## 🔄 Example Audit Pipelines

### 🔹 Pipeline A: On-Chain Package ID

**Input:** Package ID  
**Output:** Bytecode diff, call graph, selectors

```bash
sui client get object <package_id> > onchain.json
move disassemble onchain.json > disassembly.txt
move-analyzer inspect onchain.json > report.txt
```

### 🔹 Pipeline B: .move File Only
**Input:** Single contract file
**Output:** Static analysis, AI lint, call flow

```bash
move-analyzer analyze ./my_module.move > static_report.txt
python3 ./ai_linter/main.py ./my_module.move > ai_findings.md
```

### 🔹 Pipeline C: Full Project Folder
**Input:** Folder with Move.toml, sources/
**Output:** Full audit suite (build + lint + formal + AI)

```bash
sui move build
move-analyzer check
move prove
python3 ./ai_linter/main.py ./sources/
```

## 🤖 AI Integration

AuditWarp pipelines can invoke AI-based tools (OpenAI, Claude, etc.) with custom prompts to check for:

- ✅ Known Move vulnerabilities  
- 📎 Signature inconsistencies  
- ❗ Undocumented `abort` conditions  
- 🔓 Permissionless or unguarded operations  

All AI results are version-logged (model, temperature, timestamp) in:  
`ai-audits/logs/`

---

## 📊 Audit Report Outputs

- `*.pdf` → Visual report generated from Markdown via LaTeX or Puppeteer  
- `metadata.json` → Compiler version, hash, and audit metadata  
- `ipfs://...` → Uploaded audit content hash, stored in NFT on-chain  

---

## 🔐 Security & CI Integration

This repo includes GitHub Actions support for:

- 🛠️ Running build checks & analyzers on PRs  
- 🕵️‍♀️ Detecting `.env`/secret leak patterns  
- 📈 Enforcing test coverage for all audit logic  
- 📄 Auto-generating PDF reports and metadata before merge  

---

## 📘 Repository Structure

```bash
/
│   README.md
│
├───common_utils
│       json_utils.py
│       sui_api.py
│       type_utils.py
│
├───notebooks
│       pipeline_1_analysis.ipynb
│       pipeline_2_analysis.ipynb
│       pipeline_3_analysis.ipynb
│
├───pipeline_1_onchain_json
│       abi_visualizer.py
│       capability_analyzer.py
│       entry_function_audit.py
│       json_parser.py
│       ownership_checker.py
│       README.md
│
├───pipeline_2_move_source
│       capability_usage_scan.py
│       formal_verifier_stub.py
│       function_graph.py
│       linter.py
│       parser.py
│       README.md
│       resource_usage.py
│       source_ownership_analysis.py
│       spec_checker.py
│       static_linter.py
│
└───pipeline_3_bytecode_disassembly
        bytecode_loader.py
        control_flow_mapper.py
        disassembly_parser.py
        README.md
```

---

## 🧑‍💻 Authors

Maintained by `sr18z`, part of the **AuditWarp** infrastructure and protocol team.

---

## 🔐 Notice

> ⚠️ While this repository is public, it is intended **for internal audit automation and infrastructure documentation only**.  
> It is **not** intended for submitting or sharing public audits.


