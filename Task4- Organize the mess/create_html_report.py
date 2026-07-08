import csv
from pathlib import Path
import html

OUTPUT = "folder_cleanup_report.html"


def read_csv(filename):
    path = Path(filename)

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        return list(csv.reader(f))


def make_table(title, filename):
    rows = read_csv(filename)

    if not rows:
        return f"""
        <h2>{title}</h2>
        <p>No items found.</p>
        """

    table = f"<h2>{title}</h2><table>"

    for row_index, row in enumerate(rows):
        table += "<tr>"

        for cell in row:
            if row_index == 0:
                table += f"<th>{html.escape(cell)}</th>"
            else:
                table += f"<td>{html.escape(cell)}</td>"

        table += "</tr>"

    table += "</table>"

    return table


html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Folder Cleanup Report</title>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 30px;
}

h1 {
    color: #333;
}

h2 {
    margin-top: 40px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 30px;
}

th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}

th {
    font-weight: bold;
}

tr:nth-child(even) {
    background: #f5f5f5;
}

</style>

</head>

<body>

<h1>Folder Cleanup Analysis Report</h1>

"""


# Add summary

if Path("summary.txt").exists():

    summary = Path("summary.txt").read_text(encoding="utf-8")

    html_content += """
    <h2>Summary</h2>
    <pre>
    """

    html_content += html.escape(summary)

    html_content += "</pre>"


html_content += make_table(
    "Duplicate Files (Identical Content)",
    "duplicates.csv"
)

html_content += make_table(
    "Files With Same Name",
    "same_names.csv"
)

html_content += make_table(
    "Large Files",
    "large_files.csv"
)

html_content += make_table(
    "Old Files",
    "old_files.csv"
)


html_content += """
</body>
</html>
"""


Path(OUTPUT).write_text(
    html_content,
    encoding="utf-8"
)


print("Created:")
print(OUTPUT)