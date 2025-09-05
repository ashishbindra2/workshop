# ASSIGNMENT

## 1. **Problem:**  

You are given a list of **file paths** and a list of **allowed file extensions**. Your task is to return a dictionary where each key is a file extension from the allowed list, and the value is the count of files that have that extension.  
If a file has an extension that is not in the allowed list, it should be ignored.  

### **Example Input:**  

```python
file_paths = [
    "/home/user/docs/report.pdf",
    "/home/user/docs/data.csv",
    "/home/user/images/photo.jpg",
    "/home/user/docs/notes.txt",
    "/home/user/docs/summary.pdf",
    "/home/user/music/song.mp3"
]
allowed_extensions = ["pdf", "csv", "txt"]
```

### **Expected Output:**  

```python
{
    "pdf": 2,
    "csv": 1,
    "txt": 1
}
```

### **Instructions:**  

1. Extract the file extension from each file path.  
2. If the extension is in the `allowed_extensions` list, count its occurrences.  
3. Return a dictionary where the keys are the file extensions and the values are their counts.

---

sol

```py
from pathlib import Path

file_paths = [
    "/home/user/docs/report.pdf",
    "/home/user/docs/data.csv",
    "/home/user/images/photo.jpg",
    "/home/user/docs/notes.txt",
    "/home/user/docs/summary.pdf",
    "/home/user/music/song.mp3"
]
allowed_extensions = ["pdf", "csv", "txt"]
# d = {k:0 for k in allowed_extensions}
d = {}
path = Path("/home/user/docs/report.pdf")

for path in file_paths: 
    k = str(Path(path).suffix.lstrip('.'))
    d[k] = d.get(k,0) + 1
print(d)
```

output
> {'pdf': 2, 'csv': 1, 'jpg': 1, 'txt': 1, 'mp3': 1}

---

