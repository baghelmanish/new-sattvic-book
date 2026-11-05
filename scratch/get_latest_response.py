import json

path = r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    entry = json.loads(line)
    if entry.get('type') == 'PLANNER_RESPONSE' and entry.get('content'):
        print(f"Step {entry.get('step_index')}:")
        print(entry.get('content')[:1000])
        break

