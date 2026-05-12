# Harness 重構：系統架構設計

**scope**: 從零重新設計 agents-stack harness 的架構，捨棄現有低效部分，建立最小化、自洽的螺旋推理+執行系統
**status**: informative

---

## 1. 當前設計的核心缺陷

現有 harness 經過 oracle 審查，識別出三個層次的問題：

### 結構性缺陷：把推理管道誤認為執行管道

當前是線性裝配線：`brainstorm → proposal → contract → execution → review → state-update → compound`。這假設所有工作都是「需求明確、範圍可界定、結果可驗證」的任務執行。但許多高價值工作是在未知空間中建立知識——它的運動模式不是線性推進，而是螺旋深入。

### 複雜性缺陷：每個有效原則都被放大成完整子系統

load-bearing 的核心原則只有四個：
1. 檔案是狀態（files beat chat memory）
2. 一次一個活躍事物（single active sprint）
3. 生成器 ≠ 審查者（adversarial separation）
4. 證據鏈解決衝突（artifact precedence）

但當前設計把它們放大成：12 層證據優先級、records 子系統（含生命週期管理）、六個維護腳本、五要素 dispatch packet 形式主義、19 欄位 status.json、五類失敗分類學、P0-P2 硬化清單、三層驗證鏈 A→B→C。

**oracle 的判決：約 60% 的表面積可以移除，不影響核心功能。**

### 假設性缺陷：對抗審查的可靠性未經驗證

整個架構依賴一個獨立 reviewer LLM 誠實地區分 PASS/FAIL/BLOCKED。但目前 LLM 傾向同意、容易被表面正確的輸出滿足、不善於多步驟重現、不擅長自我限制評估。harness 保護了生成器不自審，但沒保護審查者不是壞審查者。

**新設計必須承認這個限制，並在結構中內建升級路徑（escalation to human），而不是假裝它不存在。**

---

## 2. 重新設計的核心洞察

當前 harness 管理的對象是 **task status**（任務狀態：待辦/執行中/已完成）。

但 SOP 中展示的有效協作模式揭示了一個不同的事實：真正需要被管理的是 **understanding state**——理解的深度、理解的邊界、理解何時需要換角色、理解何時需要換形式。

**新 harness 的核心命題：**

> Harness 不是工作追蹤器，是理解追蹤器。它管理一個問題從「模糊的困惑」到「自洽的框架」的演化過程。執行（寫程式、建 artifact）是這個過程中的一個手段，不是目的。

---

## 3. 架構：三層螺旋

### 3.1 總體結構

```
                    ┌──────────────────────────────┐
                    │        DIRECTION LAYER        │
                    │    「我們在理解什麼？」         │
                    │                                │
                    │   Thesis  ←─── Challenge       │
                    │   (命題)        (對抗檢驗)      │
                    │       │              │          │
                    └───────┼──────────────┼──────────┘
                            │              │
                    ┌───────┼──────────────┼──────────┐
                    │       ▼              ▼          │
                    │        METHOD LAYER             │
                    │    「我們如何回應？」             │
                    │                                │
                    │   Response  ───→  Synthesis     │
                    │   (戰術設計)       (架構合成)    │
                    │       │              │          │
                    └───────┼──────────────┼──────────┘
                            │              │
                    ┌───────┼──────────────┼──────────┐
                    │       ▼              ▼          │
                    │        ACTION LAYER             │
                    │    「我們建造什麼？」             │
                    │                                │
                    │   Contract → Build → Audit      │
                    │   (合約)    (實作)  (驗證)      │
                    │                                │
                    └────────────────────────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │ Audit 產出的  │
                    │ insight 是否  │
                    │ 揭示了更深層  │
                    │ 的問題？      │
                    │              │
                    │ 是 → 回到     │
                    │ Direction     │
                    │ Layer         │
                    │ (spiral turn) │
                    │              │
                    │ 否 → 歸檔     │
                    └──────────────┘
```

### 3.2 三層的職責

