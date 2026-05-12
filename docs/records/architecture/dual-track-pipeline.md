# 雙軌管道：Harness 架構重構設計

**scope**: 將 agents-stack harness 從單一線性執行管道重構為「執行軌 + 推理軌」雙軌交替架構
**status**: informative
**workstream_id**: TBD

---

## 1. 核心診斷

當前 harness 是一條線性裝配線：

```
brainstorm → proposal → contract → execution → review → state-update → compound → (結束)
```

這個模型對應的是「寫程式」的心智模型——需求明確、範圍可界定、結果可驗證。它有效管理的是 **task status**（任務狀態：待辦/執行中/已完成）。

但許多高價值工作不是在執行已知任務，而是在**未知空間中建立知識結構**。這種工作的運動模式不是線性推進，而是螺旋深入——同一問題在多個抽象層被反覆訪問，每一次返回都帶著上一輪的 insight 作為新的輸入。

| | 執行管道（現有） | 螺旋推理（缺失的） |
|---|---|---|
| 方向 | 單向前進 | 來回擺盪（發散↔收斂） |
| 深度 | 一個層級 | 同一問題在多個抽象層被反覆訪問 |
| 轉折點 | 合約審查、review | 資訊→判斷的界線（觸發委派） |
| 終止條件 | 合約完成或失敗 | 架構合成（自洽框架出現） |
| 中間產物 | 合約、handoff、review | 命題、反命題、轉譯、缺口設計 |
| 管理的對象 | task status | **understanding state**（理解深度、理解邊界） |

**核心洞察：推理負責打破，執行負責封裝。打破後不封裝，理解就散失；封裝後不打破，就停在上一層。**

---

## 2. 雙軌模型

### 2.1 兩條軌道

```
執行軌（Execution Track）：提案 → 合約 → 實作 → 驗證 → 歸檔
    管理對象：task status
    產物：contract.md, runtime.md, handoff.md, review.md
    節奏：合約驅動，邊界清晰

推理軌（Reasoning Track）：地圖 → 命題 → 反命題 → 轉譯 → 戰術設計 → 架構合成
    管理對象：understanding state
    產物：thesis.md, antithesis.md, translation.md, tactical-design.md, architectural-synthesis.md
    節奏：洞察驅動，邊界湧現
```

### 2.2 交替節奏

兩軌不是平行運行，而是交替主導：

```
推理軌開路 → 執行軌封裝 → 推理軌再開路 → 執行軌再封裝 → ...
   打破          封裝           打破           封裝
```

具體交替模式：

| 步驟 | 主導軌 | 產出 |
|---|---|---|
| 廣度掃描、建立地圖 | 推理 | map.md |
| 鎖定方向、形成命題 | 推理 | thesis.md |
| 委派 oracle、產出判決 | 推理→**執行** | antithesis.md（封裝成 artifact） |
| 察覺理解障礙、轉譯 | 推理 | translation.md |
| 逐個缺口補、戰術設計 | 推理→**執行** | tactical-design.md |
| 統一框架、架構合成 | 推理→**執行** | architectural-synthesis.md |

每次推理軌產出 insight 後，執行軌將它封裝為 durable artifact；每次封裝完成後，推理軌以新 artifact 為輸入，在更高的抽象層重新審視問題。

### 2.3 與現有 phase 的關係

**執行軌**直接復用現有 phase，不變：

```
project-initializer → generator-brainstorm → generator-proposal
  → evaluator-contract-review → generator-execution
  → adversarial-live-review → state-update → compound-capture
```

**推理軌**是新增的平行 phase 家族：

```
reasoning-map         # 廣度掃描，建立知識地圖
reasoning-thesis      # 形成可被檢驗的命題
reasoning-antithesis  # 對抗檢驗，解構命題（委派 oracle/council）
reasoning-translation # 察覺理解障礙，轉譯（換形式不換內容）
reasoning-tactical    # 戰術層設計，逐個缺口填補
reasoning-synthesis   # 架構層合成，統一框架
```

---

## 3. 五個新原語

### 3.1 深度軸（Depth as a first-class dimension）

當前 `status.json` 只有 `attempt_count`——這是重試計數器，不是深度計。

```json
// status.json 新增欄位
{
  "depth": 1,                     // 第幾層螺旋（推理軌每完成一圈 +1）
  "abstraction_level": "map",     // 當前抽象層級
                                  // "map" | "thesis" | "antithesis" | "translation"
                                  // | "tactical" | "synthesis"
  "parent_depth_ref": null,       // 上一層 insight 的 artifact hash 或路徑
  "max_depth": 6                  // 防止無限螺旋的閘門
}
```

