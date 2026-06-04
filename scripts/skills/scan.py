"""
Skill: Scan repository structure
Returns folder list, README status, SKILL.md status
"""
import os, json

def run(repo_path):
    if not os.path.exists(repo_path):
        return {"error": "not found", "folders": []}
    
    folders = []
    for item in sorted(os.listdir(repo_path)):
        fpath = os.path.join(repo_path, item)
        if not os.path.isdir(fpath) or item.startswith("."):
            continue
        files = [f for f in os.listdir(fpath) if not f.startswith(".")]
        folders.append({
            "name": item,
            "files": len(files),
            "has_readme": "README.md" in files,
            "has_skill": "SKILL.md" in files,
            "has_example": False  # sẽ check sau
        })
    return {"folders": folders, "total": len(folders)}
