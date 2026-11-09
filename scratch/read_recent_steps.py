import json

with open(r'C:/Users/snssystem/.gemini/antigravity/brain/759ab44a-00fb-4289-9607-47a4eec89958/.system_generated/logs/transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') >= 5860:
            print(f"Step {data.get('step_index')}: {data.get('type')} - {data.get('source')}")
            content = data.get('content', '')
            if content:
                print("Content:")
                print(content[:1500])
                print("-" * 40)

