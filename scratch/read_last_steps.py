import json

path = r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for line in lines[-8:]:
    entry = json.loads(line)
    step = entry.get('step_index')
    source = entry.get('source')
    step_type = entry.get('type')
    content = str(entry.get('content', ''))[:300]
    print(f"Step {step} | {source} | {step_type}")
    if step_type == 'USER_INPUT':
        print(f"   >>> {content}\n")
    elif step_type == 'PLANNER_RESPONSE':
        print(f"   Model response preview: {content[:150]}...\n")