| 層 | 核心問題 | 產物 | 特徵 |
|---|---|---|---|
| **Direction** | 我們在理解什麼？ | thesis.md, challenge.md | 發散→收斂：先提出主張，再對抗檢驗 |
| **Method** | 我們如何回應缺口？ | response.md, synthesis.md | 發散→收斂：先逐個補洞，再統合成框架 |
| **Action** | 我們建造什麼來驗證？ | contract.md, handoff.md, audit.md | 合約驅動：邊界清晰、可被獨立驗證 |

### 3.3 層間的流動

```
Direction Layer 完成 → 產出 challenge.md（缺口清單）
                         │
                         ▼
                    Method Layer
                    Response（逐個缺口設計方案）
                         │
                         ▼
                    Synthesis（統合成自洽框架）
                         │
                         ▼
                    Action Layer
                    Contract（定義建造邊界）
                         │
                         ▼
                    Build（實作）
                         │
                         ▼
                    Audit（獨立驗證）
                         │
              ┌──────────┴──────────┐
              │                     │
         Audit PASS            Audit 產出
              │                deeper insight
              ▼                     │
          歸檔                      ▼
                              Spiral Turn
                              返回 Direction Layer
                              帶著新 evidence
                              depth++
```

---

## 4. 核心原語（五個）

不再有 19 個 phase、12 層證據優先級、五類失敗分類學。只有五個原語：

### 4.1 Thesis（命題）

```
定義：一個可被推翻的主張，描述我們當前對問題的理解
格式：主張 + 前提條件 + 預期結果 + 邊界
反例：「這個架構好嗎」不是 thesis。「多 Agent 只是單 Agent 的變體」才是。
```

### 4.2 Challenge（對抗檢驗）

```
定義：對 Thesis 的系統性攻擊，識別它在什麼條件下成立、在什麼條件下不成立
執行者：oracle（單一深度審查）或 council（多模型共識）
產出：不是「對/錯」，而是「在哪個層級、什麼條件下，成立或不成立」
```

### 4.3 Response（戰術回應）

```
定義：針對 Challenge 發現的每一個缺口，給出具體設計方案
格式：一個缺口一個方案，各自完備、獨立可驗證
原則：不留模糊地帶——每個方案必須有具體 schema 或合約
```

### 4.4 Synthesis（架構合成）

```
定義：將分散的 Response 統合成一個自洽的框架
產出：設計哲學 + 核心概念關係 + 關鍵流程 + 跨切面
終止條件：框架內部無矛盾。若有矛盾 → spiral turn
前置條件：Response 必須先完成（順序不可反）
```

### 4.5 Action（執行與驗證）

```
定義：將 Synthesis 轉化為可建造的合約，建造，獨立驗證
子步驟：
  Contract  — 定義建造邊界和驗收條件
  Build     — 在邊界內實作
  Audit     — 獨立驗證（generator ≠ auditor）
```

---

## 5. 狀態模型（最小化）

### 5.1 全局狀態：`docs/live/plan.md`

合併當前的 `roadmap.md` + `current-focus.md` + `ideas.md`。一個檔案，三個區段：

```markdown
# Plan

## Why（為什麼做這個）
- 來源目標、背景

## What（現況）
- 當前活躍的 workstream：WS-003
- 當前層級：direction / thesis
- 深度：第 2 圈螺旋
- 最強 artifact：.harness/WS-003/challenge.md

## What's Next（下一步）
- 等待 challenge 完成 → route response
- 阻塞點：無
```

### 5.2 工作流註冊：`docs/live/tracked-work.json`

保持單一註冊表角色，但大幅簡化：

```json
{
  "active_workstream_id": "WS-003",
  "parked_workstream_ids": ["WS-001"],
  "workstreams": {
    "WS-003": {
      "title": "Agent Framework Architecture",
      "depth": 2,
      "layer": "direction",
      "phase": "challenge",
      "evidence_path": ".harness/WS-003/"
    }
  }
}
```