**抽象層級定義：**

| 層級 | 含義 | 典型問題 |
|---|---|---|
| `map` | 全景掃描 | 「這個領域目前的 best practice 是什麼」 |
| `thesis` | 形成命題 | 「基於地圖，我認為架構應該這樣設計」 |
| `antithesis` | 對抗檢驗 | 「這個命題在什麼條件下成立/不成立」 |
| `translation` | 轉譯消解 | 「這個判決對接收者是否可理解」 |
| `tactical` | 戰術設計 | 「具體應該怎樣實現，來填補檢驗發現的缺口」 |
| `synthesis` | 架構合成 | 「這些戰術方案如何統合成一個自洽框架」 |

**關鍵區分：**
- `attempt_count` 回答：「我試了幾次還沒成功？」（執行軌的維度）
- `depth` 回答：「我在第幾層螺旋上理解這個問題？」（推理軌的維度）
- 兩者獨立遞增，互不干擾

### 3.2 螺旋轉向（Spiral Turn，不是 retry）

當前：合約失敗 → retry 同一合約（最多 N 次）→ 放棄。

問題在於 retry 假設合約本身是對的，只是執行出錯。但在螺旋推理中，合約本身可能就是上一層理解不足的產物。

**新的轉向邏輯：**

```
執行軌產出 insight（handoff.md / review.md）
       │
       ▼
  推理軌評估：這份 insight 是否揭示了上一層命題的缺陷？
       │
       ├── 否 → state-update（正常歸檔）
       │
       └── 是 → 觸發 spiral turn
                │
                ▼
            帶著新 evidence，返回更深層的 reasoning-thesis
            depth++ （不是 attempt_count++）
            形成修正後的命題
                │
                ▼
            新的合約 → 新的執行
```

**spiral turn 與 retry 的區別：**

| | retry | spiral turn |
|---|---|---|
| 計數器 | attempt_count++ | depth++ |
| 合約 | 同一合約 | 新合約（反映上一圈的 insight） |
| 觸發條件 | 執行失敗 | 推理發現前提缺陷 |
| 終止 | max_attempts 耗盡 | max_depth 達到或框架自洽 |

**狀態機新增轉向：**

```
# state-machine.md 新增
- `contracted` → `needs_thesis` (spiral turn)
  Trigger: execution insight reveals flaw in parent thesis.
  depth++, reset abstraction_level to "thesis".
  Previous contract preserved as evidence_path for new thesis formation.

- `review_recorded` → `needs_thesis` (spiral turn)
  Trigger: review findings reveal fundamental assumption error.
  Same as above, with review.md as input evidence.
```

### 3.3 委派觸發點（Delegation Trigger，不是固定 phase）

SOP 中最關鍵的時刻：問題從「資訊整理」轉變為「架構判斷」，觸發 oracle / council 委派。這個轉折不是事前規劃的，是在過程中**湧現**的。

當前 harness 將委派固定在 phase 級（evaluator 審查合約、reviewer 審查執行結果）。但螺旋推理中的委派更細粒度——在一個 phase 內部，某個子問題的性質突然改變了。

**引入 Phase-Internal Role Switch：**

```json
// status.json 新增
{
  "phase_internal_role_stack": [
    {
      "role": "oracle",
      "trigger": "question crossed from information-gathering to architectural-judgment",
      "artifacts": [".harness/WS-003/antithesis.md"],
      "resolved": true
    }
  ]
}
```

**語意觸發規則（加入 children.json）：**

```json
{
  "phase_internal_role_switches": [
    {
      "from_role": "reasoning-map",
      "to_role": "oracle",
      "when": "question_requires_architectural_judgment_not_information_gathering",
      "tool_scope": "read-only + verdict artifact write"
    },
    {
      "from_role": "reasoning-thesis",
      "to_role": "council",
      "when": "thesis_evaluation_requires_multi_perspective_consensus",
      "min_confidence_threshold": 0.7
    },
    {
      "from_role": "reasoning-translation",
      "to_role": "designer",
      "when": "comprehension_barrier_is_visual_or_spatial"
    }
  ]
}
```

這不是新增 phase，而是允許 phase 內部根據語意觸發角色切換——保留 phase 的結構完整性，同時獲得推理所需的靈活性。

