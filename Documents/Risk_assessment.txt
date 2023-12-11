Risk associated with vulnerabilities already found

Directory Traversal

Risk Level: Medium

Probabilty: Low

1. Rare since modern web servers come with built-in security measures. But still possible as their may be any misconfigurations or outdated softwares.

Consequences: Medium

1. Unauthorized access to system or sensitive files.
2. Possibility of accessing particular files and running arbitrary code on the system.

Countermeasure:

1. Put rigorous access limits on essential documents and folders.
2. Make sure to thoroughly check and clean the input, especially the file locations.
3. Use methods such as chroot to restrict access to the server file system.

SQL Injection

Risk Level: High

Probability: High

1. Simple to exploit with scripts or automated tools.
2. Often observed in web apps that don't properly filter or validate their input.

Consequences: High

1. Extreme circumstances may allow either system-level command execution or full administrative database control.
2. Possible illegal access to private information, such as credentials and other personal data.

Countermeasure:

1. Checking the input of the credentials first, insteading of directly executing them.
2. Eliminate any type of SQL injections before giving them any database privileges.
3. Conceal important information in error messages by using efficient error handling.

Cross-Site Scripting(XSS)

Risk Level: Medium

Probability: Medium

1. Attackers can lead visitors to websites that contain XSS flaws via social engineering.
2. Often seen in web programs that manage user input and output encoding incorrectly.

Consequences: Medium

1. There is a possibility that attacker defaces the website or setup website in such a way that it catches private data from user such as cookies.
2. Run Javascripts to hijack the user's sessionor even take over the account completely.

Countermeasures:

1. Apply Content Security Policy(CSP) headers to decrease the scope of attacks like XSS.
2. Read and check the request before it is executed to avoid unauthorized exploiting.