移除了：`compound_pending_feature_ids`、`record_paths`、`reference_paths`、`roadmap_ref`、複雜的 backlog 優先級邏輯。Compound 合併到 state-update（見下文）。

### 5.3 Sprint 局部狀態：`.harness/<id>/status.json`

從 19 個欄位縮減到 6 個核心欄位：

```json
{
  "workstream_id": "WS-003",
  "depth": 2,
  "layer": "direction",
  "phase": "challenge",
  "attempt": 1,
  "max_attempts": 3
}
```

移除了：`local_url`、`active_pids`、`blocked_on`、`worker_id`、`worker_subject`、`tool_scope_profile`、`spawn_depth`、`parent_worker_id`、`pause_reason`、`human_action_required`、`escalation_reason`、`resume_from`、`last_verified_step`。

原因：這些是 traceability metadata，不影響路由決策。需要時由 worker 自行在 artifact 中記錄，不需要結構化 schema。

### 5.4 Artifact 檔案（七個）

```
.harness/<id>/
├── thesis.md       # Direction Layer
├── challenge.md    # Direction Layer
├── response.md     # Method Layer
├── synthesis.md    # Method Layer
├── contract.md     # Action Layer
├── handoff.md      # Action Layer (build 完成後)
├── audit.md        # Action Layer
└── status.json     # 局部狀態
```

對比當前：從 8 個 phase 對應的分散檔案 + 5 個 live 控制檔案，減少到 7 個 sprint 檔案 + 2 個 live 檔案。

---

## 6. 路由系統

### 6.1 路由原則

不再有 18 步驟決策梯。路由由三條規則決定：

1. **層內推進**：在同一層內，按 artifact 存在與否決定下一步
2. **層間流動**：上一層完成後自動進入下一層
3. **螺旋轉向**：Action Layer 的 audit 產出 deeper insight 時，回到 Direction Layer（depth++）

### 6.2 層內路由

```
Direction Layer:
  thesis.md 不存在 → route thesis
  thesis.md 存在 + challenge.md 不存在 → route challenge
  challenge.md 存在 + translation needed → route translation
  challenge.md 存在 + no translation needed → 進入 Method Layer

Method Layer:
  response.md 不存在 → route response
  response.md 存在 + synthesis.md 不存在 → route synthesis
  synthesis.md 存在 → 進入 Action Layer

Action Layer:
  contract.md 不存在 → route contract
  contract.md 存在 + handoff.md 不存在 → route build
  handoff.md 存在 + audit.md 不存在 → route audit
  audit.md 存在 → 評估下一步（歸檔 or spiral turn）
```

### 6.3 轉譯閘門（Comprehension Gate）

Challenge 產出後，檢查是否需要轉譯：

```
challenge.md 存在
       │
       ▼
  檢查：challenge 的內容對下游（人或 agent）是否可理解？
       │
       ├── 是 → 進入 Method Layer
       │
       └── 否 → route translation
                產出故事、類比、場景演練
                → 回到檢查
```

Translation 不是一個 layer，是 Direction 和 Method 之間的一個**可選閘門**。它不產生新的 artifact 類型——產出直接 append 到 challenge.md 的 `## Translation` 區段。

### 6.4 螺旋轉向（Spiral Turn）

```
audit.md 存在
       │
       ▼
  評估：audit 的發現是否揭示了更深層的問題？
  （不只是實作錯誤，而是前提假設有缺陷）
       │
       ├── 否 → 歸檔（workstream 完成）
       │
       └── 是 → Spiral Turn
                depth++
                當前 layer 重置為 "direction"
                當前 phase 重置為 "thesis"
                帶著 audit.md + synthesis.md 作為新的 evidence
                形成更深層的 thesis
```

**Spiral turn 與 retry 的關鍵區別：**

