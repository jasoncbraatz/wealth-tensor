import importlib.util, pathlib, json, os
R = pathlib.Path.home()/"repos/wealth-tensor"; os.chdir(R)
spec = importlib.util.spec_from_file_location("wt148", R/"scripts/wt148_promise_sweep.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
want = {"cf6cccf14b","b81698b0b2","3cf6e7157d","e3b3a9a430","aedac9e82c","4bca6e5db1","fcb2ac1551",
        "a5fce86466","a41a260fb0","684154869b"}
for stem in ("paper-III-dual-tensor/paper-III","paper-IV-composition/paper-IV"):
    for p in m.emit(R/f"docs/papers/{stem}.md"):
        if p["pid"] in want:
            print(json.dumps({"pid":p["pid"],"artefact":p["artefact"],"sentence":p["sentence"]}))
