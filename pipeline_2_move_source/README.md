# 🧩 Bytecode Reconstruction & ABI Analysis

### 📌 Objective

To reconstruct `.move` source files from JSON and recompile them into `.mv` files for use with Move analysis tools. This facilitates ABI inspection, mutation analysis, and limited static/dynamic auditing.

---

### 🔁 Reverse Compilation Flow

[Normalized JSON]
│
▼ Reverse Compiler
│
▼ [Approximate .move]
│
▼ sui move build
│
▼ Compiled .mv bytecode + ABI + layout

---

### 🔨 Toolchain and Roles

| Tool               | Input            | Output              | Use Case                                           |
| ------------------ | ---------------- | ------------------- | -------------------------------------------------- |
| Custom Parser      | Normalized JSON  | `.move` files       | Reconstruct source structure                       |
| `sui move build`   | `.move` + layout | `.mv` bytecode      | Generate binary modules for analysis               |
| `move-disassemble` | `.mv`            | Disassembled text   | Inspect bytecode for logic and capability patterns |
| `move-analyzer`    | `.move`          | Static reports      | Type, resource, and visibility analysis            |
| `move-prover`      | `.move` + specs  | Verification output | ❌ Cannot use without original `spec` blocks       |

---

### 🧠 ABI and Risk Inference

| Insight Type      | Source                  | Analysis Method                            |
| ----------------- | ----------------------- | ------------------------------------------ |
| Ownership Fields  | Struct layout           | Look for `address`-type named fields       |
| Capability Usage  | Function params/body    | Detect `*Cap` struct usage and mutability  |
| Access Control    | Function logic          | Check for `tx_context::sender` assertions  |
| Public Entry List | `is_entry` flag in JSON | Determine externally callable functions    |
| Transfer Logic    | Move ops/patterns       | Look for `transfer`, `move_from`, `delete` |

---

### ✅ Supported Audit Use Cases

| Use Case                     | Supported? | Tools Required                                  |
| ---------------------------- | ---------- | ----------------------------------------------- |
| Entry Point Enumeration      | ✅         | JSON, Python parser, move-analyzer              |
| Struct & Resource Extraction | ✅         | JSON struct parser                              |
| Capability Flow Detection    | ✅         | JSON + function logic analysis                  |
| Bytecode Disassembly         | ✅         | move-disassemble                                |
| Transaction Simulation       | ✅         | sui client dry-run                              |
| Formal Verification          | ❌         | Not possible without full `specs`               |
| Bytecode Hash Matching       | ❌         | Recompiled `.mv` is not byte-for-byte identical |

---

### ⚠️ Known Issues with Reconstruction

- **Lossy reverse compilation**: Names, specs, macros are stripped
- **Control flow**: Hard to recover exact loops/matches
- **No formal guarantees**: Recompiled code ≠ deployed binary
- **Cannot re-deploy**: You cannot verify match via hash

---

### 📚 Appendix – Glossary

| Term            | Definition                                                        |
| --------------- | ----------------------------------------------------------------- |
| `.move`         | Source code file for a Move module or script                      |
| `.mv`           | Compiled bytecode for a Move module                               |
| Normalized JSON | Canonical representation of a module’s ABI and structure from Sui |
| Capability      | A resource that allows privileged access (e.g., `TransferCap`)    |
| Entry Function  | Public function marked `entry`, callable by users                 |
| `tx_context`    | Transaction context giving access to sender and environment info  |
