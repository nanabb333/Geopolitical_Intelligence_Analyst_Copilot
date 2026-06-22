# Example Output Placeholder: Military Exercise

## Scenario

Analyst question placeholder for military exercises that raise geopolitical-risk or technology-supply-chain concerns.

## Coverage Status

Partially supported. The current dataset can support technology-restriction or semiconductor-exposure framing, but it does not include direct military-exercise or military-escalation cases.

## Intended Use

Use this placeholder only for a cautious future Analyst Workbench report framed around technology restrictions that could follow escalation. Direct military-exercise analysis would require future dataset expansion.

## Suggested Command

```bash
python3 src/run_scenario.py \
  --query "What technology-restriction analogues are relevant if a regional military exercise raises concern about semiconductor export controls?" \
  --top-k 5 \
  --output docs/example_outputs/military_exercise.md
```

## Status

Placeholder only. No new product functionality is added by this file. Direct military-escalation coverage is outside the current dataset.
