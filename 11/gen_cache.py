import hashlib
import os

files_to_cache = [
    "includes/script.js",
    "includes/style.css",
    "patches/1100.bin",
    "patches/1102.bin",
    "src/lapse.js",
    "src/loader.js",
    "src/main.js",
    "src/misc.js",
    "src/netctrl.js",
    "src/worker.js",
    "src/workers.js",
    "src/ps4/constants.js",
    "src/ps4/userland.js",
    "src/ps4/kernel.js",
    "lapse_1100.html",
    "payload.bin",
    "logo.png",

]

print("CACHE MANIFEST")
print(f"# build {hashlib.sha256(str(os.urandom(8)).encode()).hexdigest()[:13]}\n")

for f in files_to_cache:
    if os.path.exists(f):
        hasher = hashlib.sha256()
        with open(f, "rb") as afile:
            buf = afile.read()
            hasher.update(buf)
        print(f"{f} #{hasher.hexdigest()}")
    else:
        print(f"# Missing: {f}")

print("\nNETWORK:\n*")