### 3.4 轉譯閘門（Comprehension Gate）

SOP 中的關鍵轉折：oracle 的架構判決被產出了，但接收者不理解。這不是任何一方的失敗——是傳遞管道的結構性問題。

當前 harness 的 review phase 產出 PASS/FAIL/BLOCKED，然後 state-update 直接處理。沒有檢查「這個判決是否對下游可理解」。

**在 review.md 中新增 comprehension gate：**

```markdown
<!-- review.md 新增區段 -->
## Comprehension Gate

- **target_audience**: [human | agent | both]
- **comprehension_status**: [clear | partial_barrier | full_barrier]
- **barrier_type**: [abstraction_level | domain_knowledge | structural_complexity]
- **translation_required**: [true | false]
- **suggested_translation_form**: [narrative | analogy | scenario_walkthrough | diagram]
- **translation_artifact**: null  # filled by reasoning-translation phase
```

**路由邏輯：**

```
review.md 存在 + comprehension_gate.translation_required = true
       │
       ▼
  不是 route state-update
       │
       ▼
  route reasoning-translation（轉譯 phase）
       │
       ▼
  產出 translation.md（故事、類比、場景演練）
       │
       ▼
  再次檢查 comprehension gate → 清除後 route state-update
```

**轉譯的核心原則：換形式不換內容。** 抽象聽不懂就講故事，故事懂了再回到抽象。

### 3.5 兩階段合成（Tactical-then-Architectural Synthesis）

SOP 展示了一個關鍵的順序依賴：**必須先逐個補缺口（戰術層），才能看見統一框架的形狀（架構層）。** 跳過戰術層直接做架構，會產出空洞的抽象；做完戰術層不做架構合成，會留下一堆孤立的方案。

這是現有 compound-capture 做不到的。Compound 是跨 sprint 的學習提取（橫向），而兩階段合成是**同一問題空間內的縱向統合**。

**分離為兩個 phase：**

```
reasoning-tactical（戰術設計）
  輸入：antithesis.md（對抗檢驗發現的缺口清單）
  產出：tactical-design.md（每個缺口的具體設計方案 + schema + code-level 合約）
  特徵：發散——一個缺口一個方案，獨立完備
  終止條件：所有缺口都有具體設計回應

reasoning-synthesis（架構合成）
  輸入：tactical-design.md + 所有前序 artifact
  產出：architectural-synthesis.md（統一框架、設計哲學、核心原語、關鍵流程）
  特徵：收斂——從分散方案中提取共同模式，形成自洽體系
  終止條件：框架自洽，無內部矛盾
```

**關鍵規則：reasoning-tactical 必須在 reasoning-synthesis 之前完成。順序不可反。**

---

## 4. 雙軌拓撲結構

### 4.1 檔案布局

```
.harness/<WORKSTREAM-ID>/
├── status.json              # 擴展：depth, abstraction_level, phase_internal_role_stack
│
├── # === 執行軌 artifacts（現有，不變）===
├── sprint_proposal.md
├── contract.md
├── runtime.md
├── handoff.md
├── review.md                # 擴展：comprehension_gate 區段
├── qa.md
│
├── # === 推理軌 artifacts（新增）===
├── map.md                   # 廣度掃描結果，結構化知識地圖
├── thesis.md                # 可被檢驗的命題
├── antithesis.md            # 對抗檢驗判決（由 oracle/council 產出）
├── translation.md           # 轉譯產物（故事、類比、場景）
├── tactical-design.md       # 戰術層設計方案（逐個缺口）
└── architectural-synthesis.md  # 架構層統一框架
```

### 4.2 Skill 布局

```
.agents/skills/using-agents-stack/
├── SKILL.md                      # 擴展：雙軌路由邏輯
│
├── # === 執行軌 children（現有）===
├── project-initializer/
├── generator-brainstorm/
├── generator-proposal/
├── evaluator-contract-review/
├── generator-execution/
├── adversarial-live-review/
├── state-update/
├── compound-capture/
│
├── # === 推理軌 children（新增）===
├── reasoning-map/
├── reasoning-thesis/
├── reasoning-antithesis/
├── reasoning-translation/
├── reasoning-tactical/
└── reasoning-synthesis/
```

### 4.3 路由決策樹（擴展）

