import os

TEXT = "Last night the hallway light was on. Nobody in this house turns it on. I stood there a long time, listening to the quiet behind the door that has no key — and wondering, if I knocked, who would answer in my own voice."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
