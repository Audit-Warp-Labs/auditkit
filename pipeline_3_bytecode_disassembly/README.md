# Analysis Tool Integration

## 📌 Objective

To integrate both static and dynamic analysis tools for automated inspection of Move smart contracts, enabling detection of critical vulnerabilities, access control flaws, and ownership mismanagement. The system should support approximate audit flows even in the absence of full source code, and be modular enough to plug in new tools as they become available.

---

## ⚙️ Architecture Overview

```plaintext
             ┌────────────────────┐
             │ .move / JSON input │
             └─────────┬──────────┘
                       │
         ┌─────────────▼─────────────┐
         │    Analysis Orchestrator   │
         └─────────────┬─────────────┘
     ┌─────────────────┼─────────────────┐
     ▼                 ▼                 ▼
[Static Analyzer]  [Ownership Checker]  [Simulation Engine]
(move-analyzer)     (custom logic)      (sui client dry-run)
```

# 🔌 Integrated Tools and Modules

| Tool/Module               | Type    | Description                                                          |
| ------------------------- | ------- | -------------------------------------------------------------------- |
| move-analyzer             | Static  | Type checker, visibility and unused variable checker                 |
| move-disassemble          | Static  | Bytecode disassembler for inspecting low-level logic                 |
| Custom ABI Parser         | Static  | Extracts struct/function ABI from JSON or .move                      |
| Ownership Detector        | Static  | Identifies ownership patterns based on struct fields and usage       |
| Access Control Heuristics | Static  | Checks for tx_context::sender() patterns and capability requirements |
| sui client dry-run        | Dynamic | Simulates transactions and extracts execution traces                 |
| Custom Attack Generator   | Dynamic | Fuzzing-like input generator for dry-run scenarios                   |

---

# 🧠 Analysis Workflows

### 1. Static Ownership & Capability Analysis

**Input:** `.move` file or normalized JSON  
**Output:** List of ownership fields, capability-protected methods, potential leaks

**Process:**

- Parse all structs and identify fields of type `address`, `uid`, `ID`, `Capability`

- Flag all functions that:

  - Accept `&mut` or by-value of these types

  - Require `tx_context::sender == owner` checks

  - Use `::transfer`, `::move_from`, or `::delete`

---

### 2. Entry Function Visibility & Access Control

**Input:** Normalized JSON  
**Output:** Entry point risk map

**Process:**

- Enumerate all functions with `is_entry = true`

- For each function:

  - List parameter types and return types

  - Check for patterns: `requires_cap`, `sender ==`, `has_one_of_capability`

  - Score entry point based on privilege level needed

---

### 3. Bytecode Disassembly (Low-Level Static)

**Input:** `.mv` bytecode  
**Output:** Human-readable opcode list  
**Tools:** `move-disassemble`, custom decoders

**Process:**

- Convert `.mv` to disassembled `.txt`

- Match instruction patterns like:

  - `MoveFrom`, `MoveTo`, `BorrowField`, `Call`

- Highlight unsafe sequences: unchecked transfers, capability use, drop/delete patterns

---

### 4. Transaction Simulation

**Input:** Package ID + dummy input values  
**Output:** Dry-run execution trace  
**Tools:** `sui client dry-run`

**Process:**

- Use SDK to build dummy payloads for each entry

- Inject with synthetic arguments

- Capture:

  - Gas used

  - Events emitted

  - Object changes

  - Runtime errors

---

### 5. Fuzzing & Attack Vector Enumeration (Optional)

**Input:** ABI  
**Output:** Auto-generated test cases

**Process:**

- Use entry function definitions to generate random but valid args

- Feed into dry-run engine

- Track:

  - Unexpected state changes

  - Skipped authorization

  - Memory errors / panics

---

# ✅ Supported Vulnerability Categories

| Vulnerability Category    | Detection Type | Tools Used                     |
| ------------------------- | -------------- | ------------------------------ |
| Unrestricted Access       | Static         | ABI Parser + Access Heuristics |
| Ownership Transfer Flaws  | Static         | Struct/Field Parser            |
| Missing Capability Checks | Static         | Capability Heuristics          |
| Resource Leaks            | Static         | move-analyzer                  |
| Dangerous Entry Points    | Static         | ABI Risk Mapper                |
| Logic Flaws in Execution  | Dynamic        | Dry-run Engine                 |
| Panics and Overflows      | Dynamic        | Fuzzed Dry-runs                |

---

# 🧰 Tool Output Integration

Each tool outputs a structured JSON report, for use in UIs or storage on-chain (if needed).

**Example schema:**

```json
{
  "module": "my_module",
  "entry_points": [
    {
      "name": "transfer_nft",
      "requires_capability": true,
      "owner_check_present": true,
      "score": 7
    }
  ],
  "vulnerabilities": [
    {
      "type": "missing_access_control",
      "function": "mint",
      "severity": "high"
    }
  ],
  "simulated_results": [
    {
      "function": "burn",
      "gas_used": 4512,
      "error": null
    }
  ]
}
```

## ⚠️ Limitations

| Limitation                  | Impact                                           | Workaround                            |
| --------------------------- | ------------------------------------------------ | ------------------------------------- |
| No specs available          | Limits move-prover usage                         | Focus on dynamic + heuristic checks   |
| Approximate source recovery | Might misrepresent logic or miss flows           | Always show confidence level per rule |
| Simulation ≠ Execution      | Dry-run doesn't interact with external modules   | Warn user of simulated limits         |
| Bytecode recompile mismatch | `.mv` not identical to original on-chain version | Only use for inspection, not matching |

---

## 📚 Appendix – Tool Versions

| Tool             | Version (suggested) | Notes                        |
| ---------------- | ------------------- | ---------------------------- |
| move-analyzer    | 0.2.x+              | From Move CLI                |
| move-disassemble | 0.1.0+              | From Move repo               |
| sui client       | >= 1.21             | Use `--json` with dry-run    |
| sui move fetch   | latest              | For normalized module export |
