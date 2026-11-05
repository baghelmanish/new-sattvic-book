import json

path = r'C:\Users\snssystem\.gemini\antigravity\brain\759ab44a-00fb-4289-9607-47a4eec89958\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines[3358:]:
    entry = json.loads(line)
    step = entry.get('step_index')
    stype = entry.get('type')
    calls = entry.get('tool_calls', [])
    content = entry.get('content', '')
    call_names = [c.get('function', {}).get('name') for c in calls] if calls else []
    print(f"Step {step} | {stype} | Calls: {call_names} | Content: {str(content)[:100]}")