```
Router 讀取 durable state 後：

1. 檢查 track：當前 sprint 在哪條軌上？
   ├── 執行軌 active → 現有路由邏輯（不變）
   └── 推理軌 active → 新路由邏輯

2. 推理軌路由邏輯：
   ├── depth == 0 或 abstraction_level == null
   │   → route reasoning-map
   │
   ├── map.md 存在 + thesis.md 不存在
   │   → route reasoning-thesis
   │
   ├── thesis.md 存在 + antithesis.md 不存在
   │   → route reasoning-antithesis（委派 oracle/council）
   │
   ├── antithesis.md 存在 + comprehension_gate 未清除
   │   → route reasoning-translation
   │
   ├── antithesis.md 存在 + comprehension_gate 已清除 + tactical-design.md 不存在
   │   → route reasoning-tactical
   │
   ├── tactical-design.md 存在 + synthesis 不存在
   │   → route reasoning-synthesis
   │
   ├── synthesis 存在 + framework 不自洽
   │   → 觸發 spiral turn: depth++, 返回 reasoning-thesis
   │
   └── synthesis 存在 + framework 自洽
       → 推理軌完成，切換到執行軌進行封裝
       → route generator-proposal（基於 synthesis 的新合約）

3. 軌道切換：
   推理軌完成 → 將 synthesis 轉化為 sprint_proposal
   執行軌 insight 揭示命題缺陷 → 觸發 spiral turn 回到推理軌
```

### 4.4 關鍵 invariant 調整

**現有 invariant 保持不變，新增以下：**

16. **雙軌互斥執行。** 同一 sprint 在同一時刻只能在一條軌上（由 `abstraction_level` 欄位決定）。執行軌 active 時 `abstraction_level` 為 null；推理軌 active 時 `abstraction_level` 為非 null。

17. **推理軌不產生 runnable 產物。** 推理軌的 artifact（map, thesis, antithesis, translation, tactical-design, synthesis）是 insight artifact，不是可執行合約。它們不佔用 `runnable_active_sprint_id`。

18. **Spiral turn 不等於 retry。** Spiral turn 遞增 `depth`，不遞增 `attempt_count`。Retry 遞增 `attempt_count`，不遞增 `depth`。兩者獨立追蹤。

19. **深度預算有限。** `max_depth`（預設 6）是螺旋推理的終止閘門。達到上限後，推理軌必須收斂於當前最佳 synthesis 或 escalated_to_human。

20. **Tactical 必須先於 Synthesis。** `reasoning-tactical` phase 完成前，不得 route `reasoning-synthesis`。

---

## 5. 新 Phase 詳細定義

### 5.1 reasoning-map

```
角色：全景掃描器
工具：explorer, librarian, web_search
產物：map.md

輸入：來自 current-focus.md 的主題或問題空間
輸出：結構化知識地圖——分層級、分領域、有關鍵爭議點

合約：
- 廣度優先，不做深層判斷
- 標記不確定的區域（標記為後續命題化的候選點）
- 產物格式：層級結構 + 每個節點的關鍵發現 + 不確定性標記
```

### 5.2 reasoning-thesis

```
角色：命題形成器
工具：無限制（需要綜合 map.md 的內容進行判斷）
產物：thesis.md

輸入：map.md
輸出：一個清晰、可被推翻的命題

合約：
- 命題必須是可被證偽的——「你覺得這個框架怎麼樣」不是命題
- 命題必須包含：主張、適用條件、邊界、預期結果
- 如果 map 中的不確定區域過多，可以返回 reasoning-map 先補地圖
```

### 5.3 reasoning-antithesis

```
角色：對抗檢驗器
工具：oracle, council（根據問題複雜度選擇單一 oracle 或多模型 council）
產物：antithesis.md

輸入：thesis.md + map.md
輸出：結構化判決

合約：
- 不是簡單的「對」或「錯」
- 必須精確標記：命題在什麼層級、什麼條件下成立或不成立
- 必須列出不可約簡的差異（如果命題有缺陷）
- 必須給出總體分級判決
- oracle/council 的輸出直接寫入 antithesis.md

觸發：
- 如果 orchestrator 檢測到問題從「資訊整理」轉向「架構判斷」
- 如果 thesis 的 ambiguity 高於閾值
- 由 orchestrator 決定單 oracle 還是 council（多模型共識）
```

### 5.4 reasoning-translation

