import subprocess

# time = "2023/8/25 16:18:20"
# status = "Success"
# sender = "Crypto Bot"
# receiver = "Canfly's Tonkeeper Wallet"
# quantity = 0.1
# asset = "TON"


def generate_mmd(time, status, sender, receiver, quantity, asset):
    mermaid_code = f"""---
title: {time} ({status})
---
flowchart LR
    A("{sender}")
    B("{receiver}")
    A -- {quantity} {asset} --> B
"""
    return mermaid_code


async def mmd_to_png(mermaid_code):
    output_path = "si8a1.mmd"
    with open(output_path, "w") as f:
        f.write(mermaid_code)
    print("waiting for generate flow chart...")
    process = subprocess.Popen(f"mmdc -i {output_path} -o out.png", shell=True)
    process.wait()
