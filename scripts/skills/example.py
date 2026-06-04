"""
Skill: Add example output to README
Appends bilingual Ví dụ output / Example output section
"""
import os

def run(readme_path, folder_name, scenario, output_lines):
    """Add example output to README
    
    Args:
        readme_path: path to README.md
        folder_name: e.g. 00-campaign-level
        scenario: Vietnamese scenario description
        output_lines: list of (VI, EN) tuples for each output line
    """
    if not os.path.exists(readme_path):
        return {"error": f"README not found: {readme_path}"}
    
    with open(readme_path) as f:
        content = f.read()
    
    # Check if example already exists
    if "Ví dụ output" in content or "Example output" in content:
        # Count existing examples
        ex_count = content.count("Ví dụ output")
        return {"error": f"Example already exists ({ex_count} sections)"}
    
    # Build VI section
    vi_parts = ["### 🎯 Ví dụ output", "", "**Đầu vào:** " + scenario, "", "**Kết quả:**"]
    for vi_line, en_line in output_lines:
        vi_parts.append(vi_line)
    vi_parts.append("")
    
    # Build EN section
    en_parts = ["### 🎯 Example output", "", "**Input:** " + scenario, "", "**Result:**"]
    for vi_line, en_line in output_lines:
        en_parts.append(en_line)
    en_parts.append("")
    
    vi_section = "\n".join(vi_parts)
    en_section = "\n".join(en_parts)
    
    # Append before the English section marker or at end
    if "## English" in content:
        parts = content.split("## English", 1)
        new_content = parts[0] + vi_section + "\n\n## English" + parts[1]
    else:
        new_content = content + "\n\n" + vi_section + "\n---\n\n" + en_section
    
    with open(readme_path, "w") as f:
        f.write(new_content)
    
    return {"status": "ok", "folder": folder_name, "lines_added": len(output_lines) * 2}
