import pexpect

# Start SSH session
child = pexpect.spawn("ssh user@remote_host")

# Wait for password prompt and send password
child.expect("password:")
child.sendline("mypassword")

# Wait for shell prompt ($) and run command
child.expect("\$")
child.sendline("ls -l")  

# Capture output of the command
child.expect("\$")
output = child.before.decode()
print("Directory listing:\n", output)

# Exit remote session
child.sendline("exit")
child.close()
