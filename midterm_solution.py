print('Project title: Canteen Order System')
print("Group name: Squad Zero")
print("") 
print("======================================")
print("    COM 103 PROJECT -- TASK TYPES     ")  
print("======================================")
print(" 1. Program Logic / Coding       [6h] ")
print(" 2. UI / Output Formatting       [3h] ")
print(" 3. Testing & Debugging          [2h] ")
print(" 4. Documentatioin / README      [2H] ")
print(" 5. Presentation Slides          [2H] ")
print("======================================")
# 1. Configuration
task_catalog = {
    1: ("Program Logic / Coding", "6h"),
    2: ("UI / Output Formatting", "3h"),
    3: ("Testing & Debugging", "2h"),
    4: ("Documentation / README", "2h"),
    5: ("Presentation Slides", "2h")
}

project_title = "Canteen Ordering System"
group_name = "Squad Zero"
assigned_tasks = []

# 2. Interactive Input Loop
for i in range(1, 5):
    print(f"\n--- TASK {i} ---")
    task_num = int(input("Task number (0 to skip): "))
    
    if task_num == 0:
        continue
    
    member = input("Member name: ")
    status = input("Status (done/pending): ").lower()
    
    # Get details from catalog and store
    name, duration = task_catalog.get(task_num, ("Unknown Task", "0h"))
    points = 2 if status == "done" else 1
    
    assigned_tasks.append({
        "name": name,
        "duration": duration,
        "member": member,
        "status": status,
        "points": points
    })

# 3. Calculations
earned = sum(t["points"] for t in assigned_tasks)
max_pts = len(assigned_tasks) * 2
progress = int((earned / max_pts) * 100) if max_pts > 0 else 0
proj_status = "PROJECT READY!" if progress >= 75 else "IN PROGRESS"

# 4. Final Display
print("\n" + "="*48)
print("     Canteen Ordering System -- TASK BOARD")
print("="*48)
print(f"Project : {project_title}")
print(f"Group   : {group_name}")
print("-" * 48)

for idx, t in enumerate(assigned_tasks, 1):
    print(f"[{idx}] {t['name']:<25} [{t['duration']}]")
    print(f"    Assigned to : {t['member']}")
    print(f"    Status      : {t['status']}")
    print(f"    Points      : {t['points']} / 2\n")

print("-" * 48)
print(f"Points Earned   : {earned} / {max_pts}")
print(f"Progress        : {progress}%")
print(f"Project Status  : {proj_status}")
print("=" * 48)
def run_task_board():
    # 1. Setup Project Info
    project_title = "Canteen Ordering System"
    group_name = "Squad Zero"

    # Task Type Catalog
    task_catalog = {
        1: ("Program Logic / Coding", "6h"),
        2: ("UI / Output Formatting", "3h"),
        3: ("Testing & Debugging", "2h"),
        4: ("Documentation / README", "2h"),
        5: ("Presentation Slides", "2h")
    }

    # 2. Input Data (Simulating the sample run)
    inputs = [
        {"num": 1, "member": "Ana", "status": "done"},     # Task 1
        {"num": 3, "member": "Ben", "status": "pending"},  # Task 2
        {"num": 0, "member": None, "status": None},        # Task 3 (Skipped)
        {"num": 4, "member": "Carlo", "status": "done"}    # Task 4
    ]

    assigned_tasks = []
    total_earned = 0

    # 3. Logic: Filter skipped tasks and calculate points
    for item in inputs:
        task_num = item["num"]
        if task_num == 0:
            continue
        
        # Get details from catalog
        name, duration = task_catalog[task_num]
        status = item["status"]
        
        # Points: done = 2, pending = 1
        pts = 2 if status == "done" else 1
        total_earned += pts
        
        assigned_tasks.append({
            "name": name,
            "duration": duration,
            "member": item["member"],
            "status": status,
            "points": pts
        })

    # 4. Final Calculations
    max_pts = len(assigned_tasks) * 2
    progress = int((total_earned / max_pts) * 100) if max_pts > 0 else 0
    proj_status = "PROJECT READY!" if progress >= 75 else "IN PROGRESS"

    # 5. Formatted Output
    print("=" * 48)
    print("     Canteen Ordering System -- TASK BOARD")
    print("=" * 48)
    print(f"Project : {project_title}")
    print(f"Group   : {group_name}")
    print("-" * 48)

    for i, t in enumerate(assigned_tasks, 1):
        print(f"[{i}] {t['name']:<25} [{t['duration']}]")
        print(f"    Assigned to : {t['member']}")
        print(f"    Status      : {t['status']}")
        print(f"    Points      : {t['points']} / 2\n")

    print("-" * 48)
    print(f"Points Earned   : {total_earned} / {max_pts}")
    print(f"Progress        : {progress}%")
    print(f"Project Status  : {proj_status}")
    print("=" * 48)

if __name__ == "__main__":
    run_task_board()