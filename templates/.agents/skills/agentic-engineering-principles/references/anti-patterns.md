# Anti-Patterns

Patterns AI must actively avoid. Every item here has a concrete alternative.

| Anti-pattern | What it looks like | Correct behavior | Why this hurts |
|---|---|---|---|
| Over-abstraction | An interface with only one implementation | Delete the interface; use the implementation directly | Every abstraction selects some details and omits others. With only one consumer, you don't know which details matter — you're locking in assumptions you can't yet validate. The abstraction will likely need to change when the second consumer arrives anyway. |
| Pattern-mapping | "React has useState, so we should make one too" | Wait for a concrete use case first | — |
| Dead code retention | "This function might be useful later" | Delete it. Git history remembers it. | — |
| Config bloat | Adding an env var to toggle a new feature | Code is configuration; no toggles | — |
| Doc padding | Generating JSDoc for every function | Comment only when semantics aren't obvious | — |
| Toolchain bloat | Adding a new build step / plugin | Default: don't add. Ask: can existing tools do this? | — |
| Test-only public methods | Changing private to public just for testing | Test through the public API, or rethink the design | — |
| Defensive future-proofing | "Might need to support X later, so wrap it in an abstraction now" | Later's problem stays in the future | Most predicted futures never arrive. The abstraction you add today for a future that never materializes is pure cost — cognitive load, indirection, and the illusion of flexibility (an abstraction tested against zero real-world scenarios is fragile). |
| Premature generalization | "Let me make this generic so it handles all cases" | Handle the one case you have. Generalize only when the second case arrives. | Without two concrete examples, you're guessing the commonality. Half the time the cases diverge in the opposite direction from your guess, and the "generic" code becomes a straitjacket you must refactor around. The cost is paid by every future reader who must understand the unused generality. |
| Silent complexity | Hiding a significant decision behind a thin wrapper | Make complexity explicit in the caller's code, not buried in a helper | — |
| Speculative refactoring | "While I'm here, let me clean up this unrelated code" | Stay in scope. Create a separate task. | — |
| Framework envy | "Next.js does it this way, so our Go service should mirror it" | Choose idioms that match the language, runtime, and problem domain | — |