| | Retry | Spiral Turn |
|---|---|---|
| 觸發 | 實作/驗證失敗 | 前提假設被推翻 |
| 計數器 | attempt++ | depth++ |
| 合約 | 同一合約 | 新 thesis，新合約 |
| 循環 | 在同一層重試 | 進入更深層 |

兩者獨立追蹤，互不干擾。

### 6.5 人類介入點

保留兩個關鍵的人類閘門（比當前更簡潔）：

```
awaiting_human:  automation 暫停在 durable artifact 邊界，等待人類輸入/編輯
                觸發：challenge 產出 BLOCKED、環境阻斷、需要人類決策

escalated_to_human: attempt 預算耗盡或 depth 達到上限，自動化無法繼續
                    觸發：attempt >= max_attempts 或 depth >= max_depth
```

---

## 7. 角色模型

### 7.1 Orchestrator（只有一個）

```
職責：讀取狀態、路由決策、委派 worker、合併結果、作為人類界面
約束：不實作、不審查、不自驗證
權限：唯一可以委派 worker 的角色
```

### 7.2 Workers（每次重新產生）

```
Thesis Worker    — 形成命題（需要綜合能力）
Challenge Worker — 對抗檢驗（委派 oracle 或 council）
Response Worker  — 戰術設計（需要 schema/code 設計能力）
Synthesis Worker — 架構合成（可選委派 oracle 驗證自洽性）
Contract Worker  — 定義建造邊界
Build Worker     — 實作（有寫入權限）
Audit Worker     — 獨立驗證（唯讀 + audit.md 寫入權限）
```

### 7.3 Specialists（按需調用）

```
oracle    — 深度架構判斷（challenge phase 內部）
council   — 多模型共識（高風險 challenge）
explorer  — 程式碼庫搜尋
librarian — 外部文檔查詢
designer  — UI/UX 審查
```

---

## 8. 跨切面

### 8.1 安全注入點

不變：tool walls 仍然是 hard boundary。Audit worker 唯讀 + 僅寫入 audit.md。Build worker 有寫入權限但限於合約定義的檔案邊界。

### 8.2 深度預算

```
max_depth = 6  （預設，可在 plan.md 中覆寫）
達到上限後：spiral turn 被阻止，workstream 進入 escalated_to_human
```

### 8.3 可恢復性

不變：cold-start agent 必須能從檔案恢復。新增：`plan.md` 是最小化的 resume anchor——包含 why/what/next。

---

## 9. 與當前設計的對比

| | 當前設計 | 新設計 | 縮減 |
|---|---|---|---|
| Phase 數量 | 16（含 parked 狀態） | 7（thesis, challenge, response, synthesis, contract, build, audit） | -56% |
| Live 控制檔案 | 6（tracked-work.json, ideas.md, roadmap.md, current-focus.md, progress.md, memory.md） | 2（tracked-work.json, plan.md） | -67% |
| status.json 欄位 | 19 | 7（workstream_id, depth, layer, phase, attempt, max_attempts, blocked_reason） | -63% |
| 證據優先級層數 | 12 | 4（artifact precedence: audit > handoff > contract > thesis/challenge/response/synthesis） | -67% |
| 腳本數量 | 8+ | 0（路由邏輯內嵌於 SKILL.md） | -100% |
| 核心 invariant | 15 | 8 | -47% |
| 路由步驟 | 18 步決策梯 | 3 條規則 | 實質簡化 |

### 9.1 被移除的

