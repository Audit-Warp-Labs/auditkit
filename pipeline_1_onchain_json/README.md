# 🧠 On-Chain Reverse Engineering Flow

## 📌 Objective

To reverse-engineer deployed Sui smart contracts **without the original `.move` source code** by using publicly available on-chain data. This process enables auditing of contracts for ownership, access control, and capability flows using approximate logic reconstruction.

---

## 🧱 Components

| Component               | Description                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| `sui move fetch`        | CLI tool to fetch normalized JSON of on-chain package/module              |
| Normalized JSON         | Output from above; includes ABI, bytecode, struct/function signatures     |
| Disassembler (optional) | CLI-based or custom logic to parse base64-encoded bytecode for inspection |
| Reverse Compiler        | Converts JSON representation into approximated `.move` source (lossy)     |

---

## 🧩 Flow Diagram

### 🔄 Audit Pipeline Flow

| Step | Action                           | Tool / Description                            |
| ---- | -------------------------------- | --------------------------------------------- |
| 1    | 🔗 On-chain Package ID           | Starting point (e.g., `0xabc123...`)          |
| 2    | 📦 `sui move fetch`              | Fetches normalized JSON of the module         |
| 3    | 📄 Normalized Module JSON        | Structured ABI and type metadata              |
| 4a   | 🔍 Parse ABI                     | Extract entry functions, visibility, types    |
| 4b   | 🧱 Parse Structs                 | Identify resource types and capabilities      |
| 4c   | ⚙ Analyze Entry Functions        | Inspect call patterns, argument usage         |
| 4d   | 🧭 Detect Events & Access Checks | Look for `emit`, `tx_context::sender()`, etc. |

---

## 🔍 Extracted Artifacts

| Artifact Type    | Extracted From        | Notes                                                     |
| ---------------- | --------------------- | --------------------------------------------------------- |
| ABI              | `sui move fetch` JSON | Entry functions, param types, return types                |
| Struct Info      | JSON `structs` field  | Used to infer resources, capabilities, ownership fields   |
| Bytecode         | JSON base64           | Optional, for low-level tooling (e.g. `move-disassemble`) |
| Entry Visibility | `is_entry` flags      | To build attack surface maps                              |

---

## ⚠️ Limitations

- Function and struct **names may be minified or hashed**
- No access to **developer comments** or `spec` blocks
- **Loops and control flow** are harder to interpret without source
- Bytecode does **not** allow full reconstruction of original logic

# 🔄 Reverse to Source + Recompilation

## 📌 Objective

To take the normalized JSON output (from `sui move fetch`) and reverse-engineer it into approximated `.move` source files, then recompile the reconstructed source into `.mv` bytecode files for use in analysis tools like `move-disassembler`, `move-bytecode-viewer`, etc.

---

## 🧱 Components

| Component              | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| JSON to `.move` Parser | Custom tool to convert normalized JSON → approximated `.move` |
| `move build`           | Compiles reconstructed `.move` into `.mv` (bytecode)          |
| `move-disassembler`    | CLI tool to inspect `.mv` bytecode                            |
| Optional GUI tools     | View compiled bytecode via GUIs like `move-bytecode-viewer`   |

---

## 🧩 Flow Diagram

### 🔁 Reverse Compilation and Bytecode Analysis Flow

| Step | Action                                            | Tool / Description                                   |
| ---- | ------------------------------------------------- | ---------------------------------------------------- |
| 1    | 📄 Normalized Module JSON                         | Output from `sui move fetch`                         |
| 2    | 🔁 Reverse Compile JSON → `.move`                 | Convert disassembled JSON to approximate Move source |
| 3    | 📝 Approximate `.move` Source                     | Functional but not identical source code             |
| 4    | 🧱 Compile with `move build` / `sui move build`   | Generates `.mv` bytecode files                       |
| 5    | 🗃️ Compiled `.mv` Bytecode                        | Intermediate format for tooling                      |
| 6    | 🔍 Analyze with `move-disassembler` / GUI Viewers | Tools like `move-bytecode-viewer`, etc.              |

---

## ⚙️ Commands

### 1. Reconstruct Source Code (pseudo):

```bash
# Custom script or tool (see samples/)
python reverse_json_to_move.py --input module.json --output sources/
```

### 2. Compile Reconstructed Source:

```bash
move build
# or in Sui-compatible layout:
sui move build
```

### 3. View Bytecode:

```bash
move-disassemble <path_to_mv_file>
```

## 🧪 Use Cases for Recompiled `.mv`

| Use Case                    | Supported? | Tool Example            |
| --------------------------- | ---------- | ----------------------- |
| ABI Exploration             | ✅         | JSON ABI → UI generator |
| Capability / Ownership View | ✅         | move-disassembler       |
| Bytecode Pattern Matching   | ✅         | bytecode-viewer         |
| Formal Verification         | ❌         | Not without full `spec` |
| Re-deployment or Forking    | ❌         | Source is not original  |

---

## ⚠️ Caveats

- Reconstructed `.move` is **not bitwise equivalent** to the original
- Function names, struct names may be **obfuscated**
- Control flow and error logic may differ from original
- Specs, documentation, developer intent is **lost**
- Use for analysis, **not for redeployment or patching**

---

## ✅ Recommended Follow-ups

- Run `move-analyzer` and `move-doctor` for static bug detection
- Use `sui client dry-run` to test reconstructed ABI inputs
- Feed bytecode into symbolic analysis tools for deeper insight
