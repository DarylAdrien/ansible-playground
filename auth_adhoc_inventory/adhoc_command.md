## 🟩 Syntax:

        ansible <host-pattern> -i <inventory-file> -m <module> -a "<arguments>"

host-pattern is nothig but the managed nodes (not the control node)

Example:

        ansible all -i dynamic_inventory.ini -m ping

## ✅ Basic Ad-Hoc Commands

### Task	Command
🔁 Ping all hosts	ansible all -i dynamic_inventory.ini -m ping

🖥️ Check disk usage	ansible all -i dynamic_inventory.ini -m shell -a "df -h"

📁 Create a directory	ansible all -i dynamic_inventory.ini -m file -a "path=/tmp/test_dir state=directory"

🗑️ Remove a file	ansible all -i dynamic_inventory.ini -m file -a "path=/tmp/test.txt state=absent"

📜 Run a shell command	ansible all -i dynamic_inventory.ini -m shell -a "uptime"

🔍 Check hostname	ansible all -i dynamic_inventory.ini -m command -a "hostname"

🧑 Add a user	ansible all -i dynamic_inventory.ini -m user -a "name=devuser state=present"

📦 Install a package (e.g., nginx)	ansible all -i dynamic_inventory.ini -m apt -a "name=nginx state=present update_cache=true" -b (Debian/Ubuntu)

🔥 Start a service	ansible all -i dynamic_inventory.ini -m service -a "name=nginx state=started" -b

    -b means "become root" (like using sudo)