| 移除的部分 | 原因 |
|---|---|
| `docs/records/*` 子系統（含生命週期、metadata、domain 分類） | 需要持久化的 insight 直接寫入對應的 artifact（thesis/challenge/response/synthesis），不需要獨立的 records CMS |
| `docs/scripts/*`（除 init.sh） | 路由邏輯回歸 SKILL.md 決策表，不需要腳本中介層 |
| Compound-capture phase | 跨 sprint 學習由 state-update（歸檔時）直接 append 到 plan.md 的「Lessons」區段。不隊列、不分離 phase |
| Roadmap + current-focus + ideas 三分離 | 合併為 plan.md 的三個區段（Why/What/Next） |
| 三層驗證鏈 A→B→C | 保留 A→B（generator → auditor），第三層不加——成本高於價值 |
| Dispatch packet 五要素形式主義 | 簡化為：worker prompt（SKILL.md）+ workstream ID + artifact 路徑 |
| P0-P2 硬化清單 | invariant 自身就是硬化。清單是重複 |
| 失敗分類學（五類） | 路由規則自身已包含分類邏輯，不需要平行分類系統 |
| `progress.md` | plan.md 的「What」區段反映當前狀態，不需要獨立的 append-only 日誌 |
| `memory.md` | plan.md 的「Lessons」區段 |

### 9.2 被保留的

| 保留的部分 | 原因 |
|---|---|
| Files beat chat memory | 整個架構的基礎 |
| Single active workstream | 防止路由歧義 |
| Generator ≠ Auditor（adversarial separation） | 品質機制核心 |
| Artifact precedence chain | 衝突解決 |
| tracked-work.json 作為單一註冊表 | 全局狀態的唯一真相來源 |
| 可恢復性（cold start from files） | 中斷後繼續的基礎 |
| Tool walls | 防止越權 |
| Orchestrator-only delegation | 防止遞迴複雜度 |
| Retry 機制（attempt, max_attempts, clean restore） | 執行軌的可靠性保證 |

---

## 10. 八個 Invariant

1. **Files beat chat memory.** 檔案和對話不一致時，檔案勝出。
2. **One active workstream.** 同一時刻只有一個 workstream 處於非 parked 狀態。
3. **Generator ≠ Auditor.** 建造和驗證必須由獨立 worker 執行。
4. **Artifact precedence.** `audit.md > handoff.md > contract.md > (thesis/challenge/response/synthesis)` 解決檔案衝突。
5. **Depth and attempt are independent.** depth 追蹤理解深度，attempt 追蹤實作重試。互不干擾。
6. **Response before Synthesis.** response.md 必須在 synthesis.md 之前完成。順序不可反。
7. **Spiral turn is not retry.** spiral turn 遞增 depth 並重置 thesis。retry 遞增 attempt 並保持同一合約。
8. **Cold start must work.** 新 agent 從檔案就能恢復全部狀態，不需要 chat history。

---

## 11. 實施注意事項

### 11.1 對抗審查的誠實性問題

oracle 審查指出：LLM 作為 reviewer 的可靠性未經驗證。新設計的對策：

1. **承認限制**：audit 產出 FAIL/BLOCKED 時，自動附帶升級路徑（awaiting_human）
2. **降低期待**：audit 的目標不是「完美的判斷」，而是「比 self-review 更好的判斷」
3. **結構性冗餘**：對高風險 workstream，challenge phase 使用 council（多模型共識）而非單一 oracle
4. **人類作為最終仲裁者**：當 depth 達到上限或 attempt 預算耗盡，強制 escalated_to_human

### 11.2 向後兼容

`generator-brainstorm` 和 `generator-proposal` 在新設計中被 thesis phase 吸收——thesis worker 同時承擔「澄清想法」和「形成提案」的職責。舊的 phase 名稱不再使用。

`state-update` 被歸檔動作吸收——audit PASS 後，orchestrator 直接更新 tracked-work.json 和 plan.md，不需要獨立的 state-update phase。

### 11.3 純推理工作流 vs. 含實作的工作流

新設計的好處：同一個三層結構同時服務兩種工作流。

**純推理工作流**（例如：設計 Agent Framework 架構）：
```
thesis → challenge → translation? → response → synthesis → (spiral turn or complete)
```
Action Layer 可以完全跳過——synthesis 自身就是最終產物。

**含實作的工作流**（例如：實作一個功能）：
```
thesis → challenge → response → synthesis → contract → build → audit → (spiral turn or archive)
```
完整走完三層。

這解決了當前設計的核心問題：純推理工作和執行工作被迫擠進同一條管道。