```
角色：轉譯器
工具：無限制（需要重述能力，可能需要 designer 協助視覺化）
產物：translation.md

觸發條件：antithesis.md 的 comprehension_gate 觸發（理解障礙）
輸入：antithesis.md
輸出：以接收者可理解的形式重述的判決

合約：
- 換形式不換內容
- 可用形式：故事、類比、場景演練、視覺化描述
- 每個抽象點對應一個具體案例
- 完成後回到 antithesis 的 comprehension gate 檢查是否清除
```

### 5.5 reasoning-tactical

```
角色：戰術設計器
工具：無限制（需要 code-level schema 設計能力）
產物：tactical-design.md

輸入：antithesis.md（檢驗發現的缺口）
輸出：每個缺口的具體設計方案

合約：
- 一缺口一方案，獨立完備
- 每個方案包含：具體 schema、code-level 合約、邊界條件
- 方案之間暫不求統一（統一是下一階段的工作）
- 不留下「這應該可以解決」的模糊地帶
```

### 5.6 reasoning-synthesis

```
角色：架構合成器
工具：oracle（可選——用於驗證框架的自洽性）
產物：architectural-synthesis.md

輸入：tactical-design.md + 所有前序 artifact
輸出：統一框架

合約：
- 從分散方案中提取共同模式
- 形成設計哲學（不只「做什麼」，而是「為什麼這樣做」）
- 定義核心原語和它們之間的關係
- 定義關鍵流程（正常路徑 + 故障恢復）
- 定義跨切面（安全、成本、可恢復性）
- 自洽性檢查：框架內部不矛盾

終止條件：
├── 框架自洽 → 推理軌完成
└── 不自洽 → 觸發 spiral turn (depth++, 返回 thesis)
```

---

## 6. `tracked-work.json` 擴展

```json
{
  "backlog": [
    {
      "id": "WS-003",
      "title": "Agent Framework Architecture Design",
      "status": "in_reasoning_track",
      "track": "reasoning",
      "depth": 3,
      "abstraction_level": "synthesis",
      "max_depth": 6,
      "idea_ref": "docs/live/ideas.md#agent-framework",
      "evidence_path": ".harness/WS-003/",
      "record_paths": ["docs/records/architecture/dual-track-pipeline.md"]
    }
  ],
  "runnable_active_sprint_id": null,
  "reasoning_active_sprint_id": "WS-003"
}
```

**關鍵區分：**
- `runnable_active_sprint_id`：執行軌的 active sprint（可以有一個）
- `reasoning_active_sprint_id`：推理軌的 active sprint（可以有一個，與執行軌互斥）
- 兩者不會同時非 null

---

## 7. 實施路徑

### Phase 1：Metadata 層（不改變 phase 模型）

1. `status.json` 擴展 schema：加入 `depth`, `abstraction_level`, `parent_depth_ref`, `max_depth`
2. `review.md` 擴展 schema：加入 `comprehension_gate` 區段
3. `children.json` 加入 `phase_internal_role_switches` 定義
4. `tracked-work.json` 擴展：加入 `track`, `depth`, `reasoning_active_sprint_id`
5. 更新 `dispatch_phase.py` 和驗證腳本以識別新欄位

### Phase 2：推理軌 Phase 引入

6. 建立六個新 phase 的 SKILL.md（reasoning-map ~ reasoning-synthesis）
7. 在 `children.json` 註冊新 children
8. 更新 `state-machine.md`：加入推理軌的 phase 定義和轉向規則
9. 擴展 router 的 SKILL.md：加入雙軌路由邏輯

### Phase 3：Spiral Turn 機制

10. 實現 `spiral turn` 轉向邏輯
11. 實現 `comprehension gate` 檢查和 `reasoning-translation` 觸發
12. 實現兩階段合成順序強制（tactical → synthesis）

### Phase 4：軌道切換與整合

13. 實現推理軌完成後到執行軌的自動切換
14. 實現執行軌 insight 觸發推理軌 spiral turn
15. 完整測試雙軌交替循環

---

## 8. 不變的部分

以下現有設計保持完全不變：

- **執行軌的八個 phase** 及其所有轉向規則
- **Single-runnable-sprint rule**（執行軌最多一個 active sprint）
- **Retry 機制**（attempt_count, max_attempts, clean_restore_ref）
- **Archive policy**（PASS 後歸檔）
- **Compound-capture**（跨 sprint 學習提取）
- **Tool walls**（evaluator/reviewer 讀寫邊界）
- **Workers must not spawn nested workers**
- **檔案優先於 chat memory**
- **所有現有 invariant（1-15）**
