from pathlib import Path

WORKSPACE = Path("workspace").resolve()

def read_file(filename: str):
    try:
        file_path = (WORKSPACE / filename).resolve()

        if not dir_path.is_dir():
            return {
                "success": False,
                "error": f"{dir_path} is not a directory"
            }

        if not str(file_path).startswith(str(WORKSPACE)):
            return {
                "success": False,
                "error": "Access denied"
            }

        if not file_path.exists():
            return {
                "success" : False,
                "error" : "File does not exist"
            }
        
        if not file_path.is_file():
            return {
                "success" : False,
                "error" : f"{filename} is not a file"
            }
        
        content = file_path.read_text(encoding='utf-8')

        return {
            "success": True,
            "path": str(file_path),
            "content":content
        }
    except Exception as e:
        return {
                "success" : False,
                "error" : str(e)
            }

def write_file(path: str, content: str):
    try:

        file_path = (WORKSPACE / path).resolve()

        if not str(file_path).startswith(str(WORKSPACE)):
            return {
                "success": False,
                "error": "Access denied"
            }
        
        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "success": True,
            "path": str(file_path),
            "bytes_written": len(content.encode("utf-8"))
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def list_files(directory: str = ""):
    try:
        dir_path = (WORKSPACE / directory).resolve()

        if not str(dir_path).startswith(str(WORKSPACE)):
            return {
                "success":False,
                "error":"Access denied"
            }
        
        if not dir_path.exists():
            return {
                "success":False,
                "error":f"{str(dir_path)} does not exist"
            }
        
        entries = []

        for item in dir_path.iterdir():
            entries.append({
                "name": item.name,
                "type": "directory" if item.is_dir() else "file"
            })

        return {
            "success":True,
            "entries": entries
        }

    except Exception as e:
        return {
            "success":False,
            "error": str(e)
        }
