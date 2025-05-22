# Error Handling in Ansible

This document explains how we handle errors in our Ansible playbooks and roles to ensure resilient automation and clear diagnostics.

---

## 🔄 General Strategies

### 1. `ignore_errors: yes`

Use this to **continue execution** even if a task fails. Use **with caution**, as it can hide important failures.

        - name: This task might fail, but we continue
        command: /bin/false
        ignore_errors: yes


### 2. failed_when

Customize the failure condition for a task using expressions.


        - name: Fail only if return code is not 42
        command: some_command
        register: result
        failed_when: result.rc != 42


### 3. rescue and always blocks (like try/catch)

These provide structured error handling (since Ansible 2.0).


        - name: Try/Except style block
        block:
            - name: This might fail
            command: /bin/false
        rescue:
            - name: Handle the error
            debug:
                msg: "Something went wrong!"
        always:
            - name: Always runs
            debug:
                msg: "Cleanup or notification"


## 📝 Logging and Debugging

Use register to capture output

        - name: Run command and store output
        command: uptime
        register: uptime_output

        - name: Display command output
        debug:
            var: uptime_output.stdout


## ✅ Best Practices

Avoid ignore_errors unless absolutely needed.

Use block + rescue to catch and handle specific task failures.

Use tags to rerun only failed sections.

Store outputs with register and use debug to inspect.

Document where failures are expected and why.