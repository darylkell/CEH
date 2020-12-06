# questions from https://ceh.cagy.org

def setup():
	print("Welcome to the CEH quiz.\n\nDuring questions, enter 'q' or CTRL-C to stop, and enter multi-choice answers together like 'abc'.\n\nGood luck!")
	randomise = input("\n\nDo you want questions to be in random order? y/N\n> ")
	if "y" in randomise:
		randomise = True
		import random
		random.shuffle(questions)
	else:
		randomise = False
	answers_on_the_fly = input("Do you want your answers checked as you go? Y/n\n> ")
	if "n" in answers_on_the_fly:
		answers_on_the_fly = False
	else:
		answers_on_the_fly = True
	return randomise, answers_on_the_fly


questions = [
	{
		"question": "Which solution can be used to emulate real services such as ftp, mail, etc and capture login attempts and related information? They're often used to study hacker\u2019s activities. ",
		"num": "1",
		"correct_answer": "a",
		"answers": {
			"a": "Honeypot",
			"b": "Layer 4 switch",
			"c": "Core server",
			"d": "Firewall"
		}
	},
	{
		"question": "Keystroke logging is the action of tracking (or logging) the keys struck on a keyboard, typically in a covert manner so that the person using the keyboard is unaware that their actions are being monitored.\n\nHow will you defend against hardware keyloggers when using public computers and Internet Kiosks?\n(Select 3 answers)",
		"num": "2",
		"correct_answer": "acd",
		"answers": {
			"a": "Alternate between typing the login credentials and typing characters somewhere else in the focus window",
			"b": "Type a wrong password first, later type the correct password on the login page defeating the keylogger recording",
			"c": "Type a password beginning with the last letter and then using the mouse to move the cursor for each subsequent letter.",
			"d": "The next key typed replaces selected text portion. E.g. if the password is \"secret\", one could type \"s\",then some dummy keys \"asdfsd\".\r\nThen these dummies could be selected with mouse, and next character from the password \"e\" is typed, which replaces the dummies \"asdfsd\""
		}
	},
	{
		"question": "What type of OS fingerprinting technique sends specially crafted packets to the remote OS and analyzes the received response?",
		"num": "3",
		"correct_answer": "c",
		"answers": {
			"a": "Passive",
			"b": "Reflective",
			"c": "Active",
			"d": "Distributive"
		}
	},
	{
		"question": "What is the command used to create a binary log file using tcpdump?",
		"num": "4",
		"correct_answer": "a",
		"answers": {
			"a": "tcpdump -w ./log",
			"b": "tcpdump -r log",
			"c": "tcpdump -vde logtcpdump -vde ? log",
			"d": "tcpdump -l /var/log/"
		}
	},
	{
		"question": "Which of the following viruses tries to hide from anti-virus programs by actively altering and corrupting the chosen service call interruptions when they are being run?",
		"num": "5",
		"correct_answer": "d",
		"answers": {
			"a": "Cavity virus",
			"b": "Polymorphic virus",
			"c": "Tunneling virus",
			"d": "Stealth virus"
		}
	},
	{
		"question": "A hacker, who posed as a heating and air conditioning specialist, was able to install a sniffer program in a switched environment network.\nWhich attack could the hacker use to sniff all of the packets in the network?",
		"num": "6",
		"correct_answer": "b",
		"answers": {
			"a": "Fraggle",
			"b": "MAC Flood",
			"c": "Smurf",
			"d": "Tear Drop"
		}
	},
	{
		"question": "Which of the following settings enables Nessus to detect when it is sending too many packets and the network pipe is approaching capacity?",
		"num": "7",
		"correct_answer": "d",
		"answers": {
			"a": "Netstat WMI Scan",
			"b": "Silent Dependencies",
			"c": "Consider unscanned ports as closed",
			"d": "Reduce parallel connections on congestion"
		}
	},
	{
		"question": "When you are testing a web application, it is very useful to employ a proxy tool to save every request and response.\nYou can manually test every request and analyze the response to find vulnerabilities.\nYou can test parameter and headers manually to get more precise results than if using web vulnerability scanners.\nWhat proxy tool will help you find web vulnerabilities?",
		"num": "8",
		"correct_answer": "a",
		"answers": {
			"a": "Burpsuite",
			"b": "Proxy chains",
			"c": "Dimitry",
			"d": "Maskgen"
		}
	},
	{
		"question": "Firewall is a set of related programs, located at a network gateway server that protects the resources of a private network from users from other networks. A firewall examines all traffic routed between the two networks to see if it meets certain criteria.\nPacket filter is one of the categories of firewall.\nPacket filtering firewall works at which of these layers of the OSI model?  ",
		"num": "9",
		"correct_answer": "a",
		"answers": {
			"a": "Network layer",
			"b": "Physical layer",
			"c": "Session layer",
			"d": "Application layer"
		}
	},
	{
		"question": "Nation-state threat actors often discover vulnerabilities and hold on to them until they want to launch a sophisticated attack. Stuxnet attack was an unprecedented style of attack because it used four types of this vulnerability. What is this style of attack called?",
		"num": "10",
		"correct_answer": "b",
		"answers": {
			"a": "zero-sum",
			"b": "zero-day",
			"c": "no-day",
			"d": "zero-hour"
		}
	},
	{
		"question": "What is the correct command to run Netcat on a server using port 56 that spawns command shell when connected?",
		"num": "11",
		"correct_answer": "d",
		"answers": {
			"a": "nc -port 56 -s cmd.exe",
			"b": "nc -p 56 -p -e shell.exe",
			"c": "nc -r 56 -c cmd.exe",
			"d": "nc -L 56 -t -e cmd.exe"
		}
	},
	{
		"question": "To determine if a software program properly handles a wide range of invalid input, a form of automated testing can be used to randomly generate invalid input in an attempt to crash the program.\nWhat term is commonly used when referring to this type of testing?",
		"num": "12",
		"correct_answer": "c",
		"answers": {
			"a": "Mutating",
			"b": "Randomizing",
			"c": "Fuzzing",
			"d": "Bounding"
		}
	},
	{
		"question": "What does ICMP (type 11, code 0) denote?",
		"num": "13",
		"correct_answer": "c",
		"answers": {
			"a": "Source Quench",
			"b": "Destination Unreachable",
			"c": "Time Exceeded",
			"d": "Unknown Type"
		}
	},
	{
		"question": "Bob has a good understanding of cryptography, having worked with it for many years. Cryptography is used\nto secure data from specific threats, but it does not secure the application from coding errors. It can provide\ndata privacy; integrity and enable strong authentication but it cannot mitigate programming errors. What is a\ngood example of a programming error that Bob can use to explain to the management how encryption will\nnot address all their security concerns?\n  ",
		"num": "14",
		"correct_answer": "a",
		"answers": {
			"a": "Bob can explain that using a weak key management technique is a form of programming error",
			"b": "Bob can explain that using passwords to derive cryptographic keys is a form of a programming error",
			"c": "Bob can explain that a buffer overflow is an example of programming error and it is a common mistake associated with poor programming technique",
			"d": "Bob can explain that a random number generator can be used to derive cryptographic keys but it uses a weak seed value and this is a form of a programming error"
		}
	},
	{
		"question": "Leesa is the senior security analyst for a publicly traded company. The IT department recently rolled out an intranet for company use only with information ranging from training, to holiday schedules, to human resources data. Leesa wants to make sure the site is not accessible from outside and she also wants to ensure the site is Sarbanes-Oxley (SOX) compliant. Leesa goes to a public library as she wants to do some Google searching to verify whether the company's intranet is accessible from outside and has been indexed by Google. Leesa wants to search for a website title of \"intranet\" with part of the URL containing the word \"intranet\" and the words \"human resources\" somewhere in the webpage. What Google search will accomplish this?",
		"num": "15",
		"correct_answer": "c",
		"answers": {
			"a": "related:intranet allinurl:intranet:\"human resources\"",
			"b": "cache:\"human resources\" inurl:intranet(SharePoint)",
			"c": "intitle:intranet inurl:intranet+intext:\"human resources\"",
			"d": "site:\"human resources\"+intext:intranet intitle:intranet"
		}
	},
	{
		"question": "Penetration testing is a method of actively evaluating the security of an information system or network by simulating an attack from a malicious source.\nWhich of the following technique is used to simulate an attack from someone who is unfamiliar with the system?",
		"num": "16",
		"correct_answer": "a",
		"answers": {
			"a": "Black box pen testing",
			"b": "White box pen testing",
			"c": "Grey box pen testing",
			"d": "Maintaining Access",
			"e": "Announced pen testing"
		}
	},
	{
		"question": "Charlie is the network administrator for his company. Charlie just received a new Cisco router and wants to test its capabilities out and to see if it might be susceptible to a DoS attack resulting in its locking up.\nThe IP address of the Cisco switch is 172.16.0.45.\nWhat command can Charlie use to attempt this task?",
		"num": "17",
		"correct_answer": "a",
		"answers": {
			"a": "Charlie can use the command ping -l 56550 172.16.0.45 -t.",
			"b": "Charlie can try using the command ping 56550 172.16.0.45.",
			"c": "By using the command ping 172.16.0.45 Charlie would be able to lockup the router",
			"d": "He could use the command ping -4 56550 172.16.0.45."
		}
	},
	{
		"question": "This kind of malware is installed by criminals on your computer so they can lock it from a remote location. This malware generates a popup window, webpage, or\nemail warning from what looks like an official authority such as the FBI. It explains your computer has been locked because of possible illegal activities and\ndemands payment before you can access your files and programs again. Which term best matches this definition?\n\nCorrect Answer:",
		"num": "18",
		"correct_answer": "a",
		"answers": {
			"a": "Ransomware",
			"b": "Adware",
			"c": "Riskware",
			"d": "Spyware"
		}
	},
	{
		"question": "Under the \"Post-attack Phase and Activities,\" it is the responsibility of the tester to restore the systems to a pre-test state.\n\nWhich of the following activities should not be included in this phase?\nI. Removing all files uploaded on the system\nII. Cleaning all registry entries\nIII. Removing all tools and maintaining backdoor for reporting\nIV. Mapping of network state",
		"num": "19",
		"correct_answer": "a",
		"answers": {
			"a": "III",
			"b": "III and IV",
			"c": "IV",
			"d": "All should be included"
		}
	},
	{
		"question": "Oregon Corp is fighting a litigation suit with Scamster Inc.\nOregon has assigned a private investigative agency to go through garbage, recycled paper, and other rubbish at Scamster's office site in order to find relevant information.\nWhat would you call this kind of activity?",
		"num": "20",
		"correct_answer": "c",
		"answers": {
			"a": "CI Gathering",
			"b": "Scanning",
			"c": "Dumpster Diving",
			"d": "Garbage Scooping"
		}
	},
	{
		"question": "Which utility will tell you in real time which ports are listening or in another state?",
		"num": "21",
		"correct_answer": "d",
		"answers": {
			"a": "Netview",
			"b": "Loki",
			"c": "Nmap",
			"d": "TCPView"
		}
	},
	{
		"question": "Address Resolution Protocol (ARP) is a protocol for mapping an IP address to a physical machine address that is recognized in the local network.\nARP Spoofing involves constructing a large number of forged ARP request and reply packets to overload:",
		"num": "22",
		"correct_answer": "a",
		"answers": {
			"a": "Switch",
			"b": "Router",
			"c": "Hub",
			"d": "Bridge"
		}
	},
	{
		"question": "Which of the following activities is not considered to be anti-forensics?",
		"num": "23",
		"correct_answer": "a",
		"answers": {
			"a": "Data sanitizing",
			"b": "Trail obfuscation",
			"c": "Artifact wiping",
			"d": "Data hiding"
		}
	},
	{
		"question": "The TJ Max breach happened in part because this type of weak wireless security was implemented.",
		"num": "24",
		"correct_answer": "c",
		"answers": {
			"a": "WiFi Protected Access (WPA)",
			"b": "TKIP",
			"c": "Wired Equivalent Privacy (WEP)",
			"d": "WPA2"
		}
	},
	{
		"question": "It is a short-range wireless communication technology intended to replace the cables connecting portable or fixed devices while maintaining high levels of security.\nIt allows mobile phones, computers and other devices to connect and communicate using a short-range wireless connection.\nWhich of the following terms best matches the definition?",
		"num": "25",
		"correct_answer": "a",
		"answers": {
			"a": "Bluetooth",
			"b": "WLAN",
			"c": "InfraRed",
			"d": "Radio-Frequency identification"
		}
	},
	{
		"question": "Perspective clients want to see sample reports from previous penetration tests. What should you do next?",
		"num": "26",
		"correct_answer": "a",
		"answers": {
			"a": "Decline, just provide the details of the components that will be there in the report.",
			"b": "Share full reports, not redacted.",
			"c": "Decline, just provide references.",
			"d": "Share sample reports with redactions after NDA is signed."
		}
	},
	{
		"question": "_____________ is a type of symmetric-key encryption algorithm that transforms a fixed-length block of plaintext (unencrypted text) data into a block of ciphertext (encrypted text) data of the same length.",
		"num": "27",
		"correct_answer": "b",
		"answers": {
			"a": "Stream Cipher",
			"b": "Block Cipher",
			"c": "Bit Cipher",
			"d": "Hash Cipher"
		}
	},
	{
		"question": "The precaution of prohibiting employees from bringing personal computing devices into a facility is what type of security control?",
		"num": "28",
		"correct_answer": "b",
		"answers": {
			"a": "Physical",
			"b": "Procedural",
			"c": "Technical",
			"d": "Compliance"
		}
	},
	{
		"question": "How do you defend against Privilege Escalation?",
		"num": "29",
		"correct_answer": "abce",
		"answers": {
			"a": "Use encryption to protect sensitive data",
			"b": "Restrict the interactive logon privileges",
			"c": "Run services as unprivileged accounts",
			"d": "Allow security settings of IE to zero or Low",
			"e": "Run users and applications on the least privileges"
		}
	},
	{
		"question": "An Internet Service Provider (ISP) has a need to authenticate users connecting using analog modems,\nDigital Subscriber Lines (DSL), wireless data services, and Virtual Private Networks (VPN) over a Frame Relay network.\nWhich AAA protocol is most likely able to handle this requirement?",
		"num": "30",
		"correct_answer": "a",
		"answers": {
			"a": "RADIUS",
			"b": "Kerberos",
			"c": "DIAMETER",
			"d": "TACACS+"
		}
	},
	{
		"question": "What two conditions must a digital signature meet?",
		"num": "31",
		"correct_answer": "b",
		"answers": {
			"a": "Has to be legible and neat.",
			"b": "Has to be unforgeable, and has to be authentic.",
			"c": "Must be unique and have special characters.",
			"d": "Has to be the same number of characters as a physical signature and must be unique."
		}
	},
	{
		"question": "A developer for a company is tasked with creating a program that will allow customers to update their billing and shipping information.\nThe billing address field used is limited to 50 characters.\nWhat pseudo code would the developer use to avoid a buffer overflow attack on the billing address field?",
		"num": "32",
		"correct_answer": "d",
		"answers": {
			"a": "if (billingAddress = 50) {update field} else exit",
			"b": "if (billingAddress != 50) {update field} else exit",
			"c": "if (billingAddress >= 50) {update field} else exit",
			"d": "if (billingAddress <= 50) {update field} else exit"
		}
	},
	{
		"question": "You are footprinting an organization and gathering competitive intelligence. You visit the company's website for contact information and telephone numbers but do not find them listed there. You know they had the entire staff directory listed on their website 12 months ago but now it is not \n here. Is there any way you can retrieve information from a website that is outdated?",
		"num": "33",
		"correct_answer": "c",
		"answers": {
			"a": "Visit Google's search engine and view the cached copy",
			"b": "Crawl the entire website and store them into your computer",
			"c": "Visit Archive.org web site to retrieve the Internet archive of the company's website",
			"d": "Visit the company's partners and customers website for this information"
		}
	},
	{
		"question": "An attacker has been successfully modifying the purchase price of items purchased on the company's web site.\nThe security administrators verify the web server and Oracle database have not been compromised directly.\nThey have also verified the Intrusion Detection System (IDS) logs and found no attacks that could have caused this.\nWhat is the mostly likely way the attacker has been able to modify the purchase price?",
		"num": "34",
		"correct_answer": "b",
		"answers": {
			"a": "By using SQL injection",
			"b": "By changing hidden form values",
			"c": "By using cross site scripting",
			"d": "By utilizing a buffer overflow attack"
		}
	},
	{
		"question": "which one of these BEST describes a Buffer Overflow attack that allows access to a remote system?",
		"num": "35",
		"correct_answer": "c",
		"answers": {
			"a": "The attacker attempts to have the receiving server pass information to a back-end database from which it can compromise the stored information",
			"b": "The attacker overwhelms a system or application, causing a crash and bringing the server down to cause an outage",
			"c": "The attacker overwhelms a system or application, causing it to crash, and then redirects the memory address to read from a location holding the payload.",
			"d": "The attacker attempts to have the receiving server run a payload using programming commonly found on web servers"
		}
	},
	{
		"question": "Kevin is an IT security analyst working for Emerson Time Makers, a watch manufacturing company in Miami.\nKevin and his girlfriend Katy recently broke up after a big fight. Kevin believes that she was seeing another person.\nKevin, who has an online email account that he uses for most of his mail, knows that Katy has an account with that same company.\nKevin logs into his email account online and gets the following URL after successfully logged in:\nhttp://www.youremailhere.com/mail.asp?mailbox=Kevin&Smith=121%22\n\nKevin changes the URL to:\nhttp://www.youremailhere.com/mail.asp?mailbox=Katy&Sanchez=121%22\n\nKevin is trying to access her email account to see if he can find out any information.\nWhat is Kevin attempting here to gain access to Katy's mailbox?",
		"num": "36",
		"correct_answer": "c",
		"answers": {
			"a": "This type of attempt is called URL obfuscation when someone manually changes a URL to try and gain unauthorized access",
			"b": "By changing the mailbox's name in the URL, Kevin is attempting directory transversal",
			"c": "Kevin is trying to utilize query string manipulation to gain access to her email account",
			"d": "He is attempting a path-string attack to gain access to her mailbox"
		}
	},
	{
		"question": "Which of the following are types of buffer overflow?",
		"num": "37",
		"correct_answer": "c",
		"answers": {
			"a": "Heap-based",
			"b": "Stack-based",
			"c": "Both Stack-based and Heap-based",
			"d": "Dynamic-based"
		}
	},
	{
		"question": "Which of the following scanning method splits the TCP header into several packets and makes it difficult for packet filters to detect the purpose of the packet?",
		"num": "38",
		"correct_answer": "b",
		"answers": {
			"a": "ICMP Echo scanning",
			"b": "SYN/FIN scanning using IP fragments",
			"c": "ACK flag probe scanning",
			"d": "IPID scanning"
		}
	},
	{
		"question": "The term that is best described as a process of replacing unwanted bits in an image and its source files with the secret data is known as_____.",
		"num": "39",
		"correct_answer": "b",
		"answers": {
			"a": "Forensic Analysis",
			"b": "Steganography",
			"c": "Network Analysis",
			"d": "Cryptography"
		}
	},
	{
		"question": "How can telnet be used to fingerprint a web server?",
		"num": "40",
		"correct_answer": "a",
		"answers": {
			"a": "telnet webserverAddress 80 HEAD / HTTP/1.0",
			"b": "telnet webserverAddress 80 PUT / HTTP/1.0",
			"c": "telnet webserverAddress 80 HEAD / HTTP/2.0",
			"d": "telnet webserverAddress 80 PUT / HTTP/2.0"
		}
	},
	{
		"question": "A virus is a self-replicating program that produces its own code by attaching copies of it into other executable codes.\n\nWhich of the following virus evade the anti-virus software by intercepting its requests to the operating system?",
		"num": "41",
		"correct_answer": "a",
		"answers": {
			"a": "Stealth/Tunneling virus",
			"b": "Cluster virus",
			"c": "Macro virus",
			"d": "System or boot sector virus"
		}
	},
	{
		"question": "Which of the following lists are valid data-gathering activities associated with a risk assessment?",
		"num": "42",
		"correct_answer": "a",
		"answers": {
			"a": "Threat identification, vulnerability identification, control analysis",
			"b": "Threat identification, response identification, mitigation identification",
			"c": "Attack profile, defense profile, loss profile",
			"d": "System profile, vulnerability identification, security determination"
		}
	},
	{
		"question": "How would you describe an attack where an attacker attempts to deliver the payload over multiple packets\nover long periods of time with the purpose of defeating simple pattern matching in IDS systems without\nsession reconstruction? A characteristic of this attack would be a continuous stream of small packets.",
		"num": "43",
		"correct_answer": "c",
		"answers": {
			"a": "Session Hijacking",
			"b": "Session Stealing",
			"c": "Session Splicing",
			"d": "Session Fragmentation"
		}
	},
	{
		"question": "Which of the following is the successor of SSL?",
		"num": "44",
		"correct_answer": "d",
		"answers": {
			"a": "GRE",
			"b": "IPSec",
			"c": "RSA",
			"d": "TLS"
		}
	},
	{
		"question": "Which of the following Wi-Fi chalking method refers to drawing symbols in public places to advertise open Wi-Fi networks?",
		"num": "45",
		"correct_answer": "c",
		"answers": {
			"a": "WarWalking",
			"b": "WarFlying",
			"c": "WarChalking ",
			"d": "WarDriving"
		}
	},
	{
		"question": "SOAP services use which technology to format information?",
		"num": "46",
		"correct_answer": "c",
		"answers": {
			"a": "SATA",
			"b": "PCI",
			"c": "XML",
			"d": "ISDN"
		}
	},
	{
		"question": "Choose one of the following pseudo codes to describe this statement:\n\"If we have written 200 characters to the buffer variable, the stack should stop because it cannot hold any more data.\"",
		"num": "47",
		"correct_answer": "d",
		"answers": {
			"a": "If (I > 200) then exit (1)",
			"b": "If (I < 200) then exit (1)",
			"c": "If (I <= 200) then exit (1)",
			"d": "If (I >= 200) then exit (1)"
		}
	},
	{
		"question": "How is sniffing broadly categorized?",
		"num": "48",
		"correct_answer": "a",
		"answers": {
			"a": "Active and passive",
			"b": "Broadcast and unicast",
			"c": "Unmanaged and managed",
			"d": "Filtered and unfiltered"
		}
	},
	{
		"question": "Which of the following algorithms provides better protection against brute force attacks by using a 160-bit message digest?",
		"num": "49",
		"correct_answer": "b",
		"answers": {
			"a": "MD5",
			"b": "SHA-1",
			"c": "RC4",
			"d": "MD4"
		}
	},
	{
		"question": "After trying multiple exploits, you've gained root access to a Centos 6 server. To ensure you maintain access, what would you do first?",
		"num": "50",
		"correct_answer": "d",
		"answers": {
			"a": "Disable Key Services",
			"b": "Create User Account",
			"c": "Disable IPTables",
			"d": "Download and Install Netcat"
		}
	},
	{
		"question": "An attacker is attempting to telnet into a corporation's system in the DMZ.\nThe attacker doesn't want to get caught and is spoofing his IP address.\nAfter numerous tries he remains unsuccessful in connecting to the system.\nThe attacker rechecks that the target system is actually listening on Port 23 and he verifies it with both nmap and hping2.\nHe is still unable to connect to the target system.\nWhat could be the reason?",
		"num": "51",
		"correct_answer": "c",
		"answers": {
			"a": "The firewall is blocking port 23 to that system",
			"b": "He needs to use an automated tool to telnet in",
			"c": "He cannot spoof his IP and successfully use TCP",
			"d": "He is attacking an operating system that does not reply to telnet even when open"
		}
	},
	{
		"question": "What does FIN in TCP flag define?",
		"num": "52",
		"correct_answer": "b",
		"answers": {
			"a": "Used to abort a TCP connection abruptly",
			"b": "Used to close a TCP connection",
			"c": "Used to acknowledge receipt of a previous packet or transmission",
			"d": "Used to indicate the beginning of a TCP connection"
		}
	},
	{
		"question": "You are attempting to man-in-the-middle a session.\nWhich protocol will allow you to guess a sequence number?",
		"num": "53",
		"correct_answer": "b",
		"answers": {
			"a": "ICMP",
			"b": "TCP",
			"c": "UPX",
			"d": "UPD"
		}
	},
	{
		"question": "Which type of antenna is used in wireless communication?",
		"num": "54",
		"correct_answer": "a",
		"answers": {
			"a": "Omnidirectional",
			"b": "Parabolic",
			"c": "Uni-directional",
			"d": "Bi-directional"
		}
	},
	{
		"question": "You've just been hired to perform a pen test on an organization that has been subjected to a large-scale attack.\nThe CIO is concerned with mitigating threats and vulnerabilities to totally eliminate risk. What is one of the first things you should do when given the job?",
		"num": "55",
		"correct_answer": "a",
		"answers": {
			"a": "Explain to the CIO that you cannot eliminate all risk, but you will be able to reduce risk to acceptable levels.",
			"b": "Interview all employees in the company to rule out possible insider threats",
			"c": "Establish attribution to suspected attackers",
			"d": "Start the Wireshark application to start sniffing network traffic."
		}
	},
	{
		"question": "Hampton is the senior security analyst for the city of Columbus in Ohio. His primary responsibility is to ensure that all physical and logical aspects of the city's computer network are secure from all angles. Bill is an IT technician that works with Hampton in the same IT department. Bill's primary responsibility is to keep PC's and servers up to date and to keep track of all the agency laptops that the company owns and lends out to its employees. After Bill setup a wireless network for the agency, Hampton made sure that everything was secure. He instituted encryption, rotating keys, turned off SSID broadcasting, and enabled MAC filtering. According to agency policy, only company laptops are allowed to use the wireless network, so Hampton entered all the MAC addresses for those laptops into the wireless security utility so that only those laptops should be able to access the wireless network.\nHampton does not keep track of all the laptops, but he is pretty certain that the agency only purchases Dell laptops. Hampton is curious about this because he notices Bill working on a Toshiba laptop one day and saw that he was on the Internet. Instead of jumping to conclusions, Hampton decides to talk to Bill's \n boss and see if they had purchased a Toshiba laptop instead of the usual Dell. Bill's boss said no, so now Hampton is very curious to see how Bill is accessing the Internet. Hampton does site surveys every couple of days, and has yet to see any outside wireless network signals inside the company's building.\nHow was Bill able to get Internet access without using an agency laptop?",
		"num": "56",
		"correct_answer": "a",
		"answers": {
			"a": "Bill spoofed the MAC address of Dell laptop",
			"b": "Bill connected to a Rogue access point",
			"c": "Toshiba and Dell laptops share the same hardware address",
			"d": "Bill brute forced the Mac address ACLs"
		}
	},
	{
		"question": "What is the primary drawback to using advanced encryption standard (AES) algorithm with a 256 bit key to share sensitive data?",
		"num": "57",
		"correct_answer": "d",
		"answers": {
			"a": "Due to the key size, the time it will take to encrypt and decrypt the message hinders efficient communication.",
			"b": "To get messaging programs to function with this algorithm requires complex configurations.",
			"c": "It has been proven to be a weak cipher; therefore, should not be trusted to protect sensitive data.",
			"d": "It is a symmetric key algorithm, meaning each recipient must receive the key through a different channel than the message."
		}
	},
	{
		"question": "How do you defend against ARP Spoofing? Select three.",
		"num": "58",
		"correct_answer": "acd",
		"answers": {
			"a": "Use ARPWALL system and block ARP spoofing attacks",
			"b": "Tune IDS Sensors to look for large amount of ARP traffic on local subnets",
			"c": "Use private VLANS",
			"d": "Place static ARP entries on servers, workstation and routers"
		}
	},
	{
		"question": "TCP SYN Flood attack uses the three-way handshake mechanism.\n1. An attacker at system A sends a SYN packet to victim at system \n2. System B sends a SYN/ACK packet to victim A.\n3. As a normal three-way handshake mechanism system A should send an ACK packet to system B, however, system A does not send an ACK packet to system B.\nIn this case client B is waiting for an ACK packet from client A.\nThis status of client B is called ____________",
		"num": "59",
		"correct_answer": "b",
		"answers": {
			"a": "\"half-closed\"",
			"b": "\"half open\"",
			"c": "\"full-open\"",
			"d": "\"xmas-open\""
		}
	},
	{
		"question": "In order to have an anonymous Internet surf, which of the following is best choice?",
		"num": "60",
		"correct_answer": "b",
		"answers": {
			"a": "Use SSL sites when entering personal information",
			"b": "Use Tor network with multi-node",
			"c": "Use shared WiFi",
			"d": "Use public VPN"
		}
	},
	{
		"question": "The purpose of a _______is to deny network access to local area networks and other information assets by unauthorized wireless devices.\n",
		"num": "61",
		"correct_answer": "d",
		"answers": {
			"a": "Wireless Analyzer",
			"b": "Wireless Jammer",
			"c": "Wireless Access Point",
			"d": "Wireless Access Control List"
		}
	},
	{
		"question": "Which of the following identifies the three modes in which Snort can be configured to run?",
		"num": "62",
		"correct_answer": "a",
		"answers": {
			"a": "Sniffer, Packet Logger, and Network Intrusion Detection System",
			"b": "Sniffer, Network Intrusion Detection System, and Host Intrusion Detection System",
			"c": "Sniffer, Host Intrusion Prevention System, and Network Intrusion Prevention System",
			"d": "Sniffer, Packet Logger, and Host Intrusion Prevention System"
		}
	},
	{
		"question": "An engineer is learning to write exploits in C++ and is using the exploit tool Backtrack.\nThe engineer wants to compile the newest C++ exploit and name it calc.exe.\nWhich command would the engineer use to accomplish this?",
		"num": "63",
		"correct_answer": "a",
		"answers": {
			"a": "g++ hackersExploit.cpp -o calc.exe",
			"b": "g++ hackersExploit.py -o calc.exe",
			"c": "g++ -i hackersExploit.pl -o calc.exe",
			"d": "g++ --compile i hackersExploit.cpp -o calc.exe"
		}
	},
	{
		"question": "Steve scans the network for SNMP enabled devices. Which port number Steve should scan?",
		"num": "64",
		"correct_answer": "b",
		"answers": {
			"a": "150",
			"b": "161",
			"c": "169",
			"d": "69"
		}
	},
	{
		"question": "Bob was frustrated with his competitor, Brownies Inc., and decided to launch an attack that would result in serious financial losses.\nHe planned the attack carefully and carried out the attack at the appropriate moment.\nMeanwhile, Trent, an administrator at Brownies Inc., realized that their main financial transaction server had been attacked.\nAs a result of the attack, the server crashed and Trent needed to reboot the system, as no one was able to access the resources of the company.\nThis process  involves human interaction to fix it.\nWhat kind of Denial of Service attack was best illustrated in the scenario above?",
		"num": "65",
		"correct_answer": "c",
		"answers": {
			"a": "Simple DDoS attack",
			"b": "DoS attacks which involves flooding a network or system",
			"c": "DoS attacks which involves crashing a network or system",
			"d": "DoS attacks which is done accidentally or deliberately"
		}
	},
	{
		"question": "Websites and web portals that provide web services commonly use the Simple Object Access Protocol (SOAP).\nWhich of the following is an incorrect definition or characteristics of the protocol?",
		"num": "66",
		"correct_answer": "b",
		"answers": {
			"a": "Based on XML",
			"b": "Only compatible with the application protocol HTTP",
			"c": "Exchanges data between web services",
			"d": "Provides a structured model for messaging"
		}
	},
	{
		"question": "Which of the following problems can be solved by using Wireshark?",
		"num": "67",
		"correct_answer": "b",
		"answers": {
			"a": "Resetting the administrator password on multiple systems",
			"b": "Troubleshooting communication resets between two systems",
			"c": "Tracking version changes of source code",
			"d": "Checking creation dates on all webpages on a server"
		}
	},
	{
		"question": "Which of the following descriptions is true about a static NAT?",
		"num": "68",
		"correct_answer": "d",
		"answers": {
			"a": "A static NAT uses a many-to-many mapping.",
			"b": "A static NAT uses a one-to-many mapping.",
			"c": "A static NAT uses a many-to-one mapping.",
			"d": "A static NAT uses a one-to-one mapping."
		}
	},
	{
		"question": "Which of the following is a protocol that is prone to a man-in-the-middle (MITM) attack and maps a 32-bit address to a 48-bit address?",
		"num": "69",
		"correct_answer": "b",
		"answers": {
			"a": "ICPM",
			"b": "ARP",
			"c": "RARP",
			"d": "ICMP"
		}
	},
	{
		"question": "An attacker has successfully compromised a remote computer. Which of the following comes as one of the last steps that should be taken to ensure that the compromise cannot be traced back to the source of the problem?",
		"num": "70",
		"correct_answer": "d",
		"answers": {
			"a": "Install patches",
			"b": "Setup a backdoor",
			"c": "Install a zombie for DDOS",
			"d": "Cover your tracks"
		}
	},
	{
		"question": "The Open Web Application Security Project (OWASP) is the worldwide not-for-profit charitable organization focused on improving the security of software.\nWhat item is the primary concern on OWASP\u2019s Top Ten Project Most Critical Web Application Security Risks?",
		"num": "71",
		"correct_answer": "b",
		"answers": {
			"a": "Cross Site Scripting",
			"b": "Injection",
			"c": "Path disclosure",
			"d": "Cross Site Request Forgery"
		}
	},
	{
		"question": "Which of the following Bluetooth hacking techniques does an attacker use to send messages to users without the recipient\u2019s consent, similar to email spamming?",
		"num": "72",
		"correct_answer": "d",
		"answers": {
			"a": "Bluesmacking",
			"b": "Bluesniffing",
			"c": "Bluesnarfing",
			"d": "Bluejacking"
		}
	},
	{
		"question": "Your company has blocked all the ports via external firewall and only allows port 80/443 to connect to the Internet.\nYou want to use FTP to connect to some remote server on the Internet.\nHow would you accomplish this?",
		"num": "73",
		"correct_answer": "a",
		"answers": {
			"a": "Use HTTP Tunneling",
			"b": "Use Proxy Chaining",
			"c": "Use TOR Network",
			"d": "Use Reverse Chaining"
		}
	},
	{
		"question": "You have invested millions of dollars for protecting your corporate network. You have the best IDS, firewall with strict rules and routers with no configuration errors.\nWhich of the following techniques practiced by an attacker exploits human behavior to make your network vulnerable to attacks? ",
		"num": "74",
		"correct_answer": "a",
		"answers": {
			"a": "Social Engineering",
			"b": "Buffer overflow",
			"c": "Denial of Service",
			"d": "SQL injection"
		}
	},
	{
		"question": "Joel and her team have been going through tons of garbage, recycled paper, and other rubbish in order to find Some information about the target they are attempting to penetrate.\nHow would you call this type of activity?",
		"num": "75",
		"correct_answer": "a",
		"answers": {
			"a": "Dumpster Diving",
			"b": "Scanning",
			"c": "CI Gathering",
			"d": "Garbage Scooping"
		}
	},
	{
		"question": "Which of the following antennas is commonly used in communications for a frequency band of 10 MHz to VHF and UHF?",
		"num": "76",
		"correct_answer": "c",
		"answers": {
			"a": "Omnidirectional antenna",
			"b": "Dipole antenna",
			"c": "Yagi antenna",
			"d": "Parabolic grid antenna"
		}
	},
	{
		"question": "An individual who aims to bring down critical infrastructure for a \"cause\" and is not worried about facing 30 years in jail for their action.",
		"num": "77",
		"correct_answer": "b",
		"answers": {
			"a": "Black Hat",
			"b": "Suicide Hacker",
			"c": "Gray Hat",
			"d": "White Hat"
		}
	},
	{
		"question": "A network administrator received an administrative alert at 3:00 a.m. from the intrusion detection system.\nThe alert was generated because a large number of packets were coming into the network over ports 20 and 21.\nDuring analysis, there were no signs of attack on the FTP servers.\nHow should the administrator classify this situation?",
		"num": "78",
		"correct_answer": "d",
		"answers": {
			"a": "True negatives",
			"b": "False negatives",
			"c": "True positives",
			"d": "False positives"
		}
	},
	{
		"question": "Which of the following program infects the system boot sector and the executable files at the same time?",
		"num": "79",
		"correct_answer": "d",
		"answers": {
			"a": "Stealth virus",
			"b": "Polymorphic virus",
			"c": "Macro virus",
			"d": "Multipartite Virus"
		}
	},
	{
		"question": "Which of the following network attacks relies on sending an abnormally large packet size that exceeds TCP/IP specifications?",
		"num": "80",
		"correct_answer": "a",
		"answers": {
			"a": "Ping of death",
			"b": "SYN flooding",
			"c": "TCP hijacking",
			"d": "Smurf attack"
		}
	},
	{
		"question": "Which of the following protocols are susceptible to sniffing? ",
		"num": "81",
		"correct_answer": "d",
		"answers": {
			"a": "SNMP",
			"b": "FTP",
			"c": "NNTP",
			"d": "Telnet"
		}
	},
	{
		"question": "Which regulation defines security and privacy controls for Federal information systems and organizations?",
		"num": "82",
		"correct_answer": "d",
		"answers": {
			"a": "EU Safe Harbor",
			"b": "PCI-DSS",
			"c": "HIPAA",
			"d": "NIST-800-53"
		}
	},
	{
		"question": "The use of technologies like IPSec can help guarantee the following: authenticity, integrity, confidentiality and",
		"num": "83",
		"correct_answer": "a",
		"answers": {
			"a": "non-repudiation.",
			"b": "operability.",
			"c": "security.",
			"d": "usability."
		}
	},
	{
		"question": "NTP allows you to set the clocks on your systems very accurately, to within 100ms and sometimes-even 10ms.\nKnowing the exact time is extremely important for enterprise security.\nVarious security protocols depend on an accurate source of time information in order to prevent \"playback\" attacks.\nThese protocols tag their communications with the current time, to prevent attackers from replaying the same communications, e.g., a login/password interaction or even an entire communication, at a later date.\nOne can circumvent this tagging, if the clock can be set back to the time the communication was recorded.\nAn attacker attempts to try corrupting the clocks on devices on your network.\nYou run Wireshark to detect the NTP traffic to see if there are any irregularities on the network.\n\nWhat port number you should enable in Wireshark display filter to view NTP packets?",
		"num": "84",
		"correct_answer": "c",
		"answers": {
			"a": "TCP Port 124",
			"b": "UDP Port 125",
			"c": "UDP Port 123",
			"d": "TCP Port 126"
		}
	},
	{
		"question": "Which devices are causing difficulty for security administrators in the workplace to maintain secure networks?",
		"num": "85",
		"correct_answer": "d",
		"answers": {
			"a": "copiers",
			"b": "laptops",
			"c": "scanners",
			"d": "Employees' personal devices"
		}
	},
	{
		"question": "Which NMAP command combination would let a tester scan every TCP port from a class C network that is blocking ICMP with fingerprinting and service detection?",
		"num": "86",
		"correct_answer": "b",
		"answers": {
			"a": "NMAP -PN -A -O -sS 192.168.2.0/24",
			"b": "NMAP -P0 -A -O -p1-65535 192.168.0/24",
			"c": "NMAP -P0 -A -sT -p0-65535 192.168.0/16",
			"d": "NMAP -PN -O -sS -p 1-1024 192.168.0/8"
		}
	},
	{
		"question": "During a black box pen test you attempt to pass IRC traffic over port 80/TCP from a compromised web enabled host.\nThe traffic gets blocked; however, outbound HTTP traffic is unimpeded.\nWhat type of firewall is inspecting outbound traffic?",
		"num": "87",
		"correct_answer": "d",
		"answers": {
			"a": "Packet Filtering",
			"b": "Application",
			"c": "Circuit",
			"d": "Stateful"
		}
	},
	{
		"question": "Which form of steganography generally includes a replication of an image so that any document source can be authenticated in a partial manner?",
		"num": "88",
		"correct_answer": "c",
		"answers": {
			"a": "BMP tagging",
			"b": "Time stamp",
			"c": "Digital watermarking",
			"d": "Date stamp"
		}
	},
	{
		"question": "Which of the following is an advantage of utilizing security testing methodologies to conduct a security audit?",
		"num": "89",
		"correct_answer": "a",
		"answers": {
			"a": "They provide a repeatable framework.",
			"b": "Anyone can run the command line scripts.",
			"c": "They are available at low cost.",
			"d": "They are subject to government regulation."
		}
	},
	{
		"question": "A company has made the decision to host their own email and basic web services.\nThe administrator needs to set up the external firewall to limit what protocols should be allowed to get to the public part of the company's network.\nWhich ports should the administrator open?\nChoose three answers",
		"num": "90",
		"correct_answer": "cde",
		"answers": {
			"a": "Port 22",
			"b": "Port 23",
			"c": "Port 25",
			"d": "Port 53",
			"e": "Port 80",
			"f": "Port 139",
			"g": "Port 445"
		}
	},
	{
		"question": "Based on the below log, which of the following sentences are true?\n\nMar 1, 2016, 7:33:28 AM 10.240.250.23 \u2013 54373 10.249.253.15 \u2013 22 tcp_ip",
		"num": "91",
		"correct_answer": "c",
		"answers": {
			"a": "SSH communications are encrypted it\u2019s impossible to know who is the client or the server",
			"b": "Application is FTP and 10.240.250.23 is the client and 10.249.253.15 is the server",
			"c": "Application is SSH and 10.240.250.23 is the client and 10.249.253.15 is the server",
			"d": "Application is SSH and 10.240.250.23 is the server and 10.249.253.15 is the server"
		}
	},
	{
		"question": "What sequence of packets is sent during the initial TCP three-way handshake?",
		"num": "92",
		"correct_answer": "a",
		"answers": {
			"a": "SYN, SYN-ACK, ACK",
			"b": "SYN, URG, ACK",
			"c": "SYN, ACK, SYN-ACK",
			"d": "FIN, FIN-ACK, ACK"
		}
	},
	{
		"question": "When you are getting information about a web server, it is very important to know the HTTP Methods (GET, POST, HEAD, PUT, DELETE, and TRACE) that are available because there are two critical methods (PUT and DELETE).\nPUT can upload a file to the server and DELETE can delete a file from the server.\nYou can detect all these methods (GET, POST, HEAD, PUT, DELETE, TRACE) using NMAP script engine.\nWhat nmap script will help you with this task?",
		"num": "93",
		"correct_answer": "b",
		"answers": {
			"a": "http-git",
			"b": "http-methods",
			"c": "http-headers",
			"d": "http enum"
		}
	},
	{
		"question": "You have chosen a 22 character word from the dictionary as your password. How long will it take to crack the password by an attacker?",
		"num": "94",
		"correct_answer": "b",
		"answers": {
			"a": "16 million years",
			"b": "5 minutes",
			"c": "23 days",
			"d": "200 years"
		}
	},
	{
		"question": "Firewall implementation and design for an enterprise can be a daunting task.\nChoices made early in the design process can have far-reaching security implications for years to come.\nWhich of the following firewall architecture is designed to host servers that offer public services?",
		"num": "95",
		"correct_answer": "b",
		"answers": {
			"a": "Bastion Host",
			"b": "Screened subnet",
			"c": "Screened host",
			"d": "Screened"
		}
	},
	{
		"question": "You are the security administrator for a large network.\nYou want to prevent attackers from running any sort of traceroute into your DMZ and discovering the internal structure of publicly accessible areas of the network.\nHow can you achieve this?",
		"num": "96",
		"correct_answer": "a",
		"answers": {
			"a": "There is no way to completely block tracerouting into this area",
			"b": "Block UDP at the firewall",
			"c": "Block TCP at the firewall",
			"d": "Block ICMP at the firewall"
		}
	},
	{
		"question": "Code injection is a form of attack in which a malicious user:",
		"num": "97",
		"correct_answer": "a",
		"answers": {
			"a": "Inserts text into a data field that gets interpreted as code",
			"b": "Gets the server to execute arbitrary code using a buffer overflow",
			"c": "Inserts additional code into the JavaScript running in the browser",
			"d": "Gains access to the codebase on the server and inserts new code"
		}
	},
	{
		"question": "What is the main advantage that a network-based IDS/IPS system has over a host-based solution?",
		"num": "98",
		"correct_answer": "a",
		"answers": {
			"a": "They do not use host system resources.",
			"b": "They are placed at the boundary, allowing them to inspect all traffic.",
			"c": "They are easier to install and configure.",
			"d": "They will not interfere with user interfaces."
		}
	},
	{
		"question": "You are using NMAP to resolve domain names into IP addresses for a ping sweep later. Which of the following commands looks for IP addresses?",
		"num": "99",
		"correct_answer": "b",
		"answers": {
			"a": ">host -t AXFR hackeddomain.com",
			"b": ">host -t a hackeddomain.com",
			"c": ">host -t soa hackeddomain.com",
			"d": ">host -t ns hackeddomain.com"
		}
	},
	{
		"question": "When an alert rule is matched in a network-based IDS like snort, the IDS does which of the following?",
		"num": "100",
		"correct_answer": "b",
		"answers": {
			"a": "Drops the packet and moves on to the next one",
			"b": "Continues to evaluate the packet until all rules are checked",
			"c": "Stops checking rules, sends an alert, and lets the packet continue",
			"d": "Blocks the connection with the source IP address in the packet"
		}
	},
	{
		"question": "TCP packets transmitted in either direction after the initial three-way handshake will have which of the following bit set?",
		"num": "101",
		"correct_answer": "b",
		"answers": {
			"a": "SYN flag",
			"b": "ACK flag",
			"c": "FIN flag",
			"d": "XMAS flag"
		}
	},
	{
		"question": "What term describes the amount of risk that remains after the vulnerabilities are classified and the countermeasures have been deployed?",
		"num": "102",
		"correct_answer": "d",
		"answers": {
			"a": "Impact Risk",
			"b": "Inherent Risk",
			"c": "Deferred Risk",
			"d": "Residual Risk"
		}
	},
	{
		"question": "Let's imagine three companies (A, B and C), all competing in a challenging global environment.\nCompany A and B are working together in developing a product that will generate a major competitive advantage for them.\nCompany A has a secure DNS server while company B has a DNS server vulnerable to spoofing.\nWith a spoofing attack on the DNS server of company B, company C gains access to outgoing e-mails from company A.\nHow do you prevent DNS spoofing?  Select the Best Answer.\n",
		"num": "103",
		"correct_answer": "c",
		"answers": {
			"a": "Install DNS logger and track vulnerable packets",
			"b": "Disable DNS timeouts",
			"c": "Install DNS Anti-spoofing",
			"d": "Disable DNS Zone Transfer"
		}
	},
	{
		"question": "A company has publicly hosted web applications and an internal Intranet protected by a firewall.\nWhich technique will help protect against enumeration?",
		"num": "104",
		"correct_answer": "c",
		"answers": {
			"a": "Reject all invalid email received via SMTP.",
			"b": "Allow full DNS zone transfers.",
			"c": "Remove A records for internal hosts.",
			"d": "Enable null session pipes."
		}
	},
	{
		"question": "Which of the following statements is FALSE with respect to Intrusion Detection Systems?",
		"num": "105",
		"correct_answer": "a",
		"answers": {
			"a": "Intrusion Detection Systems can easily distinguish a malicious payload in an encrypted traffic",
			"b": "Intrusion Detection Systems can examine the contents of the data in context of the network protocol",
			"c": "Intrusion Detection Systems can be configured to distinguish specific content in network packets",
			"d": "Intrusion Detection Systems require constant update of the signature library"
		}
	},
	{
		"question": "Which of the following is used to indicate a single-line comment in structured query language (SQL)?",
		"num": "106",
		"correct_answer": "a",
		"answers": {
			"a": "--",
			"b": "||",
			"c": "%%",
			"d": "''"
		}
	},
	{
		"question": "Which of the following programs is usually targeted at Microsoft Office products?",
		"num": "107",
		"correct_answer": "c",
		"answers": {
			"a": "Polymorphic virus",
			"b": "Multipart virus",
			"c": "Macro virus",
			"d": "Stealth virus"
		}
	},
	{
		"question": "Which of the following ensures that updates to policies, procedures, and configurations are made in a controlled and documented fashion?",
		"num": "108",
		"correct_answer": "c",
		"answers": {
			"a": "Regulatory compliance",
			"b": "Peer review",
			"c": "Change management",
			"d": "Penetration testing"
		}
	},
	{
		"question": "To send a PGP encrypted message, which piece of information from the recipient must the sender have before encrypting the message?",
		"num": "109",
		"correct_answer": "b",
		"answers": {
			"a": "Recipient's private key",
			"b": "Recipient's public key",
			"c": "Master encryption key",
			"d": "Sender's public key"
		}
	},
	{
		"question": "Which of the following are variants of mandatory access control mechanisms? (Choose two.)",
		"num": "110",
		"correct_answer": "ac",
		"answers": {
			"a": "Two factor authentication",
			"b": "Acceptable use policy",
			"c": "Username / password",
			"d": "User education program",
			"e": "Sign in register"
		}
	},
	{
		"question": "env x=`(){ :;};echo exploit` bash -c 'cat /etc/passwd'\n\nWhat is the Shellshock bash vulnerability attempting to do on a vulnerable Linux host?",
		"num": "111",
		"correct_answer": "a",
		"answers": {
			"a": "Display passwd content to prompt",
			"b": "Changes all passwords in passwd",
			"c": "Add new user to the passwd file",
			"d": "Removes the passwd file"
		}
	},
	{
		"question": "Harold works for Jacobson Unlimited in the IT department as the security manager. Harold has created a security policy requiring all employees to use complex 14 character passwords. Unfortunately, the membersof management do not want to have to use such long complicated \npasswords so they tell Harold's boss this new password policy should not apply to them. To comply with the management's wishes, the IT department creates another Windows domain and moves all the management users to that domain. This new domain has a password policy only requiring 8 characters.\nHarold is concerned about having to accommodate the managers, but cannot do anything about it. Harold is also concerned about using LanManager security on his network instead of NTLM or NTLMv2, but the many legacy applications on the network prevent using the more secure NTLM and NTLMv2. Harold pulls the SAM files from the DC's on the original domain and the new domain using Pwdump6. Harold uses the password cracking software John the Ripper to crack users' passwords to make sure they are strong enough. Harold expects that the users' passwords in the original domain will take much longer to crack than the management's passwords in the new domain. After running the software, Harold discovers that the 14 character passwords only took a short time longer to crack than the 8 character passwords.\nWhy did the 14 character passwords not take much longer to crack than the 8 character passwords?",
		"num": "112",
		"correct_answer": "d",
		"answers": {
			"a": "Harold should have used Dumpsec instead of Pwdump6",
			"b": "Harold's dictionary file was not large enough",
			"c": "Harold should use LC4 instead of John the Ripper",
			"d": "LanManger hashes are broken up into two 7 character fields"
		}
	},
	{
		"question": "This tool is an 802.11 WEP and WPA-PSK keys cracking program that can recover keys once enough data packets have been captured.\nIt implements the standard FMS attack along with some optimizations like KoreK attacks, as well as the PTW attack, thus making the attack much faster compared to other WEP cracking tools.\nWhich of the following tools is being described?",
		"num": "113",
		"correct_answer": "a",
		"answers": {
			"a": "Aircrack-ng",
			"b": "Wificracker",
			"c": "Airguard",
			"d": "WLAN-crack"
		}
	},
	{
		"question": "The study of discovering messages that were hidden using the process of steganography is known as_____.",
		"num": "114",
		"correct_answer": "d",
		"answers": {
			"a": "None of these",
			"b": "Steganographics",
			"c": "Steganographism",
			"d": "Steganalysis"
		}
	},
	{
		"question": "Secure Hashing Algorithm (SHA) is an algorithm for generating cryptographically secure one-way hash, published by the National Institute of Standards and Technology as a U.S.Federal Information Processing Standard.\n What is the block (word) size used by SHA-512 algorithm?",
		"num": "115",
		"correct_answer": "b",
		"answers": {
			"a": "32-bit",
			"b": "64-bit",
			"c": "128-bit",
			"d": "256-bit"
		}
	},
	{
		"question": "Google uses a unique cookie for each browser used by an individual user on a computer. This cookie contains information that allows Google to identify records about that user on its database. This cookie is submitted every time a user launches a Google search, visits a site using AdSense etc. The information stored in Google's database, identified by the cookie, includes\n- Everything you search for using Google\n- Every web page you visit that has Google Adsense ads\nHow would you prevent Google from storing your search keywords?",
		"num": "116",
		"correct_answer": "a",
		"answers": {
			"a": "Block Google Cookie by applying Privacy and Security settings in your web browser",
			"b": "Disable the Google cookie using Google Advanced Search settings on Google Search page",
			"c": "Do not use Google but use another search engine Bing which will not collect and store your search keywords",
			"d": "Use MAC OS X instead of Windows 7. Mac OS has higher level of privacy controls by default."
		}
	},
	{
		"question": "Fake Anti-Virus, is one of the most frequently encountered and persistent threats on the web. This malwareuses social engineering to lure users into infected websites with a technique called Search Engine Optimization.\nOnce the Fake AV is downloaded into the user's computer, the software will scare them into believing their system is infected with threats that do not really exist, and then push users to purchase services to clean up the non-existent threats.\nThe Fake AntiVirus will continue to send these annoying and intrusive alerts until a payment is made.\nWhat is the risk of installing Fake AntiVirus?",
		"num": "117",
		"correct_answer": "b",
		"answers": {
			"a": "Victim's Operating System versions, services running and applications installed will be published on Blogs and Forums",
			"b": "Victim's personally identifiable information such as billing address and credit card details, may be extracted and exploited by the attacker",
			"c": "Once infected, the computer will be unable to boot and the Trojan will attempt to format the hard disk",
			"d": "Denial of Service attack will be launched against the infected computer crashing other machines on the connected network"
		}
	},
	{
		"question": "What results will the following command yield:\n\n'NMAP -sS -O -p 123-153 192.168.100.3'?",
		"num": "118",
		"correct_answer": "d",
		"answers": {
			"a": "A stealth scan, opening port 123 and 153",
			"b": "A stealth scan, checking open ports 123 to 153",
			"c": "A stealth scan, checking all open ports excluding ports 123 to 153",
			"d": "A stealth scan, determine operating system, and scanning ports 123 to 153"
		}
	},
	{
		"question": "Jason, a penetration tester, is testing a web application that he knows is vulnerable to an SQL injection but the results of the injection are not visible to him.\nHe tried waitfor delay command to check the SQL execution status which confirmed the presence of the SQL injection vulnerability.\nWhich type of SQL injection Jason is attempting on the web application?",
		"num": "119",
		"correct_answer": "a",
		"answers": {
			"a": "Blind SQL injection",
			"b": "Error-based SQL injection",
			"c": "UNION SQL Injection",
			"d": "Simple SQL Injection"
		}
	},
	{
		"question": "Blane is a network security analyst for his company.\nFrom an outside IP, Blane performs an XMAS scan using Nmap.\nAlmost every port scanned does not illicit a response.\n\nWhat can he infer from this kind of response?",
		"num": "120",
		"correct_answer": "a",
		"answers": {
			"a": "These ports are open because they do not illicit a response.",
			"b": "He can tell that these ports are in stealth mode.",
			"c": "If a port does not respond to an XMAS scan using NMAP, that port is closed.",
			"d": "The scan was not performed correctly using NMAP since all ports, no matter what their state, will illicit some sort of response from an XMAS scan."
		}
	},
	{
		"question": "Johnny is a member of the hacking group Orpheus1. He is currently working on breaking into the Department of Defense's front end Exchange Server.\nHe was able to get into the server, located in a DMZ, by using an unused service account that had a very weak password that he was able to guess. Johnny wants to crack the administrator password, but does not have a lot of time to crack it. He wants to use a tool that already has the LM hashes computed for all possible permutations of the administrator password.\nWhat tool would be best used to accomplish this?",
		"num": "121",
		"correct_answer": "d",
		"answers": {
			"a": "SMBCrack",
			"b": "SmurfCrack",
			"c": "PSCrack",
			"d": "RainbowTables"
		}
	},
	{
		"question": "Which of the following countermeasure can specifically protect against both the MAC Flood and MAC Spoofing attacks?",
		"num": "122",
		"correct_answer": "a",
		"answers": {
			"a": "Configure Port Security on the switch",
			"b": "Configure Port Recon on the switch",
			"c": "Configure Switch Mapping",
			"d": "Configure Multiple Recognition on the switch"
		}
	},
	{
		"question": "Which of the following is a component of a risk assessment?",
		"num": "123",
		"correct_answer": "d",
		"answers": {
			"a": "Administrative safeguards",
			"b": "Logical interface",
			"c": "DMZ",
			"d": "Physical security"
		}
	},
	{
		"question": "Which Steganography technique uses Whitespace to hide secret messages?",
		"num": "124",
		"correct_answer": "a",
		"answers": {
			"a": "snow",
			"b": "beetle",
			"c": "magnet",
			"d": "cat"
		}
	},
	{
		"question": "Data hiding analysis can be useful in",
		"num": "125",
		"correct_answer": "b",
		"answers": {
			"a": "determining the level of encryption used to encrypt the data.",
			"b": "detecting and recovering data that may indicate knowledge, ownership or intent.",
			"c": "identifying the amount of central processing unit (cpu) usage over time to process the data.",
			"d": "preventing a denial of service attack on a set of enterprise servers to prevent users from accessing the data."
		}
	},
	{
		"question": "OS fingerprinting is the method used to determine the operating system running on a remote target system. It is an important scanning method, as the attacker will have a greater probability of success if he/she knows the OS. Active stack fingerprinting is one of the types of OS fingerprinting.\n\nWhich of the following is true about active stack fingerprinting? ",
		"num": "126",
		"correct_answer": "b",
		"answers": {
			"a": "Uses password crackers to escalate system privileges",
			"b": "Is based on the fact that various vendors of OS implement the TCP stack differently",
			"c": "TCP connect scan",
			"d": "Uses sniffing techniques instead of the scanning techniques",
			"e": "Is based on the differential implantation of the stack and the various ways an OS responds to it"
		}
	},
	{
		"question": "Which of the following techniques will identify if computer files have been changed?",
		"num": "127",
		"correct_answer": "b",
		"answers": {
			"a": "Network sniffing",
			"b": "Integrity checking hashes",
			"c": "Firewall alerts",
			"d": "Permissions sets"
		}
	},
	{
		"question": "Anonymizer sites access the Internet on your behalf, protecting your personal information from disclosure.\nAn anonymizer protects all of your computer's identifying information while it surfs for you, enabling you to remain at least one step removed from the sites you visit.\nYou can visit Web sites without allowing anyone to gather information on sites visited by you. Services that provide anonymity disable pop-up windows and cookies, and conceal visitor's IP address.\nThese services typically use a proxy server to process each HTTP request. When the user requests a Web page by clicking a hyperlink or typing a URL into their browser, the service retrieves and displays the information using its own server.\nThe remote server (where the requested Web page resides) receives information on the anonymous Web surfing service in place of your information.\nIn which situations would you want to use anonymizer? (Select 3 answers)",
		"num": "128",
		"correct_answer": "bcd",
		"answers": {
			"a": "Increase your Web browsing bandwidth speed by using Anonymizer",
			"b": "To protect your privacy and Identity on the Internet",
			"c": "To bypass blocking applications that would prevent access to Web sites or parts of sites that you want to visit.",
			"d": "Post negative entries in blogs without revealing your IP identity"
		}
	},
	{
		"question": "A network administrator discovers several unknown files in the root directory of his Linux FTP server.\nOne of the files is a tarball, two are shell script files, and the third is a binary file is named \"nc.\"\nThe FTP server's access logs show that the anonymous user account logged in to the server, uploaded the files, and extracted the contents of the tarball and ran the script using a function provided by the FTP server's software.\nThe ps command shows that the nc file is running as process, and the netstat command shows the nc process is listening on a network port.\nWhat kind of vulnerability must be present to make this remote attack possible?",
		"num": "129",
		"correct_answer": "b",
		"answers": {
			"a": "File system permissions",
			"b": "Directory traversal",
			"c": "Brute force login",
			"d": "Privilege escalation"
		}
	},
	{
		"question": "Vulnerability scanners are automated tools that are used to identify vulnerabilities and misconfigurations of\nhosts. They also provide information regarding mitigating discovered vulnerabilities.\nWhich of the following statements is incorrect?",
		"num": "130",
		"correct_answer": "d",
		"answers": {
			"a": "Vulnerability scanners attempt to identify vulnerabilities in the hosts scanned.",
			"b": "Vulnerability scanners can help identify out-of-date software versions, missing patches, or system upgrades.",
			"c": "They can validate compliance with or deviations from the organization's security policy",
			"d": "Vulnerability scanners can identify weakness and automatically fix and patch the vulnerabilities without user intervention"
		}
	},
	{
		"question": "A corporation hired an ethical hacker to test if it is possible to obtain users' login credentials using methods other than social engineering.\nAccess to offices and to a network node is granted.\nResults from server scanning indicate all are adequately patched and physical access is denied, thus, administrators have access only through Remote Desktop.\nWhich technique could be used to obtain login credentials?",
		"num": "131",
		"correct_answer": "d",
		"answers": {
			"a": "Capture every users' traffic with Ettercap.",
			"b": "Capture LANMAN Hashes and crack them with LC6.",
			"c": "Guess passwords using Medusa or Hydra against a network service.",
			"d": "Capture administrators RDP traffic and decode it with Cain and Abel."
		}
	},
	{
		"question": "Which of the following steganography utilities exploits the nature of white space and allows the user to conceal information in these white spaces?",
		"num": "132",
		"correct_answer": "b",
		"answers": {
			"a": "Image Hide",
			"b": "Snow",
			"c": "Gif-It-Up",
			"d": "NiceText"
		}
	},
	{
		"question": "Which of the following is the greatest threat posed by backups?",
		"num": "133",
		"correct_answer": "d",
		"answers": {
			"a": "A backup is incomplete because no verification was performed.",
			"b": "A backup is unavailable during disaster recovery.",
			"c": "A backup is the source of Malware or illicit information.",
			"d": "An un-encrypted backup can be misplaced or stolen."
		}
	},
	{
		"question": "Which of the following is an adaptive SQL Injection testing technique used to discover coding errors by inputting massive amounts of random data and observing the changes in the output?",
		"num": "134",
		"correct_answer": "d",
		"answers": {
			"a": "Function Testing",
			"b": "Dynamic Testing",
			"c": "Static Testing",
			"d": "Fuzzing Testing"
		}
	},
	{
		"question": "Data is sent over the network as clear text (unencrypted) when Basic Authentication is configured on Web Servers.",
		"num": "135",
		"correct_answer": "a",
		"answers": {
			"a": "true",
			"b": "false"
		}
	},
	{
		"question": "What term describes the amount of risk that remains after the vulnerabilities are classified and the countermeasures have been deployed?",
		"num": "136",
		"correct_answer": "d",
		"answers": {
			"a": "Impact Risk",
			"b": "Inherent Risk",
			"c": "Deferred Risk",
			"d": "Residual Risk"
		}
	},
	{
		"question": "A virus is a self-replicating program that produces its own code by attaching copies of it into other executable codes.\nWhich of the following virus evade the anti-virus software by intercepting its requests to the operating system?",
		"num": "137",
		"correct_answer": "c",
		"answers": {
			"a": "Macro virus",
			"b": "Cluster virus",
			"c": "Stealth/Tunneling virus",
			"d": "System or boot sector virus"
		}
	},
	{
		"question": "Secret communications where the existence of the message is hidden is known as .",
		"num": "138",
		"correct_answer": "d",
		"answers": {
			"a": "Concealment Cipher",
			"b": "Image Processing",
			"c": "Running Cipher",
			"d": "Steganography"
		}
	},
	{
		"question": "What software can be used to alter an image in stenography?",
		"num": "139",
		"correct_answer": "a",
		"answers": {
			"a": "Photoshop",
			"b": "Firefox",
			"c": "Explorer",
			"d": "S-Tools"
		}
	},
	{
		"question": "Denial of Service (DoS) is an attack on a computer or network that prevents legitimate use of its resources. In a DoS attack, attackers flood a victim system with non-legitimate service requests or traffic to overload its resources, which prevents it from performing intended tasks.\n\nWhich of the following is a symptom of a DoS attack? ",
		"num": "140",
		"correct_answer": "a",
		"answers": {
			"a": "Unavailability of a particular website",
			"b": "Decrease in the amount of spam emails received",
			"c": "Automatic increase in network bandwidth",
			"d": "Automatic increase in network performance"
		}
	},
	{
		"question": "When utilizing technical assessment methods to assess the security posture of a network, which of the following techniques would be most effective in determining whether end-user security training would be beneficial?",
		"num": "141",
		"correct_answer": "b",
		"answers": {
			"a": "Vulnerability scanning",
			"b": "Social engineering",
			"c": "Application security testing",
			"d": "Network sniffing"
		}
	},
	{
		"question": "You want to know whether a packet filter is in front of 192.168.1.10. Pings to 192.168.1.10 don't get answered.\nA basic nmap scan of 192.168.1.10 seems to hang without returning any information.\n\nWhat should you do next?",
		"num": "142",
		"correct_answer": "a",
		"answers": {
			"a": "Run NULL TCP hping2 against 192.168.1.10",
			"b": "Run nmap XMAS scan against 192.168.1.10",
			"c": "The firewall is blocking all the scans to 192.168.1.10",
			"d": "Use NetScan Tools Pro to conduct the scan"
		}
	},
	{
		"question": "In StackGuard, whenever a function is called, code is added that pushes a small value called a ___ value over to the stack.",
		"num": "143",
		"correct_answer": "c",
		"answers": {
			"a": "Stackgap",
			"b": "Runtime bound checkers",
			"c": "Canary",
			"d": "CRED"
		}
	},
	{
		"question": "You just purchased the latest DELL computer, which comes pre-installed with Windows 7, McAfee antivirus software and a host of other applications.\nYou want to connect Ethernet wire to your cable modem and start using the computer immediately.\nWindows is dangerously insecure when unpacked from the box, and there are a few things that you must do before you use it.\n",
		"num": "144",
		"correct_answer": "acdef",
		"answers": {
			"a": "New installation of Windows should be patched by installing the latest service packs and hotfixes",
			"b": "Key applications such as Adobe Acrobat, Macromedia Flash, Java, Winzip etc., must have the latest security patches installed",
			"c": "Install a personal firewall and lock down unused ports from connecting to your computer",
			"d": "Install the latest signatures for Antivirus software",
			"e": "Configure \"Windows Update\" to automatic",
			"f": "Create a non-admin user with a complex password and logon to this account ",
			"g": "You can start using your computer as vendors such as DELL, HP and IBM would have already installed the latest service packs."
		}
	},
	{
		"question": "It is a kind of malware (malicious software) that criminals install on your computer so they can lock it from a remote location.\nThis malware generates a pop-up window, webpage, or email warning from what looks like an official authority.\nIt explains that your computer has been locked because of possible illegal activities on it and demands payment before you can access your files and programs again.\nWhich of the following terms best matches the definition?",
		"num": "145",
		"correct_answer": "a",
		"answers": {
			"a": "Ransomware",
			"b": "Spyware",
			"c": "Riskware",
			"d": "Adware"
		}
	},
	{
		"question": "A company\u2019s security policy states that all Web browsers must automatically delete their HTTP browser cookies upon terminating.\nWhat sort of security breach is this policy attempting to mitigate?",
		"num": "146",
		"correct_answer": "b",
		"answers": {
			"a": "Attempts by attackers to access the user and password information stored in the company\u2019s SQL database.",
			"b": "Attempts by attackers to access Web sites that trust the Web browser user by stealing the user\u2019s authentication credentials.",
			"c": "Attempts by attackers to access password stored on the user\u2019s computer without the user\u2019s knowledge.",
			"d": "Attempts by attackers to determine the user\u2019s Web browser usage patterns, including when sites were visited and for how long."
		}
	},
	{
		"question": "Which one of the following Google advanced search operators allows an attacker to restrict the results to those websites in the given domain?",
		"num": "147",
		"correct_answer": "b",
		"answers": {
			"a": "[cache:]",
			"b": "[site:]",
			"c": "[inurl:]",
			"d": "[link:]"
		}
	},
	{
		"question": "As a system administrator, you are responsible for maintaining the website of your company which deals in online recharge of mobile phone cards.\nOne day to your surprise, you find the home page of your company's website defaced.\nWhat is the reason for webpage defacement?",
		"num": "148",
		"correct_answer": "c",
		"answers": {
			"a": "Denial of Service attack",
			"b": "Session Hijacking",
			"c": "DNS attack through cache poisoning",
			"d": "Buffer overflow"
		}
	},
	{
		"question": "A security engineer is attempting to map a company's internal network. The engineer enters in the following NMAP command.\n\n  NMAP -n -sS -P0 -p 80 ***.***.**.**\n\nWhat type of scan is this?",
		"num": "149",
		"correct_answer": "c",
		"answers": {
			"a": "Quick scan",
			"b": "Intense scan",
			"c": "Stealth scan",
			"d": "Comprehensive scan"
		}
	},
	{
		"question": "You are logged in as a local admin on a Windows 7 system and you need to launch the Computer Management Console from command line.\nWhich command would you use?",
		"num": "150",
		"correct_answer": "d",
		"answers": {
			"a": "c:\\ncpa.cpl",
			"b": "c:\\services.msc",
			"c": "c:\\gpedit",
			"d": "c:\\compmgmt.msc"
		}
	},
	{
		"question": "When setting up a wireless network, an administrator enters a pre-shared key for security. Which of the following is true?",
		"num": "151",
		"correct_answer": "a",
		"answers": {
			"a": "The key entered is a symmetric key used to encrypt the wireless data.",
			"b": "The key entered is a hash that is used to prove the integrity of the wireless data.",
			"c": "The key entered is based on the Diffie-Hellman method.",
			"d": "The key is an RSA key used to encrypt the wireless data."
		}
	},
	{
		"question": "Which type of scan does NOT open a full TCP connection?",
		"num": "152",
		"correct_answer": "a",
		"answers": {
			"a": "Stealth Scan",
			"b": "XMAS Scan",
			"c": "Null Scan",
			"d": "FIN Scan"
		}
	},
	{
		"question": "Identify the web application attack where attackers exploit a webpage vulnerabilities to force an unsuspecting user's browser to send malicious requests they did not intend.\nThe victim holds an active session with a trusted site and simultaneously visits a malicious site, which injects an HTTP request for the trusted site into the victim user's session, compromising its integrity.",
		"num": "153",
		"correct_answer": "b",
		"answers": {
			"a": "Cross-Site Scripting (XSS)",
			"b": "Cross-Site Request Forgery (CSRF)",
			"c": "LDAP Injection attack",
			"d": "SQL injection attack"
		}
	},
	{
		"question": "Which of the following is the least-likely physical characteristic to be used in biometric control that supports a large company?",
		"num": "154",
		"correct_answer": "b",
		"answers": {
			"a": "Fingerprints",
			"b": "Height and Weight",
			"c": "Iris patterns",
			"d": "Voice"
		}
	},
	{
		"question": "Security Policy is a definition of what it means to be secure for a system, organization or other entity.\nFor Information Technologies, there are sub-policies like Computer Security Policy, Information Protection Policy, Information Security Policy, network Security Policy, Physical Security Policy, Remote Access Policy, and User Account Policy.\nWhat is the main theme of the sub-policies for Information Technologies?",
		"num": "155",
		"correct_answer": "a",
		"answers": {
			"a": "Confidentiality, Integrity, Availability",
			"b": "Availability, Non-repudiation, Confidentiality",
			"c": "Authenticity, Integrity, Non-repudiation",
			"d": "Authenticity, Confidentiality, Integrity"
		}
	},
	{
		"question": "What's stack smashing?",
		"num": "156",
		"correct_answer": "b",
		"answers": {
			"a": "The input of No Operation instruction code in a string",
			"b": "A buffer overflow that overwrites the return address",
			"c": "It's when code is executed from a default heap.",
			"d": "It's when an attacker gets to a stack after they're done with the pumpkins."
		}
	},
	{
		"question": "Consider the attack scenario given below:\n\nStep 1: User browses a web page\nStep 2: Web server replies with requested page and sets a cookie on the user's browser\nStep 3: Attacker steals cookie (Sniffing, XSS, phishing attack)\nStep 4: Attacker orders for product using modified cookie\nStep 5: Product is delivered to attacker's address\n\nIdentify the web application attack.\n",
		"num": "157",
		"correct_answer": "c",
		"answers": {
			"a": "Session fixation attack",
			"b": "Unvalidated redirects attack",
			"c": "Cookie poisoning attack",
			"d": "Denial-of-Service (DoS) attack"
		}
	},
	{
		"question": "You have invested millions of dollars for protecting your corporate network.\nYou have the best IDS, firewall with strict rules and routers with no configuration errors.\nWhich of the following techniques practiced by an attacker exploits human behavior to make your network vulnerable to attacks?",
		"num": "158",
		"correct_answer": "c",
		"answers": {
			"a": "Denial of Service",
			"b": "Buffer overflow",
			"c": "Social Engineering",
			"d": "SQL injection"
		}
	},
	{
		"question": "Which of the following tools performs comprehensive tests against web servers, including dangerous files and CGIs?",
		"num": "159",
		"correct_answer": "d",
		"answers": {
			"a": "Dsniff",
			"b": "John the Ripper",
			"c": "Snort",
			"d": "Nikto"
		}
	},
	{
		"question": "Attackers may place a Null Operation (NOP) instruction code at the beginning of a string in the buffer overflow attack process. True or false?",
		"num": "160",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "LAN Manager Passwords are concatenated to 14 bytes, and split in half. The two halves are hashed individually. If the password is 7 characters or less, than the second half of the hash is always:",
		"num": "161",
		"correct_answer": "a",
		"answers": {
			"a": "0xAAD3B435B51404EE",
			"b": "0xAAD3B435B51404AA",
			"c": "0xAAD3B435B51404BB",
			"d": "0xAAD3B435B51404CC"
		}
	},
	{
		"question": "Which wireless standard has bandwidth up to 54 Mbps and signals in a regulated frequency spectrum around 5 GHz?",
		"num": "162",
		"correct_answer": "a",
		"answers": {
			"a": "802.11a",
			"b": "802.11b",
			"c": "802.11g",
			"d": "802.11i"
		}
	},
	{
		"question": "Which of the following describes the characteristics of a Boot Sector Virus?",
		"num": "163",
		"correct_answer": "b",
		"answers": {
			"a": "Moves the MBR to another location on the RAM and copies itself to the original location of the MBR",
			"b": "Moves the MBR to another location on the hard disk and copies itself to the original location of the MBR",
			"c": "Modifies directory table entries so that directory entries point to the virus code instead of the actual program",
			"d": "Overwrites the original MBR and only executes the new virus code"
		}
	},
	{
		"question": "What does ICMP (type 11, code 0) denote?",
		"num": "164",
		"correct_answer": "c",
		"answers": {
			"a": "Source Quench",
			"b": "Destination Unreachable",
			"c": "Time Exceeded"
		}
	},
	{
		"question": "Neil is an IT security consultant working on contract for Davidson Avionics.\nNeil has been hired to audit the network of Davidson Avionics.\nHe has been given permission to perform any tests necessary.\nNeil has created a fake company ID badge and uniform.\nNeil waits by one of the company's entrance doors and follows an employee into the office after they use their valid access card to gain entrance.\nWhat type of social engineering attack has Neil employed here?",
		"num": "165",
		"correct_answer": "a",
		"answers": {
			"a": "Neil has used a tailgating social engineering attack to gain access to the offices",
			"b": "He has used a piggybacking technique to gain unauthorized access",
			"c": "This type of social engineering attack is called man trapping",
			"d": "Neil is using the technique of reverse social engineering to gain access to the offices of Davidson Avionic"
		}
	},
	{
		"question": "Which type of access control is used on a router or firewall to limit network activity?",
		"num": "166",
		"correct_answer": "c",
		"answers": {
			"a": "Mandatory",
			"b": "Discretionary",
			"c": "Rule-based",
			"d": "Role-based"
		}
	},
	{
		"question": "In the C++ Object-oriented programming language, which of these situations can result in a buffer overflow?",
		"num": "167",
		"correct_answer": "c",
		"answers": {
			"a": "When an object returns a null (empty) value",
			"b": "When a program fails to compile properly",
			"c": "When a program returns an incorrect output",
			"d": "When the length of some input data is not correctly checked"
		}
	},
	{
		"question": "Which tool allows analysts and pen testers to examine links between data using graphs and link analysis?",
		"num": "168",
		"correct_answer": "c",
		"answers": {
			"a": "Metasploit",
			"b": "Cain & Abel",
			"c": "Maltego",
			"d": "Wireshark"
		}
	},
	{
		"question": "Which of the following represents a form of steganography technique?",
		"num": "169",
		"correct_answer": "d",
		"answers": {
			"a": "Password protection",
			"b": "Encryption",
			"c": "Highlight",
			"d": "Digital watermarking"
		}
	},
	{
		"question": "It is common for buffer overflows to occur in the heap memory space.\nApplication dynamically allocates heap memory as needed through a function.\nThis function is called what?",
		"num": "170",
		"correct_answer": "d",
		"answers": {
			"a": "strncopy()",
			"b": "strprint()",
			"c": "strcopy()",
			"d": "malloc()"
		}
	},
	{
		"question": "\ufeffThe program snow is used for:",
		"num": "171",
		"correct_answer": "c",
		"answers": {
			"a": "Password attacks",
			"b": "Spyware",
			"c": "Steganography",
			"d": "Sniffing"
		}
	},
	{
		"question": "CAM table in switch stores information such as MAC addresses available on physical ports with their associated VLAN parameters.\nWhat happens when the CAM table is full?",
		"num": "172",
		"correct_answer": "c",
		"answers": {
			"a": "Additional ARP request traffic will not be forwarded to any port on the switch",
			"b": "The switch will stop functioning and get disconnected from network ",
			"c": "Additional ARP request traffic will flood every port on the switch",
			"d": "It does not affect the switch functioning"
		}
	},
	{
		"question": "Which of the following is a component of a risk assessment?",
		"num": "173",
		"correct_answer": "b",
		"answers": {
			"a": "Physical security",
			"b": "Administrative safeguards",
			"c": "DMZ",
			"d": "Logical interface"
		}
	},
	{
		"question": "An attacker sniffs encrypted traffic from the network and is subsequently able to decrypt it.\nThe attacker can now use which cryptanalytic technique to attempt to discover the encryption key?",
		"num": "174",
		"correct_answer": "d",
		"answers": {
			"a": "Birthday attack",
			"b": "Plaintext attack",
			"c": "Meet in the middle attack",
			"d": "Chosen ciphertext attack"
		}
	},
	{
		"question": "Session splicing is an IDS evasion technique in which an attacker delivers data in multiple, small sized packets to the target computer, making it very Difficult for an IDS to detect the attack signatures.\nWhich tool can be used to perform session splicing attacks?",
		"num": "175",
		"correct_answer": "c",
		"answers": {
			"a": "Burp",
			"b": "Hydra",
			"c": "Whisker",
			"d": "TCP splice"
		}
	},
	{
		"question": "What do you call a pre-computed hash?",
		"num": "176",
		"correct_answer": "c",
		"answers": {
			"a": "Sun tables",
			"b": "Apple tables",
			"c": "Rainbow tables",
			"d": "Moon tables"
		}
	},
	{
		"question": "What is the broadcast address for the subnet 190.86.168.0/22?",
		"num": "177",
		"correct_answer": "c",
		"answers": {
			"a": "190.86.168.255",
			"b": "190.86.255.255",
			"c": "190.86.171.255",
			"d": "190.86.169.255"
		}
	},
	{
		"question": "Identify the denial-of-service attack that is carried out using a method known as ?bricking a system.?\nUnlike other DoS attacks, it sabotages the system hardware, requiring the victim to replace or reinstall the hardware.\n",
		"num": "178",
		"correct_answer": "c",
		"answers": {
			"a": "ICMP Flood Attack",
			"b": "Application Level Flood Attacks",
			"c": "Phlashing ",
			"d": "Bandwidth Attacks"
		}
	},
	{
		"question": "The FIN flag is set and sent from host A to host B when host A has no more data to transmit (Closing a TCP connection). This flag releases the connection resources.\nHowever, host A can continue to receive data as long as the SYN sequence numbers of transmitted packets from host B are lower than the packet segment containing the set FIN flag.",
		"num": "179",
		"correct_answer": "b",
		"answers": {
			"a": "false",
			"b": "true"
		}
	},
	{
		"question": "Firewalls are the software or hardware systems that are able to control and monitor the traffic coming in and out the target network based on pre-defined set of rules.\nWhich of the following types of firewalls can protect against SQL injection attacks?",
		"num": "180",
		"correct_answer": "d",
		"answers": {
			"a": "Data-driven firewall",
			"b": "Stateful firewall",
			"c": "Packet firewall",
			"d": "Web application firewall"
		}
	},
	{
		"question": "Which tool is used to automate SQL injections and exploit a database by forcing a given web application to connect to another database controlled by a hacker?",
		"num": "181",
		"correct_answer": "d",
		"answers": {
			"a": "DataThief",
			"b": "NetCat",
			"c": "Cain and Abel",
			"d": "SQLInjector"
		}
	},
	{
		"question": "A regional bank hires your company to perform a security assessment on their network after a recent data breach.\nThe attacker was able to steal financial data from the bank by compromising only a single server.\nBased on this information, what should be one of your key recommendations to the bank?",
		"num": "182",
		"correct_answer": "a",
		"answers": {
			"a": "Place a front-end web server in a demilitarized zone that only handles external web traffic",
			"b": "Require all employees to change their passwords immediately",
			"c": "Move the financial data to another server on the same IP subnet",
			"d": "Issue new certificates to the web servers from the root certificate authority"
		}
	},
	{
		"question": "What is the IV key size used in WPA2?",
		"num": "183",
		"correct_answer": "d",
		"answers": {
			"a": "32",
			"b": "24",
			"c": "16",
			"d": "48",
			"e": "128"
		}
	},
	{
		"question": "Session Hijacking refers to the exploitation of a valid computer session where an attacker takes over a session between two computers.\nWhich of the following factor contribute to a successful session hijacking attack?",
		"num": "184",
		"correct_answer": "c",
		"answers": {
			"a": "Account lockout for invalid session IDs",
			"b": "Definite session expiration time",
			"c": "Weak session ID generation algorithm",
			"d": "No clear text transmission"
		}
	},
	{
		"question": "An unauthorized individual enters a building following an employee through the employee entrance after the lunch rush.\nWhat type of breach has the individual just performed?",
		"num": "185",
		"correct_answer": "b",
		"answers": {
			"a": "Reverse Social Engineering",
			"b": "Tailgating",
			"c": "Piggybacking",
			"d": "Announced"
		}
	},
	{
		"question": "The fundamental difference between symmetric and asymmetric key cryptographic systems is that symmetric key cryptography uses which of the following?",
		"num": "186",
		"correct_answer": "d",
		"answers": {
			"a": "Multiple keys for non-repudiation of bulk data",
			"b": "Different keys on both ends of the transport medium",
			"c": "Bulk encryption for data transmission over fiber",
			"d": "The same key on each end of the transmission medium"
		}
	},
	{
		"question": "In which location, SAM hash passwords are stored in Windows 7?",
		"num": "187",
		"correct_answer": "a",
		"answers": {
			"a": "c:\\windows\\system32\\config\\SAM",
			"b": "c:\\winnt\\system32\\machine\\SAM",
			"c": "c:\\windows\\etc\\drivers\\SAM",
			"d": "c:\\windows\\config\\etc\\SAM"
		}
	},
	{
		"question": "Identify the UDP port that Network Time Protocol (NTP) uses as its primary means of communication?",
		"num": "188",
		"correct_answer": "a",
		"answers": {
			"a": "123",
			"b": "161",
			"c": "69",
			"d": "113"
		}
	},
	{
		"question": "An ethical hacker for a large security research firm performs penetration tests, vulnerability tests, and risk assessments.\nA friend recently started a company and asks the hacker to perform a penetration test and vulnerability assessment of the new company as a favor.\nWhat should the hacker's next step be before starting work on this job?",
		"num": "189",
		"correct_answer": "b",
		"answers": {
			"a": "Start by foot printing the network and mapping out a plan of attack.",
			"b": "Ask the employer for authorization to perform the work outside the company.",
			"c": "Begin the reconnaissance phase with passive information gathering and then move into active information gathering.",
			"d": "Use social engineering techniques on the friend's employees to help identify areas that may be susceptible to attack."
		}
	},
	{
		"question": "A bank stores and processes sensitive privacy information related to home loans.\nHowever, auditing has never been enabled on the system.\nWhat is the first step that the bank should take before enabling the audit feature?",
		"num": "190",
		"correct_answer": "b",
		"answers": {
			"a": "Perform a vulnerability scan of the system.",
			"b": "Determine the impact of enabling the audit feature.",
			"c": "Perform a cost/benefit analysis of the audit feature.",
			"d": "Allocate funds for staffing of audit log review."
		}
	},
	{
		"question": "A hacker is attempting to use nslookup to query Domain Name Service (DNS).\nThe hacker uses the nslookup interactive mode for the search.\nWhich command should the hacker type into the command shell to request the appropriate records?",
		"num": "191",
		"correct_answer": "c",
		"answers": {
			"a": "Locate type=ns",
			"b": "Request type=ns",
			"c": "Set type=ns",
			"d": "Transfer type=ns"
		}
	},
	{
		"question": "Which type of intrusion detection system can monitor and alert on attacks, but cannot stop them?",
		"num": "192",
		"correct_answer": "b",
		"answers": {
			"a": "Detective",
			"b": "Passive",
			"c": "Intuitive",
			"d": "Reactive"
		}
	},
	{
		"question": "The configuration allows a wired or wireless network interface controller to pass all traffic it receives to the central processing unit (CPU), rather than passing only the frames that the controller is intended to receive.\nWhich of the following is being described?",
		"num": "193",
		"correct_answer": "d",
		"answers": {
			"a": "Port forwarding",
			"b": "Multi-cast mode",
			"c": "WEP",
			"d": "promiscuous mode"
		}
	},
	{
		"question": "How can a rootkit bypass Windows 7 operating system\u2019s kernel mode, code signing policy?",
		"num": "194",
		"correct_answer": "a",
		"answers": {
			"a": "Attaching itself to the master boot record in a hard drive and changing the machine\u2019s boot sequence/options.",
			"b": "Replacing patch system calls with its own version that hides the rootkit (attacker\u2019s) actions.",
			"c": "Performing common services for the application process and replacing real applications with fake ones.",
			"d": "Defeating the scanner from detecting any code change at the kernel."
		}
	},
	{
		"question": "Michael is a junior security analyst working for the National Security Agency (NSA) working primarily on\nbreaking terrorist encrypted messages. The NSA has a number of methods they use to decipher encrypted\nmessages including Government Access to Keys (GAK) and inside informants. The NSA holds secret\nbackdoor keys to many of the encryption algorithms used on the Internet. The problem for the NSA, and\nMichael, is that terrorist organizations are starting to use custom-built algorithms or obscure algorithms\npurchased from corrupt governments. For this reason, Michael and other security analysts like him have\nbeen forced to find different methods of deciphering terrorist messages. One method that Michael thought\nof using was to hide malicious code inside seemingly harmless programs. Michael first monitors sites and\nbulletin boards used by known terrorists, and then he is able to glean email addresses to some of these\nsuspected terrorists. Michael then inserts a stealth keylogger into a mapping program file readme.txt and\nthen sends that as an attachment to the terrorist. This keylogger takes screenshots every 2 minutes and\nalso logs all keyboard activity into a hidden file on the terrorist's computer. Then, the keylogger emails those\nfiles to Michael twice a day with a built in SMTP server. What technique has Michael used to disguise this\nkeylogging software?",
		"num": "195",
		"correct_answer": "c",
		"answers": {
			"a": "Steganography",
			"b": "Wrapping",
			"c": "ADS",
			"d": "Hidden Channels"
		}
	},
	{
		"question": "Which of these is NOT a countermeasure against a buffer overflow attack?",
		"num": "196",
		"correct_answer": "a",
		"answers": {
			"a": "All of the choices are countermeasures against a buffer overflow attack",
			"b": "Canary (security cookie)",
			"c": "Address space layout randomization",
			"d": "Setting the NX bit"
		}
	},
	{
		"question": "Which tool queries publicly available databases that contain domain name registration contact information?",
		"num": "197",
		"correct_answer": "c",
		"answers": {
			"a": "netstat",
			"b": "ifconfig",
			"c": "WHOIS",
			"d": "nslookup"
		}
	},
	{
		"question": "You are attempting to man-in-the-middle a session. Which protocol will allow you to guess a sequence number?",
		"num": "198",
		"correct_answer": "b",
		"answers": {
			"a": "ICMP",
			"b": "TCP",
			"c": "UPX",
			"d": "UPD"
		}
	},
	{
		"question": "Which of the following cryptography attack methods is usually performed without the use of a computer?",
		"num": "199",
		"correct_answer": "c",
		"answers": {
			"a": "Ciphertext-only attack",
			"b": "Chosen key attack",
			"c": "Rubber hose attack",
			"d": "Rainbow table attack"
		}
	},
	{
		"question": "In the software security development life cyle process, threat modeling occurs in which phase?",
		"num": "200",
		"correct_answer": "a",
		"answers": {
			"a": "Design",
			"b": "Requirements",
			"c": "Verification",
			"d": "Implementation"
		}
	},
	{
		"question": "Which of the following bit size images provides the most hiding space for information?",
		"num": "201",
		"correct_answer": "c",
		"answers": {
			"a": "Single bit",
			"b": "16-bit",
			"c": "24-bit",
			"d": "8-bit"
		}
	},
	{
		"question": "Jake is a network administrator who needs to get reports from all the computer and network devices on his network.\nJake wants to use SNMP but is afraid that won't be secure since passwords and messages are in clear text.\nHow can Jake gather network information in a secure manner?",
		"num": "202",
		"correct_answer": "a",
		"answers": {
			"a": "He can use SNMPv3",
			"b": "Jake can use SNMPrev5",
			"c": "He can use SecWMI",
			"d": "Jake can use SecSNMP"
		}
	},
	{
		"question": "Company A and Company B have just merged and each has its own Public Key Infrastructure (PKI).\nWhat must the Certificate Authorities (CAs) establish so that the private PKIs for Company A and Company B trust one another and each private PKI can validate digital certificates from the other company?",
		"num": "203",
		"correct_answer": "b",
		"answers": {
			"a": "Poly key exchange",
			"b": "Cross certification",
			"c": "Poly key reference",
			"d": "Cross-site exchange"
		}
	},
	{
		"question": "OpenSSL on Linux servers includes a command line tool for testing TLS.\nWhat is the name of the tool and the correct syntax to connect to a web server?",
		"num": "204",
		"correct_answer": "d",
		"answers": {
			"a": "openssl s_client \u2013site www.website.com:443",
			"b": "openssl_client \u2013site www.website.com:443",
			"c": "openssl_client \u2013connect www.website.com:443",
			"d": "openssl s_client \u2013connect www.website.com:443"
		}
	},
	{
		"question": "Your company was hired by a small healthcare provider to perform a technician assessment on the network.\nWhat is the best approach for discovering vulnerabilities on a Windows-based computer?",
		"num": "205",
		"correct_answer": "c",
		"answers": {
			"a": "Create a disk image of a clean Windows installation",
			"b": "Use the built-in Windows Update tool",
			"c": "Use a scan tool like Nessus",
			"d": "Check MITRE.org for the latest list of CVE findings"
		}
	},
	{
		"question": "Which of the following is a strong post designed to stop a car?",
		"num": "206",
		"correct_answer": "c",
		"answers": {
			"a": "Gate",
			"b": "Fence",
			"c": "Bollard",
			"d": "Reinforced rebar"
		}
	},
	{
		"question": "When a normal TCP connection starts, a destination host receives a SYN (synchronize/start) packet from a source host and sends back a SYN/ACK (synchronize acknowledge).\nThe destination host must then hear an ACK (acknowledge) of the SYN/ACK before the connection is established.\nThis is referred to as the \"TCP three-way handshake.\"\nWhile waiting for the ACK to the SYN ACK, a connection queue of finite size on the destination host keeps track of connections waiting to be completed.\nThis queue typically empties quickly since the ACK is expected to arrive a few milliseconds after the SYN ACK.\n\nHow would an attacker exploit this design by launching TCP SYN attack?",
		"num": "207",
		"correct_answer": "b",
		"answers": {
			"a": "Attacker generates TCP SYN packets with random destination addresses towards a victim host",
			"b": "Attacker floods TCP SYN packets with random source addresses towards a victim host",
			"c": "Attacker generates TCP ACK packets with random source addresses towards a victim host",
			"d": "Attacker generates TCP RST packets with random source addresses towards a victim host"
		}
	},
	{
		"question": "What is the best way a designer can mitigate buffer overflow from occurring in their code? Choose all that apply.",
		"num": "208",
		"correct_answer": "ad",
		"answers": {
			"a": "Use a protocol robustness test to verify the code meets qualifications for proper boundary and common key stroke entries.",
			"b": "Write code without boundary scans.",
			"c": "Write code that uses C++ and everything will be great, no worries.",
			"d": "Write code using boundary checks within the code."
		}
	},
	{
		"question": "When analyzing the IDS logs, the system administrator notices connections from outside of the LAN have been sending packets where the Source IP address and Destination IP address are the same.\nThere have been no alerts sent via email or logged in the IDS.\nWhich type of an alert is this?",
		"num": "209",
		"correct_answer": "b",
		"answers": {
			"a": "False positive",
			"b": "False negative",
			"c": "True positive",
			"d": "True negative"
		}
	},
	{
		"question": "What will the following command produce on a website's login page if executed successfully?\n\n  SELECT email, passwd, login_id, full_name FROM members WHERE email = 'someone@somewhere.com'; DROP TABLE members; --'",
		"num": "210",
		"correct_answer": "b",
		"answers": {
			"a": "This code will insert the someone@somewhere.com email address into the members table.",
			"b": "This command will delete the entire members table.",
			"c": "It retrieves the password for the first user in the members table.",
			"d": "This command will not produce anything since the syntax is incorrect."
		}
	},
	{
		"question": "Which of the following incident handling process phases is responsible for defining rules, collaborating human workforce, creating a back-up plan, and testing the plans for an organization?",
		"num": "211",
		"correct_answer": "d",
		"answers": {
			"a": "Containment phase",
			"b": "Recovery phase",
			"c": "Identification phase",
			"d": "Preparation phase"
		}
	},
	{
		"question": "Which of the following parameters describe LM Hash?\nI - The maximum password length is 14 characters.\nII - There are no distinctions between uppercase and lowercase.\nIII - The password is split into two 7-byte halves.",
		"num": "212",
		"correct_answer": "c",
		"answers": {
			"a": "I",
			"b": "II",
			"c": "I, II and III",
			"d": "I and II"
		}
	},
	{
		"question": "Which wireless standard has bandwidth up to 54 Mbps and signals in a regulated frequency spectrum around 5 GHz?",
		"num": "213",
		"correct_answer": "a",
		"answers": {
			"a": "802.11a",
			"b": "802.11b",
			"c": "802.11g",
			"d": "802.11i"
		}
	},
	{
		"question": "When writing shellcodes, you must avoid ____________ because these will end the string.",
		"num": "214",
		"correct_answer": "b",
		"answers": {
			"a": "Root bytes",
			"b": "Null bytes",
			"c": "Char bytes",
			"d": "Unicode bytes"
		}
	},
	{
		"question": "Perimeter testing means determining exactly what your firewall blocks and what it allows.\nTo conduct a good test, you can spoof source IP addresses and source ports.\nWhich of the following command results in packets that will appear to originate from the system at 10.8.8.8?\nSuch a packet is useful for determining whether the firewall is allowing random packets in or out of your network.\n",
		"num": "215",
		"correct_answer": "d",
		"answers": {
			"a": "hping3 -T 10.8.8.8 -S netbios -c 2 -p 80",
			"b": "hping3 -Y 10.8.8.8 -S windows -c 2 -p 80",
			"c": "hping3 -O 10.8.8.8 -S server -c 2 -p 80",
			"d": "hping3 -a 10.8.8.8 -S springfield -c 2 -p 80"
		}
	},
	{
		"question": "Neil is a network administrator working in Istanbul. Neil wants to setup a protocol analyzer on his network\nthat will receive a copy of every packet that passes through the main office switch. What type of port will\nNeil need to setup in order to accomplish this?",
		"num": "216",
		"correct_answer": "b",
		"answers": {
			"a": "Neil will have to configure a Bridged port that will copy all packets to the protocol analyzer.",
			"b": "Neil will need to setup SPAN port that will copy all network traffic to the protocol analyzer.",
			"c": "He will have to setup an Ether channel port to get a copy of all network traffic to the analyzer.",
			"d": "He should setup a MODS port which will copy all network traffic."
		}
	},
	{
		"question": "Which of the following is considered the most dangerous type of rootkit?",
		"num": "217",
		"correct_answer": "c",
		"answers": {
			"a": "System level",
			"b": "Library level",
			"c": "Kernel level",
			"d": "Application level"
		}
	},
	{
		"question": "Which tool would be used to collect wireless packet data?",
		"num": "218",
		"correct_answer": "a",
		"answers": {
			"a": "NetStumbler",
			"b": "John the Ripper",
			"c": "Nessus",
			"d": "Netcat"
		}
	},
	{
		"question": "Which of the following is an example of two factor authentication?",
		"num": "219",
		"correct_answer": "d",
		"answers": {
			"a": "PIN Number and Birth Date",
			"b": "Username and Password",
			"c": "Digital Certificate and Hardware Token",
			"d": "Fingerprint and Smartcard ID"
		}
	},
	{
		"question": "Which of the following types of firewalls ensures that the packets are part of the established session?",
		"num": "220",
		"correct_answer": "a",
		"answers": {
			"a": "Stateful inspection firewall",
			"b": "Application-level firewall",
			"c": "Circuit-level firewall",
			"d": "Switch-level firewall"
		}
	},
	{
		"question": "While checking the settings on the internet browser, a technician finds that the proxy server settings have been checked and a computer is trying to use itself as a proxy server.\nWhat specific octet within the subnet does the technician see?",
		"num": "221",
		"correct_answer": "b",
		"answers": {
			"a": "10.10.10.10",
			"b": "127.0.0.1",
			"c": "192.168.1.1",
			"d": "192.168.168.168"
		}
	},
	{
		"question": "What is the most secure way to mitigate the theft of corporate information from a laptop that was left in a hotel room?",
		"num": "222",
		"correct_answer": "b",
		"answers": {
			"a": "Set a BIOS password",
			"b": "Encrypt the data on the hard drive.",
			"c": "Use a strong logon password to the operating system.",
			"d": "Back up everything on the laptop and store the backup in a safe place."
		}
	},
	{
		"question": "You are trying to break into a highly classified top-secret mainframe computer with highest security system in place at Merclyn Barley Bank located in Los Angeles.\nYou know that conventional hacking doesn't work in this case, because organizations such as banks are generally tight and secure when it comes to protecting their systems.\nIn other words you are trying to penetrate an otherwise impenetrable system.\nHow would you proceed?",
		"num": "223",
		"correct_answer": "b",
		"answers": {
			"a": "Look for \"zero-day\" exploits at various underground hacker websites in Russia and China and buy the necessary exploits from these hackers and target the bank's network ",
			"b": "Try to hang around the local pubs or restaurants near the bank, get talking to a poorly-paid or disgruntled employee, and offer them money if they'll abuse their access privileges by providing you with sensitive information",
			"c": "Launch DDOS attacks against Merclyn Barley Bank's routers and firewall systems using 100, 000 or more \"zombies\" and \"bots\"",
			"d": "Try to conduct Man-in-the-Middle (MiTM) attack and divert the network traffic going to the Merclyn Barley Bank's Webserver to that of your machine using DNS Cache Poisoning techniques"
		}
	},
	{
		"question": "Information gathered from social networking websites such as Facebook, Twitter and LinkedIn can be used to launch which of the following types of attacks?\nChoose two answers.",
		"num": "224",
		"correct_answer": "bd",
		"answers": {
			"a": "Smurf attack",
			"b": "Social engineering attack",
			"c": "SQL injection attack",
			"d": "Phishing attack",
			"e": "Fraggle attack",
			"f": "Distributed denial of service attack"
		}
	},
	{
		"question": "Rootkits are kernel programs having the ability to hide themselves and cover up traces of activities. It replaces certain operating system calls and utilities with its own modified versions of those routines.\n\nWhich of the following rootkit modifies the boot sequence of the machine to load themselves instead of the original virtual machine monitor or operating system?",
		"num": "225",
		"correct_answer": "a",
		"answers": {
			"a": "Hypervisor level rootkit",
			"b": "Kernel level rootkit",
			"c": "Boot loader level rootkit",
			"d": "Library level rootkits"
		}
	},
	{
		"question": "What are common signs that a system has been compromised or hacked? (Choose three.)",
		"num": "226",
		"correct_answer": "abc",
		"answers": {
			"a": "Increased amount of failed logon events",
			"b": "Patterns in time gaps in system and/or event logs",
			"c": "New user accounts created",
			"d": "Consistency in usage baselines"
		}
	},
	{
		"question": "Study the snort rule given below and interpret the rule.\n\n  alert tcp any any --> 192.168.1.0/24 111 (content:\"|00 01 86 a5|\"; msG. \"mountd access\";)",
		"num": "227",
		"correct_answer": "d",
		"answers": {
			"a": "An alert is generated when a TCP packet is generated from any IP on the 192.168.1.0 subnet and destined to any IP on port 111",
			"b": "An alert is generated when any packet other than a TCP packet is seen on the network and destined for the 192.168.1.0 subnet",
			"c": "An alert is generated when a TCP packet is originated from port 111 of any IP address to the 192.168.1.0 subnet",
			"d": "An alert is generated when a TCP packet originating from any IP address is seen on the network and destined for any IP address on the 192.168.1.0 subnet on port 111"
		}
	},
	{
		"question": "Hacker is a person who illegally breaks into a system or network without any authorization to destroy, steal sensitive data or to perform any malicious attacks.Black hat hackers are:",
		"num": "228",
		"correct_answer": "a",
		"answers": {
			"a": "Individuals with extraordinary computing skills, resorting to malicious or destructive activities and are also known as crackers",
			"b": "Individuals professing hacker skills and using them for defensive purposes and are also known as security analysts",
			"c": "Individuals who aim to bring down critical infrastructure for a 'cause' and are not worried about facing 30 years in jail for their actions",
			"d": "Individuals who work both offensively and defensively at various times"
		}
	},
	{
		"question": "In IPv6 what is the major difference concerning application layer vulnerabilities compared to IPv4?",
		"num": "229",
		"correct_answer": "b",
		"answers": {
			"a": "Implementing IPv4 security in a dual-stack network offers protection from IPv6 attacks too.",
			"b": "Vulnerabilities in the application layer are independent of the network layer. Attacks and mitigation techniques are almost identical.",
			"c": "Due to the extensive security measures built in IPv6, application layer vulnerabilities need not be addresses.",
			"d": "Vulnerabilities in the application layer are greatly different from IPv4."
		}
	},
	{
		"question": "Which of the following scan only works if operating system?s TCP/IP implementation is based on RFC 793?",
		"num": "230",
		"correct_answer": "a",
		"answers": {
			"a": "NULL scan",
			"b": "IDLE scan",
			"c": "TCP connect scan",
			"d": "Maintaining Access",
			"e": "FTP bounce scan"
		}
	},
	{
		"question": "Which of these is present in BOTH Windows and Linux:",
		"num": "231",
		"correct_answer": "b",
		"answers": {
			"a": "Program code",
			"b": "All of these",
			"c": "Stack segment",
			"d": "Heap address space"
		}
	},
	{
		"question": "Identify SQL injection attack from the HTTP requests shown below:",
		"num": "232",
		"correct_answer": "a",
		"answers": {
			"a": "http://www.myserver.c0m/search.asp?lname=smith%27%3bupdate%20usertable%20set%20passwd%3d%27hAx0r%27%3b--%00",
			"b": "http://www.myserver.c0m/script.php?mydata=%3cscript%20src=%22",
			"c": "http%3a%2f%2fwww.yourserver.c0m%2fbadscript.js%22%3e%3c%2fscript%3e",
			"d": "http://www.victim.com/example accountnumber=67891&creditamount=999999999"
		}
	},
	{
		"question": "Which of these functions are vulnerable to buffer overflows?",
		"num": "233",
		"correct_answer": "d",
		"answers": {
			"a": "gets",
			"b": "sprintf",
			"c": "strcpy",
			"d": "All of these"
		}
	},
	{
		"question": "Which of the following techniques will identify if computer files have been changed?",
		"num": "234",
		"correct_answer": "c",
		"answers": {
			"a": "Network sniffing",
			"b": "Permission sets",
			"c": "Integrity checking hashes",
			"d": "Firewall alerts"
		}
	},
	{
		"question": "A new wireless client is configured to join an 802.11 network.\nThis client uses the same hardware and software as many of the other clients on the network.\nThe client can see the network, but cannot connect.\nA wireless packet sniffer shows that the Wireless Access Point (WAP) is not responding to the association requests being sent by the wireless client.\nWhat is a possible source of this problem?",
		"num": "235",
		"correct_answer": "a",
		"answers": {
			"a": "The WAP does not recognize the client\u2019s MAC address",
			"b": "The client cannot see the SSID of the wireless network",
			"c": "Client is configured for the wrong channel",
			"d": "The wireless client is not configured to use DHCP"
		}
	},
	{
		"question": "What is the best description of SQL Injection?",
		"num": "236",
		"correct_answer": "a",
		"answers": {
			"a": "It is an attack used to gain unauthorized access to a database.",
			"b": "It is an attack used to modify code in an application.",
			"c": "It is a Man-in-the-Middle attack between your SQL Server and Web App Server.",
			"d": "It is a Denial of Service Attack."
		}
	},
	{
		"question": "Samuel is the network administrator of DataX Communications, Inc. He is trying to configure his firewall to\nblock password brute force attempts on his network. He enables blocking the intruder's IP address for a\nperiod of 24 hours' time after more than three unsuccessful attempts. He is confident that this rule will\nsecure his network from hackers on the Internet.\nBut he still receives hundreds of thousands brute-force attempts generated from various IP addresses\naround the world. After some investigation he realizes that the intruders are using a proxy somewhere else\non the Internet which has been scripted to enable the random usage of various proxies on each request so\nas not to get caught by the firewall rule.\nLater he adds another rule to his firewall and enables small sleep on the password attempt so that if the\npassword is incorrect, it would take 45 seconds to return to the user to begin another attempt. Since an\nintruder may use multiple machines to brute force the password, he also throttles the number of\nconnections that will be prepared to accept from a particular IP address.\nThis action will slow the intruder's attempts.\nSamuel wants to completely block hackers brute force attempts on his network.\nWhat are the alternatives to defending against possible brute-force password attacks on his site?\n\n",
		"num": "237",
		"correct_answer": "d",
		"answers": {
			"a": "Enforce a password policy and use account lockouts after three wrong logon attempts even though this might lock out legit users",
			"b": "Enable the IDS to monitor the intrusion attempts and alert you by e-mail about the IP address of the intruder so that you can block them at the Firewall manually",
			"c": "Enforce complex password policy on your network so that passwords are more difficult to brute force",
			"d": "You cannot completely block the intruders attempt if they constantly switch proxies"
		}
	},
	{
		"question": "Which of the following statements would NOT be a proper definition for a Trojan Horse?",
		"num": "238",
		"correct_answer": "a",
		"answers": {
			"a": "An authorized program that has been designed to capture keyboard keystroke while the user is unaware of such activity being performed",
			"b": "An unauthorized program contained within a legitimate program. This unauthorized program performs functions unknown (and probably unwanted) by the user",
			"c": "A legitimate program that has been altered by the placement of unauthorized code within it; this code performs functions unknown (and probably unwanted) by the user",
			"d": "Any program that appears to perform a desirable and necessary function but that (because of unauthorized code within it that is unknown to the user) performs functions unknown (and definitelyunwanted) by the user."
		}
	},
	{
		"question": "Which layered approach to security hides data in ICMP traffic?",
		"num": "239",
		"correct_answer": "c",
		"answers": {
			"a": "Hiding directories",
			"b": "Encryption",
			"c": "Covert channels",
			"d": "Unique"
		}
	},
	{
		"question": "A Certificate Authority (CA) generates a key pair that will be used for encryption and decryption of email.\nThe integrity of the encrypted email is dependent on the security of which of the following?",
		"num": "240",
		"correct_answer": "b",
		"answers": {
			"a": "Public key",
			"b": "Private key",
			"c": "Modulus length",
			"d": "Email server certificate"
		}
	},
	{
		"question": "This international organization regulates billions of transactions daily and provides security guidelines to protect personally identifiable information (PII).\nThese security controls provide a baseline and prevent low-level hackers sometimes known as script kiddies from causing a data breach.\nWhich of the following organizations is being described?",
		"num": "241",
		"correct_answer": "b",
		"answers": {
			"a": "International Security Industry Organization (ISIO)",
			"b": "Payment Card Industry (PCI)",
			"c": "Institute of Electrical and Electronics Engineers (IEEE)",
			"d": "Center for Disease Control (CDC)"
		}
	},
	{
		"question": "What kind of detection techniques is being used in antivirus softwares that identifies malware by collecting data from multiple protected systems and instead of analyzing files locally it\u2019s made on the provider\u2019s environment.\n",
		"num": "242",
		"correct_answer": "d",
		"answers": {
			"a": "Behavioral based",
			"b": "Heuristics based",
			"c": "Honypot based",
			"d": "Cloud based"
		}
	},
	{
		"question": "During a penetration test, the tester conducts an ACK scan using NMAP against the external interface of the DMZ firewall.\nNMAP reports that port 80 is unfiltered.\nBased on this response, which type of packet inspection is the firewall conducting?",
		"num": "243",
		"correct_answer": "c",
		"answers": {
			"a": "Host",
			"b": "Stateful",
			"c": "Stateless",
			"d": "Application"
		}
	},
	{
		"question": "Using a swipe code is one way to increase mobile device security",
		"num": "244",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which process uses a GIF and BMP file that allows software to exactly reconstruct an original image?",
		"num": "245",
		"correct_answer": "b",
		"answers": {
			"a": "Lost",
			"b": "Lossless",
			"c": "Laid compression",
			"d": "Wasteless"
		}
	},
	{
		"question": "Which cipher encrypts the plain text digit (bit or byte) one by one?",
		"num": "246",
		"correct_answer": "d",
		"answers": {
			"a": "Classical cipher",
			"b": "Block cipher",
			"c": "Modern cipher",
			"d": "Stream cipher"
		}
	},
	{
		"question": "A company has five different subnets: 192.168.1.0, 192.168.2.0, 192.168.3.0, 192.168.4.0 and 192.168.5.0.\nHow can NMAP be used to scan these adjacent Class C networks?",
		"num": "247",
		"correct_answer": "a",
		"answers": {
			"a": "NMAP -P 192.168.1-5.",
			"b": "NMAP -P 192.168.0.0/16",
			"c": "NMAP -P 192.168.1.0, 2.0, 3.0, 4.0, 5.0",
			"d": "NMAP -P 192.168.1/17"
		}
	},
	{
		"question": "You are writing security policy that hardens and prevents Footprinting attempt by Hackers.\nWhich of the following countermeasures will NOT be effective against this attack?",
		"num": "248",
		"correct_answer": "f",
		"answers": {
			"a": "Configure routers to restrict the responses to Footprinting requests",
			"b": "Configure Web Servers to avoid information leakage and disable unwanted protocols",
			"c": "Lock the ports with suitable Firewall configuration",
			"d": "Use an IDS that can be configured to refuse suspicious traffic and pick up Footprinting patterns",
			"e": "Evaluate the information before publishing it on the Website/Intranet",
			"f": "Monitor every employee computer with Spy cameras, keyloggers and spy on them",
			"g": "Perform Footprinting techniques and remove any sensitive information found on DMZ sites"
		}
	},
	{
		"question": "Which of the following Exclusive OR transforms bits is NOT correct?",
		"num": "249",
		"correct_answer": "c",
		"answers": {
			"a": "0 xor 0 = 0",
			"b": "1 xor 0 = 1",
			"c": "1 xor 1 = 1",
			"d": "0 xor 1 = 1"
		}
	},
	{
		"question": "How do you defend against MAC attacks on a switch?",
		"num": "250",
		"correct_answer": "d",
		"answers": {
			"a": "Disable SPAN port on the switch",
			"b": "Enable SNMP Trap on the switch",
			"c": "Configure IP security on the switch",
			"d": "Enable Port Security on the switch"
		}
	},
	{
		"question": "More sophisticated IDSs look for common shellcode signatures. But even these systems can be bypassed, by using polymorphic shellcode.\nThis is a technique common among virus writers. It basically hides the true nature of the shellcode in different disguises.\nHow does a polymorphic shellcode work?",
		"num": "251",
		"correct_answer": "a",
		"answers": {
			"a": "They encrypt the shellcode by XORing values over the shellcode, using loader code to decrypt the shellcode, and then executing the decrypted shellcode",
			"b": "They convert the shellcode into Unicode, using loader to convert back to machine code then executing them",
			"c": "They reverse the working instructions into opposite order by masking the IDS signatures",
			"d": "They compress shellcode into normal instructions, uncompressed the shellcode using loader code and then executing the shellcode"
		}
	},
	{
		"question": "Joel and her team have been going through tons of garbage, recycled paper, and other rubbish in order to find some information about the target they are attempting to penetrate.\nHow would you call this type of activity?",
		"num": "252",
		"correct_answer": "a",
		"answers": {
			"a": "Dumpster Diving",
			"b": "Scanning",
			"c": "CI Gathering",
			"d": "Garbage Scooping"
		}
	},
	{
		"question": "One of the effective DoS/DDoS countermeasures is 'Throttling'. Which statement correctly defines this term?",
		"num": "253",
		"correct_answer": "a",
		"answers": {
			"a": "Set up routers that access a server with logic to adjust incoming traffic to levels that will be safe for the server to process",
			"b": "Providers can increase the bandwidth on critical connections to prevent them from going down in the event of an attack",
			"c": "Replicating servers that can provide additional failsafe protection",
			"d": "Load balance each server in a multiple-server architecture"
		}
	},
	{
		"question": "An attacker uses a communication channel within an operating system that is neither designed nor intended to transfer information.\nWhat is the name of the communications channel?",
		"num": "254",
		"correct_answer": "d",
		"answers": {
			"a": "Classified",
			"b": "Overt",
			"c": "Encrypted",
			"d": "Covert"
		}
	},
	{
		"question": "Which of the following is a component of a risk assessment?",
		"num": "255",
		"correct_answer": "a",
		"answers": {
			"a": "Administrative safeguards",
			"b": "Physical security",
			"c": "Logical interface",
			"d": "DMZ"
		}
	},
	{
		"question": "While performing online banking using a Web browser, a user receives an email that contains a link to an interesting Web site. When the user clicks on the link, another Web browser session starts and displays a video of cats playing a piano. The next business day, the user receives what looks like an email from his bank, indicating that his bank account has been accessed from a foreign country. The email asks the user to call his bank and verify the authorization of a funds transfer that took place.\nWhat Web browser-based security vulnerability was exploited to compromise the user?",
		"num": "256",
		"correct_answer": "b",
		"answers": {
			"a": "Web form input validation",
			"b": "Cross-Site Request Forgery",
			"c": "Clickjacking",
			"d": "Cross-Site Scripting"
		}
	},
	{
		"question": "You have successfully gained access to your client\u2019s internal network and successfully comprised a Linux server which is part of the internal IP network.\nYou want to know which Microsoft Windows workstations have file sharing enabled.\nWhich port would you see listening on these Windows machines in the network?",
		"num": "257",
		"correct_answer": "c",
		"answers": {
			"a": "161",
			"b": "3389",
			"c": "445",
			"d": "1433"
		}
	},
	{
		"question": "Which of the following tool would be considered as Signature Integrity Verifier (SIV)?",
		"num": "258",
		"correct_answer": "d",
		"answers": {
			"a": "Nmap",
			"b": "SNORT",
			"c": "VirusSCAN",
			"d": "Tripwire"
		}
	},
	{
		"question": "What is the benefit of performing an unannounced Penetration Testing?",
		"num": "259",
		"correct_answer": "a",
		"answers": {
			"a": "It is best approach to catch critical infrastructure unpatched.",
			"b": "The tester could easily acquire a complete overview of the infrastructure of the organization.",
			"c": "The tester will get a clearer picture of measures applied to information and system security of the organization.",
			"d": "The tester can test the response capabilities of the target organization."
		}
	},
	{
		"question": "Nmap is a free open source utility, which is designed to rapidly scan large networks.\nIdentify the Nmap Scan method that is often referred to as half open scan because it does not open a full TCP connection.\n",
		"num": "260",
		"correct_answer": "b",
		"answers": {
			"a": "ACK Scan",
			"b": "SYN Stealth",
			"c": "Half open",
			"d": "Windows Scan"
		}
	},
	{
		"question": "Which of the following protocols are susceptible to sniffing?",
		"num": "261",
		"correct_answer": "d",
		"answers": {
			"a": "SNMP",
			"b": "FTP",
			"c": "NNTP",
			"d": "Telnet"
		}
	},
	{
		"question": "In Risk Management, how is the term \"likelihood\" related to the concept of \"threat?\"",
		"num": "262",
		"correct_answer": "d",
		"answers": {
			"a": "Likelihood is a possible threat-source that may exploit a vulnerability.",
			"b": "Likelihood is the likely source of a threat that could exploit a vulnerability.",
			"c": "Likelihood is the probability that a vulnerability is a threat-source.",
			"d": "Likelihood is the probability that a threat-source will exploit a vulnerability."
		}
	},
	{
		"question": "Which security strategy requires using several, varying methods to protect IT systems against attacks?",
		"num": "263",
		"correct_answer": "a",
		"answers": {
			"a": "Defense in depth",
			"b": "Three-way handshake",
			"c": "Covert channels",
			"d": "Exponential backoff algorithm"
		}
	},
	{
		"question": "Which of these should be avoided to prevent a buffer overflow:",
		"num": "264",
		"correct_answer": "d",
		"answers": {
			"a": "streadd()",
			"b": "strcpy()",
			"c": "strcat()",
			"d": "All of these"
		}
	},
	{
		"question": "Buffer overflows can be used to perform DoS attacks. True or false?",
		"num": "265",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "What is the outcome of this command:\n\n  nc -l -p 2222 | nc 10.1.0.43 1234",
		"num": "266",
		"correct_answer": "b",
		"answers": {
			"a": "Netcat will listen on the 10.1.0.43 interface for 1234 seconds on port 2222.",
			"b": "Netcat will listen on port 2222 and output anything received to a remote connection on 10.1.0.43 port 1234.",
			"c": "Netcat will listen for a connection from 10.1.0.43 on port 1234 and output anything received to port 2222.",
			"d": "Netcat will listen on port 2222 and then output anything received to local interface 10.1.0.43."
		}
	},
	{
		"question": "How can a rootkit bypass Windows 7 operating system's kernel mode, code signing policy?",
		"num": "267",
		"correct_answer": "d",
		"answers": {
			"a": "Defeating the scanner from detecting any code change at the kernel",
			"b": "Replacing patch system calls with its own version that hides the rootkit (attacker's) actions",
			"c": "Performing common services for the application process and replacing real applications with fake ones",
			"d": "Attaching itself to the master boot record in a hard drive and changing the machine's boot sequence/ options"
		}
	},
	{
		"question": "Firewall is a set of related programs, located at a network gateway server that protects the resources of a private network from users from other networks.\nA firewall examines all traffic routed between the two networks to see if it meets certain criteria.\nPacket filter is one of the categories of firewall.\nPacket filtering firewall works at which of these layers of the OSI model?",
		"num": "268",
		"correct_answer": "a",
		"answers": {
			"a": "Network layer",
			"b": "Physical layer",
			"c": "Session layer",
			"d": "Application layer"
		}
	},
	{
		"question": "Steganography that is using a carrier chain would fail to reconstruct a message when:",
		"num": "269",
		"correct_answer": "a",
		"answers": {
			"a": "Any of these",
			"b": "A carrier is modified",
			"c": "Carriers are processed in the wrong order",
			"d": "A carrier is unavailable"
		}
	},
	{
		"question": "Which of the following is a mutation technique used for writing buffer overflow exploits in order to avoid IDS and other filtering mechanisms?",
		"num": "270",
		"correct_answer": "b",
		"answers": {
			"a": "Assuming that a string function is exploited, send a long string as the input",
			"b": "Randomly replace the NOPs with functionally equivalent segments of the code (e.g.: x++; x-; ? NOP NOP)",
			"c": "Pad the beginning of the intended buffer overflow with a long run of NOP instructions (a NOP slide or sled) so the CPU will do nothing until it gets to the ?main event? ",
			"d": "makes a buffer to overflow on the lower part of heap, overwriting other dynamic variables, which can have unexpected and unwanted effects "
		}
	},
	{
		"question": "Which of these options is the most secure procedure for storing backup tapes?",
		"num": "271",
		"correct_answer": "b",
		"answers": {
			"a": "In a cool dry environment.",
			"b": "In a climate controlled facility offsite.",
			"c": "Inside the data center for faster retrieval in a fireproof safe.",
			"d": "On a different floor in the same building."
		}
	},
	{
		"question": "Which of the following resources does NMAP need to be used as a basic vulnerability scanner covering several vectors like SMB, HTTP and FTP?",
		"num": "272",
		"correct_answer": "c",
		"answers": {
			"a": "Metasploit scripting engine",
			"b": "Nessus scripting engine",
			"c": "NMAP scripting engine",
			"d": "SAINT scripting engine"
		}
	},
	{
		"question": "Which of the following is the main use of digital watermarks and digital fingerprinting?",
		"num": "273",
		"correct_answer": "b",
		"answers": {
			"a": "Monitoring patent applications",
			"b": "Track copyright issues",
			"c": "Develop a covert communication",
			"d": "Enhance duplication"
		}
	},
	{
		"question": "How do employers protect assets with security policies pertaining to employee surveillance activities?",
		"num": "274",
		"correct_answer": "d",
		"answers": {
			"a": "Employers promote monitoring activities of employees as long as the employees demonstrate trustworthiness.",
			"b": "Employers use informal verbal communication channels to explain employee monitoring activities to employees.",
			"c": "Employers use network surveillance to monitor employee email traffic, network access, and to record employee keystrokes.",
			"d": "Employers provide employees written statements that clearly discuss the boundaries of monitoring activities and consequences."
		}
	},
	{
		"question": "Fingerprinting VPN firewalls is possible with which of the following tools?",
		"num": "275",
		"correct_answer": "c",
		"answers": {
			"a": "Angry IP",
			"b": "Nikto",
			"c": "Ike-scan",
			"d": "Arp-scan"
		}
	},
	{
		"question": "Address Resolution Protocol (ARP) is a protocol for mapping an IP address to a physical machine address that is recognized in the local network. ARP Spoofing involves constructing a large number of forged ARP request and reply packets to overload:",
		"num": "276",
		"correct_answer": "a",
		"answers": {
			"a": "Switch",
			"b": "Router",
			"c": "Hub",
			"d": "Bridge"
		}
	},
	{
		"question": "After gaining access to the password hashes used to protect access to a web based application, knowledge of which cryptographic algorithms would be useful to gain access to the application?",
		"num": "277",
		"correct_answer": "a",
		"answers": {
			"a": "SHA1",
			"b": "Diffie-Helman",
			"c": "RSA",
			"d": "AES"
		}
	},
	{
		"question": "Which of the following statements are true regarding N-tier architecture? (Choose two.)",
		"num": "278",
		"correct_answer": "ac",
		"answers": {
			"a": "Each layer must be able to exist on a physically independent system.",
			"b": "The N-tier architecture must have at least one logical layer.",
			"c": "Each layer should exchange information only with the layers above and below it.",
			"d": "When a layer is changed or updated, the other layers must also be recompiled or modified."
		}
	},
	{
		"question": "An intrusion detection system (IDS) gathers and analyzes information from within a computer or a network, to identify the possible violations of security policy, including unauthorized access, as well as misuse.\nWhich of the following IDS detection technique detects the intrusion based on the fixed behavioral characteristics of the users and components in a computer system?",
		"num": "279",
		"correct_answer": "b",
		"answers": {
			"a": "Signature recognition",
			"b": "Anomaly detection",
			"c": "Protocol anomaly detection",
			"d": "All of the above"
		}
	},
	{
		"question": "Which of the following examples best represents a logical or technical control?",
		"num": "280",
		"correct_answer": "a",
		"answers": {
			"a": "Security tokens",
			"b": "Heating and air conditioning",
			"c": "Smoke and fire alarms",
			"d": "Corporate security policy"
		}
	},
	{
		"question": "The following is part of a log file taken from the machine on the network with the IP address of\n192.168.1.106:\nTime:Mar 13 17:30:15 Port:20 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:17 Port:21 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:19 Port:22 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:21 Port:23 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:22 Port:25 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:23 Port:80 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nTime:Mar 13 17:30:30 Port:443 Source:192.168.1.103 Destination:192.168.1.106 Protocol:TCP\nWhat type of activity has been logged?",
		"num": "281",
		"correct_answer": "d",
		"answers": {
			"a": "Port scan targeting 192.168.1.103",
			"b": "Teardrop attack targeting 192.168.1.106",
			"c": "Denial of service attack targeting 192.168.1.103",
			"d": "Port scan targeting 192.168.1.106"
		}
	},
	{
		"question": "The Heartbleed bug was discovered in 2014 and is widely referred to under MITRE\u2019s Common Vulnerabilities and Exposures (CVE) as CVE- 2014- 0160.\nThis bug affects the OpenSSL implementation of the transport layer security (TLS) protocols defined in RFC6520.\nWhat type of key does this bug leave exposed to the Internet making exploitation of any compromised system very easy?",
		"num": "282",
		"correct_answer": "b",
		"answers": {
			"a": "Root",
			"b": "Private",
			"c": "Public",
			"d": "Shared"
		}
	},
	{
		"question": "You work for Acme Corporation as Sales Manager. The company has tight network security restrictions.\nYou are trying to steal data from the company's Sales database (Sales.xls) and transfer them to your home computer.\nYour company filters and monitors traffic that leaves from the internal network to the Internet.\n\nHow will you achieve this without raising suspicion?",
		"num": "283",
		"correct_answer": "c",
		"answers": {
			"a": "Encrypt the Sales.xls using PGP and e-mail it to your personal gmail account",
			"b": "Package the Sales.xls using Trojan wrappers and telnet them back your home computer",
			"c": "You can conceal the Sales.xls database in another file like photo.jpg or other files and send it out in an innocent looking email or file transfer using Steganography techniques",
			"d": "Change the extension of Sales.xls to sales.txt and upload them as attachment to your hotmail account"
		}
	},
	{
		"question": "John the hacker is sniffing the network to inject ARP packets. He injects broadcast frames onto the wire to conduct MiTM attack.\nWhat is the destination MAC address of a broadcast frame?",
		"num": "284",
		"correct_answer": "a",
		"answers": {
			"a": "0xFFFFFFFFFFFF",
			"b": "0xDDDDDDDDDDDD",
			"c": "0xAAAAAAAAAAAA",
			"d": "0xBBBBBBBBBBBB"
		}
	},
	{
		"question": "Least privilege is a security concept that requires that a user is",
		"num": "285",
		"correct_answer": "a",
		"answers": {
			"a": "limited to those functions required to do the job.",
			"b": "given root or administrative privileges.",
			"c": "trusted to keep all data and access to that data under their sole control.",
			"d": "given privileges equal to everyone else in the department."
		}
	},
	{
		"question": "This phase will increase the odds of success in later phases of the penetration test.\nIt is also the very first step in Information Gathering and it will tell you the \u201clandscape\u201d looks like.\nWhat is the most important phase of ethical hacking in which you need to spend a considerable amount of time?",
		"num": "286",
		"correct_answer": "b",
		"answers": {
			"a": "network mapping",
			"b": "footprinting",
			"c": "escalating privileges",
			"d": "gaining access"
		}
	},
	{
		"question": "Rootkits are harder to detect than other malware.",
		"num": "287",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which element of Public Key Infrastructure (PKI) verifies the applicant?",
		"num": "288",
		"correct_answer": "c",
		"answers": {
			"a": "Certificate authority",
			"b": "Validation authority",
			"c": "Registration authority",
			"d": "Verification authority"
		}
	},
	{
		"question": "A recently hired network security associate at a local bank was given the responsibility to perform daily scans of the internal network to look for unauthorized devices.\nThe employee decides to write a script that will scan the network for unauthorized devices every morning at 5:00 am.\nWhich of the following programming languages would most likely be used?",
		"num": "289",
		"correct_answer": "c",
		"answers": {
			"a": "PHP",
			"b": "C#",
			"c": "Python",
			"d": "ASP.NET"
		}
	},
	{
		"question": "Which of the following describes a component of Public Key Infrastructure (PKI) where a copy of a private key is stored to provide third-party access and to facilitate recovery operations?",
		"num": "290",
		"correct_answer": "d",
		"answers": {
			"a": "Key registry",
			"b": "Recovery agent",
			"c": "Directory",
			"d": "Key escrow"
		}
	},
	{
		"question": "Joseph has just been hired on to a contractor company of the Department of Defense as their Senior Security Analyst.\nJoseph has been instructed on the company's strict security policies that have been implemented, and the policies that have yet to be put in place.\nPer the Department of Defense, all DoD users and the users of their contractors must use two-factor authentication to access their networks.\nJoseph has been delegated the task of researching and implementing the best two-factor authentication method for his company.\nJoseph's supervisor has told him that they would like to use some type of hardware device in tandem with a security or identifying pin number.\nJoseph's company has already researched using smart cards and all the resources needed to implement them, but found the smart cards to not be cost effective.\nWhat type of device should Joseph use for two-factor authentication?",
		"num": "291",
		"correct_answer": "d",
		"answers": {
			"a": "Biometric device",
			"b": "OTP",
			"c": "Proximity cards",
			"d": "Security token"
		}
	},
	{
		"question": "What should you do if a friend asks you to perform and penetration test as a favor outside your normal job of being a pentester for a consulting company?",
		"num": "292",
		"correct_answer": "a",
		"answers": {
			"a": "Ask your employer for permission to perform the test outside of your normal work",
			"b": "Start social engineering the friends company",
			"c": "Start foot printing the friends\u2019 network",
			"d": "Start the test immediately"
		}
	},
	{
		"question": "What is the main use of digital watermarks and digital fingerprinting today?",
		"num": "293",
		"correct_answer": "a",
		"answers": {
			"a": "Track copyright issues",
			"b": "To develop covert communications",
			"c": "To monitor patent applications",
			"d": "To enhance duplication"
		}
	},
	{
		"question": "Steven the hacker realizes the network administrator of Acme Corporation is using syskey in Windows\n2008 Server to protect his resources in the organization. Syskey independently encrypts the hashes so that\nphysical access to the server, tapes, or ERDs is only first step to cracking the passwords. Steven must\nbreak through the encryption used by syskey before he can attempt to use brute force dictionary attacks on\nthe hashes. Steven runs a program called \"SysCracker\" targeting the Windows 2008 Server machine in\nattempting to crack the hash used by Syskey. He needs to configure the encryption level before he can\nlaunch the attack. How many bits does Syskey use for encryption?",
		"num": "294",
		"correct_answer": "b",
		"answers": {
			"a": "40-bit encryption",
			"b": "128-bit encryption",
			"c": "256-bit encryption",
			"d": "64-bit encryption"
		}
	},
	{
		"question": "WPA2 uses AES for wireless data encryption at which of the following encryption levels?",
		"num": "295",
		"correct_answer": "c",
		"answers": {
			"a": "64 bit and CCMP",
			"b": "128 bit and CRC",
			"c": "128 bit and CCMP",
			"d": "128 bit and TKIP"
		}
	},
	{
		"question": "Which command lets a tester enumerate alive systems in a class C network via ICMP using native Windows tools?",
		"num": "296",
		"correct_answer": "d",
		"answers": {
			"a": "ping 192.168.2.",
			"b": "ping 192.168.2.255",
			"c": "for %V in (1 1 255) do PING 192.168.2.%V",
			"d": "for /L %V in (1 1 254) do PING -n 1 192.168.2.%V | FIND /I \"Reply\""
		}
	},
	{
		"question": "Bob is going to perform an active session hijack against Brownies Inc. He has found a target that allows session oriented connections (Telnet) and performs the sequence prediction on the target operating system.\nHe manages to find an active session due to the high level of traffic on the network.\nWhat is Bob supposed to do next?",
		"num": "297",
		"correct_answer": "c",
		"answers": {
			"a": "Take over the session",
			"b": "Reverse sequence prediction",
			"c": "Guess the sequence numbers",
			"d": "Take one of the parties offline"
		}
	},
	{
		"question": "Denial of Service (DoS) is an attack on a computer or network that prevents legitimate use of its resources.\nIn a DoS attack, attackers flood a victim system with non-legitimate service requests or traffic to overload its resources, which prevents it from performing intended tasks.\nWhich of the following is a symptom of a DoS attack?",
		"num": "298",
		"correct_answer": "d",
		"answers": {
			"a": "Automatic increase in network performance",
			"b": "Decrease in the amount of spam emails received",
			"c": "Automatic increase in network bandwidth",
			"d": "Unavailability of a particular website"
		}
	},
	{
		"question": "A penetration tester is hired to do a risk assessment of a company's DMZ.\nThe rules of engagement states that the penetration test be done from an external IP address with no prior knowledge of the internal IT systems.\nWhat kind of test is being performed?",
		"num": "299",
		"correct_answer": "d",
		"answers": {
			"a": "white box",
			"b": "grey box",
			"c": "red box",
			"d": "black box"
		}
	},
	{
		"question": "A hacker searches in Google for filetype:pcf to find Cisco VPN config files.\nThose files may contain connectivity passwords that can be decoded with which of the following?",
		"num": "300",
		"correct_answer": "c",
		"answers": {
			"a": "Cupp",
			"b": "Nessus",
			"c": "Cain and Abel",
			"d": "John The Ripper Pro"
		}
	},
	{
		"question": "What should you do if a friend asks you to perform and penetration test as a favor outside your normal job of being a pen tester for a consulting company?",
		"num": "301",
		"correct_answer": "d",
		"answers": {
			"a": "Start the test immediately",
			"b": "Start foot printing the friend\u2019s network",
			"c": "Start social engineering the friends company",
			"d": "Ask your employer for permission to perform the test outside of your normal work"
		}
	},
	{
		"question": "Port scanning can be used as part of a technical assessment to determine network vulnerabilities.\nThe TCP XMAS scan is used to identify listening ports on the targeted system.\nIf a scanned port is open, what happens?",
		"num": "302",
		"correct_answer": "c",
		"answers": {
			"a": "The port will ignore the packets",
			"b": "The port will send an RST",
			"c": "The port will send a SYN",
			"d": "The port will send an ACK"
		}
	},
	{
		"question": "A hacker has successfully infected an internet-facing server which he will then use to send junk mail, take part in coordinated attacks, or host junk email content.\nWhich sort of Trojan infects this server?",
		"num": "303",
		"correct_answer": "c",
		"answers": {
			"a": "Turtle Trojans",
			"b": "Ransomware Trojans",
			"c": "Botnet Trojan",
			"d": "Banking Trojans"
		}
	},
	{
		"question": "What does a firewall check to prevent particular ports and applications from getting packets into an organization?",
		"num": "304",
		"correct_answer": "a",
		"answers": {
			"a": "Application layer port numbers and the transport layer headers",
			"b": "Transport layer port numbers and application layer headers",
			"c": "Presentation layer headers and the session layer port numbers",
			"d": "Network layer headers and the session layer port numbers"
		}
	},
	{
		"question": "Which of the following security policies defines the use of VPN for gaining access to an internal corporate network?",
		"num": "305",
		"correct_answer": "d",
		"answers": {
			"a": "Network security policy",
			"b": "Information protection policy",
			"c": "Access control policy",
			"d": "Remote access policy"
		}
	},
	{
		"question": "A covert channel is a channel that:",
		"num": "306",
		"correct_answer": "a",
		"answers": {
			"a": "transfers information over, within a computer system, or network that is outside of the security policy.",
			"b": "transfers information over, within a computer system, or network that is within the security policy.",
			"c": "transfers information via a communication path within a computer system, or network for transfer of data.",
			"d": "transfers information over, within a computer system, or network that is encrypted."
		}
	},
	{
		"question": "Session Hijacking refers to the exploitation of a valid computer session where an attacker takes over a session between two computers. \n\nWhich of the following factor contribute to a successful session hijacking attack?",
		"num": "307",
		"correct_answer": "c",
		"answers": {
			"a": "Account lockout for invalid session IDs",
			"b": "Definite session expiration time",
			"c": "Weak session ID generation algorithm",
			"d": "No clear text transmission"
		}
	},
	{
		"question": "Splint is a source code analyzer that is capable of detecting a ______",
		"num": "308",
		"correct_answer": "c",
		"answers": {
			"a": "XSRF",
			"b": "XSS",
			"c": "Buffer overflow",
			"d": "SQL injection"
		}
	},
	{
		"question": "A rootkit is capable of:",
		"num": "309",
		"correct_answer": "c",
		"answers": {
			"a": "Hiding processes",
			"b": "Hiding registry keys",
			"c": "All of these",
			"d": "Hiding files"
		}
	},
	{
		"question": "Which property ensures that a hash function will not produce the same hashed value for two different messages?",
		"num": "310",
		"correct_answer": "a",
		"answers": {
			"a": "Collision resistance",
			"b": "Bit length",
			"c": "Key strength",
			"d": "Entropy"
		}
	},
	{
		"question": "Which of the following areas is considered a strength of symmetric key cryptography when compared with asymmetric algorithms?",
		"num": "311",
		"correct_answer": "b",
		"answers": {
			"a": "Scalability",
			"b": "Speed",
			"c": "Key distribution",
			"d": "Security"
		}
	},
	{
		"question": "Which of the following is assured by the use of a hash?",
		"num": "312",
		"correct_answer": "d",
		"answers": {
			"a": "Authentication",
			"b": "Confidentially",
			"c": "Availability",
			"d": "Integrity"
		}
	},
	{
		"question": "Which definition below best describes a covert channel?",
		"num": "313",
		"correct_answer": "b",
		"answers": {
			"a": "A server program using a port that is not well known",
			"b": "Making use of a protocol in a way it was not intended to be used",
			"c": "It is the multiplexing taking place on a communication link",
			"d": "It is one of the weak channels used by WEP that makes it insecure"
		}
	},
	{
		"question": "You just set up a security system in your network.\nIn what kind of system would you find the following string of characters used as a rule within its configuration?\n\nalert tcp any any ->192.168.100.0/24 21 (msg:\u201d\u201dFTP on the network!\u201d\u201d;)",
		"num": "314",
		"correct_answer": "d",
		"answers": {
			"a": "A firewall IPTable",
			"b": "FTP Server rule",
			"c": "A Router IPTable",
			"d": "An Intrusion Detection System"
		}
	},
	{
		"question": "File extensions provide information regarding the underlying server technology. Attackers can use this information to search vulnerabilities and launch attacks.\nHow would you disable file extensions in Apache servers?",
		"num": "315",
		"correct_answer": "b",
		"answers": {
			"a": "Use disable-eXchange",
			"b": "Use mod_negotiation",
			"c": "Use Stop_Files",
			"d": "Use Lib_exchanges"
		}
	},
	{
		"question": "WWW wanderers or spiders are programs that traverse many pages in the World Wide Web by recursively retrieving linked pages.\nSearch engines like Google, frequently spider web pages for indexing.\nHow will you stop web spiders from crawling certain directories on your website?",
		"num": "316",
		"correct_answer": "a",
		"answers": {
			"a": "Place robots.txt file in the root of your website with listing of directories that you don't want to be crawled",
			"b": "Place authentication on root directories that will prevent crawling from these spiders",
			"c": "Enable SSL on the restricted directories which will block these spiders from crawling",
			"d": "Place \"HTTP:NO CRAWL\" on the html pages that you don't want the crawlers to index"
		}
	},
	{
		"question": "The traditional traceroute sends out ICMP ECHO packets with a TTL of one, and increments the TTL until the destination has been reached.\nBy printing the gateways that generate ICMP time exceeded messages along the way, it is able to determine the path packets take to reach the destination.\nThe problem is that with the widespread use of firewalls on the Internet today, many of the packets that traceroute sends out end up being filtered, making it impossible to completely trace the path to the destination.\nHow would you overcome the Firewall restriction on ICMP ECHO packets?",
		"num": "317",
		"correct_answer": "a",
		"answers": {
			"a": "Firewalls will permit inbound TCP packets to specific ports that hosts sitting behind the firewall are listening for connections. By sending out TCP SYN packets instead of ICMP ECHO packets, traceroute can bypass the most common firewall filters.",
			"b": "Firewalls will permit inbound UDP packets to specific ports that hosts sitting behind the firewall are listening for connections. By sending out TCP SYN packets instead of ICMP ECHO packets, traceroute can bypass the most common firewall filters.",
			"c": "Firewalls will permit inbound UDP packets to specific ports that hosts sitting behind the firewall are listening for connections. By sending out TCP SYN packets instead of ICMP ECHO packets, traceroute can bypass the most common firewall filters.",
			"d": "Do not use traceroute command to determine the path packets take to reach the destination instead use the custom hacking tool JOHNTHETRACER and run with the command\n\\> JOHNTHETRACER www.eccouncil.org -F -evade"
		}
	},
	{
		"question": "Dan is conducting penetration testing and has found a vulnerability in a Web Application which gave him the\nsessionID token via a cross site scripting vulnerability. Dan wants to replay this token. However, the session\nID manager (on the server) checks the originating IP address as well. Dan decides to spoof his IP address\nin order to replay the sessionI\n\nWhy do you think Dan might not be able to get an interactive session?",
		"num": "318",
		"correct_answer": "c",
		"answers": {
			"a": "Dan cannot spoof his IP address over TCP network",
			"b": "The scenario is incorrect as Dan can spoof his IP and get responses",
			"c": "The server will send replies back to the spoofed IP address",
			"d": "Dan can establish an interactive session only if he uses a NAT"
		}
	},
	{
		"question": "This IDS defeating technique works by splitting a datagram (or packet) into multiple fragments and the IDS will not spot the true nature of the fully assembled datagram.\nThe datagram is not reassembled until it reaches its final destination. It would be a processor-intensive task for IDS to reassemble all fragments itself, and on a busy system the packet will slip through the IDS onto the network.\nWhat is this technique\ncalled?",
		"num": "319",
		"correct_answer": "c",
		"answers": {
			"a": "IP Routing or Packet Dropping",
			"b": "IDS Spoofing or Session Assembly",
			"c": "IP Fragmentation or Session Splicing",
			"d": "IP Splicing or Packet Reassembly"
		}
	},
	{
		"question": "What does the \u2013oX flag do in an Nmap scan?",
		"num": "320",
		"correct_answer": "d",
		"answers": {
			"a": "Perform an Xmas scan",
			"b": "Perform an eXpress scan",
			"c": "Output the results in truncated format to the screen",
			"d": "Output the results in XML format to a file"
		}
	},
	{
		"question": "A Network Administrator was recently promoted to Chief Security Officer at a local university.\nOne of employee's new responsibilities is to manage the implementation of an RFID card access system to a new server room on campus.\nThe server room will house student enrollment information that is securely backed up to an off-site location.\nDuring a meeting with an outside consultant, the Chief Security Officer explains that he is concerned that the existing security controls have not been designed properly.\nCurrently, the Network Administrator is responsible for approving and issuing RFID card access to the server room, as well as reviewing the electronic access logs on a weekly basis.\nWhich of the following is an issue with the situation?",
		"num": "321",
		"correct_answer": "a",
		"answers": {
			"a": "Segregation of duties",
			"b": "Undue influence",
			"c": "Lack of experience",
			"d": "Inadequate disaster recovery plan"
		}
	},
	{
		"question": "Some passwords are stored using specialized encryption algorithms known as hashes.\nWhy is this an appropriate method?",
		"num": "322",
		"correct_answer": "d",
		"answers": {
			"a": "It is impossible to crack hashed user passwords unless the key used to encrypt them is obtained.",
			"b": "If a user forgets the password, it can be easily retrieved using the hash key stored by administrators.",
			"c": "Hashing is faster compared to more traditional encryption algorithms.",
			"d": "Passwords stored using hashes are non-reversible, making finding the password much more difficult."
		}
	},
	{
		"question": "Bluetooth hacking refers to exploitation of Bluetooth stack implementation vulnerabilities to compromise sensitive data in Bluetooth-enabled devices and networks.\nWhich of the following Bluetooth attack refers to sending unsolicited messages over Bluetooth to Bluetooth-enabled devices such as PDA and mobile phones?",
		"num": "323",
		"correct_answer": "b",
		"answers": {
			"a": "Bluesmacking",
			"b": "Bluejacking",
			"c": "Blue Snarfing",
			"d": "BlueSniff"
		}
	},
	{
		"question": "In this type of Man-in-the-Middle attack, packets and authentication tokens are captured using a sniffer.\nOnce the relevant information is extracted, the tokens are placed back on the network to gain access.",
		"num": "324",
		"correct_answer": "a",
		"answers": {
			"a": "Token Injection Replay attacks",
			"b": "Shoulder surfing attack",
			"c": "Rainbow and Hash generation attack",
			"d": "Dumpster diving attack"
		}
	},
	{
		"question": "John is an incident handler at a financial institution.\nHis steps in a recent incident are not up to the standards of the company.\nJohn frequently forgets some steps and procedures while handling responses as they are very stressful to perform.\nWhich of the following actions should John take to overcome this problem with the least administrative effort?",
		"num": "325",
		"correct_answer": "d",
		"answers": {
			"a": "Increase his technical skills",
			"b": "Read the incident manual every time it occurs",
			"c": "Select someone else to check the procedures",
			"d": "Create an incident checklist"
		}
	},
	{
		"question": "What type of encryption does WPA2 use?",
		"num": "326",
		"correct_answer": "b",
		"answers": {
			"a": "DES 64 bit",
			"b": "AES-CCMP 128 bit",
			"c": "MD5 48 bit",
			"d": "SHA 160 bit"
		}
	},
	{
		"question": "A security consultant decides to use multiple layers of anti-virus defense, such as end user desktop antivirus and E-mail gateway.\nThis approach can be used to mitigate which kind of attack?",
		"num": "327",
		"correct_answer": "c",
		"answers": {
			"a": "Forensic attack",
			"b": "ARP spoofing attack",
			"c": "Social engineering attack",
			"d": "Scanning attack"
		}
	},
	{
		"question": "Hayden is the network security administrator for her company, a large finance firm based in Miami.\nHayden just returned from a security conference in Las Vegas where they talked about all kinds of old and new security threats; many of which she did not know of.\nHayden is worried about the current security state of her company's network so she decides to start scanning the network from an external IP address.\nTo see how some of the hosts on her network react, she sends out SYN packets to an IP range.\nA number of IPs responds with a SYN/ACK response.\nBefore the connection is established she sends RST packets to those hosts to stop the session.\nShe does this to see how her intrusion detection system will log the traffic.\nWhat type of scan is Hayden attempting here?",
		"num": "328",
		"correct_answer": "d",
		"answers": {
			"a": "Hayden is attempting to find live hosts on her company's network by using an XMAS scan",
			"b": "She is utilizing a SYN scan to find live hosts that are listening on her network",
			"c": "The type of scan, she is using is called a NULL scan",
			"d": "Hayden is using a half-open scan to find live hosts on her network"
		}
	},
	{
		"question": "A technician is resolving an issue where a computer is unable to connect to the Internet using a wireless access point.\nThe computer is able to transfer files locally to other machines, but cannot successfully reach the Internet.\nWhen the technician examines the IP address and default gateway they are both on the 192.168.1.0/24.\nWhich of the following has occurred?",
		"num": "329",
		"correct_answer": "a",
		"answers": {
			"a": "The gateway is not routing to a public IP address.",
			"b": "The computer is using an invalid IP address.",
			"c": "The gateway and the computer are not on the same network.",
			"d": "The computer is not using a private IP address."
		}
	},
	{
		"question": "To maintain compliance with regulatory requirements, a security audit of the systems on a network must be performed to determine their compliance with security policies.\nWhich one of the following tools would most likely be used in such an audit?",
		"num": "330",
		"correct_answer": "c",
		"answers": {
			"a": "Intrusion Detection System",
			"b": "Protocol analyzer",
			"c": "Vulnerability scanner",
			"d": "Port scanner"
		}
	},
	{
		"question": "In the context of Trojans, what is the definition of a Wrapper?",
		"num": "331",
		"correct_answer": "b",
		"answers": {
			"a": "An encryption tool to protect the Trojan",
			"b": "A tool used to bind the Trojan with a legitimate file",
			"c": "A tool used to calculate bandwidth and CPU cycles wasted by the Trojan",
			"d": "A tool used to encapsulate packets within a new header and footer"
		}
	},
	{
		"question": "User which Federal Statutes does FBI investigate for computer crimes involving e-mail scams and mail fraud?",
		"num": "332",
		"correct_answer": "b",
		"answers": {
			"a": "18 U.S.C 1029 Possession of Access Devices",
			"b": "18 U.S.C 1030 Fraud and related activity in connection with computers",
			"c": "18 U.S.C 1343 Fraud by wire, radio or television",
			"d": "18 U.S.C 1361 Injury to Government Property",
			"e": "18 U.S.C 1362 Government communication systems",
			"f": "18 U.S.C 1831 Economic Espionage Act",
			"g": "18 U.S.C 1832 Trade Secrets Act"
		}
	},
	{
		"question": "SNMP is a connectionless protocol that uses UDP instead of TCP packets (True or False)",
		"num": "333",
		"correct_answer": "a",
		"answers": {
			"a": "true",
			"b": "false"
		}
	},
	{
		"question": "Trojan horse attacks pose one of the most serious threats to computer security.\nWhich are the easiest and most convincing ways to infect a computer?",
		"num": "334",
		"correct_answer": "b",
		"answers": {
			"a": "IRC (Internet Relay Chat)",
			"b": "Legitimate \"shrink-wrapped\" software packaged by a disgruntled employee",
			"c": "NetBIOS (File Sharing)",
			"d": "Downloading files, games and screensavers from Internet sites"
		}
	},
	{
		"question": "You are the Systems Administrator for a large corporate organization. You need to monitor all network traffic on your local network for suspicious activities and receive notifications when an attack is occurring. Which tool would allow you to accomplish this goal?",
		"num": "335",
		"correct_answer": "c",
		"answers": {
			"a": "Firewall",
			"b": "Proxy",
			"c": "Network-based IDS",
			"d": "Host-based IDS"
		}
	},
	{
		"question": "The SYN flood attack sends TCP connections requests faster than a machine can process them.\n- Attacker creates a random source address for each packet\n- SYN flag set in each packet is a request to open a new connection to the server from the spoofed IP address\n- Victim responds to spoofed IP address, then waits for confirmation that never arrives (timeout wait is about 3 minutes)\n- Victim's connection table fills up waiting for replies and ignores new connections\n- Legitimate users are ignored and will not be able to access the server\n\nHow do you protect your network against SYN Flood attacks?\n\nnumber generated as a hash of the clients IP address, port number, and other information. When the\nclient responds with a normal ACK, that special sequence number will be included, which the server\nthen verifies. Thus, the server first allocates memory on the third packet of the handshake, not the first.\n\nRST packet telling the server that something is wrong. At this point, the server knows the client is valid\nand will now accept incoming connections from that client normally\n\nusing ACLs at the Firewall\n\nReduce the timeout before a stack frees up the memory allocated for a connection\n\nfor the incoming SYN object",
		"num": "336",
		"correct_answer": "abde",
		"answers": {
			"a": "SYN cookies. Instead of allocating a record, send a SYN-ACK with a carefully constructed sequence number generated as a hash of the clients IP address, port number, and other information. When the client responds with a normal ACK, that special sequence number will be included, which the server then verifies. Thus, the server first allocates memory on the third packet of the handshake, not the first.",
			"b": "RST cookies - The server sends a wrong SYN/ACK back to the client. The client should then generate a RST packet telling the server that something is wrong. At this point, the server knows the client is valid and will now accept incoming connections from that client normally",
			"c": "Check the incoming packet's IP address with the SPAM database on the Internet and enable the filter using ACLs at the Firewal",
			"d": "Stack Tweaking. TCP stacks can be tweaked in order to reduce the effect of SYN floods. Reduce the timeout before a stack frees up the memory allocated for a connection",
			"e": "Micro Blocks. Instead of allocating a complete connection, simply allocate a micro record of 16- bytes for the incoming SYN object"
		}
	},
	{
		"question": "Which type of security document is written with specific step-by-step details?",
		"num": "337",
		"correct_answer": "b",
		"answers": {
			"a": "Process",
			"b": "Procedure",
			"c": "Policy",
			"d": "Paradigm"
		}
	},
	{
		"question": "Keystroke loggers are stealth software packages that are used to monitor keyboard activities. Which is the best location to place such keyloggers? ",
		"num": "338",
		"correct_answer": "a",
		"answers": {
			"a": "Keyboard hardware and the operating system",
			"b": "UPS and keyboard",
			"c": "Operating system and UPS",
			"d": "Monitor and keyboard software"
		}
	},
	{
		"question": "Ricardo wants to send secret messages to a competitor company.\nTo secure these messages, he uses a technique of hiding a secret message within an ordinary message.\nThe technique provides \u2018security through obscurity\u2019.\nWhat technique is Ricardo using?",
		"num": "339",
		"correct_answer": "b",
		"answers": {
			"a": "Encryption",
			"b": "Steganography",
			"c": "RSA algorithm",
			"d": "Public-key cryptography"
		}
	},
	{
		"question": "Lee is using Wireshark to log traffic on his network. He notices a number of packets being directed to an internal IP from an outside IP where the packets are ICMP and their size is around 65, 536 bytes.\nWhat is Lee seeing here?",
		"num": "340",
		"correct_answer": "c",
		"answers": {
			"a": "Lee is seeing activity indicative of a Smurf attack.",
			"b": "Most likely, the ICMP packets are being sent in this manner to attempt IP spoofing.",
			"c": "Lee is seeing a Ping of death attack.",
			"d": "This is not unusual traffic, ICMP packets can be of any size."
		}
	},
	{
		"question": "Yancey is a network security administrator for a large electric company. This company provides power for over 100, 000 people in Las Vegas.\nYancey has worked for his company for over 15 years and has become very successful.\nOne day, Yancey comes in to work and finds out that the company will be downsizing and he will be out of a job in two weeks.\nYancey is very angry and decides to place logic bombs, viruses, Trojans, and backdoors all over the network to take down the company once he has left.\nYancey does not care if his actions land him in jail for 30 or more years, he just wants the company to pay for what they are doing to him.\n\nWhat would Yancey be considered?",
		"num": "341",
		"correct_answer": "a",
		"answers": {
			"a": "Yancey would be considered a Suicide Hacker",
			"b": "Since he does not care about going to jail, he would be considered a Black Hat",
			"c": "Because Yancey works for the company currently; he would be a White Hat",
			"d": "Yancey is a Hacktivist Hacker since he is standing up to a company that is downsizing"
		}
	},
	{
		"question": "It is possible to hide a text message in _.",
		"num": "342",
		"correct_answer": "a",
		"answers": {
			"a": "All of these",
			"b": "A graphic file",
			"c": "An audio file",
			"d": "Another message"
		}
	},
	{
		"question": "While performing data validation of web content, a security technician is required to restrict malicious input.\nWhich of the following processes is an efficient way of restricting malicious input?",
		"num": "343",
		"correct_answer": "c",
		"answers": {
			"a": "Validate web content input for query strings.",
			"b": "Validate web content input with scanning tools.",
			"c": "Validate web content input for type, length, and range.",
			"d": "Validate web content input for extraneous queries."
		}
	},
	{
		"question": "Nation-state threat actors often discover vulnerabilities and hold on to them until they want to launch a sophisticated attack.\nThe Sutxnet attack was an unprecedented style of attack because it used four types of vulnerability.\nWhat is this style of attack called?",
		"num": "344",
		"correct_answer": "c",
		"answers": {
			"a": "zero-sum",
			"b": "no-day",
			"c": "zero-day",
			"d": "zero-hour"
		}
	},
	{
		"question": "A rooted Android device is usually less secure than an unrooted Android device. True or false?",
		"num": "345",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Password cracking is a technique used to extract user's password of application/files without the knowledge of the legitimate user.\nWhich of the password cracking technique will the attacker use if he/she gets some information about the password to crack?",
		"num": "346",
		"correct_answer": "c",
		"answers": {
			"a": "Denial of Service Attack",
			"b": "Syllable Attack",
			"c": "Rule-based Attack",
			"d": "Distributed Network Attack (DNA)"
		}
	},
	{
		"question": "A penetration tester is conducting a port scan on a specific host. The tester found several ports opened that were confusing in concluding the Operating System (OS) version installed.\nConsidering the NMAP result below, which of the following is likely to be installed on the target machine by the OS?\n\nStarting NMAP 5.21 at 2011-03-15 11:06 NMAP scan report for 172.16.40.65\nHost is up (1.00s latency)\nNot shown: 993 closed ports PORT STATE SERVICE 21/\ntcp open ftp 23/tcp open telnet 80/tcp open http 139/tcp open netbios-ssn 515/tcp open 631/tcp open ipp 9100/tcp open MAC Address: 00:00:48:0D:EE:8",
		"num": "347",
		"correct_answer": "d",
		"answers": {
			"a": "The host is likely a Windows machine",
			"b": "The host is likely a Linux machine.",
			"c": "The host is likely a router.",
			"d": "The host is likely a printer."
		}
	},
	{
		"question": "A security consultant is trying to bid on a large contract that involves penetration testing and reporting.\nThe company accepting bids wants proof of work so the consultant prints out several audits that have been performed.\nWhich of the following is likely to occur as a result?",
		"num": "348",
		"correct_answer": "b",
		"answers": {
			"a": "The consultant will ask for money on the bid because of great work.",
			"b": "The consultant may expose vulnerabilities of other companies.",
			"c": "The company accepting bids will want the same type of format of testing.",
			"d": "The company accepting bids will hire the consultant because of the great work performed."
		}
	},
	{
		"question": "You are analyzing a traffic on the network with Wireshark.\nYou want to routinely run a cron job which will run the capture against a specific set of IPs.\n\u2013 192.168.8.0/24.\nWhat command you would use?",
		"num": "349",
		"correct_answer": "b",
		"answers": {
			"a": "tshark \u2013net 192.255.255.255 mask 192.168.8.0",
			"b": "wireshark \u2013capture \u2013local \u2013masked 192.168.8.0 \u2013range 24",
			"c": "sudo tshark \u2013f \u201cnet 192.168.8.0/24\u201d",
			"d": "wireshark \u2013fetch \u201c192.168.8/*\u201d"
		}
	},
	{
		"question": "Defense-in-depth is a security strategy in which several protection layers are placed throughout an information system. It helps to prevent direct attacks against an information system and data because a break in one layer only leads the attacker to the next layer.",
		"num": "350",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "This type of Port Scanning technique splits TCP header into several packets so that the packet filters are not able to detect what the packets intends to do?",
		"num": "351",
		"correct_answer": "b",
		"answers": {
			"a": "UDP Scanning",
			"b": "IP Fragment Scanning",
			"c": "Inverse TCP flag scanning",
			"d": "ACK flag scanning"
		}
	},
	{
		"question": "What technique is used to perform a Connection Stream Parameter Pollution (CSPP) attack?",
		"num": "352",
		"correct_answer": "a",
		"answers": {
			"a": "Injecting parameters into a connection string using semicolons as a separator",
			"b": "Inserting malicious Javascript code into input parameters",
			"c": "Setting a user's session identifier (SID) to an explicit known value",
			"d": "Adding multiple parameters with the same name in HTTP requests"
		}
	},
	{
		"question": "Which vital role does the U.S. Computer Security Incident Response Team (CSIRT) provide?",
		"num": "353",
		"correct_answer": "a",
		"answers": {
			"a": "Incident response services to any user, company, government agency, or organization in partnership with the Department of Homeland Security",
			"b": "Maintenance of the nation's Internet infrastructure, builds out new Internet infrastructure, and decommissions old Internet infrastructure",
			"c": "Registration of critical penetration testing for the Department of Homeland Security and public and private sectors",
			"d": "Measurement of key vulnerability assessments on behalf of the Department of Defense (DOD) and State Department, as well as private sectors"
		}
	},
	{
		"question": "You want to perform advanced SQL Injection attack against a vulnerable website.\nYou are unable to perform command shell hacks on this server.\nWhat must be enabled in SQL Server to launch these attacks?",
		"num": "354",
		"correct_answer": "c",
		"answers": {
			"a": "System services",
			"b": "EXEC master access",
			"c": "xp_cmdshell",
			"d": "RDC"
		}
	},
	{
		"question": "Which statement is TRUE regarding network firewalls preventing Web Application attacks?",
		"num": "355",
		"correct_answer": "b",
		"answers": {
			"a": "Network firewalls can prevent attacks because they can detect malicious HTTP traffic.",
			"b": "Network firewalls cannot prevent attacks because ports 80 and 443 must be opened.",
			"c": "Network firewalls can prevent attacks if they are properly configured.",
			"d": "Network firewalls cannot prevent attacks because they are too complex to configure."
		}
	},
	{
		"question": "You generate MD5 128-bit hash on all files and folders on your computer to keep a baseline check for security reasons.\nWhat is the length of the MD5 hash?",
		"num": "356",
		"correct_answer": "a",
		"answers": {
			"a": "32 character",
			"b": "64 byte",
			"c": "48 char",
			"d": "128 kb"
		}
	},
	{
		"question": "The \"white box testing\" methodology enforces what kind of restriction?",
		"num": "357",
		"correct_answer": "d",
		"answers": {
			"a": "The internal operation of a system is only partly accessible to the tester.",
			"b": "Only the internal operation of a system is known to the tester.",
			"c": "Only the external operation of a system is accessible to the tester.",
			"d": "The internal operation of a system is completely known to the tester."
		}
	},
	{
		"question": "Why should the security analyst disable/remove unnecessary ISAPI filters?",
		"num": "358",
		"correct_answer": "b",
		"answers": {
			"a": "To defend against social engineering attacks",
			"b": "To defend against webserver attacks",
			"c": "To defend against jailbreaking",
			"d": "To defend against wireless attacks"
		}
	},
	{
		"question": "True or False: it is important to assess end-user security awareness on mobile devices.",
		"num": "359",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which device in a wireless local area network (WLAN) determines the next network point to which a packet should be forwarded toward its destination?",
		"num": "360",
		"correct_answer": "c",
		"answers": {
			"a": "Wireless modem",
			"b": "Antenna",
			"c": "Wireless router",
			"d": "Mobile station"
		}
	},
	{
		"question": "During a black-box pen test you attempt to pass IRC traffic over port 80/TCP from a compromised web enabled host.\nThe traffic gets blocked; however, outbound HTTP traffic is unimpeded.\nWhat type of firewall is inspecting outbound traffic?",
		"num": "361",
		"correct_answer": "c",
		"answers": {
			"a": "Circuit",
			"b": "Stateful",
			"c": "Application",
			"d": "Packet Filtering"
		}
	},
	{
		"question": "As a system administrator, you are responsible for maintaining the website of your company which deals in online recharge of mobile phone cards. One day to your surprise, you find the home page of your company?s website defaced. What is the reason for webpage defacement? ",
		"num": "362",
		"correct_answer": "c",
		"answers": {
			"a": "Denial of Service attack",
			"b": "Session Hijacking",
			"c": "DNS attack through cache poisoning",
			"d": "Buffer overflow"
		}
	},
	{
		"question": "Which of the following defines the role of a root Certificate Authority (CA) in a Public Key Infrastructure (PKI)?",
		"num": "363",
		"correct_answer": "d",
		"answers": {
			"a": "The root CA stores the user's hash value for safekeeping.",
			"b": "The root CA is the recovery agent used to encrypt data when a user's certificate is lost",
			"c": "The root CA is used to encrypt email messages to prevent unintended disclosure of data",
			"d": "The CA is the trusted root that issues certificates"
		}
	},
	{
		"question": "You have successfully compromised a machine on the network and found a server that is alive on the same network.\nYou tried to ping it but you didn't get any response back. What is happening?",
		"num": "364",
		"correct_answer": "b",
		"answers": {
			"a": "The ARP is disabled on the target server.",
			"b": "ICMP could be disabled on the target server.",
			"c": "TCP/IP doesn't support ICMP.",
			"d": "You need to run the ping command with root privileges."
		}
	},
	{
		"question": "One of the ways to map a targeted network for live hosts is by sending an ICMP ECHO request to the broadcast or the network address. The request would be broadcasted to all hosts on the targeted network.\nThe live hosts will send an ICMP ECHO Reply to the attacker's source IP address.\nYou send a ping request to the broadcast address 192.168.5.255.\nThere are 40 computers up and running on the target network. Only 13 hosts send a reply while others do not. Why?",
		"num": "365",
		"correct_answer": "a",
		"answers": {
			"a": "Windows machines will not generate an answer (ICMP ECHO Reply) to an ICMP ECHO request aimed at the broadcast address or at the network address.",
			"b": "Linux machines will not generate an answer (ICMP ECHO Reply) to an ICMP ECHO request aimed at the broadcast address or at the network address.",
			"c": "You should send a ping request with this command ping ? 192.168.5.0-255",
			"d": "You cannot ping a broadcast address. The above scenario is wrong."
		}
	},
	{
		"question": "Steganography can be used for legitimate purposes.",
		"num": "366",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "What is the purpose of DNS AAAA record?",
		"num": "367",
		"correct_answer": "d",
		"answers": {
			"a": "Address prefix record",
			"b": "Address database record",
			"c": "Authorization, Authentication and Auditing record",
			"d": "IPv6 address resolution record"
		}
	},
	{
		"question": "Which of the following is designed to identify malicious attempts to penetrate systems?",
		"num": "368",
		"correct_answer": "a",
		"answers": {
			"a": "Intrusion Detection System",
			"b": "Router",
			"c": "Proxy",
			"d": "Firewall"
		}
	},
	{
		"question": "It is a short-range wireless communication technology intended to replace the cables connecting portable of fixed devices while maintaining high levels of security.\nIt allows mobile phones, computers and other devices to connect and communicate using a short-range wireless connection.\nWhich of the following terms best matches the definition?\n\n",
		"num": "369",
		"correct_answer": "a",
		"answers": {
			"a": "Bluetooth",
			"b": "InfraRed",
			"c": "Radio-Frequency Identification",
			"d": "WLAN"
		}
	},
	{
		"question": "When performing a buffer overflow attack against a system protected by SafeSEH \nIf the canary is known, an attacker could potentially pass the canary check code by overwriting the canary with its known value, and controlling information with mismatched values.",
		"num": "370",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "What is the best way to defend against network sniffing?",
		"num": "371",
		"correct_answer": "a",
		"answers": {
			"a": "Register all machines MAC address in a Centralized Database and limit network connection to those machines.",
			"b": "Use Static IP's",
			"c": "Using encryption protocols on network communications",
			"d": "Restrict physical access to server rooms host critical servers."
		}
	},
	{
		"question": "Which of the following scanning technique attackers use to bypass firewall rules, logging mechanism, and hide themselves as usual network traffic?",
		"num": "372",
		"correct_answer": "a",
		"answers": {
			"a": "Stealth scanning technique",
			"b": "TCP connect scanning technique",
			"c": "Xmas scanning technique",
			"d": "Maintaining Access",
			"e": "FIN scanning technique"
		}
	},
	{
		"question": "Stephanie works as a records clerk in a large office building in downtown Chicago. On Monday, she went to\na mandatory security awareness class (Security5) put on by her company's IT department. During the\nclass, the IT department informed all employees that everyone's Internet activity was thenceforth going to\nbe monitored.\nStephanie is worried that her Internet activity might give her supervisor reason to write her up, or worse get\nher fired. Stephanie's daily work duties only consume about four hours of her time, so she usually spends\nthe rest of the day surfing the web. Stephanie really enjoys surfing the Internet but definitely does not want\nto get fired for it.\nWhat should Stephanie use so that she does not get in trouble for surfing the Internet?",
		"num": "373",
		"correct_answer": "b",
		"answers": {
			"a": "Stealth IE",
			"b": "Stealth Anonymizer",
			"c": "Stealth Firefox",
			"d": "Cookie Disabler"
		}
	},
	{
		"question": "Which programming language is the most likely to be susceptible to a buffer overflow attack?",
		"num": "374",
		"correct_answer": "c",
		"answers": {
			"a": "Java",
			"b": "Python",
			"c": "C",
			"d": "C#"
		}
	},
	{
		"question": "Which of the following is NOT part of CEH Scanning Methodology?",
		"num": "375",
		"correct_answer": "e",
		"answers": {
			"a": "Check for Live systems",
			"b": "Check for Open Ports",
			"c": "Banner Grabbing",
			"d": "Prepare Proxies",
			"e": "Social Engineering attacks",
			"f": "Scan for Vulnerabilities",
			"g": "Draw Network Diagrams"
		}
	},
	{
		"question": "Low humidity in a data center can cause which of the following problems?",
		"num": "376",
		"correct_answer": "c",
		"answers": {
			"a": "Heat",
			"b": "Corrosion",
			"c": "Static electricity",
			"d": "Airborne contamination"
		}
	},
	{
		"question": "What file system vulnerability does the following command take advantage of?\ntype c:\\anyfile.exe > c:\\winnt\\system32\\calc.exe:anyfile.exe",
		"num": "377",
		"correct_answer": "d",
		"answers": {
			"a": "HFS",
			"b": "Backdoor access",
			"c": "XFS",
			"d": "ADS"
		}
	},
	{
		"question": "Which of the following is one of the most effective ways to prevent Cross- site Scripting (XSS) flaws in software applications?",
		"num": "378",
		"correct_answer": "c",
		"answers": {
			"a": "Use digital certificates to authenticate a server prior to sending data",
			"b": "Use security policies and procedures to define and implement proper security settings",
			"c": "Validate and escape all information sent to a server",
			"d": "Verify access right before allowing access to protected information and UI controls"
		}
	},
	{
		"question": "This is an attack that takes advantage of a web site vulnerability in which the site displays content that includes un-sanitized user-provided data.\n\n  &lt;a href=\"http://foobar.com/index.html?id=%3Cscript%20src=%22http://baddomain.com/badscript.js %22%3E%3C/script%3E\"&gt;See foobar&lt;/a&gt;\n\nWhat is this attack?",
		"num": "379",
		"correct_answer": "a",
		"answers": {
			"a": "Cross-site-scripting attack",
			"b": "SQL Injection",
			"c": "URL Traversal attack",
			"d": "Buffer Overflow attack"
		}
	},
	{
		"question": "A security engineer has been asked to deploy a secure remote access solution that will allow employees to connect to the company's internal network.\nWhich of the following can be implemented to minimize the opportunity for the man-in-the-middle attack to occur?",
		"num": "380",
		"correct_answer": "c",
		"answers": {
			"a": "SSL",
			"b": "Mutual authentication",
			"c": "IPSec",
			"d": "Static IP addresses"
		}
	},
	{
		"question": "Blane is a security analyst for a law firm.\nOne of the lawyers needs to send out an email to a client but he wants to know if the email is forwarded on to any other recipients.\nThe client is explicitly asked not to resend the email since that would be a violation of the lawyer's and client's agreement for this particular case.\nWhat can Blane use to accomplish this?",
		"num": "381",
		"correct_answer": "d",
		"answers": {
			"a": "He can use a split-DNS service to ensure the email is not forwarded on.",
			"b": "A service such as HTTrack would accomplish this.",
			"c": "Blane could use MetaGoofil tracking tool.",
			"d": "Blane can use a service such as ReadNotify tracking tool."
		}
	},
	{
		"question": "The network in ABC company is using the network address 192.168.1.64 with mask 255.255.255.192.\nIn the network the servers are in the addresses 192.168.1.122, 192.168.1.123 and 192.168.1.124.\nAn attacker is trying to find those servers but he cannot see them in his scanning.\nThe command he is using is: nmap 192.168.1.64/28\n\nWhy he cannot see the servers?",
		"num": "382",
		"correct_answer": "c",
		"answers": {
			"a": "He needs to change the address to 192.168.1.0 with the same mask",
			"b": "He needs to add the command \u201c\u201dip address\u201d\u201d just before the IP address.",
			"c": "He is scanning from 192.168.1.64 to 192.168.1.78 because of the mask /28 and the servers are not in that range.",
			"d": "The network must be down and the nmap command and IP address are ok"
		}
	},
	{
		"question": "An Intrusion Detection System (IDS) has alerted the network administrator to a possibly malicious sequence of packets sent to a Web server in the network's external DMZ.\nThe packet traffic was captured by the IDS and saved to a PCAP file. What type of network tool can be used to determine if these packets are genuinely malicious or simply a false positive?",
		"num": "383",
		"correct_answer": "c",
		"answers": {
			"a": "Protocol analyzer",
			"b": "Network sniffer",
			"c": "Intrusion Prevention System (IPS)",
			"d": "Vulnerability scanner"
		}
	},
	{
		"question": "Web servers often contain directories that do not need to be indexed. You create a text file with search engine indexing restrictions and place it on the root directory of the Web Server.\n\nUser-agent: *\nDisallow: /images/\nDisallow: /banners/\nDisallow: /Forms/\nDisallow: /Dictionary/\nDisallow: /_borders/\nDisallow: /_fpclass/\nDisallow: /_overlay/\nDisallow: /_private/\nDisallow: /_themes/\n\nWhat is the name of this file?",
		"num": "384",
		"correct_answer": "a",
		"answers": {
			"a": "robots.txt",
			"b": "search.txt",
			"c": "blocklist.txt",
			"d": "spf.txt"
		}
	},
	{
		"question": "This IDS defeating technique works by splitting a datagram (or packet) into multiple fragments and the IDS will not spot the true nature of the fully assembled datagram.\nThe datagram is not reassembled until it reaches its final destination.\nIt would be a processor-intensive task for IDS to reassemble all fragments itself, and on a busy system the packet will slip through the IDS onto the network.\nWhat is this technique called?",
		"num": "385",
		"correct_answer": "c",
		"answers": {
			"a": "IP Routing or Packet Dropping",
			"b": "IDS Spoofing or Session Assembly",
			"c": "IP Fragmentation or Session",
			"d": "Splicing IP Splicing or Packet Reassembly"
		}
	},
	{
		"question": "Which of the following is a detective control?",
		"num": "386",
		"correct_answer": "c",
		"answers": {
			"a": "Smart card authentication",
			"b": "Security policy",
			"c": "Audit trail",
			"d": "Continuity of operations plan"
		}
	},
	{
		"question": "When you return to your desk after a lunch break, you notice a strange email in your inbox.\nThe sender is someone you did business with recently, but the subject line has strange characters in it.\nWhat should you do?",
		"num": "387",
		"correct_answer": "c",
		"answers": {
			"a": "Delete the email and pretend nothing happened.",
			"b": "Reply to the sender and ask them for more information about the message contents.",
			"c": "Forward the message to your company\u2019s security response team and permanently delete the message from your computer.",
			"d": "Forward the message to your supervisor and ask for her opinion on how to handle the situation."
		}
	},
	{
		"question": "You have compromised a server and successfully gained a root access.\nYou want to pivot and pass traffic undetected over the network and evade any possible Intrusion Detection System.\nWhat is the best approach?",
		"num": "388",
		"correct_answer": "c",
		"answers": {
			"a": "Install and use Telnet to encrypt all outgoing traffic from this server.",
			"b": "Use Alternate Data Streams to hide the outgoing packets from this server.",
			"c": "Install Cryptcat and encrypt outgoing packets from this server.",
			"d": "Use HTTP so that all traffic can be routed via a browser, thus evading the internal Intrusion Detection Systems."
		}
	},
	{
		"question": "Canaries are known values that are placed between a buffer and control data on the stack to monitor buffer overflows.",
		"num": "389",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Jason, a penetration tester, is testing a web application that he knows is vulnerable to an SQL injection but the results of the injection are not visible to him.\nHe tried waitfor delay command to check the SQL execution status which confirmed the presence of the SQL injection vulnerability.\nWhich type of SQL injection Jason is attempting on the web application?",
		"num": "390",
		"correct_answer": "d",
		"answers": {
			"a": "Simple SQL Injection",
			"b": "Error-based SQL injection",
			"c": "UNION SQL Injection",
			"d": "Blind SQL injection"
		}
	},
	{
		"question": "Wired Equivalent Privacy (WEP) is an IEEE 802.11 wireless protocol which provides security algorithms for data confidentiality during wireless transmissions.\nWEP uses stream cipher RC4 for confidentiality, and the CRC-32 checksum for integrity of wireless transmission.\nWhat is the size of WEP initialization vector (IV)?",
		"num": "391",
		"correct_answer": "c",
		"answers": {
			"a": "8-bit ",
			"b": "16-bit",
			"c": "24-bit ",
			"d": "32-bit"
		}
	},
	{
		"question": "Fred is the network administrator for his company. Fred is testing an internal switch.\nFrom an external IP address, Fred wants to try and trick this switch into thinking it already has established a session with his computer.\nHow can Fred accomplish this?",
		"num": "392",
		"correct_answer": "d",
		"answers": {
			"a": "Fred can accomplish this by sending an IP packet with the RST/SIN bit and the source address of his computer.",
			"b": "He can send an IP packet with the SYN bit and the source address of his computer.",
			"c": "Fred can send an IP packet with the ACK bit set to zero and the source address of the switch.",
			"d": "Fred can send an IP packet to the switch with the ACK bit and the source address of his machine."
		}
	},
	{
		"question": "When analyzing the IDS logs, the system administrator noticed an alert was logged when the external router was accessed from the administrator\u2019s Computer to update the router configuration.\nWhat type of an alert is this?",
		"num": "393",
		"correct_answer": "d",
		"answers": {
			"a": "False negative",
			"b": "True negative",
			"c": "True positive",
			"d": "False positive"
		}
	},
	{
		"question": "What does Cross-Site Scripting allow an attacker to do to a computer system?",
		"num": "394",
		"correct_answer": "e",
		"answers": {
			"a": "Defend themselves",
			"b": "Call people",
			"c": "Agree with policies",
			"d": "Delete information",
			"e": "Inject script into web pages"
		}
	},
	{
		"question": "John the Ripper is a technical assessment tool used to test the weakness of which of the following?",
		"num": "395",
		"correct_answer": "d",
		"answers": {
			"a": "Usernames",
			"b": "File permissions",
			"c": "Firewall rulesets",
			"d": "Passwords"
		}
	},
	{
		"question": "David is a security administrator working in Boston. David has been asked by the office's manager to block all POP3 traffic at the firewall because he believes employees are spending too much time reading personal email.\nHow can David block POP3 at the firewall?",
		"num": "396",
		"correct_answer": "d",
		"answers": {
			"a": "David can block port 125 at the firewall.",
			"b": "David can block all EHLO requests that originate from inside the office.",
			"c": "David can stop POP3 traffic by blocking all HELO requests that originate from inside the office.",
			"d": "David can block port 110 to block all POP3 traffic."
		}
	},
	{
		"question": "Which of the following is the BEST way to defend against network sniffing?",
		"num": "397",
		"correct_answer": "d",
		"answers": {
			"a": "Use Static IP Address",
			"b": "Register all machines MAC Address in a Centralized Database",
			"c": "Restrict Physical Access to Server Rooms hosting Critical Servers",
			"d": "Using encryption protocols to secure network communications"
		}
	},
	{
		"question": "The FIN flag is set and sent from host A to host B when host A has no more data to transmit (Closing a TCP connection).\nThis flag releases the connection resources.\nHowever, host A can continue to receive data as long as the SYN sequence numbers of transmitted packets from host B are lower than the packet segment containing the set FIN flag.",
		"num": "398",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "The Open Web Application Security Project (OWASP) testing methodology addresses the need to secure web applications by providing which one of the following services?",
		"num": "399",
		"correct_answer": "b",
		"answers": {
			"a": "An extensible security framework named COBIT",
			"b": "A list of flaws and how to fix them",
			"c": "Web application patches",
			"d": "A security certification for hardened web applications"
		}
	},
	{
		"question": "Your team has won a contract to infiltrate an organization.\nThe company wants to have the attack be as realistic as possible; therefore, they did not provide any information besides the company name.\nWhat should be the first step in security testing the client?",
		"num": "400",
		"correct_answer": "d",
		"answers": {
			"a": "Scanning",
			"b": "Enumeration",
			"c": "Escalation",
			"d": "Reconnaissance"
		}
	},
	{
		"question": "Finding tools to run dictionary and brute forcing attacks against FTP and Web servers is an easy task for hackers. They use tools such as arhontus or brutus to break into remote servers.\nA command such as this, will attack a given 10.0.0.34 FTP and Telnet servers simultaneously with a list of passwords and a single login name from major security sites.\nWhat defensive measures will you take to protect your network from these attacks?",
		"num": "401",
		"correct_answer": "abce",
		"answers": {
			"a": "Never leave a default password",
			"b": "Never use a password that can be found in a dictionary",
			"c": "Never use a password related to your hobbies, pets, relatives, or date of birth.",
			"d": "Use a word that has more than 21 characters from a dictionary as the password",
			"e": "Many FTP-specific password-guessing tools are also available",
			"f": "Never use a password related to the hostname, domain name, or anything else that can be found with whois"
		}
	},
	{
		"question": "Which of the following techniques can be used to mitigate the risk of an on-site attacker from connecting to an unused network port and gaining full access to the network? \nChoose three answers.",
		"num": "402",
		"correct_answer": "ace",
		"answers": {
			"a": "Port Security",
			"b": "IPSec Encryption",
			"c": "Network Admission Control (NAC)",
			"d": "802.1q Port Based Authentication",
			"e": "802.1x Port Based Authentication",
			"f": "Intrusion Detection System (IDS)"
		}
	},
	{
		"question": "You are the Security Administrator of Xtrinity, Inc. You write security policies and conduct assessments to protect the company's network. During one of your periodic checks to see how well policy is being observed by the employees, you discover an employee has attached cell phone 3G modem to his  elephone line and workstation. He has used this cell phone 3G modem to dial in to his workstation, thereby bypassing your firewall. A security breach has occurred as a direct result of this activity. The employee explains that he used the modem because he had to download software for a department project. How would you resolve this situation?",
		"num": "403",
		"correct_answer": "b",
		"answers": {
			"a": "Reconfigure the firewall",
			"b": "Enforce the corporate security policy",
			"c": "Install a network-based IDS",
			"d": "Conduct a needs analysis"
		}
	},
	{
		"question": "Switches maintain a CAM Table that maps individual MAC addresses on the network to physical ports on the switch.\nIn MAC flooding attack, a switch is fed with many Ethernet frames, each containing different source MAC addresses, by the attacker.\nSwitches have a limited memory for mapping various MAC addresses to physical ports.\nWhat happens when the CAM table becomes full?",
		"num": "404",
		"correct_answer": "a",
		"answers": {
			"a": "Switch then acts as hub by broadcasting packets to all machines on the network",
			"b": "The CAM overflow table will cause the switch to crash causing Denial of Service",
			"c": "The switch replaces outgoing frame switch factory default MAC address of FF:FF:FF:FF:FF:FF",
			"d": "Every packet is dropped and the switch sends out SNMP alerts to the IDS port"
		}
	},
	{
		"question": "What techniques would you use to evade IDS during a Port Scan? (Select 4 answers)",
		"num": "405",
		"correct_answer": "abde",
		"answers": {
			"a": "Use fragmented IP packets",
			"b": "Spoof your IP address when launching attacks and sniff responses from the server",
			"c": "Overload the IDS with Junk traffic to mask your scan",
			"d": "Use source routing (if possible)",
			"e": "Connect to proxy servers or compromised Trojaned machines to launch attacks"
		}
	},
	{
		"question": "Which security strategy requires using several, varying methods to protect IT systems against attacks?",
		"num": "406",
		"correct_answer": "a",
		"answers": {
			"a": "Defense in depth",
			"b": "Covert channels",
			"c": "Exponential backoff algorithm",
			"d": "Three-way handshake"
		}
	},
	{
		"question": "A penetration tester is conducting a port scan on a specific host.\nThe tester found several ports opened that were confusing in concluding the Operating System (OS) version installed.\nConsidering the NMAP result below, which of the following is likely to be installed on the target machine by the OS?\n\nStarting NMAP 5.21 at 2011-03-15 11:06\nNMAP scan report for 172.16.40.65\nHost is up (1.00s latency).\nNot shown: 993 closed ports\nPORT STATE SERVICE\n21/tcp open ftp\n23/tcp open telnet\n80/tcp open http\n139/tcp open netbios-ssn\n515/tcp open\n631/tcp open ipp\n9100/tcp open\nMAC Address: 00:00:48:0D:EE:89",
		"num": "407",
		"correct_answer": "d",
		"answers": {
			"a": "The host is likely a Windows machine.",
			"b": "The host is likely a Linux machine.",
			"c": "The host is likely a router.",
			"d": "The host is likely a printer."
		}
	},
	{
		"question": "In this attack, a victim receives an e-mail claiming from PayPal stating that their account has been disabled and confirmation is required before activation.\nThe attackers then scam to collect not one but two credit card numbers, ATM PIN number and other personal details.\n\nIgnorant users usually fall prey to this scam. Which of the following statement is incorrect related to this attack?",
		"num": "408",
		"correct_answer": "d",
		"answers": {
			"a": "Do not reply to email messages or popup ads asking for personal or financial information",
			"b": "Do not trust telephone numbers in e-mails or popup ads",
			"c": "Review credit card and bank account statements regularly",
			"d": "Antivirus, anti-spyware, and firewall software can very easily detect these type of attacks",
			"e": "Do not send credit card numbers, and personal or financial information via e-mail"
		}
	},
	{
		"question": "Which type of password cracking technique works like dictionary attack but adds some numbers and symbols to the words from the dictionary and tries to crack the password?",
		"num": "409",
		"correct_answer": "c",
		"answers": {
			"a": "Dictionary attack",
			"b": "Brute forcing attack",
			"c": "Hybrid attack",
			"d": "Syllable attack",
			"e": "Rule-based attack"
		}
	},
	{
		"question": "Will buffer overflows lead to remote code executions.",
		"num": "410",
		"correct_answer": "b",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which of these is the best defense against a buffer overflow attack?",
		"num": "411",
		"correct_answer": "d",
		"answers": {
			"a": "Dynamic runtime checks",
			"b": "Stack execute invalidation",
			"c": "Compiler tools",
			"d": "Write secure code"
		}
	},
	{
		"question": "What is the default Password Hash Algorithm used by NTLMv2?",
		"num": "412",
		"correct_answer": "d",
		"answers": {
			"a": "MD4",
			"b": "DES",
			"c": "SHA-1",
			"d": "MD5"
		}
	},
	{
		"question": "Which United States legislation mandates that the Chief Executive Officer (CEO) and the Chief Financial Officer (CFO) must sign statements verifying the completeness and accuracy of financial reports?",
		"num": "413",
		"correct_answer": "a",
		"answers": {
			"a": "Sarbanes-Oxley Act (SOX)",
			"b": "Gramm-Leach-Bliley Act (GLBA)",
			"c": "Fair and Accurate Credit Transactions Act (FACTA)",
			"d": "Federal Information Security Management Act (FISMA)"
		}
	},
	{
		"question": "Jason is the network administrator of Spears Technology. He has enabled SNORT IDS to detect attacks going through his network. He receives Snort SMS alerts on his iPhone whenever there is an attempted intrusion to his network.\nHe receives the following SMS message during the weekend.\nAn attacker Chew Siew sitting in Beijing, China had just launched a remote scan on Jason's network with the hping command.\nWhich of the following hping2 command is responsible for the above snort alert?",
		"num": "414",
		"correct_answer": "a",
		"answers": {
			"a": "chenrocks:/home/siew # hping -S -R -P -A -F -U 192.168.2.56 -p 22 -c 5 -t 118",
			"b": "chenrocks:/home/siew # hping -F -Q -J -A -C -W 192.168.2.56 -p 22 -c 5 -t 118",
			"c": "chenrocks:/home/siew # hping -D -V -R -S -Z -Y 192.168.2.56 -p 22 -c 5 -t 118",
			"d": "chenrocks:/home/siew # hping -G -T -H -S -L -W 192.168.2.56 -p 22 -c 5 -t 118"
		}
	},
	{
		"question": "What is this Shellshock bash vulnerability attempting to do on this vulnerable Linux host? env x='(){:;};echo exploit' bash -c 'cat /etc/passwd'",
		"num": "415",
		"correct_answer": "d",
		"answers": {
			"a": "Change all password in passwd",
			"b": "Remove the passwd file.",
			"c": "Add new user to the passwd file",
			"d": "Display passwd contents to prompt"
		}
	},
	{
		"question": "Which of the following Trojans would be considered 'Botnet Command Control Center'?",
		"num": "416",
		"correct_answer": "c",
		"answers": {
			"a": "YouKill DOOM",
			"b": "Damen Rock",
			"c": "Poison Ivy",
			"d": "Matten Kit"
		}
	},
	{
		"question": "Identify the denial-of-service attack that is carried out using a method known as bricking a system.\nUnlike other DoS attacks, it sabotages the system hardware, requiring the victim to replace or reinstall the hardware.\n",
		"num": "417",
		"correct_answer": "c",
		"answers": {
			"a": "ICMP Flood Attack",
			"b": "Application Level Flood Attacks",
			"c": "Phlashing",
			"d": "Bandwidth Attacks"
		}
	},
	{
		"question": "You have compromised a server on a network and successfully opened a shell. You aimed to identify all operating systems running on the network.\nHowever, as you attempt to fingerprint all machines in the network using the nmap syntax below, it is not going through.\n\ninvictus@victim_server:\n~$ nmap -T4 -O 10.10.0.0/24\nTCP/IP fingerprinting (for OS scan) xxxxxxx xxxxxx xxxxxxxxx. QUITTING!\n\nWhat seems to be wrong?",
		"num": "418",
		"correct_answer": "a",
		"answers": {
			"a": "OS Scan requires root privileges.",
			"b": "The nmap syntax is wrong.",
			"c": "This is a common behavior for a corrupted nmap application.",
			"d": "The outgoing TCP/IP fingerprinting is blocked by the host firewall."
		}
	},
	{
		"question": "You have several plain-text firewall logs that you must review to evaluate network traffic.\nYou know that in order to do fast, efficient searches of the logs you must use regular expressions.\nWhich command-line utility are you most likely to use?",
		"num": "419",
		"correct_answer": "a",
		"answers": {
			"a": "Grep",
			"b": "Relational Database",
			"c": "Notepad",
			"d": "MS Excel"
		}
	},
	{
		"question": "Maintaining a secure Web server requires constant effort, resources, and vigilance from an organization.\nSecurely administering a Web server on a daily basis is an essential aspect of Web server security.\nMaintaining the security of a Web server will usually involve the following steps:\n1. Configuring, protecting, and analyzing log files\n2. Backing up critical information frequently\n3. Maintaining a protected authoritative copy of the organization's Web content\n4. Establishing and following procedures for recovering from compromise\n5. Testing and applying patches in a timely manner\n6. Testing security periodically.\nIn which step would you engage a forensic investigator?",
		"num": "420",
		"correct_answer": "d",
		"answers": {
			"a": "1",
			"b": "2",
			"c": "3",
			"d": "4",
			"e": "5",
			"f": "6"
		}
	},
	{
		"question": "In keeping with the best practices of layered security, where are the best places to place intrusion detection/\nintrusion prevention systems? (Choose two.)",
		"num": "421",
		"correct_answer": "ac",
		"answers": {
			"a": "HID/HIP (Host-based Intrusion Detection/Host-based Intrusion Prevention)",
			"b": "NID/NIP (Node-based Intrusion Detection/Node-based Intrusion Prevention)",
			"c": "NID/NIP (Network-based Intrusion Detection/Network-based Intrusion Prevention)",
			"d": "CID/CIP (Computer-based Intrusion Detection/Computer-based Intrusion Prevention)"
		}
	},
	{
		"question": "John runs a Web server, IDS and firewall on his network.\nRecently his Web server has been under constant hacking attacks.\nHe looks up the IDS log files and sees no intrusion attempts but the Web server constantly locks up and needs rebooting due to various brute force and buffer overflow attacks but still the IDS alerts no intrusion whatsoever.\nJohn becomes suspicious and views the Firewall logs and he notices huge SSL connections constantly hitting his Web server.\nHackers have been using the encrypted HTTPS protocol to send exploits to the Web server and that was the reason the IDS did not detect the intrusions.\nHow would John protect his network from these types of attacks?\n(select 2 answers)",
		"num": "422",
		"correct_answer": "ac",
		"answers": {
			"a": "Install a proxy server and terminate SSL at the proxy",
			"b": "Enable the IDS to filter encrypted HTTPS traffic",
			"c": "Install a hardware SSL \"accelerator\" and terminate SSL at this layer",
			"d": "Enable the Firewall to filter encrypted HTTPS traffic"
		}
	},
	{
		"question": "Which of the following is a preventive control?",
		"num": "423",
		"correct_answer": "a",
		"answers": {
			"a": "Smart card authentication",
			"b": "Security policy",
			"c": "Audit trail",
			"d": "Continuity of operations plan"
		}
	},
	{
		"question": "Which of the following statement correctly defines ICMP Flood Attack? (Select 2 answers)",
		"num": "424",
		"correct_answer": "bd",
		"answers": {
			"a": "Bogus ECHO reply packets are flooded on the network spoofing the IP and MAC address",
			"b": "The ICMP packets signal the victim system to reply and the combination of traffic saturates the bandwidth of the victim's network",
			"c": "ECHO packets are flooded on the network saturating the bandwidth of the subnet causing denial of service",
			"d": "A DDoS ICMP flood attack occurs when the zombies send large volumes of ICMP_ECHO_REPLY packets to the victim system."
		}
	},
	{
		"question": "How do you defend against DHCP Starvation attack?",
		"num": "425",
		"correct_answer": "b",
		"answers": {
			"a": "Enable ARP-Block on the switch",
			"b": "Enable DHCP snooping on the switch",
			"c": "Configure DHCP-BLOCK to 1 on the switch",
			"d": "Install DHCP filters on the switch to block this attack"
		}
	},
	{
		"question": "Which of the following is a command line packet analyzer similar to GUI- based Wireshark?",
		"num": "426",
		"correct_answer": "c",
		"answers": {
			"a": "Ethereal",
			"b": "Nessus",
			"c": "Tcpdump",
			"d": "Jack the ripper"
		}
	},
	{
		"question": "Consider the following code:\n\nURL:http://www.certified.com/search.pl?text=&lt;script&gt;alert(document.cookie)&lt;/script&gt;\n\nIf an attacker can trick a victim user to click a link like this, and the Web application does not validate input, then the victim's browser will pop up an alert showing the users current set of cookies. An attacker can do much more damage, including stealing passwords, resetting your home page, or redirecting the user to another Web site.\n\nWhat is the countermeasure against XSS scripting?",
		"num": "427",
		"correct_answer": "b",
		"answers": {
			"a": "Create an IP access list and restrict connections based on port number",
			"b": "Replace \"<\" and \">\" characters with \"& l t;\" and \"& g t;\" using server scripts",
			"c": "Disable Javascript in IE and Firefox browsers",
			"d": "Connect to the server using HTTPS protocol instead of HTTP"
		}
	},
	{
		"question": "Windows file servers commonly hold sensitive files, databases, passwords and more.\nWhich of the following choices would be a common vulnerability that usually exposes them?",
		"num": "428",
		"correct_answer": "c",
		"answers": {
			"a": "Cross-site scripting",
			"b": "SQL injection",
			"c": "Missing patches",
			"d": "CRLF injection"
		}
	},
	{
		"question": "You receive an e-mail with the following text message.\n\"Microsoft and HP today warned all customers that a new, highly dangerous virus has been discovered which will erase all your files at midnight. If there's a file called hidserv.exe on your computer, you have been infected and your computer is now running a hidden server that allows \n hackers to access your computer. Delete the file immediately. Please also pass this message to all your friends and colleagues as soon as possible.\"\nYou launch your antivirus software and scan the suspicious looking file hidserv.exe located in c:\\windows directory and the AV comes out clean meaning the file is not infected. You view the file signature and confirm that it is a legitimate Windows system file \"Human Interface Device service\".\nWhat category of virus is this?",
		"num": "429",
		"correct_answer": "a",
		"answers": {
			"a": "Virus hoax",
			"b": "Spooky Virus",
			"c": "Stealth Virus",
			"d": "Polymorphic Virus"
		}
	},
	{
		"question": "A penetration tester is attempting to scan an internal corporate network from the internet without alerting the border sensor.\nWhich is the most efficient technique should the tester consider using?",
		"num": "430",
		"correct_answer": "b",
		"answers": {
			"a": "Spoofing an IP address",
			"b": "Tunneling scan over SSH",
			"c": "Tunneling over high port numbers",
			"d": "Scanning using fragmented IP packets"
		}
	},
	{
		"question": "What information should an IT system analysis provide to the risk assessor?",
		"num": "431",
		"correct_answer": "c",
		"answers": {
			"a": "Management buy-in",
			"b": "Threat statement",
			"c": "Security architecture",
			"d": "Impact analysis"
		}
	},
	{
		"question": "Which of the following is an application that requires a host application for replication?",
		"num": "432",
		"correct_answer": "d",
		"answers": {
			"a": "Micro",
			"b": "Worm",
			"c": "Trojan",
			"d": "Virus"
		}
	},
	{
		"question": "Pentest results indicate that voice over IP traffic is traversing a network.\nWhich of the following tools will decode a packet capture and extract the voice conversations?",
		"num": "433",
		"correct_answer": "a",
		"answers": {
			"a": "Cain",
			"b": "John the Ripper",
			"c": "Nikto",
			"d": "Hping"
		}
	},
	{
		"question": "Which of these attacks does bounds checking prevent:",
		"num": "434",
		"correct_answer": "c",
		"answers": {
			"a": "SQL injection",
			"b": "DoS",
			"c": "Buffer overflow",
			"d": "Memory overflow"
		}
	},
	{
		"question": "More sophisticated IDSs look for common shellcode signatures. But even these systems can be bypassed, by using polymorphic shellcode. This is a technique common among virus writers. It basically hides the true nature of the shellcode in different disguises.\nHow does a polymorphic shellcode work?",
		"num": "435",
		"correct_answer": "a",
		"answers": {
			"a": "They encrypt the shellcode by XORing values over the shellcode, using loader code to decrypt the shellcode, and then executing the decrypted shellcode",
			"b": "They convert the shellcode into Unicode, using loader to convert back to machine code then executing them",
			"c": "They reverse the working instructions into opposite order by masking the IDS signatures",
			"d": "They compress shellcode into normal instructions, uncompress the shellcode using loader code and then executing the shellcode"
		}
	},
	{
		"question": "Which of the following is a common Service Oriented Architecture (SOA) vulnerability?",
		"num": "436",
		"correct_answer": "d",
		"answers": {
			"a": "Cross-site scripting",
			"b": "SQL injection",
			"c": "VPath injection",
			"d": "XML denial of service issues"
		}
	},
	{
		"question": "You perform a scan of your company\u2019s network and discover that TCP port 123 is open.\nWhat services by default run on TCP port 123?",
		"num": "437",
		"correct_answer": "c",
		"answers": {
			"a": "Telnet",
			"b": "POP3",
			"c": "Network Time Protocol",
			"d": "DNS"
		}
	},
	{
		"question": "True or false. The robustness of spread spectrum steganography against active text comes at the cost of low and embedding capacity.",
		"num": "438",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Simon is security analyst writing signatures for a Snort node he placed internally that captures all mirrored traffic from his border firewall.\nFrom the following signature, what will Snort look for in the payload of the suspected packets?\n\nalert tcp $EXTERNAL_NET any -> $HOME_NET 27374 (msG.\"BACKDOOR SIG - SubSseven 22\";flags: A +; content: \"|0d0a5b52504c5d3030320d0a|\"; reference:arachnids, 485;) alert",
		"num": "439",
		"correct_answer": "b",
		"answers": {
			"a": "The payload of 485 is what this Snort signature will look for.",
			"b": "Snort will look for 0d0a5b52504c5d3030320d0a in the payload.",
			"c": "Packets that contain the payload of BACKDOOR SIG - SubSseven 22 will be flagged.",
			"d": "From this snort signature, packets with HOME_NET 27374 in the payload will be flagged."
		}
	},
	{
		"question": "Firewalk has just completed the second phase (the scanning phase) and a technician receives the output shown below.\nWhat conclusions can be drawn based on these scan results?\n\nTCP port 21 no response\nTCP port 22 no response\nTCP port 23 Time-to-live exceeded",
		"num": "440",
		"correct_answer": "c",
		"answers": {
			"a": "The firewall itself is blocking ports 21 through 23 and a service is listening on port 23 of the target host.",
			"b": "The lack of response from ports 21 and 22 indicate that those services are not running on the destination server.",
			"c": "The scan on port 23 passed through the filtering device. This indicates that port 23 was not blocked at the firewall.",
			"d": "The scan on port 23 was able to make a connection to the destination host prompting the firewall to respond with a TTL error."
		}
	},
	{
		"question": "Lori is a Certified Ethical Hacker as well as a Certified Hacking Forensics Investigator working as an IT\nsecurity consultant. Lori has been hired on by Kiley Innovators, a large marketing firm that recently\nunderwent a string of thefts and corporate espionage incidents. Lori is told that a rival marketing company\ncame out with an exact duplicate product right before Kiley Innovators was about to release it. The\nexecutive team believes that an employee is leaking information to the rival company. Lori questions all\nemployees, reviews server logs, and firewall logs; after which she finds nothing. Lori is then given\npermission to search through the corporate email system. She searches by email being sent to and sent\nfrom the rival marketing company.\nShe finds one employee that appears to be sending very large email to this other marketing company, even\nthough they should have no reason to be communicating with them. Lori tracks down the actual emails sent\nand upon opening them, only finds picture files attached to them. These files seem perfectly harmless,\nusually containing some kind of joke. Lori decides to use some special software to further examine the\npictures and finds that each one had hidden text that was stored in each picture.\nWhat technique was used by the Kiley Innovators employee to send information to the rival marketing\ncompany?",
		"num": "441",
		"correct_answer": "c",
		"answers": {
			"a": "The Kiley Innovators employee used cryptography to hide the information in the emails sent",
			"b": "The method used by the employee to hide the information was logical watermarking",
			"c": "The employee used steganography to hide information in the picture attachments",
			"d": "By using the pictures to hide information, the employee utilized picture fuzzing"
		}
	},
	{
		"question": "OS fingerprinting is the method used to determine the operating system running on a remote target system.\nIt is an important scanning method, as the attacker will have a greater probability of success if he/she knows the OS.\nActive stack fingerprinting is one of the types of OS fingerprinting.\nWhich of the following is true about active stack fingerprinting?",
		"num": "442",
		"correct_answer": "b",
		"answers": {
			"a": "Uses password crackers to escalate system privileges",
			"b": "Is based on the fact that various vendors of OS implement the TCP stack differently",
			"c": "TCP connect scan",
			"d": "Uses sniffing techniques instead of the scanning techniques",
			"e": "Is based on the differential implantation of the stack and the various ways an OS responds to it"
		}
	},
	{
		"question": "True or false, lossless compression is better suited to applications where the integrity of the original information must be maintained?",
		"num": "443",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which of the following is the structure designed to verify and authenticate the identity of individuals within the enterprise taking part in a data exchange?",
		"num": "444",
		"correct_answer": "a",
		"answers": {
			"a": "PKI",
			"b": "SOA",
			"c": "biometrics",
			"d": "single sign on"
		}
	},
	{
		"question": "Cyber Criminals have long employed the tactic of masking their true identity. In IP spoofing, an attacker gains unauthorized access to a computer or a network by making it appear that a malicious message has come from a trusted machine, by \"spoofing\" the IP address of that machine.\nHow would you detect IP spoofing?\n",
		"num": "445",
		"correct_answer": "d",
		"answers": {
			"a": "Check the IPID of the spoofed packet and compare it with TLC checksum. If the numbers match then it is spoofed packet.",
			"b": "Probe a SYN Scan on the claimed host and look for a response SYN/FIN packet, if the connection completes then it is a spoofed packet",
			"c": "Turn on 'Enable Spoofed IP Detection' in Wireshark, you will see a flag tick if the packet is spoofed",
			"d": "Sending a packet to the claimed host will result in a reply. If the TTL in the reply is not the same as the packet being checked then it is a spoofed packet"
		}
	},
	{
		"question": "A tester is attempting to capture and analyze the traffic on a given network and realizes that the network has several switches.\nWhat could be used to successfully sniff the traffic on this switched network?\n(Choose three answers)",
		"num": "446",
		"correct_answer": "abc",
		"answers": {
			"a": "ARP spoofing",
			"b": "MAC duplication",
			"c": "MAC flooding",
			"d": "SYN flood",
			"e": "Reverse smurf attack",
			"f": "ARP broadcasting"
		}
	},
	{
		"question": "An intrusion detection system (IDS) gathers and analyzes information from within a computer or a network, to identify the possible violations of security policy, including unauthorized access, as well as misuse.\nAttackers use various IDS evasion techniques to bypass intrusion detection mechanisms.\nWhich of the following evasion technique rely on Time-to-Live (TTL) fields of a TCP/IP packet?",
		"num": "447",
		"correct_answer": "c",
		"answers": {
			"a": "Denial-of-Service Attack",
			"b": "Obfuscation",
			"c": "Insertion Attack ",
			"d": "Unicode Evasion "
		}
	},
	{
		"question": "Which of the following are three primary colors that are normally used in image analysis?",
		"num": "448",
		"correct_answer": "c",
		"answers": {
			"a": "Peach, yellow, pink",
			"b": "Brown, red, orange",
			"c": "Red, green, blue",
			"d": "Black, white, gray"
		}
	},
	{
		"question": "Which of the choices is a form of steganography?",
		"num": "449",
		"correct_answer": "b",
		"answers": {
			"a": "Video recordings",
			"b": "Digital watermarking",
			"c": "Audio tapes",
			"d": "Password protection"
		}
	},
	{
		"question": "Which of the following provides a security professional with most information about the system\u2019s security posture?",
		"num": "450",
		"correct_answer": "d",
		"answers": {
			"a": "Wardriving, warchalking, social engineering",
			"b": "Social engineering, company site browsing, tailgating",
			"c": "Phishing, spamming, sending trojans",
			"d": "Port scanning, banner grabbing, service identification"
		}
	},
	{
		"question": "Which of the following processes evaluates the adherence of an organization to its stated security policy?",
		"num": "451",
		"correct_answer": "d",
		"answers": {
			"a": "Vulnerability assessment",
			"b": "Penetration testing",
			"c": "Risk assessment",
			"d": "Security auditing"
		}
	},
	{
		"question": "How can rainbow tables be defeated?",
		"num": "452",
		"correct_answer": "a",
		"answers": {
			"a": "Password salting",
			"b": "Use of non-dictionary words",
			"c": "All uppercase character passwords",
			"d": "Lockout accounts under brute force password cracking attempts"
		}
	},
	{
		"question": "A newly discovered flaw in a software application would be considered which kind of security vulnerability?",
		"num": "453",
		"correct_answer": "c",
		"answers": {
			"a": "Input validation flaw",
			"b": "HTTP header injection vulnerability",
			"c": "0-day vulnerability",
			"d": "Time-to-check to time-to-use flaw"
		}
	},
	{
		"question": "How does the Address Resolution Protocol (ARP) work?",
		"num": "454",
		"correct_answer": "b",
		"answers": {
			"a": "It sends a request packet to all the network elements, asking for the domain name from a specific IP.",
			"b": "It sends a request packet to all the network elements, asking for the MAC address from a specific IP.",
			"c": "It sends a reply packet for a specific IP, asking for the MAC address.",
			"d": "It sends a reply packet to all the network elements, asking for the MAC address from a specific IP."
		}
	},
	{
		"question": "Proxy is a network computer that can serve as an intermediary for connecting with other computers.\nWhich of the following sentence is true about a proxy?",
		"num": "455",
		"correct_answer": "d",
		"answers": {
			"a": "Cannot be used to filter out unwanted content",
			"b": "Does not allow the connection of a number of computers to the Internet when having only one IP address",
			"c": "Allows attacker to view the desktop of users system",
			"d": "Protects the local network from outside access"
		}
	},
	{
		"question": "To maintain compliance with regulatory requirements, a security audit of the systems on a network must be performed to determine their compliance with security policies.\nWhich one of the following tools would most likely be used in such an audit?",
		"num": "456",
		"correct_answer": "d",
		"answers": {
			"a": "Protocol analyzer ",
			"b": "Intrusion Detection System",
			"c": "Port scanner",
			"d": "Vulnerability scanner"
		}
	},
	{
		"question": "Traffic security can be correctly categorized under:",
		"num": "457",
		"correct_answer": "d",
		"answers": {
			"a": "Traffic intelligence",
			"b": "Electric intelligence",
			"c": "Electronic security",
			"d": "Communication security"
		}
	},
	{
		"question": "An Attacker creates a zuckerjournals.com website by copying and mirroring HACKERJOURNALS.COM site to spread the news that Hollywood actor Jason Jenkins died in a car accident.\nThe attacker then submits his fake site for indexing in major search engines.\nWhen users search for \"Jason Jenkins\", attacker's fake site shows up and dupes victims by the fake news.\nThis is another great example that some people do not know what URL's are.\n\n  Real website: http://www.hackerjournals.com\n  Fake website: http://www.zuckerjournals.com\n\nThe website is clearly not WWW.HACKERJOURNALS.COM.\nIt is obvious for many, but unfortunately some people still do not know what an URL is. It's the address that you enter into the address bar at the top your browser and this is clearly not legit site, its www.zuckerjournals.com\n\nHow would you verify if a website is authentic or not?",
		"num": "458",
		"correct_answer": "d",
		"answers": {
			"a": "Visit the site using secure HTTPS protocol and check the SSL certificate for authenticity",
			"b": "Navigate to the site by visiting various blogs and forums for authentic links",
			"c": "Enable Cache on your browser and lookout for error message warning on the screen",
			"d": "Visit the site by clicking on a link from Google search engine"
		}
	},
	{
		"question": "What are the limitations of Vulnerability scanners? (Select 2 answers)",
		"num": "459",
		"correct_answer": "ac",
		"answers": {
			"a": "There are often better at detecting well-known vulnerabilities than more esoteric ones",
			"b": "The scanning speed of their scanners are extremely high",
			"c": "It is impossible for any, one scanning product to incorporate all known vulnerabilities in a timely manner",
			"d": "The more vulnerabilities detected, the more tests required",
			"e": "They are highly expensive and require per host scan license"
		}
	},
	{
		"question": "Using Windows CMD, how would an attacker list all the shares to which the current user context has access?",
		"num": "460",
		"correct_answer": "c",
		"answers": {
			"a": "NET FILE",
			"b": "NET USE",
			"c": "NET VIEW",
			"d": "NET CONFIG"
		}
	},
	{
		"question": "In which step Steganography fits in CEH System Hacking Cycle (SHC)",
		"num": "461",
		"correct_answer": "e",
		"answers": {
			"a": "Step 1: Enumerate users",
			"b": "Step 2: Crack the password",
			"c": "Step 3: Escalate privileges",
			"d": "Step 4: Execute applications",
			"e": "Step 5: Hide files",
			"f": "Step 6: Cover your tracks"
		}
	},
	{
		"question": "During a wireless penetration test, a tester detects an access point using WPA2 encryption.\nWhich of the following attacks should be used to obtain the key?",
		"num": "462",
		"correct_answer": "a",
		"answers": {
			"a": "The tester must capture the WPA2 authentication handshake and then crack it.",
			"b": "The tester must use the tool inSSIDer to crack it using the ESSID of the network.",
			"c": "The tester cannot crack WPA2 because it is in full compliance with the IEEE 802.11i standard.",
			"d": "The tester must change the MAC address of the wireless network card and then use the AirTraf tool to obtain the key."
		}
	},
	{
		"question": "Some clients of TPNQM SA were redirected to a malicious site when they tried to access the TPNQM main site.\nBob, a system administrator at TPNQM SA, found that they were victims of DNS Cache Poisoning.\nWhat should Bob recommend to deal with such a threat?",
		"num": "463",
		"correct_answer": "b",
		"answers": {
			"a": "The use of security agents in clients\u2019 computers",
			"b": "The use of DNSSEC",
			"c": "The use of double-factor authentication",
			"d": "Client awareness"
		}
	},
	{
		"question": "A pentester gains acess to a Windows application server and needs to determine the settings of the built-in Windows firewall.\nWhich command would be used?",
		"num": "464",
		"correct_answer": "a",
		"answers": {
			"a": "Netsh firewall show config",
			"b": "WMIC firewall show config",
			"c": "Net firewall show config",
			"d": "Ipconfig firewall show config"
		}
	},
	{
		"question": "In steganography, it is crucial that only those people who are expecting the message know the message exists.",
		"num": "465",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which of the following programming languages are less vunerable to buffer overflow attacks? (select 3)",
		"num": "466",
		"correct_answer": "aef",
		"answers": {
			"a": "Ruby",
			"b": "C",
			"c": "C++",
			"d": "Assembly",
			"e": "Java",
			"f": "Python"
		}
	},
	{
		"question": "You are the Network Admin, and you get a complaint that some of the websites are no longer accessible.\nYou try to ping the servers and find them to be reachable.\nThen you type the IP address and then you try on the browser, and find it to be accessible.\nBut they are not accessible when you try using the URL.\nWhat may be the problem?",
		"num": "467",
		"correct_answer": "a",
		"answers": {
			"a": "Traffic is Blocked on TCP Port 53",
			"b": "Traffic is Blocked on TCP Port 80",
			"c": "Traffic is Blocked on UDP Port 54",
			"d": "Traffic is Blocked on UDP Port 80"
		}
	},
	{
		"question": "Stephanie works as senior security analyst for a manufacturing company in Detroit. Stephanie manages network security throughout the organization.\nHer colleague Jason told her in confidence that he was able to see confidential corporate information posted on the external website http://www.jeansclothesman.com.\nHe tries random URLs on the company's website and finds confidential information leaked over the web.\nJason says this happened about a month ago. Stephanie visits the said URLs, but she finds nothing. She is very concerned about this, since someone should be held accountable if there was sensitive information posted on the website.\nWhere can Stephanie go to see past versions and pages of a website?",
		"num": "468",
		"correct_answer": "c",
		"answers": {
			"a": "She should go to the web page Samspade.org to see web pages that might no longer be on the website",
			"b": "If Stephanie navigates to Search.com; she will see old versions of the company website",
			"c": "Stephanie can go to Archive.org to see past versions of the company website",
			"d": "AddressPast.com would have any web pages that are no longer hosted on the company's website"
		}
	},
	{
		"question": "Which of these choices is a form of steganography?",
		"num": "469",
		"correct_answer": "a",
		"answers": {
			"a": "Digital watermarking",
			"b": "Video recordings",
			"c": "Audio tapes",
			"d": "Password protection"
		}
	},
	{
		"question": "International Organization for Standardization (ISO) standard 27002 provides guidance for compliance by outlining",
		"num": "470",
		"correct_answer": "a",
		"answers": {
			"a": "guidelines and practices for security controls.",
			"b": "financial soundness and business viability metrics.",
			"c": "standard best practice for configuration management.",
			"d": "contract agreement writing standards."
		}
	},
	{
		"question": "What is the purpose of conducting security assessments on network resources?",
		"num": "471",
		"correct_answer": "b",
		"answers": {
			"a": "Documentation",
			"b": "Validation",
			"c": "Implementation",
			"d": "Management"
		}
	},
	{
		"question": "What is the best description of SQL Injection?",
		"num": "472",
		"correct_answer": "d",
		"answers": {
			"a": "It is an attack used to modify the code in an application",
			"b": "It is a Denial of Service Attack (DoS)",
			"c": "It is a MiTM attack",
			"d": "It is an attack used to gain unauthorized access to a database"
		}
	},
	{
		"question": "Shayla is an IT security consultant, specializing in social engineering and external penetration tests. Shayla\nhas been hired on by Treks Avionics, a subcontractor for the Department of Defense. Shayla has been\ngiven authority to perform any and all tests necessary to audit the company's network security.\nNo employees for the company, other than the IT director, know about Shayla's work she will be doing.\nShayla's first step is to obtain a list of employees through company website contact pages. Then she\nbefriends a female employee of the company through an online chat website. After meeting with the female\nemployee numerous times, Shayla is able to gain her trust and they become friends. One day, Shayla\nsteals the employee's access badge and uses it to gain unauthorized access to the Treks Avionics offices.\nWhat type of insider threat would Shayla be considered?",
		"num": "473",
		"correct_answer": "a",
		"answers": {
			"a": "She would be considered an Insider Affiliate",
			"b": "Because she does not have any legal access herself, Shayla would be considered an Outside Affiliate",
			"c": "Shayla is an Insider Associate since she has befriended an actual employee",
			"d": "Since Shayla obtained access with a legitimate company badge; she would be considered a Pure Insider"
		}
	},
	{
		"question": "You are looking for SQL injection vulnerability by sending a special character to web applications.\nWhich of the following is the most useful for quick validation?",
		"num": "474",
		"correct_answer": "d",
		"answers": {
			"a": "Double quotation",
			"b": "Backslash",
			"c": "Semicolon",
			"d": "Single quotation"
		}
	},
	{
		"question": "Hacker is a person who illegally breaks into a system or network without any authorization to destroy, steal sensitive data or to perform any malicious attacks.\n\nBlack hat hackers are:",
		"num": "475",
		"correct_answer": "a",
		"answers": {
			"a": "Individuals with extraordinary computing skills, resorting to malicious or destructive activities and are also known as crackers",
			"b": "Individuals professing hacker skills and using them for defensive purposes and are also known as security analysts",
			"c": "Individuals who aim to bring down critical infrastructure for a \"cause\" and are not worried about facing 30 years in jail for their actions ",
			"d": "Individuals who work both offensively and defensively at various times"
		}
	},
	{
		"question": "Which of the following processes of PKI (Public Key Infrastructure) ensures that a trust relationship exists and that a certificate is still valid for specific operations?",
		"num": "476",
		"correct_answer": "b",
		"answers": {
			"a": "Certificate issuance",
			"b": "Certificate validation",
			"c": "Certificate cryptography",
			"d": "Certificate revocation"
		}
	},
	{
		"question": "This asymmetry cipher is based on factoring the product of two large prime numbers.\n\nWhat cipher is described above?",
		"num": "477",
		"correct_answer": "c",
		"answers": {
			"a": "RC5",
			"b": "MD5",
			"c": "RSA",
			"d": "SHA"
		}
	},
	{
		"question": "Which of the following is an adaptive SQL Injection testing technique used to discover coding errors by inputting massive amounts of random data and observing the changes in the output?",
		"num": "478",
		"correct_answer": "d",
		"answers": {
			"a": "Function Testing",
			"b": "Dynamic Testing",
			"c": "Static Testing",
			"d": "Fuzzing Testing"
		}
	},
	{
		"question": "June, a security analyst, understands that a polymorphic virus has the ability to mutate and can change its known viral signature and hide from signature-based antivirus programs. Can June use an antivirus program in this case and would it be effective against a polymorphic virus?",
		"num": "479",
		"correct_answer": "c",
		"answers": {
			"a": "Yes. June can use an antivirus program since it compares the parity bit of executable files to the database of known check sum counts and it is effective on a polymorphic virus.",
			"b": "Yes. June can use an antivirus program since it compares the signatures of executable files to the database of known viral signatures and it is very effective against a polymorphic virus.",
			"c": "No. June can't use an antivirus program since it compares the signatures of executable files to the database of known viral signatures and in the case the polymorphic viruses cannot be detected by a signature-based anti-virus program.",
			"d": "No. June can't use an antivirus program since it compares the size of executable files to the database of known viral signatures and it is effective on a polymorphic virus."
		}
	},
	{
		"question": "Consider the attack scenario given below:\nStep 1: User browses a web page\nStep 2: Web server replies with requested page and sets a cookie on the user?s browser \nStep 3: Attacker steals cookie (Sniffing, XSS, phishing attack)\nStep 4: Attacker orders for product using modified cookie\nStep 5: Product is delivered to attacker?s address\nIdentify the web application attack.",
		"num": "480",
		"correct_answer": "c",
		"answers": {
			"a": "Session fixation attack",
			"b": "Unvalidated redirects attack",
			"c": "Cookie poisoning attack",
			"d": "Denial-of-Service (DoS) attack"
		}
	},
	{
		"question": "NetBIOS over TCP/IP allows files and/or printers to be shared over the network.\nYou are trying to intercept the traffic from a victim machine to a corporate network printer.\nYou are attempting to hijack the printer network connection from your laptop by sniffing the wire. Which port does SMB over TCP/IP use?",
		"num": "481",
		"correct_answer": "d",
		"answers": {
			"a": "443",
			"b": "139",
			"c": "179",
			"d": "445"
		}
	},
	{
		"question": "Stack buffer overflows are also known as _____.",
		"num": "482",
		"correct_answer": "a",
		"answers": {
			"a": "Stack smashing",
			"b": "Address space layout randomization",
			"c": "Shell injection",
			"d": "NOP sled"
		}
	},
	{
		"question": "An intrusion detection system (IDS) gathers and analyzes information from within a computer or a network, to identify the possible violations of security policy, including unauthorized access, as well as misuse.\nAttackers use various IDS evasion techniques to bypass intrusion detection mechanisms.\nWhich of the following evasion technique rely on Time-to-Live (TTL) fields of a TCP/IP packet?",
		"num": "483",
		"correct_answer": "c",
		"answers": {
			"a": "Denial-of-Service Attack",
			"b": "Obfuscation",
			"c": "Insertion Attack",
			"d": "Unicode Evasion"
		}
	},
	{
		"question": "Passive reconnaissance involves collecting information through which of the following?",
		"num": "484",
		"correct_answer": "d",
		"answers": {
			"a": "Social engineering",
			"b": "Network traffic sniffing",
			"c": "Man in the middle attacks",
			"d": "Publicly accessible sources"
		}
	},
	{
		"question": "Which of the following scanning technique attackers use to bypass firewall rules, logging mechanism, and hide themselves as usual network traffic?",
		"num": "485",
		"correct_answer": "a",
		"answers": {
			"a": "Stealth scanning technique",
			"b": "TCP connect scanning technique",
			"c": "Xmas scanning technique",
			"d": "Maintaining Access",
			"e": "FIN scanning technique"
		}
	},
	{
		"question": "Which of the following scanning tools is specifically designed to find potential exploits in Microsoft Windows products?",
		"num": "486",
		"correct_answer": "d",
		"answers": {
			"a": "Microsoft Security Baseline Analyzer",
			"b": "Retina",
			"c": "Core Impact",
			"d": "Microsoft Baseline Security Analyzer"
		}
	},
	{
		"question": "In order to compromise or to hack a system or network the hackers go through various phases of the hacking.\nWhat is the first hacking phase that hackers perform to gather information about a target prior to launching an attack?",
		"num": "487",
		"correct_answer": "a",
		"answers": {
			"a": "Reconnaissance",
			"b": "Scanning",
			"c": "Gaining Access",
			"d": "Maintaining Access",
			"e": "Clearing Track"
		}
	},
	{
		"question": "Which of the following tools can be used for passive OS fingerprinting?",
		"num": "488",
		"correct_answer": "a",
		"answers": {
			"a": "tracert",
			"b": "ping",
			"c": "nmap",
			"d": "tcpdump"
		}
	},
	{
		"question": "Which of the following is a hashing algorithm?",
		"num": "489",
		"correct_answer": "d",
		"answers": {
			"a": "PGP",
			"b": "DES",
			"c": "ROT13",
			"d": "MD5"
		}
	},
	{
		"question": "What is the most secure way to mitigate the theft of corporate information from a laptop that was left in a hotel room?",
		"num": "490",
		"correct_answer": "b",
		"answers": {
			"a": "Set a BIOS password.",
			"b": "Encrypt the data on the hard drive.",
			"c": "Use a strong logon password to the operating system.",
			"d": "Back up everything on the laptop and store the backup in a safe place."
		}
	},
	{
		"question": "Which of the following Wi-Fi chalking method refers to drawing symbols in public places to advertise open Wi-Fi networks?",
		"num": "491",
		"correct_answer": "c",
		"answers": {
			"a": "WarWalking",
			"b": "WarFlying",
			"c": "WarChalking",
			"d": "WarDriving"
		}
	},
	{
		"question": "How do you defend against Privilege Escalation? (4 answers)",
		"num": "492",
		"correct_answer": "abce",
		"answers": {
			"a": "Use encryption to protect sensitive data",
			"b": "Restrict the interactive logon privileges",
			"c": "Run services as unprivileged accounts",
			"d": "Allow security settings of IE to zero or Low",
			"e": "Run users and applications on the least privileges"
		}
	},
	{
		"question": "A tester has been using the msadc.pl attack script to execute arbitrary commands on a Windows NT4 web server.\nWhile it is effective, the tester finds it tedious to perform extended functions.\nOn further research, the tester come across a perl script that runs the following msadc functions:system (\"perl msadc.pl -h $host -C \\\"echo open $your >testfile\\\"\"); Which exploit is indicated by this script?",
		"num": "493",
		"correct_answer": "b",
		"answers": {
			"a": "A buffer overflow exploit",
			"b": "A chained exploit",
			"c": "A SQL injection exploit",
			"d": "A denial of service exploit"
		}
	},
	{
		"question": "John is using a special tool on his Linux platform that has a database containing signatures to be able to detect hundreds of vulnerabilities in UNIX, Windows, and commonly used web CGI/ASPX scripts.\nMoreover, the database detects DDoS zombies and Trojans as well. What would be the name of this tool?",
		"num": "494",
		"correct_answer": "b",
		"answers": {
			"a": "hping2",
			"b": "nessus",
			"c": "nmap",
			"d": "make"
		}
	},
	{
		"question": "Which of the following network attacks takes advantage of weaknesses in the fragment reassembly functionality of the TCP/IP protocol stack?",
		"num": "495",
		"correct_answer": "a",
		"answers": {
			"a": "Teardrop",
			"b": "SYN flood",
			"c": "Smurf attack",
			"d": "Ping of death"
		}
	},
	{
		"question": "Which of the following items of a computer system will an anti-virus program scan for viruses?",
		"num": "496",
		"correct_answer": "a",
		"answers": {
			"a": "Boot Sector",
			"b": "Deleted Files",
			"c": "Windows Process List",
			"d": "Password Protected Files"
		}
	},
	{
		"question": "Which of the following statements is FALSE with respect to Intrusion Detection Systems?",
		"num": "497",
		"correct_answer": "a",
		"answers": {
			"a": "Intrusion Detection Systems can easily distinguish a malicious payload in an encrypted traffic",
			"b": "Intrusion Detection Systems can examine the contents of the data in context of the network protocol",
			"c": "Intrusion Detection Systems can be configured to distinguish specific content in network packets",
			"d": "Intrusion Detection Systems require constant update of the signature library"
		}
	},
	{
		"question": "One of the most common and the best way of cracking RSA encryption is to begin to derive the two prime numbers, which are used in the RSA PKI mathematical process.\nIf the two numbers p and q are discovered through a _____________ process, then the private key can be derived.",
		"num": "498",
		"correct_answer": "a",
		"answers": {
			"a": "Factorization",
			"b": "Prime Detection",
			"c": "Hashing",
			"d": "Brute-forcing"
		}
	},
	{
		"question": "Steganography can be used to pass messages through uploaded photos on Facebook. True or False?",
		"num": "499",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Firewall implementation and design for an enterprise can be a daunting task. Choices made early in the design process can have far-reaching security implications for years to come. Which of the following firewall architecture is designed to host servers that offer public services?",
		"num": "500",
		"correct_answer": "b",
		"answers": {
			"a": "Bastion Host",
			"b": "Screened subnet",
			"c": "Screened host ",
			"d": "Screened  "
		}
	},
	{
		"question": "Which of the following tools will scan a network to perform vulnerability checks and compliance auditing?",
		"num": "501",
		"correct_answer": "c",
		"answers": {
			"a": "NMAP",
			"b": "Metasploit",
			"c": "Nessus",
			"d": "BeEF"
		}
	},
	{
		"question": "As a countermeasure to buffer overflows, bounds checking should be performed.",
		"num": "502",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which is the first step followed by Vulnerability Scanners for scanning a network?",
		"num": "503",
		"correct_answer": "d",
		"answers": {
			"a": "TCP/UDP Port scanning",
			"b": "Firewall detection",
			"c": "OS Detection",
			"d": "Checking if the remote host is alive"
		}
	},
	{
		"question": "Annie has just succeeded in stealing a secure cookie via a XSS attack. She is able to replay the cookie even while the session is invalid on the server.\nWhy do you think this is possible?",
		"num": "504",
		"correct_answer": "a",
		"answers": {
			"a": "It works because encryption is performed at the application layer (single encryption key)",
			"b": "The scenario is invalid as a secure cookie cannot be replayed",
			"c": "It works because encryption is performed at the network layer (layer 1 encryption)",
			"d": "Any cookie can be replayed irrespective of the session status"
		}
	},
	{
		"question": "Jeremy is web security consultant for Information Securitas.\nJeremy has just been hired to perform contract work for a large state agency in Michigan. Jeremy's first task is to scan all the company's external websites.\nJeremy comes upon a login page which appears to allow employees access to sensitive areas on the website.\nJames types in the following statement in the username field:\n\n    SELECT * from Users where username='admin' OR password='' OR email like '%@testers. com%'\n\nWhat will the SQL statement accomplish?",
		"num": "505",
		"correct_answer": "b",
		"answers": {
			"a": "If the page is susceptible to SQL injection, it will look in the Users table for usernames of admin",
			"b": "This statement will look for users with the name of admin, blank passwords, and email addresses that end in @testers.com",
			"c": "This Select SQL statement will log James in if there are any users with NULL passwords",
			"d": "James will be able to see if there are any default user accounts in the SQL database"
		}
	},
	{
		"question": "A certified ethical hacker (CEH) completed a penetration test of the main headquarters of a company almost two months ago, but has yet to get paid.\nThe customer is suffering from financial problems, and the CEH is worried that the company will go out of business and end up not paying.\nWhat actions should the CEH take?",
		"num": "506",
		"correct_answer": "b",
		"answers": {
			"a": "Threaten to publish the penetration test results if not paid.",
			"b": "Follow proper legal procedures against the company to request payment.",
			"c": "Tell other customers of the financial problems with payments from this company.",
			"d": "Exploit some of the vulnerabilities found on the company webserver to deface it."
		}
	},
	{
		"question": "Adding identifiable information into a file or document is known as_____.",
		"num": "507",
		"correct_answer": "c",
		"answers": {
			"a": "Copyright hiding",
			"b": "Counterfeiting",
			"c": "Watermarking",
			"d": "None of these"
		}
	},
	{
		"question": "A security engineer has been asked to deploy a secure remote access solution that will allow employees to connect to the company's internal network.\nWhich of the following can be implemented to minimize the opportunity for the man-in-the-middle attack to occur?",
		"num": "508",
		"correct_answer": "c",
		"answers": {
			"a": "SSL",
			"b": "Mutual authentication",
			"c": "IPSec",
			"d": "Static IP addresses"
		}
	},
	{
		"question": "While using your bank\u2019s online servicing you notice the following string in the URL bar:\nhttp://www.MyPersonalBank.com/account?id=368940911028389&Damount=10980&Camount=21\u201d\nYou observe that if you modify the Damount & Camount values and submit the request, that data on the web page reflect the changes.\nWhich type of vulnerability is present on this site?",
		"num": "509",
		"correct_answer": "d",
		"answers": {
			"a": "Cookie Tampering",
			"b": "XSS Reflection",
			"c": "SQL injection",
			"d": "Web Parameter Tampering"
		}
	},
	{
		"question": "Risks=Threats x Vulnerabilities is referred to as the:",
		"num": "510",
		"correct_answer": "c",
		"answers": {
			"a": "BIA equation",
			"b": "Disaster recovery formula",
			"c": "Risk equation",
			"d": "Threat assessment"
		}
	},
	{
		"question": "Steganography is a technique of hiding a secret message within an ordinary message and extracting it at the destination to maintain confidentiality of data. \n\nWhich of the following steganography technique embed secret message in the frequency domain of a signal?",
		"num": "511",
		"correct_answer": "b",
		"answers": {
			"a": "Substitution techniques",
			"b": "Transform domain techniques",
			"c": "Spread spectrum techniques",
			"d": "Domain distortion techniques",
			"e": "Cover generation techniques"
		}
	},
	{
		"question": "Smart cards use which protocol to transfer the certificate in a secure manner?",
		"num": "512",
		"correct_answer": "a",
		"answers": {
			"a": "Extensible Authentication Protocol (EAP)",
			"b": "Point to Point Protocol (PPP)",
			"c": "Point to Point Tunneling Protocol (PPTP)",
			"d": "Layer 2 Tunneling Protocol (L2TP)"
		}
	},
	{
		"question": "BankerFox is a Trojan that is designed to steal users' banking data related to certain banking entities.\nWhen they access any website of the affected banks through the vulnerable Firefox 3.5 browser, the Trojan is activated and logs the information entered by the user.\nAll the information entered in that website will be logged by the Trojan and transmitted to the attacker's machine using covert channel.\nBankerFox does not spread automatically using its own means. It needs an attacking user's intervention in order to reach the affected computer.\nWhat is the most efficient way an attacker located in remote location to infect this banking Trojan on a victim's machine?",
		"num": "513",
		"correct_answer": "e",
		"answers": {
			"a": "Physical access - the attacker can simply copy a Trojan horse to a victim's hard disk infecting the machine via Firefox add-on extensions",
			"b": "Custom packaging - the attacker can create a custom Trojan horse that mimics the appearance of a program that is unique to that particular computer",
			"c": "Custom packaging - the attacker can create a custom Trojan horse that mimics the appearance of a program that is unique to that particular computer",
			"d": "Custom packaging - the attacker can create a custom Trojan horse that mimics the appearance of a program that is unique to that particular computer",
			"e": "Downloading software from a website? An attacker can offer free software, such as shareware programs and pirated mp3 files"
		}
	},
	{
		"question": "Wireless antenna is an electrical device which converts electric currents into radio waves, and vice versa.\n\nWhich of the following antenna used in wireless base stations and provides a 360 degree horizontal radiation pattern?",
		"num": "514",
		"correct_answer": "a",
		"answers": {
			"a": "Omnidirectional antenna",
			"b": "Parabolic grid antenna",
			"c": "Yagi antenna",
			"d": "Dipole antenna"
		}
	},
	{
		"question": "You went to great lengths to install all the necessary technologies to prevent hacking attacks, such as\nexpensive firewalls, antivirus software, anti-spam systems and intrusion detection/prevention tools in your\ncompany's network. You have configured the most secure policies and tightened every device on your\nnetwork. You are confident that hackers will never be able to gain access to your network with complex\nsecurity system in place. Your peer, Peter Smith who works at the same department disagrees with you. He\nsays even the best network security technologies cannot prevent hackers gaining access to the network\nbecause of presence of \"weakest link\" in the security chain. What is Peter Smith talking about?",
		"num": "515",
		"correct_answer": "a",
		"answers": {
			"a": "Untrained staff or ignorant computer users who inadvertently become the weakest link in your security chain",
			"b": "\"zero-day\" exploits are the weakest link in the security chain since the IDS will not be able to detect these attacks",
			"c": "\"Polymorphic viruses\" are the weakest link in the security chain since the Anti-Virus scanners will not be able to detect these attacks",
			"d": "Continuous Spam e-mails cannot be blocked by your security system since spammers use different techniques to bypass the filters in your gateway"
		}
	},
	{
		"question": "In the context of password security: a simple dictionary attack involves loading a dictionary file (a text file full of dictionary words) into a cracking application such as L0phtCrack or John the Ripper, and running it against user accounts located by the application. The larger the word and \n ord fragment selection, the more effective the dictionary attack is. The brute force method is the most inclusive - though slow. Usually, it tries every possible letter and number combination in its automated exploration. If you would use both brute force and dictionary combined together to \n ave variations of words, what would you call such an attack?",
		"num": "516",
		"correct_answer": "c",
		"answers": {
			"a": "Full Blown Attack",
			"b": "Thorough Attack",
			"c": "Hybrid Attack",
			"d": "BruteDict Attack"
		}
	},
	{
		"question": "Bob, a network administrator at BigUniversity, realized that some students are connecting their notebooks in the wired network to have Internet access.\nIn the university campus, there are many Ethernet ports available for professors and authorized visitors but not for students.\nHe identified this when the IDS alerted for malware activities in the network.\nWhat should Bob do to avoid this problem?",
		"num": "517",
		"correct_answer": "c",
		"answers": {
			"a": "Disable unused ports in the switches",
			"b": "Separate students in a different VLAN",
			"c": "Use the 802.1x protocol",
			"d": "Ask students to use the wireless network"
		}
	},
	{
		"question": "Which method of password cracking takes the most time and effort?",
		"num": "518",
		"correct_answer": "a",
		"answers": {
			"a": "Rainbow tables",
			"b": "Shoulder surfing",
			"c": "Brute force",
			"d": "Dictionary attack"
		}
	},
	{
		"question": "Bob finished a C programming course and created a small C application to monitor the network traffic and produce alerts when any origin sends \u201cmany\u201d IP packets, based on the average number of packets sent by all origins and using some thresholds.\nIn concept, the solution developed by Bob is actually:",
		"num": "519",
		"correct_answer": "a",
		"answers": {
			"a": "Just a network monitoring tool",
			"b": "A signature-based IDS",
			"c": "A hybrid IDS",
			"d": "A behavior-based IDS"
		}
	},
	{
		"question": "A technician is resolving an issue where a computer is unable to connect to the Internet using a wireless access point.\nThe computer is able to transfer files locally to other machines, but cannot successfully reach the Internet.\nWhen the technician examines the IP address and default gateway they are both on the 192.168.1.0/24.\nWhich of the following has occurred?",
		"num": "520",
		"correct_answer": "b",
		"answers": {
			"a": "The computer is not using a private IP address.",
			"b": "The gateway is not routing to a public IP address.",
			"c": "The gateway and the computer are not on the same network.",
			"d": "The computer is using an invalid IP address."
		}
	},
	{
		"question": "Jayden is a network administrator for her company. Jayden wants to prevent MAC spoofing on all the Cisco switches in the network.\nHow can she accomplish this?",
		"num": "521",
		"correct_answer": "d",
		"answers": {
			"a": "Jayden can use the commanD. ip binding set.",
			"b": "Jayden can use the commanD. no ip spoofing.",
			"c": "She should use the commanD. no dhcp spoofing.",
			"d": "She can use the commanD. ip dhcp snooping binding."
		}
	},
	{
		"question": "Which of the following can the administrator do to verify that a tape backup can be recovered in its entirety?",
		"num": "522",
		"correct_answer": "b",
		"answers": {
			"a": "Read the first 512 bytes of the tape",
			"b": "Perform a full restore",
			"c": "Read the last 512 bytes of the tape",
			"d": "Restore a random file"
		}
	},
	{
		"question": "Bob has been hired to do a web application security test. Bob notices that the site is dynamic and must make use of a back end database. Bob wants to see if SQL Injection would be possible. What is the first character that Bob should use to attempt breaking valid SQL request?",
		"num": "523",
		"correct_answer": "c",
		"answers": {
			"a": "Semi Column",
			"b": "Double Quote",
			"c": "Single Quote",
			"d": "Exclamation Mark"
		}
	},
	{
		"question": "Which of the following can take an arbitrary length of input and produce a message digest output of 160 bit?",
		"num": "524",
		"correct_answer": "a",
		"answers": {
			"a": "SHA-1",
			"b": "MD5",
			"c": "HAVAL",
			"d": "MD4"
		}
	},
	{
		"question": "It is an entity or event with the potential to adversely impact a system through unauthorized access, destruction, disclosure, denial of service or modification of data.\nWhich of the following terms best matches the definition?",
		"num": "525",
		"correct_answer": "a",
		"answers": {
			"a": "Threat",
			"b": "Attack",
			"c": "Vulnerability",
			"d": "Risk"
		}
	},
	{
		"question": "Which type of sniffing technique is generally referred as MiTM attack?",
		"num": "526",
		"correct_answer": "b",
		"answers": {
			"a": "Password Sniffing",
			"b": "ARP Poisoning",
			"c": "Mac Flooding",
			"d": "DHCP Sniffing"
		}
	},
	{
		"question": "You work as a Security Analyst for a retail organization. In securing the company's network, you set up a firewall and an IDS. However, hackers are able to attack the network.\nAfter investigating, you discover that your IDS is not configured properly and therefore is unable to trigger alarms when needed.\nWhat type of alert is the IDS giving?",
		"num": "527",
		"correct_answer": "c",
		"answers": {
			"a": "True Positive",
			"b": "True Negative",
			"c": "False Negative",
			"d": "False Positive"
		}
	},
	{
		"question": "You want to hide a secret.txt document inside c:\\windows\\system32\\tcpip.dll kernel library using ADS streams. How will you accomplish this?",
		"num": "528",
		"correct_answer": "b",
		"answers": {
			"a": "copy secret.txt c:\\windows\\system32\\tcpip.dll kernel>secret.txt",
			"b": "copy secret.txt c:\\windows\\system32\\tcpip.dll:secret.txt",
			"c": "copy secret.txt c:\\windows\\system32\\tcpip.dll |secret.txt",
			"d": "copy secret.txt >< c:\\windows\\system32\\tcpip.dll kernel secret.txt"
		}
	},
	{
		"question": "Enumeration is defined as the process of extracting user names, machine names, network resources, shares, and services from a system.\nWhich of the following command can be used in UNIX environment to enumerate the shared directories on a machine?",
		"num": "529",
		"correct_answer": "a",
		"answers": {
			"a": "showmount",
			"b": "finger",
			"c": "rpcinfo",
			"d": "rpcclient"
		}
	},
	{
		"question": "Buffer Overflow occurs when an application writes more data to a block of memory, or buffer, than the buffer is allocated to hold.\nBuffer overflow attacks allow an attacker to modify the ___________ in order to control the process execution, crash the process and modify internal variables.\n",
		"num": "530",
		"correct_answer": "a",
		"answers": {
			"a": "Target process's address space",
			"b": "Target remote access",
			"c": "Target rainbow table",
			"d": "Target SAM file"
		}
	},
	{
		"question": "Which of the following defines the role of a root Certificate Authority (CA) in a Public Key Infrastructure (PKI)?",
		"num": "531",
		"correct_answer": "c",
		"answers": {
			"a": "The root CA is the recovery agent used to encrypt data when a user's certificate is lost.",
			"b": "The root CA stores the user's hash value for safekeeping.",
			"c": "The CA is the trusted root that issues certificates.",
			"d": "The root CA is used to encrypt email messages to prevent unintended disclosure of data."
		}
	},
	{
		"question": "You establish a new Web browser connection to Google. Since a 3-way handshake is required for any TCP connection, the following actions will take place.\n\n- DNS query is sent to the DNS server to resolve www.google.com\n- DNS server replies with the IP address for Google?\n- SYN packet is sent to Google.\n- Google sends back a SYN/ACK packet\n- Your computer completes the handshake by sending an ACK\n- The connection is established and the transfer of data commences\n\nWhich of the following packets represent completion of the 3-way handshake?",
		"num": "532",
		"correct_answer": "d",
		"answers": {
			"a": "4th packet",
			"b": "3rdpacket",
			"c": "6th packet",
			"d": "5th packet"
		}
	},
	{
		"question": "What statement is true regarding LM hashes?",
		"num": "533",
		"correct_answer": "d",
		"answers": {
			"a": "LM hashes consist in 48 hexadecimal characters.",
			"b": "LM hashes are based on AES128 cryptographic standard.",
			"c": "Uppercase characters in the password are converted to lowercase.",
			"d": "LM hashes are not generated when the password length exceeds 15 characters."
		}
	},
	{
		"question": "When setting up a wireless network, an administrator enters a pre-shared key for security.\nWhich of the following is true?",
		"num": "534",
		"correct_answer": "a",
		"answers": {
			"a": "The key entered is a symmetric key used to encrypt the wireless data.",
			"b": "The key entered is a hash that is used to prove the integrity of the wireless data.",
			"c": "The key entered is based on the Diffie-Hellman method.",
			"d": "The key is an RSA key used to encrypt the wireless data."
		}
	},
	{
		"question": "Jess the hacker runs L0phtCrack's built-in sniffer utility that grabs SMB password hashes and stores them for offline cracking. Once cracked, these passwords can provide easy access to whatever network resources the user account has access to. But Jess is not picking up hashes from the network.\nWhy?",
		"num": "535",
		"correct_answer": "a",
		"answers": {
			"a": "The network protocol is configured to use SMB Signing",
			"b": "The physical network wire is on fibre optic cable",
			"c": "The network protocol is configured to use IPSEC",
			"d": "L0phtCrack SMB sniffing only works through Switches and not Hubs"
		}
	},
	{
		"question": "Your company was hired by a small healthcare provider to perform a technical assessment on the network.\nWhat is the best approach for discovering vulnerabilities on a Windows- based computer?",
		"num": "536",
		"correct_answer": "d",
		"answers": {
			"a": "Use the built-in Windows Update tool",
			"b": "Create a disk image of a clean Windows installation",
			"c": "Check MITRE.org for the latest list of CVE findings",
			"d": "Use a scan tool like Nessus"
		}
	},
	{
		"question": "You have successfully gained access to a linux server and would like to ensure that the succeeding outgoing traffic from this server will not be caught by a Network Based Intrusion Detection Systems (NIDS).\nWhat is the best way to evade the NIDS?",
		"num": "537",
		"correct_answer": "d",
		"answers": {
			"a": "Out of band signaling",
			"b": "Alternate Data Streams",
			"c": "Protocol Isolation",
			"d": "Encryption"
		}
	},
	{
		"question": "Chandler works as a pen-tester in an IT-firm in New York.\nAs a part of detecting viruses in the systems, he uses a detection method where the anti-virus executes the malicious codes on a virtual machine to simulate CPU and memory activities.\nWhich type of virus detection method did Chandler use in this context?",
		"num": "538",
		"correct_answer": "b",
		"answers": {
			"a": "Heuristic Analysis",
			"b": "Code Emulation",
			"c": "Integrity checking",
			"d": "Scanning"
		}
	},
	{
		"question": "Which NMAP feature can a tester implement or adjust while scanning for open ports to avoid detection by the network's IDS?",
		"num": "539",
		"correct_answer": "a",
		"answers": {
			"a": "Timing options to slow the speed that the port scan is conducted",
			"b": "Fingerprinting to identify which operating systems are running on the network",
			"c": "ICMP ping sweep to determine which hosts on the network are not available",
			"d": "Traceroute to control the path of the packets sent during the scan"
		}
	},
	{
		"question": "You are trying to package a RAT Trojan so that Anti-Virus software will not detect it.\nWhich of the listed technique will NOT be effective in evading Anti-Virus scanner?",
		"num": "540",
		"correct_answer": "a",
		"answers": {
			"a": "Convert the Trojan.exe file extension to Trojan.txt disguising as text file",
			"b": "Break the Trojan into multiple smaller files and zip the individual pieces",
			"c": "Change the content of the Trojan using hex editor and modify the checksum",
			"d": "Encrypt the Trojan using multiple hashing algorithms like MD5 and SHA-1"
		}
	},
	{
		"question": "Which results will be returned with the following Google search query?\n\n  site:target.com -site:Marketing.target.com accounting",
		"num": "541",
		"correct_answer": "b",
		"answers": {
			"a": "Results matching all words in the query",
			"b": "Results matching \"accounting\" in domain target.com but not on the site Marketing.target.com",
			"c": "Results from matches on the site marketing.target.com that are in the domain target.com but do not include the word accounting",
			"d": "Results for matches on target.com and Marketing.target.com that include the word \"accounting\""
		}
	},
	{
		"question": "Which of the following incident handling process phases is responsible for defining rules, collaborating human workforce, creating a back-up plan, and testing the plans for an organization?",
		"num": "542",
		"correct_answer": "a",
		"answers": {
			"a": "Preparation phase",
			"b": "Containment phase",
			"c": "Identification phase",
			"d": "Recovery phase"
		}
	},
	{
		"question": "As a Certified Ethical Hacker, you were contracted by a private firm to conduct an external security assessment through penetration testing. What document describes the specifics of the testing, the associated violations, and essentially protects both the organization's interest and your liabilities as a tester?",
		"num": "543",
		"correct_answer": "b",
		"answers": {
			"a": "Project Scope",
			"b": "Rules of Engagement",
			"c": "Service Level Agreement",
			"d": "Non- Disclosure Agreement"
		}
	},
	{
		"question": "You are tasked to perform a penetration test.\nWhile you are performing information gathering, you find an employee list in Google.\nYou find the receptionist\u2019s email, and you send her an email changing the source email to her boss\u2019s email (boss@company).\nIn this email, you ask for a pdf with information.\nShe reads your email and sends back a pdf with links.\nYou exchange the pdf links with your malicious links (these links contain malware) and send back the modified pdf, saying that the links don\u2019t work.\nShe reads your email, opens the links, and her machine gets infected.\nYou now have access to the company network.\nWhat testing method did you use?",
		"num": "544",
		"correct_answer": "a",
		"answers": {
			"a": "Social engineering",
			"b": "Piggybacking",
			"c": "Tailgating",
			"d": "Eavesdropping"
		}
	},
	{
		"question": "Which property or concept ensures that a hash function will not produce the same hashed value for two different messages?",
		"num": "545",
		"correct_answer": "d",
		"answers": {
			"a": "Key strength",
			"b": "Entropy",
			"c": "Bit length",
			"d": "Collision resistance"
		}
	},
	{
		"question": "Lauren is performing a network audit for her entire company.\nThe entire network is comprised of around 500 computers.\nLauren starts an ICMP ping sweep by sending one IP packet to the broadcast address of the network, but only receives responses from around five hosts.\nWhy did this ping sweep only produce a few responses?",
		"num": "546",
		"correct_answer": "c",
		"answers": {
			"a": "Only Windows systems will reply to this scan.",
			"b": "A switched network will not respond to packets sent to the broadcast address.",
			"c": "Only Linux and Unix-like (Non-Windows) systems will reply to this scan.",
			"d": "Only servers will reply to this scan."
		}
	},
	{
		"question": "Which property or concept ensures that a hash function will not produce the same hashed value for two different messages?",
		"num": "547",
		"correct_answer": "d",
		"answers": {
			"a": "Key strength",
			"b": "Bit length",
			"c": "Entropy",
			"d": "Collision resistance"
		}
	},
	{
		"question": "Of these answers, which best describes the art of steganography?",
		"num": "548",
		"correct_answer": "d",
		"answers": {
			"a": "The act of scrambling data using complex algorithms and special keys in order to secure and conceal data.",
			"b": "A malicious act where an insider-threat uses encryption and compression to smuggle data from a secured network",
			"c": "The process by which programmers break down and analyze code that is encrypted.",
			"d": "The process of injecting or concealing secret data or code into a common, easily-readable file so that the secret cannot be easily detected by ordinary means."
		}
	},
	{
		"question": "A large mobile telephony and data network operator has a data center that houses network elements.\nThese are essentially large computers running on Linux.\nThe perimeter of the data center is secured with firewalls and IPS systems.\nWhat is the best security policy concerning this setup?",
		"num": "549",
		"correct_answer": "a",
		"answers": {
			"a": "Network elements must be hardened with user ids and strong passwords. Regular security tests and audits should be performed.",
			"b": "As long as the physical access to the network elements is restricted, there is no need for additional measures.",
			"c": "There is no need for specific security measures on the network elements as long as firewalls and IPS systems exist.",
			"d": "The operator knows that attacks and down time are inevitable and should have a backup site."
		}
	},
	{
		"question": "Which of the following can the administrator do to verify that a tape backup can be recovered in its entirety?",
		"num": "550",
		"correct_answer": "b",
		"answers": {
			"a": "Restore a random file.",
			"b": "Perform a full restore.",
			"c": "Read the first 512 bytes of the tape.",
			"d": "Read the last 512 bytes of the tape."
		}
	},
	{
		"question": "Which of the following programming languages is most vulnerable to buffer overflow attacks?",
		"num": "551",
		"correct_answer": "b",
		"answers": {
			"a": "Perl",
			"b": "C++",
			"c": "Python",
			"d": "Java"
		}
	},
	{
		"question": "Wayne is the senior security analyst for his company.\nWayne is examining some traffic logs on a server and came across some inconsistencies.\n\nWayne finds some IP packets from a computer purporting to be on the internal network.\nThe packets originate from 192.168.12.35 with a TTL of 15.\nThe server replied to this computer and received a response from 192.168.12.35 with a TTL of 21.\n\nWhat can Wayne infer from this traffic log?",
		"num": "552",
		"correct_answer": "a",
		"answers": {
			"a": "The initial traffic from 192.168.12.35 was being spoofed.",
			"b": "The traffic from 192.168.12.25 is from a Linux computer.",
			"c": "The TTL of 21 means that the client computer is on wireless.",
			"d": "The client computer at 192.168.12.35 is a zombie computer."
		}
	},
	{
		"question": "Which of the following is an example of an asymmetric encryption implementation?",
		"num": "553",
		"correct_answer": "b",
		"answers": {
			"a": "SHA1",
			"b": "PGP",
			"c": "3DES",
			"d": "MD5"
		}
	},
	{
		"question": "Which of the following is a characteristic of Public Key Infrastructure (PKI)?",
		"num": "554",
		"correct_answer": "b",
		"answers": {
			"a": "Public-key cryptosystems are faster than symmetric-key cryptosystems.",
			"b": "Public-key cryptosystems distribute public-keys within digital signatures.",
			"c": "Public-key cryptosystems do not require a secure key distribution channel.",
			"d": "Public-key cryptosystems do not provide technical non-repudiation via digital signatures."
		}
	},
	{
		"question": "When you are collecting information to perform a data analysis, Google commands are very useful to find sensitive information and files.\nThese files may contain information about passwords, system functions, or documentation.\nWhat command will help you to search files using Google as a search engine?",
		"num": "555",
		"correct_answer": "a",
		"answers": {
			"a": "site: target.com filetype:xls username password email",
			"b": "domain: target.com archieve:xls username password email",
			"c": "inurl: target.com filename:xls username password email",
			"d": "site: target.com file:xls username password email"
		}
	},
	{
		"question": "Which of the following is an example of IP spoofing?",
		"num": "556",
		"correct_answer": "b",
		"answers": {
			"a": "SQL injections",
			"b": "Man-in-the-middle",
			"c": "Cross-site scripting",
			"d": "ARP poisoning"
		}
	},
	{
		"question": "What is the best way a designer can mitigate buffer overflow from occurring in their code? Choose all that apply.",
		"num": "557",
		"correct_answer": "ad",
		"answers": {
			"a": "Write code using boundary checks within the code.",
			"b": "Write code without boundary scans.",
			"c": "Write code that uses C++ and everything will be great, no worries.",
			"d": "Use a protocol robustness test to verify the code meets qualifications for proper boundary and common key stroke entries."
		}
	},
	{
		"question": "Windows Phone 8 devices boot with Secure UEFI. True or false?",
		"num": "558",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "An attacker finds a web page for a target organization that supplies contact information for the company.\nUsing available details to make the message seem authentic, the attacker drafts e-mail to an employee on\nthe contact page that appears to come from an individual who might reasonably request confidential\ninformation, such as a network administrator.\nThe email asks the employee to log into a bogus page that requests the employee's user name and\npassword or click on a link that will download spyware or other malicious programming.\nGoogle's Gmail was hacked using this technique and attackers stole source code and sensitive data from\nGoogle servers. This is highly sophisticated attack using zero-day exploit vectors, social engineering and\nmalware websites that focused on targeted individuals working for the company.\nWhat is this deadly attack called?",
		"num": "559",
		"correct_answer": "a",
		"answers": {
			"a": "Spear phishing attack",
			"b": "Trojan server attack",
			"c": "Javelin attack",
			"d": "Social networking attack"
		}
	},
	{
		"question": "An intrusion detection system (IDS) gathers and analyzes information from within a computer or a network, to identify the possible violations of security policy, including unauthorized access, as well as misuse.\nWhich of the following IDS detection technique detects the intrusion based on the fixed behavioral characteristics of the users and components in a computer system? ",
		"num": "560",
		"correct_answer": "b",
		"answers": {
			"a": "Signature recognition",
			"b": "Anomaly detection",
			"c": "Protocol anomaly detection",
			"d": "All of the above"
		}
	},
	{
		"question": "Which wireless hacking tool attacks WEP and WPA-PSK?",
		"num": "561",
		"correct_answer": "c",
		"answers": {
			"a": "Airguard",
			"b": "wificracker",
			"c": "Aircrack-ng",
			"d": "WLAN-crack"
		}
	},
	{
		"question": "Jack Hacker wants to break into Brown Co.'s computers and obtain their secret double fudge cookie recipe.\nJack calls Jane, an accountant at Brown Co., pretending to be an administrator from Brown Co. Jack tells\nJane that there has been a problem with some accounts and asks her to verify her password with him ''just\nto double check our records.'' Jane does not suspect anything amiss, and parts with her password. Jack\ncan now access Brown Co.'s computers with a valid user name and password, to steal the cookie recipe.\nWhat kind of attack is being illustrated here?",
		"num": "562",
		"correct_answer": "c",
		"answers": {
			"a": "Reverse Psychology",
			"b": "Reverse Engineering",
			"c": "Social Engineering",
			"d": "Spoofing Identity",
			"e": "Faking Identity"
		}
	},
	{
		"question": "Steganography is used by:",
		"num": "563",
		"correct_answer": "b",
		"answers": {
			"a": "Artists/Owners",
			"b": "All of these",
			"c": "Hackers",
			"d": "Terrorists"
		}
	},
	{
		"question": "This tool is widely used for ARP Poisoning attack. Name the tool.",
		"num": "564",
		"correct_answer": "a",
		"answers": {
			"a": "Cain and Able",
			"b": "Beat Infector",
			"c": "Poison Ivy",
			"d": "Webarp Infector"
		}
	},
	{
		"question": "During a routine assessment you discover information that suggests the customer is involved in human trafficking.",
		"num": "565",
		"correct_answer": "b",
		"answers": {
			"a": "Copy the data to a thumb drive and keep it as leverage.",
			"b": "Immediately stop work and contact the proper legal authorities",
			"c": "Ignore the data complete the job collect a check. Keep it moving!",
			"d": "Confront the client in a respectful manner and ask about the data"
		}
	},
	{
		"question": "Which of the following is an example of the principle of least privilege as a system security control?",
		"num": "566",
		"correct_answer": "b",
		"answers": {
			"a": "User should have limited access to the information regardless of its purpose",
			"b": "User must be able to access only the information and resources that are necessary for legitimate purpose",
			"c": "User should access all the information stored in the business to best execute their functions",
			"d": "Companies should have only a few employees"
		}
	},
	{
		"question": "During a security audit of IT processes, an IS auditor found that there were no documented security procedures. What should the IS auditor do?",
		"num": "567",
		"correct_answer": "b",
		"answers": {
			"a": "Terminate the audit",
			"b": "Identify and evaluate existing practices",
			"c": "Create a procedures document",
			"d": "Conduct compliance testing"
		}
	},
	{
		"question": "Which of the following open source tools would be the best choice to scan a network for potential targets?",
		"num": "568",
		"correct_answer": "a",
		"answers": {
			"a": "NMAP",
			"b": "NIKTO",
			"c": "CAIN",
			"d": "John the Ripper"
		}
	},
	{
		"question": "You are doing a pen test against an organization that has just recovered from a major cyber-attack. The CISO and CIO want to completely and totally eliminate risk.\nWhat is one of the first things you should explain to these individuals?",
		"num": "569",
		"correct_answer": "d",
		"answers": {
			"a": "Start the Wireshark application to sniff traffic",
			"b": "Tell him everything is going to A ok and collect that check!",
			"c": "Explain to them that they need to buy more services.",
			"d": "Explain that you cannot eliminate all risk but you will be able to reduce risk to acceptable levels."
		}
	},
	{
		"question": "Which system consists of a publicly available set of databases that contain domain name registration contact information?",
		"num": "570",
		"correct_answer": "d",
		"answers": {
			"a": "IANA",
			"b": "CAPTCHA",
			"c": "IETF",
			"d": "WHOIS"
		}
	},
	{
		"question": "Which Open Web Application Security Project (OWASP) implements a web application full of known vulnerabilities?",
		"num": "571",
		"correct_answer": "b",
		"answers": {
			"a": "WebBugs",
			"b": "WebGoat",
			"c": "VULN_HTML",
			"d": "WebScarab"
		}
	},
	{
		"question": "Which Intrusion Detection System is the best applicable for large environments where critical assets on the network need extra security and is ideal for observing sensitive network segments?",
		"num": "572",
		"correct_answer": "c",
		"answers": {
			"a": "Honeypots",
			"b": "Firewalls",
			"c": "Network-based intrusion detection system (NIDS)",
			"d": "Host-based intrusion detection system (HIDS)"
		}
	},
	{
		"question": "On a Linux device, which of the following commands will start the Nessus client in the background so that the Nessus server can be configured?",
		"num": "573",
		"correct_answer": "c",
		"answers": {
			"a": "nessus +",
			"b": "nessus *s",
			"c": "nessus &",
			"d": "nessus -d"
		}
	},
	{
		"question": "Which of the following normally uses a layered approach for hiding the data in ICMP traffic?",
		"num": "574",
		"correct_answer": "d",
		"answers": {
			"a": "Unique",
			"b": "Encryption",
			"c": "Hiding directories",
			"d": "Covert channels"
		}
	},
	{
		"question": "Enumeration is defined as the process of extracting user names, machine names, network resources, shares, and services from a system.\n\nWhich of the following enumeration an attacker uses to obtain list of computers that belongs to a domain?",
		"num": "575",
		"correct_answer": "a",
		"answers": {
			"a": "Netbios enumeration",
			"b": "SNMP enumeration",
			"c": "NTP enumeration",
			"d": "SMTP enumeration"
		}
	},
	{
		"question": "Which of the following describes the characteristics of a Boot Sector Virus?",
		"num": "576",
		"correct_answer": "c",
		"answers": {
			"a": "Modifies directory table entries so that directory entries point to the virus code instead of the actual program.",
			"b": "Moves the MBR to another location on the RAM and copies itself to the original location of the MBR.",
			"c": "Moves the MBR to another location on the hard disk and copies itself to the original location of the MBR.",
			"d": "Overwrites the original MBR and only executes the new virus code."
		}
	},
	{
		"question": "Initiating an attack against targeted businesses and organizations, threat actors compromise a carefully selected website by inserting an exploit resulting in malware infection.\nThe attackers run exploits on well-known and trusted sites likely to be visited by their targeted victims. Aside from carefully choosing sites to compromise, these attacks are known to incorporate zero-day exploits that target unpatched vulnerabilities.\nThus, the targeted entities are left with little or no defense against these exploits. What type of attack is outlined in the scenario?",
		"num": "577",
		"correct_answer": "a",
		"answers": {
			"a": "Watering Hole Attack",
			"b": "Shellshock Attack",
			"c": "Spear Phishing Attack",
			"d": "Heartbleed Attack"
		}
	},
	{
		"question": "Fred is scanning his network to ensure it is as secure as possible. Fred sends a TCP probe packet to a host with a FIN flag and he receives a RST/ACK response. What does this mean?",
		"num": "578",
		"correct_answer": "d",
		"answers": {
			"a": "This response means the port he is scanning is open.",
			"b": "The RST/ACK response means the port Fred is scanning is disabled.",
			"c": "This means the port he is scanning is half open.",
			"d": "This means that the port he is scanning on the host is closed."
		}
	},
	{
		"question": "Which of the statements concerning proxy firewalls is correct?",
		"num": "579",
		"correct_answer": "d",
		"answers": {
			"a": "Proxy firewalls increase the speed and functionality of a network.",
			"b": "Firewall proxy servers decentralize all activity for an application.",
			"c": "Proxy firewalls block network packets from passing to and from a protected network.",
			"d": "Computers establish a connection with a proxy firewall which initiates a new network connection for the client."
		}
	},
	{
		"question": "What is a collision attack in cryptography?",
		"num": "580",
		"correct_answer": "c",
		"answers": {
			"a": "Collision attacks try to break the hash into two parts with the same bytes in each part to get the private key",
			"b": "Collision attacks try to get the public key",
			"c": "Collision attacks try to find two inputs that produce the same hash",
			"d": "Collision attacks try to break the hash into three parts."
		}
	},
	{
		"question": "The \"white box testing\" methodology enforces what kind of restriction?",
		"num": "581",
		"correct_answer": "b",
		"answers": {
			"a": "Only the internal operation of a system is known to the tester.",
			"b": "The internal operation of a system is completely known to the tester.",
			"c": "The internal operation of a system is only partly accessible to the tester.",
			"d": "Only the external operation of a system is accessible to the tester."
		}
	},
	{
		"question": "Which method of password cracking takes the most time and effort?",
		"num": "582",
		"correct_answer": "b",
		"answers": {
			"a": "Shoulder surfing",
			"b": "Brute force",
			"c": "Dictionary attack",
			"d": "Rainbow tables"
		}
	},
	{
		"question": "Ursula is a college student at a University in Amsterdam. Ursula originally went to college to study\nengineering but later changed to marine biology after spending a month at sea with her friends. These\nfriends frequently go out to sea to follow and harass fishing fleets that illegally fish in foreign waters. Ursula\neventually wants to put companies practicing illegal fishing out of business. Ursula decides to hack into the\nparent company's computers and destroy critical data knowing fully well that, if caught, she probably would\nbe sent to jail for a very long time. What would Ursula be considered?",
		"num": "583",
		"correct_answer": "b",
		"answers": {
			"a": "Ursula would be considered a gray hat since she is performing an act against illegal activities.",
			"b": "She would be considered a suicide hacker.",
			"c": "She would be called a cracker.",
			"d": "Ursula would be considered a black hat."
		}
	},
	{
		"question": "Neil is closely monitoring his firewall rules and logs on a regular basis. Some of the users have complained to Neil that there are a few employees who are visiting offensive web site during work hours, without any consideration for others.\nNeil knows that he has an up-to-date content filtering system and such access should not be authorized.\nWhat type of technique might be used by these offenders to access the Internet without restriction?",
		"num": "584",
		"correct_answer": "b",
		"answers": {
			"a": "They are using UDP that is always authorized at the firewall",
			"b": "They are using HTTP tunneling software that allows them to communicate with protocols in a way it was not intended",
			"c": "They have been able to compromise the firewall, modify the rules, and give themselves proper access",
			"d": "They are using an older version of Internet Explorer that allow them to bypass the proxy server"
		}
	},
	{
		"question": "An incident investigator asks to receive a copy of the event logs from all firewalls, proxy servers, and Intrusion Detection Systems (IDS) on the network of an organization that has experienced a possible breach of security. When the investigator attempts to correlate the information in all of the logs, the sequence of many of the logged events do not match up. What is the most likely cause?",
		"num": "585",
		"correct_answer": "a",
		"answers": {
			"a": "The attacker altered or erased events from the logs.",
			"b": "Proper chain of custody was not observed while collecting the logs.",
			"c": "The security breach was a false positive.",
			"d": "The network devices are not all synchronized."
		}
	},
	{
		"question": "Which of the following programming languages is commonly associated with buffer overflows?",
		"num": "586",
		"correct_answer": "d",
		"answers": {
			"a": "Flash",
			"b": "HTML",
			"c": "Crash",
			"d": "C and C++",
			"e": "Visual Basic"
		}
	},
	{
		"question": "What port number is used by LDAP protocol?",
		"num": "587",
		"correct_answer": "b",
		"answers": {
			"a": "110",
			"b": "389",
			"c": "464",
			"d": "445"
		}
	},
	{
		"question": "In 2007, this wireless security algorithm was rendered useless by capturing packets and discovering the passkey in a matter of seconds. This security flaw led to a network invasion of TJ Maxx and data theft through a technique known as war driving.\nWhich Algorithm is this referring to?",
		"num": "588",
		"correct_answer": "d",
		"answers": {
			"a": "Wi-Fi Protected Access 2 (WPA2)",
			"b": "Wi-Fi Protected Access (WPA)",
			"c": "Temporal Key Integrity Protocol (TKIP)",
			"d": "Wired Equivalent Privacy (WEP)"
		}
	},
	{
		"question": "Enumeration is defined as the process of extracting user names, machine names, network resources, shares, and services from a system.\nWhich of the following enumeration an attacker uses to obtain list of computers that belongs to a domain?",
		"num": "589",
		"correct_answer": "a",
		"answers": {
			"a": "NTP enumeration",
			"b": "SNMP enumeration",
			"c": "Netbios enumeration",
			"d": "SMTP enumeration"
		}
	},
	{
		"question": "In order to show improvement of security over time, what must be developed?",
		"num": "590",
		"correct_answer": "c",
		"answers": {
			"a": "Reports",
			"b": "Testing tools",
			"c": "Metrics",
			"d": "Taxonomy of vulnerabilities"
		}
	},
	{
		"question": "You have successfully comprised a server having an IP address of 10.10.0.5.\nYou would like to enumerate all machines in the same network quickly.\nWhat is the best nmap command you will use?",
		"num": "591",
		"correct_answer": "b",
		"answers": {
			"a": "nmap -T4 -q 10.10.0.0/24",
			"b": "nmap -T4 -F 10.10.0.0/24",
			"c": "nmap -T4 -r 10.10.1.0/24",
			"d": "nmap -T4 -O 10.10.0.0/24"
		}
	},
	{
		"question": "Which of the following programming languages is not susceptible to a stack-based buffer overflow attack?",
		"num": "592",
		"correct_answer": "d",
		"answers": {
			"a": "C++",
			"b": "C",
			"c": "Assembler",
			"d": "Java"
		}
	},
	{
		"question": "Sniffer turns the NIC of a system to the promiscuous mode so that it listens to all the data transmitted on its segment.\nIt can constantly read all information entering the computer through the NIC by decoding the information encapsulated in the data packet.\nPassive sniffing is one of the types of sniffing.\nPassive sniffing refers to:",
		"num": "593",
		"correct_answer": "c",
		"answers": {
			"a": "Sniffing through a switch",
			"b": "Sniffing through a router",
			"c": "Sniffing through a hub",
			"d": "Sniffing through a bridge"
		}
	},
	{
		"question": "How does an operating system protect the passwords used for account logins?",
		"num": "594",
		"correct_answer": "a",
		"answers": {
			"a": "The operating system performs a one-way hash of the passwords.",
			"b": "The operating system stores the passwords in a secret file that users cannot find.",
			"c": "The operating system encrypts the passwords, and decrypts them when needed.",
			"d": "The operating system stores all passwords in a protected segment of non-volatile memory."
		}
	},
	{
		"question": "You are a Network Security Officer. You have two machines. The first machine (192.168.0.99) has snort installed, and the second machine (192.168.0.150) has kiwi syslog installed.\nYou perform a syn scan in your network, and you notice that kiwi syslog is not receiving the alert message from snort.\nYou decide to run Wireshark in the snort machine to check if the messages are going to the kiwi syslog machine.\nWhat Wireshark filter will show the connections from the snort machine to kiwi syslog machine?",
		"num": "595",
		"correct_answer": "c",
		"answers": {
			"a": "tcp.dstport==514 && ip.dst==192.168.0.99",
			"b": "tcp.srcport==514 && ip.src==192.168.150",
			"c": "tcp.dstport==514 && ip.dst==192.168.0.150",
			"d": "tcp.srcport==514 && ip.src==192.168.0.99"
		}
	},
	{
		"question": "What technique is used to ensure a buffer overflow will successfully execute the desired code by creating a padding in memory?",
		"num": "596",
		"correct_answer": "a",
		"answers": {
			"a": "NOP sled",
			"b": "Heap spray",
			"c": "Heap sled"
		}
	},
	{
		"question": "Which of the following business challenges could be solved by using a vulnerability scanner?",
		"num": "597",
		"correct_answer": "d",
		"answers": {
			"a": "Auditors want to discover if all systems are following a standard naming convention.",
			"b": "A web server was compromised and management needs to know if any further systems were compromised.",
			"c": "There is an emergency need to remove administrator access from multiple machines for an employee  that quit.",
			"d": "There is a monthly requirement to test corporate compliance with host application usage and security policies."
		}
	},
	{
		"question": "Proxy is a network computer that can serve as an intermediary for connecting with other computers. \n\nWhich of the following sentence is true about a proxy?",
		"num": "598",
		"correct_answer": "a",
		"answers": {
			"a": "Protects the local network from outside access",
			"b": "Does not allow the connection of a number of computers to the Internet when having only one IP address",
			"c": "Allows attacker to view the desktop of users system ",
			"d": "Cannot be used to filter out unwanted content"
		}
	},
	{
		"question": "Which of the following tools can be used to perform a zone transfer?",
		"num": "599",
		"correct_answer": "acde",
		"answers": {
			"a": "NSLookup",
			"b": "Finger",
			"c": "Dig",
			"d": "Sam Spade",
			"e": "Host",
			"f": "Netcat",
			"g": "Neotrace"
		}
	},
	{
		"question": "A security administrator notices that the log file of the company`s webserver contains suspicious entries: Based on source code analysis, the analyst concludes that the login.php script is vulnerable to",
		"num": "600",
		"correct_answer": "b",
		"answers": {
			"a": "command injection.",
			"b": "SQL injection.",
			"c": "directory traversal.",
			"d": "LDAP injection."
		}
	},
	{
		"question": "Lawful intercept is a process that enables a Law Enforcement Agency (LEA) to perform electronic surveillance on a target as authorized by a judicial or administrative order.\nWhich of the following statement is true for lawful intercept?",
		"num": "601",
		"correct_answer": "b",
		"answers": {
			"a": "Affects the subscriber\u2019s services on the router",
			"b": "Hides information about lawful intercepts from all but the most privileged users",
			"c": "Does not allows multiple LEAs to run a lawful intercept on the same target without each others knowledge",
			"d": "Allows wiretaps only for outgoing communication",
			"e": "alters the traffic"
		}
	},
	{
		"question": "Secure Hashing Algorithm (SHA) is an algorithm for generating cryptographically secure one-way hash, published by the National Institute of Standards and Technology as a U.S. Federal Information Processing Standard.  What is the block (word) size used by SHA-512 algorithm?",
		"num": "602",
		"correct_answer": "b",
		"answers": {
			"a": "32-bit",
			"b": "64-bit",
			"c": "128-bit",
			"d": "256-bit"
		}
	},
	{
		"question": "Which method can provide a better return on IT security investment and provide a thorough and comprehensive assessment of organizational security covering policy, procedure design, and implementation?",
		"num": "603",
		"correct_answer": "a",
		"answers": {
			"a": "Penetration testing",
			"b": "Social engineering",
			"c": "Vulnerability scanning",
			"d": "Access control list reviews"
		}
	},
	{
		"question": "A company's Web development team has become aware of a certain type of security vulnerability in their Web software.\nTo mitigate the possibility of this vulnerability being exploited, the team wants to modify the software requirements to disallow users from entering HTML as input into their Web application.\nWhat kind of Web application vulnerability likely exists in their software?",
		"num": "604",
		"correct_answer": "c",
		"answers": {
			"a": "Cross-site Request Forgery vulnerability",
			"b": "SQL injection vulnerability",
			"c": "Cross-site scripting vulnerability",
			"d": "Session management vulnerability"
		}
	},
	{
		"question": "A jailbroken iOS device is usually less secure than an unjailbroken iOS device. True or false?",
		"num": "605",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "An IT security engineer notices that the company's web server is currently being hacked.\nWhat should the engineer do next?",
		"num": "606",
		"correct_answer": "c",
		"answers": {
			"a": "Unplug the network connection on the company's web server.",
			"b": "Determine the origin of the attack and launch a counterattack.",
			"c": "Record as much information as possible from the attack.",
			"d": "Perform a system restart on the company's web server."
		}
	},
	{
		"question": "Bob has set up three web servers on Windows Server 2008 IIS 7.0. Bob has followed all the\nrecommendations for securing the operating system and IIS. These servers are going to run numerous ecommerce\nwebsites that are projected to bring in thousands of dollars a day. Bob is still concerned about\nthe security of these servers because of the potential for financial loss. Bob has asked his company's\nfirewall administrator to set the firewall to inspect all incoming traffic on ports 80 and 443 to ensure that no\nmalicious data is getting into the network.\nWhy will this not be possible?",
		"num": "607",
		"correct_answer": "c",
		"answers": {
			"a": "Firewalls cannot inspect traffic coming through port 443",
			"b": "Firewalls can only inspect outbound traffic",
			"c": "Firewalls cannot inspect traffic at all, they can only block or allow certain ports",
			"d": "Firewalls cannot inspect traffic coming through port 80"
		}
	},
	{
		"question": "Wired Equivalent Privacy (WEP) is an IEEE 802.11 wireless protocol which provides security algorithms for data confidentiality during wireless transmissions.\nWEP uses stream cipher RC4 for confidentiality, and the CRC-32 checksum for integrity of wireless transmission.\nWhat is the size of WEP initialization vector (IV)?",
		"num": "608",
		"correct_answer": "c",
		"answers": {
			"a": "8-bit",
			"b": "16-bit",
			"c": "24-bit",
			"d": "32-bit"
		}
	},
	{
		"question": "ICMP ping and ping sweeps are used to check for active systems and to check",
		"num": "609",
		"correct_answer": "a",
		"answers": {
			"a": "if ICMP ping traverses a firewall.",
			"b": "the route that the ICMP ping took.",
			"c": "the location of the switchport in relation to the ICMP ping.",
			"d": "the number of hops an ICMP ping takes to reach a destination."
		}
	},
	{
		"question": "This attack technique is used when a Web application is vulnerable to an SQL Injection but the results of the Injection are not visible to the attacker.",
		"num": "610",
		"correct_answer": "b",
		"answers": {
			"a": "Unique SQL Injection",
			"b": "Blind SQL Injection",
			"c": "Generic SQL Injection",
			"d": "Double SQL Injection"
		}
	},
	{
		"question": "Which of the following items is unique to the N-tier architecture method of designing software applications?",
		"num": "611",
		"correct_answer": "a",
		"answers": {
			"a": "Application layers can be separated, allowing each layer to be upgraded independently from other layers.",
			"b": "It is compatible with various databases including Access, Oracle, and SQL.",
			"c": "Data security is tied into each layer and must be updated for all layers when any upgrade is performed.",
			"d": "Application layers can be written in C, ASP.NET, or Delphi without any performance loss."
		}
	},
	{
		"question": "What's stack smashing?",
		"num": "612",
		"correct_answer": "c",
		"answers": {
			"a": "It's when code is executed from a default heap.",
			"b": "It's when an attacker gets to a stack after they're done with the pumpkins.",
			"c": "A buffer overflow that overwrites the return address",
			"d": "The input of No Operation instruction code in a string"
		}
	},
	{
		"question": "Which of the following represent weak password?\n(Select 2 answers)",
		"num": "613",
		"correct_answer": "be",
		"answers": {
			"a": "Passwords that contain letters, special characters, and numbers ExamplE. ap1$%##f@52",
			"b": "Passwords that contain only numbers Example. 23698217",
			"c": "Passwords that contain only special characters Example. &*#@!(%)",
			"d": "Passwords that contain letters and numbers Example. meerdfget123",
			"e": "Passwords that contain only letters Example. QWERTYKLRTY",
			"f": "Passwords that contain only special characters and numbers Example. 123@$45",
			"g": "Passwords that contain only letters and special characters Examplbob@&ba"
		}
	},
	{
		"question": "Which technical characteristic do Ethereal/Wireshark, TCPDump, and Snort have in common?",
		"num": "614",
		"correct_answer": "d",
		"answers": {
			"a": "They are written in Java.",
			"b": "They send alerts to security monitors.",
			"c": "They use the same packet analysis engine.",
			"d": "They use the same packet capture utility."
		}
	},
	{
		"question": "Jacob is looking through a traffic log that was captured using Wireshark.\nJacob has come across what appears to be SYN requests to an internal computer from a spoofed IP address.\nWhat is Jacob seeing here?",
		"num": "615",
		"correct_answer": "b",
		"answers": {
			"a": "Jacob is seeing a Smurf attack.",
			"b": "Jacob is seeing a SYN flood.",
			"c": "He is seeing a SYN/ACK attack.",
			"d": "He has found evidence of an ACK flood."
		}
	},
	{
		"question": "From a security perspective, there is no problem in using the '>>' operator.",
		"num": "616",
		"correct_answer": "b",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which mode of IPSec should you use to assure security and confidentiality of data within the same LAN?",
		"num": "617",
		"correct_answer": "a",
		"answers": {
			"a": "ESP transport",
			"b": "mode AH Tunnel",
			"c": "mode ESP",
			"d": "AH promiscuous"
		}
	},
	{
		"question": "Jason works in the sales and marketing department for a very large advertising agency located in Atlanta.\nJason is working on a very important marketing campaign for his company's largest client. Before the\nproject could be completed and implemented, a competing advertising company comes out with the exact\nsame marketing materials and advertising, thus rendering all the work done for Jason's client unusable.\nJason is questioned about this and says he has no idea how all the material ended up in the hands of a\ncompetitor.\nWithout any proof, Jason's company cannot do anything except move on. After working on another high\nprofile client for about a month, all the marketing and sales material again ends up in the hands of another\ncompetitor and is released to the public before Jason's company can finish the project. Once again, Jason\nsays that he had nothing to do with it and does not know how this could have happened. Jason is given\nleave with pay until they can figure out what is going on.\nJason's supervisor decides to go through his email and finds a number of emails that were sent to the\ncompetitors that ended up with the marketing material. The only items in the emails were attached jpg files,\nbut nothing else. Jason's supervisor opens the picture files, but cannot find anything out of the ordinary with\nthem.\nWhat technique has Jason most likely used?",
		"num": "618",
		"correct_answer": "d",
		"answers": {
			"a": "Stealth Rootkit Technique",
			"b": "ADS Streams Technique",
			"c": "Snow Hiding Technique",
			"d": "Image Steganography Technique"
		}
	},
	{
		"question": "Rebecca commonly sees an error on her Windows system that states that a Data Execution Prevention (DEP) error has taken place.\nWhich of the following is most likely taking place?",
		"num": "619",
		"correct_answer": "a",
		"answers": {
			"a": "Malicious code is attempting to execute instruction a non-executable memory region.",
			"b": "A page fault is occuring, which forces the operating system to write data from the hard drive.",
			"c": "A race condition is being exploited, and the operating system is containing the malicious process.",
			"d": "Malware is executing in either ROM or a cache memory area."
		}
	},
	{
		"question": "You are the CIO for Avantes Finance International, a global finance company based in Geneva.\nYou are responsible for network functions and logical security throughout the entire corporation.\nYour company has over 250 servers running Windows Server, 5000 workstations running Windows Vista, and 200 mobile users working from laptops on Windows 7.\nLast week, 10 of your company's laptops were stolen from salesmen while at a conference in Amsterdam.\nThese laptops contained proprietary company information. While doing damage assessment on the possible public relations nightmare this may become, a news story leaks about the stolen laptops and also that sensitive information from those computers was posted to a blog online.\nWhat built-in Windows feature could you have implemented to protect the sensitive information on these laptops?",
		"num": "620",
		"correct_answer": "d",
		"answers": {
			"a": "You should have used 3DES which is built into Windows",
			"b": "If you would have implemented Pretty Good Privacy (PGP) which is built into Windows, the sensitive information on the laptops would not have leaked out",
			"c": "You should have utilized the built-in feature of Distributed File System (DFS) to protect the sensitive information on the laptops",
			"d": "You could have implemented Encrypted File System (EFS) to encrypt the sensitive files on the laptops"
		}
	},
	{
		"question": "What is the best description of SQL Injection?",
		"num": "621",
		"correct_answer": "d",
		"answers": {
			"a": "It is an attack used to modify the code in an application",
			"b": "It is a Denial of Service Attack (DoS)",
			"c": "It is a MiTM attack",
			"d": "It is an attack used to gain unauthorized access to a database"
		}
	},
	{
		"question": "Information may be hidden into the slack space of a file.",
		"num": "622",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "After a client sends a connection request (SYN) packet to the server, the server will respond (SYN-ACK) with a sequence number of its choosing, which then must be acknowledged (ACK) by the client.\nThis sequence number is predictable; the attack connects to a service first with its own IP address, records the sequence number chosen, and then opens a second connection from a forged IP address.\nThe attack doesn't see the SYN-ACK (or any other packet) from the server, but can guess the correct responses.\nIf the source IP address is used for authentication, then the attacker can use the one-sided communication to break into the server.\nWhat attacks can you successfully launch against a server using the above technique?",
		"num": "623",
		"correct_answer": "b",
		"answers": {
			"a": "Denial of Service attacks",
			"b": "Session Hijacking attacks",
			"c": "Web page defacement attacks",
			"d": "IP spoofing attacks"
		}
	},
	{
		"question": "A network security administrator is worried about potential man-in-the-middle attacks when users access a corporate web site from their workstations.\nWhich of the following is the best remediation against this type of attack?",
		"num": "624",
		"correct_answer": "c",
		"answers": {
			"a": "Implementing server-side PKI certificates for all connections",
			"b": "Mandating only client-side PKI certificates for all connections",
			"c": "Requiring client and server PKI certificates for all connections",
			"d": "Requiring strong authentication for all DNS queries"
		}
	},
	{
		"question": "How does traceroute map the route a packet travels from point A to point B?",
		"num": "625",
		"correct_answer": "b",
		"answers": {
			"a": "Uses a TCP timestamp packet that will elicit a time exceeded in transit message",
			"b": "Manipulates the value of the time to live (TTL) within packet to elicit a time exceeded in transit message",
			"c": "Uses a protocol that will be rejected by gateways on its way to the destination",
			"d": "Manipulates the flags within packets to force gateways into generating error messages"
		}
	},
	{
		"question": "Attackers craft malicious probe packets and scan for services such as HTTP over SSL (HTTPS), SMTP over SSL (SMPTS) and IMAP over SSL (IMAPS) to detect honeypots in a network.\nWhich of the following condition shows the presence of a honeypot?",
		"num": "626",
		"correct_answer": "a",
		"answers": {
			"a": "Ports show a particular service running but deny a three-way handshake connection",
			"b": "Ports show a particular service running and allow a three-way handshake connection",
			"c": "Ports do not show any particular service running",
			"d": "Scan shows that no scanned port is live on the network"
		}
	},
	{
		"question": "Which of these is a potential carrier file?",
		"num": "627",
		"correct_answer": "a",
		"answers": {
			"a": "All of these",
			"b": "Executable file",
			"c": "Audio file",
			"d": "Image file"
		}
	},
	{
		"question": "A hacker was able to sniff packets on a company's wireless network. The following information was discovered.\n\nThe Key\n10110010 01001011\n\nThe Cyphertext\n01100101 01011010\n\nUsing the Exlcusive OR, what was the original message?",
		"num": "628",
		"correct_answer": "b",
		"answers": {
			"a": "00101000 11101110",
			"b": "11010111 00010001",
			"c": "00001101 10100100",
			"d": "11110010 01011011"
		}
	},
	{
		"question": "_________ is a set of extensions to DNS that provide to DNS clients (resolvers) the origin authentication of DNS data to reduce the threat of DNS poisoning, spoofing, and similar types of attacks.\n",
		"num": "629",
		"correct_answer": "a",
		"answers": {
			"a": "DNSSEC",
			"b": "Resource records",
			"c": "Resource transfer",
			"d": "Zone transfer"
		}
	},
	{
		"question": "You are a security officer of a company.\nYou had an alert from IDS that indicates that one PC on your Intranet is connected to a blacklisted IP address (C2 Server) on the Internet.\nThe IP address was blacklisted just before the alert.\nYou are staring an investigation to roughly analyze the severity of the situation.\nWhich of the following is appropriate to analyze?",
		"num": "630",
		"correct_answer": "b",
		"answers": {
			"a": "Event logs on the PC",
			"b": "Internet Firewall/Proxy log",
			"c": "IDS log",
			"d": "Event logs on domain controller"
		}
	},
	{
		"question": "You are the security administrator of Jaco Banking Systems located in Boston. You are setting up ebanking website (http://www.ejacobank.com) authentication system. Instead of issuing banking customer\nwith a single password, you give them a printed list of 100 unique passwords. Each time the customer needs to log into the e-banking system website, the customer enters the next password on the list. If\nsomeone sees them type the password using shoulder surfing, MiTM or keyloggers, then no damage is\ndone because the password will not be accepted a second time. Once the list of 100 passwords is almost\nfinished, the system automatically sends out a new password list by encrypted e-mail to the customer.\nYou are confident that this security implementation will protect the customer from password abuse.\nTwo months later, a group of hackers called \"HackJihad\" found a way to access the one-time password list issued to customers of Jaco Banking Systems. The hackers set up a fake website (http://www.e-jacobank.com) and used phishing attacks to direct ignorant customers to it. The fake website asked users for their ebanking\nusername and password, and the next unused entry from their one-time password sheet. The hackers collected 200 customer's username/passwords this way. They transferred money from the customer's bank account to various offshore accounts.\nYour decision of password policy implementation has cost the bank with USD 925, 000 to hackers. You immediately shut down the e-banking website while figuring out the next best security solution\nWhat effective security solution will you recommend in this case?",
		"num": "631",
		"correct_answer": "d",
		"answers": {
			"a": "Implement Biometrics based password authentication system. Record the customers face image to the authentication database",
			"b": "Configure your firewall to block logon attempts of more than three wrong tries",
			"c": "Enable a complex password policy of 20 characters and ask the user to change the password immediately after they logon and do not store password histories",
			"d": "Implement RSA SecureID based authentication system"
		}
	},
	{
		"question": "What is a sniffing performed on a switched network called?",
		"num": "632",
		"correct_answer": "d",
		"answers": {
			"a": "Spoofed sniffing",
			"b": "Passive sniffing",
			"c": "Direct sniffing",
			"d": "Active sniffing"
		}
	},
	{
		"question": "You are gathering competitive intelligence on an organization. You notice that they have jobs listed on a few Internet job-hunting sites.\nThere are two jobs for network and system administrators.\nHow can this help you in foot printing the organization?",
		"num": "633",
		"correct_answer": "d",
		"answers": {
			"a": "To learn about the IP range used by the target network",
			"b": "To identify the number of employees working for the company",
			"c": "To test the limits of the corporate security policy enforced in the company",
			"d": "To learn about the operating systems, services and applications used on the network"
		}
	},
	{
		"question": "It is a regulation that has a set of guidelines, which should be adhered to by anyone who handles any electronic medical data.\nThese guidelines stipulate that all medical practices must ensure that all necessary measures are in place while saving, accessing, and sharing any electronic medical data to keep patient data\nsecure.\nWhich of the following regulations best matches the description?",
		"num": "634",
		"correct_answer": "b",
		"answers": {
			"a": "ISO/IEC 27002",
			"b": "HIPAA",
			"c": "FISMA",
			"d": "COBIT"
		}
	},
	{
		"question": "What is one thing a tester can do to ensure that the software is trusted and is not changing or tampering with critical data on the back end of a system it is loaded on?",
		"num": "635",
		"correct_answer": "d",
		"answers": {
			"a": "Proper testing",
			"b": "Secure coding principles",
			"c": "Systems security and architecture review",
			"d": "Analysis of interrupts within the software"
		}
	},
	{
		"question": "By manipulating a buffer overflow, an attacker can jump:\nCorrect Answer:",
		"num": "636",
		"correct_answer": "d",
		"answers": {
			"a": "To a function in the program",
			"b": "To one of the program's libraries",
			"c": "To a buffer he/she has created",
			"d": "All of these"
		}
	},
	{
		"question": "Which of the following is a mutation technique used for writing buffer overflow exploits in order to avoid IDS and other filtering mechanisms?",
		"num": "637",
		"correct_answer": "b",
		"answers": {
			"a": "Assuming that a string function is exploited, send a long string as the input",
			"b": "Randomly replace the NOPs with functionally equivalent segments of the code (e.g.: x++; x-; ? NOP NOP)",
			"c": "Pad the beginning of the intended buffer overflow with a long run of NOP instructions (a NOP slide or sled) so the CPU will do nothing until it gets to the \u201cmain event\u201d",
			"d": "makes a buffer to overflow on the lower part of heap, overwriting other dynamic variables, which can have unexpected and unwanted effects"
		}
	},
	{
		"question": "Network Time Protocol (NTP) is designed to synchronize clocks of networked computers. \n\nWhich of the following port NTP uses as its primary means of communication?",
		"num": "638",
		"correct_answer": "a",
		"answers": {
			"a": "UDP port 123",
			"b": "UDP port 113",
			"c": "UDP port 161",
			"d": "UDP port 320"
		}
	},
	{
		"question": "This attack uses social engineering techniques to trick users into accessing a fake Web site and divulging personal information.\nAttackers send a legitimate-looking e-mail asking users to update their information on the company's Web site, but the URLs in the e-mail actually point to a false Web site.",
		"num": "639",
		"correct_answer": "c",
		"answers": {
			"a": "Wiresharp attack",
			"b": "Switch and bait attack",
			"c": "Phishing attack",
			"d": "Man-in-the-Middle attack"
		}
	},
	{
		"question": "Which solution can be used to emulate computer services, such as mail and ftp, and to capture information related to logins or actions?",
		"num": "640",
		"correct_answer": "b",
		"answers": {
			"a": "Firewall",
			"b": "Honeypot",
			"c": "Core server",
			"d": "Layer 4 switch"
		}
	},
	{
		"question": "You need to monitor all traffic on your local network for suspicious activity and receive notifications when an attack is occurring. Which tool would allow you to accomplish this goal?",
		"num": "641",
		"correct_answer": "c",
		"answers": {
			"a": "Host based IDS",
			"b": "Proxy",
			"c": "Network based IDS",
			"d": "Firewall"
		}
	},
	{
		"question": "Lawful intercept is a process that enables a Law Enforcement Agency (LEA) to perform electronic surveillance on a target as authorized by a judicial or administrative order. \n\nWhich of the following statement is true for lawful intercept?",
		"num": "642",
		"correct_answer": "b",
		"answers": {
			"a": "Affects the subscriber?s services on the router",
			"b": "Hides information about lawful intercepts from all but the most privileged users",
			"c": "Does not allows multiple LEAs to run a lawful intercept on the same target without each others knowledge",
			"d": "Allows wiretaps only for outgoing communication",
			"e": "alters the traffic"
		}
	},
	{
		"question": "In which of the following password protection technique, random strings of characters are added to the password before calculating their hashes?",
		"num": "643",
		"correct_answer": "c",
		"answers": {
			"a": "Keyed Hashing",
			"b": "Key Stretching",
			"c": "Salting",
			"d": "Double Hashing"
		}
	},
	{
		"question": "Port scanning can be used as part of a technical assessment to determine network vulnerabilities.\nThe TCP XMAS scan is used to identify listening ports on the targeted system.\nIf a scanned port is open, what happens?",
		"num": "644",
		"correct_answer": "a",
		"answers": {
			"a": "The port will ignore the packets.",
			"b": "The port will send an RST.",
			"c": "The port will send an ACK.",
			"d": "The port will send a SYN."
		}
	},
	{
		"question": "You want to capture Facebook website traffic in Wireshark\nWhat display filter should you use that shows all TCP packets that contain the word 'facebook'?",
		"num": "645",
		"correct_answer": "c",
		"answers": {
			"a": "display==facebook",
			"b": "traffic.content==facebook",
			"c": "tcp contains facebook",
			"d": "list.display.facebook"
		}
	},
	{
		"question": "Which of the following levels of algorithms does Public Key Infrastructure (PKI) use?",
		"num": "646",
		"correct_answer": "a",
		"answers": {
			"a": "RSA 1024 bit strength",
			"b": "AES 1024 bit strength",
			"c": "RSA 512 bit strength",
			"d": "AES 512 bit strength"
		}
	},
	{
		"question": "A circuit level gateway works at which of the following layers of the OSI Model?",
		"num": "647",
		"correct_answer": "b",
		"answers": {
			"a": "Layer 5 - Application",
			"b": "Layer 4 - TCP",
			"c": "Layer 3 - Internet protocol",
			"d": "Layer 2 - Data link"
		}
	},
	{
		"question": "Bob, your senior colleague, has sent you a mail regarding aa deal with one of the clients.\nYou are requested to accept the offer and you oblige.\nAfter 2 days, Bob denies that he had ever sent a mail.\nWhat do you want to \u201cknow\u201d to prove yourself that it was Bob who had send a mail?",
		"num": "648",
		"correct_answer": "c",
		"answers": {
			"a": "Confidentiality",
			"b": "Integrity",
			"c": "Non-Repudiation",
			"d": "Authentication"
		}
	},
	{
		"question": "Identify the web application attack where attackers exploit webpage vulnerabilities to force an unsuspecting user?s browser to send malicious requests they did not intend.\nThe victim holds an active session with a trusted site and simultaneously visits a malicious site, which injects an HTTP request for the trusted site into the victim user?s session, compromising its integrity",
		"num": "649",
		"correct_answer": "b",
		"answers": {
			"a": "Cross-Site Scripting (XSS)",
			"b": "Cross-Site Request Forgery (CSRF) ",
			"c": "LDAP Injection attack",
			"d": "SQL injection attack"
		}
	},
	{
		"question": "You need a tool that can do network intrusion prevention and intrusion detection, function as a network sniffer, and record network activity.\nWhat tool would you most likely select?",
		"num": "650",
		"correct_answer": "a",
		"answers": {
			"a": "Snort",
			"b": "Nmap",
			"c": "Cain & Abel",
			"d": "Nessus"
		}
	},
	{
		"question": "In what stage of Virus life does a stealth virus gets activated with the user performing certain actions such as running an infected program?",
		"num": "651",
		"correct_answer": "e",
		"answers": {
			"a": "Design",
			"b": "Elimination",
			"c": "Incorporation",
			"d": "Replication",
			"e": "Launch",
			"f": "Detection"
		}
	},
	{
		"question": "While performing a ping sweep of a local subnet you receive an ICMP reply of Code 3/Type 13 for all the\npings you have sent out. What is the most likely cause of this?",
		"num": "652",
		"correct_answer": "c",
		"answers": {
			"a": "The firewall is dropping the packets",
			"b": "An in-line IDS is dropping the packets",
			"c": "A router is blocking ICMP",
			"d": "The host does not respond to ICMP packets"
		}
	},
	{
		"question": "What is the main difference between a \"Normal\" SQL Injection and a \"Blind\" SQL Injection vulnerability?",
		"num": "653",
		"correct_answer": "d",
		"answers": {
			"a": "The request to the web server is not visible to the administrator of the vulnerable application.",
			"b": "The attack is called \"Blind\" because, although the application properly filters user input, it is still vulnerable to code injection.",
			"c": "The successful attack does not show an error message to the administrator of the affected application.",
			"d": "The vulnerable application does not display errors with information about the injection results to the attacker."
		}
	},
	{
		"question": "Attacking well-known system defaults is one of the most common hacker attacks. Most software is shipped with a default configuration that makes it easy to install and setup the application.\nYou should change the default settings to secure the system.\nWhich of the following is NOT an example of default installation?",
		"num": "654",
		"correct_answer": "d",
		"answers": {
			"a": "Many systems come with default user accounts with well-known passwords that administrators forget to change",
			"b": "Often, the default location of installation files can be exploited which allows a hacker to retrieve a file from the system",
			"c": "Many software packages come with \"samples\" that can be exploited, such as the sample programs on IIS web services",
			"d": "Enabling firewall and anti-virus software on the local system"
		}
	},
	{
		"question": "You need to monitor all traffic on your local network for suspicious activity and receive notifications when an attack is occurring. Which tool would allow you to accomplish this goal?",
		"num": "655",
		"correct_answer": "c",
		"answers": {
			"a": "Host based IDS",
			"b": "Proxy",
			"c": "Network based IDS",
			"d": "Firewall"
		}
	},
	{
		"question": "Frederickson Security Consultants is currently conducting a security audit on the networks of Hawthorn Enterprises, a contractor for the Department of Defense.\nSince Hawthorn Enterprises conducts business daily with the federal government, they must abide by very stringent security policies.\nFrederickson is testing all of Hawthorn's physical and logical security measures including biometrics, passwords, and permissions.\nThe federal government requires that all users must utilize random, non-dictionary passwords that must take at least 30 days to crack. Frederickson has confirmed that all Hawthorn employees use a random password generator for their network passwords.\nThe Frederickson consultants have saved off numerous SAM files from Hawthorn's servers using Pwdump6 and are going to try and crack the network passwords.\n\nWhat method of attack is best suited to crack these passwords in the shortest amount of time?",
		"num": "656",
		"correct_answer": "a",
		"answers": {
			"a": "Brute force attack",
			"b": "Birthday attack",
			"c": "Dictionary attack",
			"d": "Brute service attack"
		}
	},
	{
		"question": "Risks = Threats x Vulnerabilities is referred to as the:",
		"num": "657",
		"correct_answer": "b",
		"answers": {
			"a": "Threat assessment",
			"b": "Risk equation",
			"c": "BIA equation",
			"d": "Disaster recovery formula"
		}
	},
	{
		"question": "While testing the company's web applications, a tester attempts to insert the following test script into the search area on the company's web site.\n\n     &lt;script&gt;alert(\" Testing Testing Testing \")&lt;/script&gt;\n\nAfterwards, when the tester presses the search button, a pop-up box appears on the screen with the text: \"Testing Testing Testing\".\nWhich vulnerability has been detected in the web application?",
		"num": "658",
		"correct_answer": "d",
		"answers": {
			"a": "Buffer overflow",
			"b": "Cross-site request forgery",
			"c": "Distributed denial of service",
			"d": "Cross-site scripting"
		}
	},
	{
		"question": "An NMAP scan of a server shows port 25 is open. What risk could this pose?",
		"num": "659",
		"correct_answer": "d",
		"answers": {
			"a": "Open printer sharing",
			"b": "Web portal data leak",
			"c": "Clear text authentication",
			"d": "Active mail relay"
		}
	},
	{
		"question": "What is a \u201cCollision attack\u201d in cryptography?",
		"num": "660",
		"correct_answer": "d",
		"answers": {
			"a": "Collision attacks try to get the public key",
			"b": "Collision attacks try to break the hash into three parts to get the plaintext value",
			"c": "Collision attacks try to break the hash into two parts, with the same bytes in each part to get the private key",
			"d": "Collision attacks try to find two inputs producing the same hash"
		}
	},
	{
		"question": "What is a rootkit?",
		"num": "661",
		"correct_answer": "c",
		"answers": {
			"a": "It's malware that intercepts packets in transit without being stored onto a target machine",
			"b": "It's malware that propagates without a specific target",
			"c": "It's malware that's used to gain access to a computer or computer system while being undetected",
			"d": "It's malware that uses social engineering techniques"
		}
	},
	{
		"question": "A company's security policy states that all Web browsers must automatically delete their HTTP browser cookies upon terminating.\nWhat sort of security breach is this policy attempting to mitigate?",
		"num": "662",
		"correct_answer": "c",
		"answers": {
			"a": "Attempts by attackers to determine the user's Web browser usage patterns, including when sites were visited and for how long.",
			"b": "Attempts by attackers to access passwords stored on the user's computer without the user's knowledge.",
			"c": "Attempts by attackers to access Web sites that trust the Web browser user by stealing the user's authentication credentials.",
			"d": "Attempts by attackers to access the user and password information stored in the company's SQL database."
		}
	},
	{
		"question": "JPEG images use discrete cosine transformation to achieve an optimal compression. True or false?",
		"num": "663",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "A hacker wants to break into Brown Co.'s computers and obtain their secret double fudge cookie recipe.\nJack calls Jane, an accountant at Brown Co., pretending to be an administrator from Brown Co.\nJack tells Jane that there has been a problem with some accounts and asks her to verify her password with him ''just to double check our records.''\nJane does not suspect anything amiss, and parts with her password. Jack can now access Brown Co.'s computers with a valid user name and password, to steal the cookie recipe.\nWhat kind of attack is being illustrated here?",
		"num": "664",
		"correct_answer": "b",
		"answers": {
			"a": "Reverse Psychology Reverse Engineering",
			"b": "Social Engineering",
			"c": "Spoofing Identity",
			"d": "Faking Identity"
		}
	},
	{
		"question": "Your computer is infected by E-mail tracking and spying Trojan. This Trojan infects the computer with a single file - emos.sys\nWhich step would you perform to detect this type of Trojan?",
		"num": "665",
		"correct_answer": "c",
		"answers": {
			"a": "Scan for suspicious startup programs using msconfig",
			"b": "Scan for suspicious network activities using Wireshark",
			"c": "Scan for suspicious device drivers in c:\\windows\\system32\\drivers",
			"d": "Scan for suspicious open ports using netstat"
		}
	},
	{
		"question": "Which of these is used during steganography to withstand statistical steganalysis?",
		"num": "666",
		"correct_answer": "d",
		"answers": {
			"a": "Stream-based cryptography process",
			"b": "Data whitening process",
			"c": "Data encoding process",
			"d": "All of these"
		}
	},
	{
		"question": "A security policy will be more accepted by employees if it is consistent and has the support of",
		"num": "667",
		"correct_answer": "b",
		"answers": {
			"a": "coworkers.",
			"b": "executive management.",
			"c": "the security officer.",
			"d": "a supervisor."
		}
	},
	{
		"question": "What is the main reason the use of a stored biometric is vulnerable to an attack?",
		"num": "668",
		"correct_answer": "d",
		"answers": {
			"a": "The digital representation of the biometric might not be unique, even if the physical characteristic is unique.",
			"b": "Authentication using a stored biometric compares a copy to a copy instead of the original to a copy.",
			"c": "A stored biometric is no longer \"something you are\" and instead becomes \"something you have\".",
			"d": "A stored biometric can be stolen and used by an attacker to impersonate the individual identified by the biometric."
		}
	},
	{
		"question": "Which of these rootkits would you rate as the most effective?",
		"num": "669",
		"correct_answer": "a",
		"answers": {
			"a": "Kernel level",
			"b": "Application level",
			"c": "Physical level",
			"d": "Library level"
		}
	},
	{
		"question": "Which of the following conditions must be given to allow a tester to exploit a Cross-Site Request Forgery (CSRF) vulnerable web application?",
		"num": "670",
		"correct_answer": "d",
		"answers": {
			"a": "The victim user must open the malicious link with an Internet Explorer prior to version 8.",
			"b": "The session cookies generated by the application do not have the HttpOnly flag set.",
			"c": "The victim user must open the malicious link with a Firefox prior to version 3.",
			"d": "The web application should not use random tokens."
		}
	},
	{
		"question": "CAM table in switch stores information such as MAC addresses available on physical ports with their associated VLAN parameters.\nWhat happens when the CAM table is full?",
		"num": "671",
		"correct_answer": "c",
		"answers": {
			"a": "Additional ARP request traffic will not be forwarded to any port on the switch",
			"b": "The switch will stop functioning and get disconnected from network",
			"c": "Additional ARP request traffic will flood every port on the switch",
			"d": "It does not affect the switch functioning"
		}
	},
	{
		"question": "\"Testing the network using the same methodologies and tools employed by attackers\"\n\nIdentify the correct terminology that defines the above statement.",
		"num": "672",
		"correct_answer": "b",
		"answers": {
			"a": "Vulnerability Scanning",
			"b": "Penetration Testing",
			"c": "Security Policy Implementation",
			"d": "Designing Network Security"
		}
	},
	{
		"question": "Firewalls are categorized into two; namely hardware firewall and software firewall. Identify the correct statement for a software firewall. ",
		"num": "673",
		"correct_answer": "d",
		"answers": {
			"a": "Software firewall is placed between the desktop and the software components of the operating system",
			"b": "Software firewall is placed between the router and the networking components of the operating system",
			"c": "Software firewall is placed between the anti-virus application and the IDS components of the operating system",
			"d": "Software firewall is placed between the normal application and the networking components of the operating system"
		}
	},
	{
		"question": "A hacker has successfully infected an internet-facing server which he will then use to send junk mail, take part in coordinated attacks, or host junk email content.\nWhich sort of trojan infects this server?",
		"num": "674",
		"correct_answer": "a",
		"answers": {
			"a": "Botnet Trojan",
			"b": "Turtle Trojans",
			"c": "Banking Trojans",
			"d": "Ransomware Trojans"
		}
	},
	{
		"question": "Bluetooth hacking refers to exploitation of Bluetooth stack implementation vulnerabilities to compromise sensitive data in Bluetooth-enabled devices and networks.\nWhich of the following Bluetooth attack refers to sending unsolicited messages over Bluetooth to Bluetooth-enabled devices such as PDA and mobile phones? ",
		"num": "675",
		"correct_answer": "b",
		"answers": {
			"a": "Bluesmacking",
			"b": "Bluejacking",
			"c": "Blue Snarfing",
			"d": "BlueSniff"
		}
	},
	{
		"question": "Which of the following parameters enables NMAP's operating system detection feature?",
		"num": "676",
		"correct_answer": "d",
		"answers": {
			"a": "NMAP -sV",
			"b": "NMAP -oS",
			"c": "NMAP -sR",
			"d": "NMAP -O"
		}
	},
	{
		"question": "This type of Port Scanning technique splits TCP header into several packets so that the packet filters are not able to detect what the packets intends to do.",
		"num": "677",
		"correct_answer": "b",
		"answers": {
			"a": "UDP Scanning",
			"b": "IP Fragment Scanning",
			"c": "Inverse TCP flag scanning",
			"d": "ACK flag scanning"
		}
	},
	{
		"question": "Splint is a source code analyzer that is capable of detecting a _____",
		"num": "678",
		"correct_answer": "c",
		"answers": {
			"a": "XSRF",
			"b": "XSS",
			"c": "Buffer overflow",
			"d": "SQL injection"
		}
	},
	{
		"question": "A computer technician is using a new version of a word processing software package when it is discovered that a special sequence of characters causes the entire computer to crash.\nThe technician researches the bug and discovers that no one else experienced the problem.\nWhat is the appropriate next step?",
		"num": "679",
		"correct_answer": "d",
		"answers": {
			"a": "Ignore the problem completely and let someone else deal with it.",
			"b": "Create a document that will crash the computer when opened and send it to friends.",
			"c": "Find an underground bulletin board and attempt to sell the bug to the highest bidder.",
			"d": "Notify the vendor of the bug and do not disclose it until the vendor gets a chance to issue a fix."
		}
	},
	{
		"question": "Attackers craft malicious probe packets and scan for services such as HTTP over SSL (HTTPS), SMTP over SSL (SMPTS) and IMAP over SSL (IMAPS) to detect honeypots in a network.\nWhich of the following condition shows the presence of a honeypot?",
		"num": "680",
		"correct_answer": "a",
		"answers": {
			"a": "Ports show a particular service running but deny a three-way handshake connection",
			"b": "Ports show a particular service running and allow a three-way handshake connection",
			"c": "Ports do not show any particular service running ",
			"d": "Scan shows that no scanned port is live on the network"
		}
	},
	{
		"question": "Steganography noticeably changes the carrier file.",
		"num": "681",
		"correct_answer": "b",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "LSB insertion can serve as a steganographic technique to hide messages in audio files.",
		"num": "682",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which of these is the best defense against a buffer overflow attack?",
		"num": "683",
		"correct_answer": "c",
		"answers": {
			"a": "Stack execute invalidation",
			"b": "Compiler tools",
			"c": "Write secure code",
			"d": "Dynamic runtime checks"
		}
	},
	{
		"question": "Which of the following is the structure designed to verify and authenticate the identity of individuals within the enterprise taking part in a data exchange?",
		"num": "684",
		"correct_answer": "c",
		"answers": {
			"a": "SOA",
			"b": "Biometrics",
			"c": "PKI",
			"d": "Single sign on"
		}
	},
	{
		"question": "What are the three types of authentication?",
		"num": "685",
		"correct_answer": "b",
		"answers": {
			"a": "Something you: know, remember, prove",
			"b": "Something you: have, know, are",
			"c": "Something you: show, prove, are",
			"d": "Something you: show, have, prove"
		}
	},
	{
		"question": "When analyzing the IDS logs, the system administrator noticed an alert was logged when the external router was accessed from the administrator's computer to update the router configuration.\nWhat type of an alert is this?",
		"num": "686",
		"correct_answer": "a",
		"answers": {
			"a": "False positive",
			"b": "False negative",
			"c": "True positve",
			"d": "True negative"
		}
	},
	{
		"question": "If an attacker's computer sends an IPID of 31400 to a zombie (Idle Scanning) computer on an open port, what will be the response?",
		"num": "687",
		"correct_answer": "b",
		"answers": {
			"a": "31400",
			"b": "31402",
			"c": "The zombie will not send a response",
			"d": "31401"
		}
	},
	{
		"question": "> NMAP -sn 192.168.11.200-215\nThe NMAP command above performs which of the following?",
		"num": "688",
		"correct_answer": "c",
		"answers": {
			"a": "A trace sweep",
			"b": "An operating system detect",
			"c": "A ping scan",
			"d": "A port scan"
		}
	},
	{
		"question": "Jimmy, an attacker, knows that he can take advantage of poorly designed input validation routines to create or alter SQL commands to gain access to private data or execute commands in the database.\nWhat technique does Jimmy use to compromise a database?",
		"num": "689",
		"correct_answer": "d",
		"answers": {
			"a": "Jimmy can submit user input that executes an operating system command to compromise a target system",
			"b": "Jimmy can gain control of system to flood the target system with requests, preventing legitimate users from gaining access",
			"c": "Jimmy can utilize an incorrect configuration that leads to access with higher-than expected privilege of the database",
			"d": "Jimmy can utilize this particular database threat that is an SQL injection technique to penetrate a target system"
		}
	},
	{
		"question": "What are noisy areas in steganography realm?",
		"num": "690",
		"correct_answer": "c",
		"answers": {
			"a": "Grayscale color area",
			"b": "Black areas",
			"c": "Areas with a great deal of natural color variation",
			"d": "Areas with little color variation"
		}
	},
	{
		"question": "This phase will increase the odds of success in later phases of the penetration test. It is also the very first step in Information Gathering, and it will tell you what the \"landscape\" looks like. What is the most important phase of ethical hacking in which you need to spend a considerable amount of time?",
		"num": "691",
		"correct_answer": "d",
		"answers": {
			"a": "Gaining access",
			"b": "Escalating privileges",
			"c": "Network mapping",
			"d": "Footprinting"
		}
	},
	{
		"question": "The network administrator at Spears Technology, Inc has configured the default gateway Cisco router's access-list as below:\nYou are hired to conduct security testing on their network. You successfully brute-force the SNMP community string using a SNMP crack tool.\nThe access-list configured at the router prevents you from establishing a successful connection.\n\nYou want to retrieve the Cisco configuration from the router. How would you proceed?",
		"num": "692",
		"correct_answer": "bd",
		"answers": {
			"a": "Use the Cisco's TFTP default password to connect and download the configuration file",
			"b": "Run a network sniffer and capture the returned traffic with the configuration file from the router",
			"c": "Run Generic Routing Encapsulation (GRE) tunneling protocol from your computer to the router masking your IP address",
			"d": "Send a customized SNMP set request with a spoofed source IP address in the range - 192.168.1.0"
		}
	},
	{
		"question": "Which solution can be used to emulate real services such as ftp, mail, etc and capture login attempts and related information? They're often used to study hacker\u2019s activities.",
		"num": "693",
		"correct_answer": "c",
		"answers": {
			"a": "Layer 4 switch",
			"b": "Core server",
			"c": "Honeypot",
			"d": "Firewall"
		}
	},
	{
		"question": "In the OSI model, where does PPTP encryption take place?",
		"num": "694",
		"correct_answer": "c",
		"answers": {
			"a": "Transport layer",
			"b": "Application layer",
			"c": "Data link layer",
			"d": "Network layer"
		}
	},
	{
		"question": "Which of the following is not a Bluetooth attack?",
		"num": "695",
		"correct_answer": "a",
		"answers": {
			"a": "Bluedriving",
			"b": "Bluesmacking",
			"c": "Bluesnarfing",
			"d": "Bluejacking"
		}
	},
	{
		"question": "A penetration test was done at a company.\nAfter the test, a report was written and given to the company\u2019s IT authorities.\nA section from the report is shown below:\n\n: Access List should be written between VLANs.\n: Port security should be enabled for the intranet.\n: A security solution which filters data packets should be set between intranet (LAN) and DMZ.\n: A WAF should be used in front of the web applications.\n\nAccording to the section from the report, which of the following choice is true?",
		"num": "696",
		"correct_answer": "a",
		"answers": {
			"a": "A stateful firewall can be used between intranet (LAN) and DMZ.",
			"b": "There is access control policy between VLANs.",
			"c": "MAC Spoof attacks cannot be performed.",
			"d": "Possibility of SQL Injection attack is eliminated."
		}
	},
	{
		"question": "Syslog is a standard for logging program messages. It allows separation of the software that generates\nmessages from the system that stores them and the software that reports and analyzes them. It also\nprovides devices, which would otherwise be unable to communicate a means to notify administrators of\nproblems or performance.\nWhat default port Syslog daemon listens on?",
		"num": "697",
		"correct_answer": "d",
		"answers": {
			"a": "242",
			"b": "312",
			"c": "416",
			"d": "514"
		}
	},
	{
		"question": "Which of the following statements regarding ethical hacking is incorrect?",
		"num": "698",
		"correct_answer": "d",
		"answers": {
			"a": "Ethical hacking should not involve writing to or modifying the target systems.",
			"b": "An organization should use ethical hackers who do not sell vendor hardware/software or other consulting services.",
			"c": "Testing should be remotely performed offsite.",
			"d": "Ethical hackers should never use tools or methods that have the potential of exploiting vulnerabilities in an organization's systems."
		}
	},
	{
		"question": "One way to defeat a multi-level security solution is to leak data via",
		"num": "699",
		"correct_answer": "c",
		"answers": {
			"a": "a bypass regulator.",
			"b": "steganography.",
			"c": "a covert channel.",
			"d": "asymmetric routing."
		}
	},
	{
		"question": "Which of the following cryptographic attack refers to extraction of cryptographic secrets (e.g. the password to an encrypted file) from a person by coercion or torture?",
		"num": "700",
		"correct_answer": "d",
		"answers": {
			"a": "Ciphertext-only Attack",
			"b": "Chosen-ciphertext Attack",
			"c": "Adaptive Chosen-plaintext Attack",
			"d": "Rubber Hose Attack"
		}
	},
	{
		"question": "The GET method should never be used when sensitive data such as credit card is being sent to a CGI program.\nThis is because any GET command will appear in the URL, and will be logged by any servers.\nFor example, let's say that you've entered your credit card information into a form that uses the GET method.\nThe URL may appear like this: https://www.xsecurity-bank.com/creditcard.asp?cardnumber=453453433532234\nThe GET method appends the credit card number to the URL.\nThis means that anyone with access to a server log will be able to obtain this information.\nHow would you protect from this type of attack?",
		"num": "701",
		"correct_answer": "c",
		"answers": {
			"a": "Never include sensitive information in a script",
			"b": "Use HTTPS SSLv3 to send the data instead of plain HTTPS",
			"c": "Replace the GET with POST method when sending data",
			"d": "Encrypt the data before you send using GET method"
		}
	},
	{
		"question": "Which type of hacker represents the highest risk to your network?",
		"num": "702",
		"correct_answer": "c",
		"answers": {
			"a": "black hat hackers",
			"b": "grey hat hackers",
			"c": "disgruntled employees",
			"d": "script kiddies"
		}
	},
	{
		"question": "Wi-Fi Protected Access (WPA) is a data encryption method for WLANs based on 802.11 standards.\nIt improves on the authentication and encryption features of WEP (Wired Equivalent Privacy).\nTemporal Key Integrity Protocol (TKIP) enhances WEP by adding a rekeying mechanism to provide fresh encryption and integrity keys.\nTemporal keys are changed for every ___________.\n",
		"num": "703",
		"correct_answer": "c",
		"answers": {
			"a": "1,000 packets",
			"b": "5,000 packets",
			"c": "10,000 packets",
			"d": "15,000 packets"
		}
	},
	{
		"question": "The establishment of a TCP connection involves a negotiation called three-way handshake.\nWhat type of message does the client send to the server in order to begin this negotiation?",
		"num": "704",
		"correct_answer": "b",
		"answers": {
			"a": "ACK",
			"b": "SYN",
			"c": "RST",
			"d": "SYN-ACK"
		}
	},
	{
		"question": "You are a Penetration Tester and are assigned to scan a server.\nYou need to use a scanning technique wherein the TCP Header is split into many packets so that it becomes difficult to detect what the packets are meant for.\nWhich of the below scanning technique will you use?",
		"num": "705",
		"correct_answer": "c",
		"answers": {
			"a": "ACK flag scanning",
			"b": "TCP Scanning",
			"c": "IP Fragment Scanning",
			"d": "Inverse TCP flag scanning"
		}
	},
	{
		"question": "Which of the following is an example of the principle of least privilege as a system security control?",
		"num": "706",
		"correct_answer": "d",
		"answers": {
			"a": "User should access all the information stored in the business to best execute their functions",
			"b": "Companies should have only a few employees",
			"c": "User should have limited access to the information regardless of its purpose",
			"d": "User must be able to access only the information and resources that are necessary for legitimate purpose"
		}
	},
	{
		"question": "What port number is used by Kerberos protocol?",
		"num": "707",
		"correct_answer": "a",
		"answers": {
			"a": "88",
			"b": "44",
			"c": "487",
			"d": "419"
		}
	},
	{
		"question": "A stego is sent as a secret information that is embedded in normal traffic. Which of the following method is used?",
		"num": "708",
		"correct_answer": "d",
		"answers": {
			"a": "Hidden active directory",
			"b": "Punching",
			"c": "Encryption",
			"d": "Covert channels"
		}
	},
	{
		"question": "Which of the following problems can be solved by using Wireshark?",
		"num": "709",
		"correct_answer": "d",
		"answers": {
			"a": "Tracking version changes of source code",
			"b": "Checking creation dates on all webpages on a server",
			"c": "Resetting the administrator password on multiple systems",
			"d": "Troubleshooting communication resets between two systems"
		}
	},
	{
		"question": "Internet Protocol Security IPSec is actually a suite of protocols.\nEach protocol within the suite provides different functionality.\nCollective IPSec does everything except.\n",
		"num": "710",
		"correct_answer": "a",
		"answers": {
			"a": "Work at the Data Link Layer",
			"b": "Protect the payload and the headers",
			"c": "Encrypt",
			"d": "Authenticate"
		}
	},
	{
		"question": "What does a firewall check to prevent particular ports and applications from getting packets into an organization?",
		"num": "711",
		"correct_answer": "a",
		"answers": {
			"a": "Transport layer port numbers and application layer headers",
			"b": "Presentation layer headers and the session layer port numbers",
			"c": "Network layer headers and the session layer port numbers",
			"d": "Application layer port numbers and the transport layer headers"
		}
	},
	{
		"question": "A company is using Windows Server 2003 for its Active Directory (AD).\nWhat is the most efficient way to crack the passwords for the AD users?",
		"num": "712",
		"correct_answer": "c",
		"answers": {
			"a": "Perform a dictionary attack.",
			"b": "Perform a brute force attack.",
			"c": "Perform an attack with a rainbow table.",
			"d": "Perform a hybrid attack."
		}
	},
	{
		"question": "When does the Payment Card Industry Data Security Standard (PCI-DSS) require organizations to perform external and internal penetration testing?",
		"num": "713",
		"correct_answer": "a",
		"answers": {
			"a": "At least once a year and after any significant upgrade or modification",
			"b": "At least once every three years or after any significant upgrade or modification",
			"c": "At least twice a year or after any significant upgrade or modification",
			"d": "At least once every two years and after any significant upgrade or modification"
		}
	},
	{
		"question": "In TCP communications there are 8 flags; FIN, SYN, RST, PSH, ACK, URG, ECE, CWR.\nThese flags have decimal numbers assigned to them:\nFIN = 1\nSYN = 2\nRST = 4\nPSH = 8\nACK = 16\nURG = 32\nECE = 64\nCWR =128\nExample: To calculate SYN/ACK flag decimal value, add 2 (which is the decimal value of the SYN flag) to 16 (which is the decimal value of the ACK flag), so the result would be 18.\n\nBased on the above calculation, what is the decimal value for XMAS scan?",
		"num": "714",
		"correct_answer": "c",
		"answers": {
			"a": "23",
			"b": "24",
			"c": "41",
			"d": "64"
		}
	},
	{
		"question": "TCP/IP Session Hijacking is carried out in which OSI layer?",
		"num": "715",
		"correct_answer": "b",
		"answers": {
			"a": "Datalink layer",
			"b": "Transport layer",
			"c": "Network layer",
			"d": "Physical layer"
		}
	},
	{
		"question": "Which of the following tools is used to analyze the files produced by several packet-capture programs such as tcpdump, WinDump, Wireshark, and EtherPeek?",
		"num": "716",
		"correct_answer": "a",
		"answers": {
			"a": "tcptrace",
			"b": "Tcptraceroute",
			"c": "OpenVAS",
			"d": "Nessus"
		}
	},
	{
		"question": "True or false? Stenography's niche in security of information is to replace cryptography?",
		"num": "717",
		"correct_answer": "b",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "A rootkit is a collection of tools (programs) that enable administrator-level access to a computer. This\nprogram hides itself deep into an operating system for malicious activity and is extremely difficult to detect.\nThe malicious software operates in a stealth fashion by hiding its files, processes and registry keys and\nmay be used to create a hidden directory or folder designed to keep out of view from a user's operating\nsystem and security software.\nWhat privilege level does a rootkit require to infect successfully on a Victim's machine?",
		"num": "718",
		"correct_answer": "d",
		"answers": {
			"a": "User level privileges",
			"b": "Ring 3 Privileges",
			"c": "System level privileges",
			"d": "Kernel level privileges"
		}
	},
	{
		"question": "While footprinting a network, what port/service should you look for to attempt a zone transfer?",
		"num": "719",
		"correct_answer": "b",
		"answers": {
			"a": "53 UDP",
			"b": "53 TCP",
			"c": "25 UDP",
			"d": "25 TCP",
			"e": "161 UDP",
			"f": "22 TCP",
			"g": "60 TCP"
		}
	},
	{
		"question": "A hacker has managed to gain access to a Linux host and stolen the password file from /etc/passwd.\nHow can he use it?",
		"num": "720",
		"correct_answer": "b",
		"answers": {
			"a": "The file reveals the passwords to the root user only.",
			"b": "The password file does not contain the passwords themselves.",
			"c": "He cannot read it because it is encrypted.",
			"d": "He can open it and read the user ids and corresponding passwords."
		}
	},
	{
		"question": "Which of the following is a symmetric cryptographic standard?",
		"num": "721",
		"correct_answer": "d",
		"answers": {
			"a": "DSA",
			"b": "PKI",
			"c": "RSA",
			"d": "3DES"
		}
	},
	{
		"question": "While conducting a penetration test, the tester determines that there is a firewall between the tester's machine and the target machine.\nThe firewall is only monitoring TCP handshaking of packets at the session layer of the OSI model.\nWhich type of firewall is the tester trying to traverse?",
		"num": "722",
		"correct_answer": "c",
		"answers": {
			"a": "Packet filtering firewall",
			"b": "Application-level firewall",
			"c": "Circuit-level gateway firewall",
			"d": "Stateful multilayer inspection firewall"
		}
	},
	{
		"question": "In Trojan terminology, what is a covert channel?",
		"num": "723",
		"correct_answer": "a",
		"answers": {
			"a": "A channel that transfers information within a computer system or network in a way that violates the security policy",
			"b": "A legitimate communication path within a computer system or network for transfer of data",
			"c": "It is a kernel operation that hides boot processes and services to mask detection",
			"d": "It is Reverse tunneling technique that uses HTTPS protocol instead of HTTP protocol to establish connections"
		}
	},
	{
		"question": "Gerald, the Systems Administrator for Hyped Enterprises, has just discovered that his network has been breached by an outside attacker.\nAfter performing routine maintenance on his servers, he discovers numerous remote tools were installed that no one claims to have knowledge of in his department.\nGerald logs onto the management console for his IDS and discovers an unknown IP address that scanned his network constantly for a week and was able to access his network through a high-level port that was not closed.\nGerald traces the IP address he found in the IDS log to a proxy server in Brazil. Gerald calls the company that owns the proxy server and after searching through their logs, they trace the source to another proxy server in Switzerland. Gerald calls the company in Switzerland that owns the proxy server and after scanning through the logs again, they trace the source back to a proxy server in China. What proxy tool has Gerald's attacker used to cover their tracks?",
		"num": "724",
		"correct_answer": "c",
		"answers": {
			"a": "ISA proxy",
			"b": "IAS proxy",
			"c": "TOR proxy",
			"d": "Cheops proxy"
		}
	},
	{
		"question": "It is a vulnerability in GNU's bash shell, discovered in September of 2014 that gives attackers access to run remote commands on a vulnerable system.\nThe malicious software can take control of an infected machine, launch denial-of-service attacks to disrupt websites, and scan for other vulnerable devices (including routers).\nWhich of the following vulnerabilities is being described?",
		"num": "725",
		"correct_answer": "c",
		"answers": {
			"a": "Shellbash",
			"b": "Rootshock",
			"c": "Shellshock",
			"d": "Rootshell"
		}
	},
	{
		"question": "Which type of stenography includes the replication of an image, text, or logo, so that the source of the document can be partially authenticated?",
		"num": "726",
		"correct_answer": "c",
		"answers": {
			"a": "Date stamping",
			"b": "JPEG tagging",
			"c": "Digital watermarking",
			"d": "Time stamping"
		}
	},
	{
		"question": "In Buffer Overflow exploit, which of the following registers gets overwritten with return address of the exploit code?",
		"num": "727",
		"correct_answer": "d",
		"answers": {
			"a": "EEP",
			"b": "ESP",
			"c": "EAP",
			"d": "EIP"
		}
	},
	{
		"question": "Lossless compression are considered best for those applications where the integrity of an original information can be maintained. True or false?",
		"num": "728",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Firewalk has just completed the second phase (the scanning phase) and a technician receives the output shown below. What conclusions can be drawn based on these scan results?\n\nTCP port 21 no response\nTCP port 22 no response\nTCP port 23 Time-to- live exceeded.",
		"num": "729",
		"correct_answer": "c",
		"answers": {
			"a": "The firewall itself is blocking ports 21 through 23 and a service is listening on port 23 of the target host.",
			"b": "The lack of response from ports 21 and 22 indicate that those services are not running on the destination server.",
			"c": "The scan on port 23 passed through the filtering device. This indicates that port 23 was not blocked at the firewall.",
			"d": "The scan on port 23 was able to make a connection to the destination host prompting the firewall to respond with a TTL error."
		}
	},
	{
		"question": "In an internal security audit, the white hat hacker gains control over a user account and attempts to acquire access to another account's confidential files and information. How can he achieve this?",
		"num": "730",
		"correct_answer": "a",
		"answers": {
			"a": "Privilege Escalation",
			"b": "Shoulder-Surfing",
			"c": "Hacking Active Directory",
			"d": "Port Scanning"
		}
	},
	{
		"question": "An LDAP directory can be used to store information similar to a SQL database.\nLDAP uses a ____ database structure instead of SQL\u2019s ______ structure.\nBecause of this, LDAP has difficulty representing many-to-one relationships.\n",
		"num": "731",
		"correct_answer": "d",
		"answers": {
			"a": "Strict, Abstract",
			"b": "Simple, Complex",
			"c": "Relational, Hierarchical",
			"d": "Hierarchical, Relational"
		}
	},
	{
		"question": "What is War Dialing?",
		"num": "732",
		"correct_answer": "a",
		"answers": {
			"a": "War dialing involves the use of a program in conjunction with a modem to penetrate the modem/PBXbased systems",
			"b": "War dialing is a vulnerability scanning technique that penetrates Firewalls",
			"c": "It is a social engineering technique that uses Phone calls to trick victims",
			"d": "Involves IDS Scanning Fragments to bypass Internet filters and stateful Firewalls"
		}
	},
	{
		"question": "Which of the following Registry location does a Trojan add entries to make it persistent on Windows 7?\n(Select 2 answers)",
		"num": "733",
		"correct_answer": "ad",
		"answers": {
			"a": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
			"b": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\System32\\CurrentVersion\\ Run",
			"c": "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\System32\\CurrentVersion\\Run",
			"d": "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
		}
	},
	{
		"question": "Which of the following is a hashing algorithm?",
		"num": "734",
		"correct_answer": "a",
		"answers": {
			"a": "MD5",
			"b": "PGP",
			"c": "DES",
			"d": "ROT13"
		}
	},
	{
		"question": "Rootkits are kernel programs having the ability to hide themselves and cover up traces of activities.\nIt replaces certain operating system calls and utilities with its own modified versions of those routines.\nWhich of the following rootkit modifies the boot sequence of the machine to load themselves instead of the original virtual machine monitor or operating system?",
		"num": "735",
		"correct_answer": "a",
		"answers": {
			"a": "Hypervisor level rootkit",
			"b": "Kernel level rootkit",
			"c": "Boot loader level rootkit",
			"d": "Library level rootkits"
		}
	},
	{
		"question": "A hacker named Jack is trying to compromise a bank\u2019s computer system.\nHe needs to know the operating system of that computer to launch further attacks.\nWhat process would help him?",
		"num": "736",
		"correct_answer": "a",
		"answers": {
			"a": "Banner Grabbing",
			"b": "IDLE/IPID Scanning",
			"c": "SSDP Scanning",
			"d": "UDP Scanning"
		}
	},
	{
		"question": "Which type of scan is used on the eye to measure the layer of blood vessels?",
		"num": "737",
		"correct_answer": "b",
		"answers": {
			"a": "Facial recognition scan",
			"b": "Retinal scan",
			"c": "Iris scan",
			"d": "Signature kinetics scan"
		}
	},
	{
		"question": "The intrusion detection system at a software development company suddenly generates multiple alerts regarding attacks against the company's external webserver, VPN concentrator, and DNS servers.\nWhat should the security team do to determine which alerts to check first?",
		"num": "738",
		"correct_answer": "c",
		"answers": {
			"a": "Investigate based on the maintenance schedule of the affected systems.",
			"b": "Investigate based on the service level agreements of the systems.",
			"c": "Investigate based on the potential effect of the incident.",
			"d": "Investigate based on the order that the alerts arrived in."
		}
	},
	{
		"question": "Ricardo wants to send secret messages to a competitor company. To secure these messages, he uses a technique of hiding a secret message within an ordinary message.\nThe technique provides 'security through obscurity'. What technique is Ricardo using?",
		"num": "739",
		"correct_answer": "d",
		"answers": {
			"a": "Encryption",
			"b": "Public-key cryptography",
			"c": "RSA algorithm",
			"d": "Steganography"
		}
	},
	{
		"question": "In order to compromise or to hack a system or network the hackers go through various phases of the hacking. \n\nWhat is the first hacking phase that hackers perform to gather information about a target prior to launching an attack?",
		"num": "740",
		"correct_answer": "a",
		"answers": {
			"a": "Reconnaissance",
			"b": "Scanning",
			"c": "Gaining Access",
			"d": "Maintaining Access",
			"e": "Clearing Track"
		}
	},
	{
		"question": "Nathan is testing some of his network devices. Nathan is using Macof to try and flood the ARP cache of these switches.\nIf these switches' ARP cache is successfully flooded, what will be the result?",
		"num": "741",
		"correct_answer": "a",
		"answers": {
			"a": "The switches will drop into hub mode if the ARP cache is successfully flooded.",
			"b": "If the ARP cache is flooded, the switches will drop into pix mode making it less susceptible to attacks.",
			"c": "Depending on the switch manufacturer, the device will either delete every entry in its ARP cache or reroute packets to the nearest switch.",
			"d": "The switches will route all traffic to the broadcast address created collisions."
		}
	},
	{
		"question": "Which of the following scan only works if the operating system's TCP/IP implementation is based on RFC 793?",
		"num": "742",
		"correct_answer": "a",
		"answers": {
			"a": "NULL scan",
			"b": "IDLE scan",
			"c": "TCP connect scan",
			"d": "Maintaining Access",
			"e": "FTP bounce scan"
		}
	},
	{
		"question": "Which command can be used to show the current TCP/IP connections?",
		"num": "743",
		"correct_answer": "c",
		"answers": {
			"a": "Netsh",
			"b": "Net use connection",
			"c": "Netstat",
			"d": "Net use"
		}
	},
	{
		"question": "It is possible to make the stack non-executable.",
		"num": "744",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "\ufeffWhich of the following countermeasure can specifically protect against both the MAC Flood and MAC Spoofing attacks?",
		"num": "745",
		"correct_answer": "a",
		"answers": {
			"a": "Configure Port Security on the switch",
			"b": "Configure Port Recon on the switch",
			"c": "Configure Switch Mapping",
			"d": "Configure Multiple Recognition on the switch"
		}
	},
	{
		"question": "While using your bank\u2019s online servicing you notice the following string in the URL bar: \u201chttp: // www.MyPersonalBank.com/ account?id=368940911028389&Damount=10980&Camount=21\u201d\nYou observe that if you modify the Damount&Camount values and submit the request, that data on the web page reflects the changes.\n\nWhich type of vulnerability is present on this site?",
		"num": "746",
		"correct_answer": "c",
		"answers": {
			"a": "Cookie Tampering",
			"b": "SQL Injection",
			"c": "Web Parameter Tampering",
			"d": "XSS Reflection"
		}
	},
	{
		"question": "Which of the following is a client-server tool utilized to evade firewall inspection?",
		"num": "747",
		"correct_answer": "a",
		"answers": {
			"a": "tcp-over-dns",
			"b": "kismet",
			"c": "nikto",
			"d": "hping"
		}
	},
	{
		"question": "TCP SYN Flood attack uses the three-way handshake mechanism.\n1. An attacker at system A sends a SYN packet to victim at system B\n2. System B sends a SYN/ACK packet to victim A\n3. As a normal three-way handshake mechanism system A should send an ACK packet to system B,\nhowever, system A does not send an ACK packet to system \"B\". In this case client B is waiting for an ACK\npacket from client A\nThis status of client B is called _________________",
		"num": "748",
		"correct_answer": "b",
		"answers": {
			"a": "\"half-closed\"",
			"b": "\"half open\"",
			"c": "\"full-open\"",
			"d": "\"xmas-open\""
		}
	},
	{
		"question": "Bluetooth uses which digital modulation technique to exchange information between paired devices?",
		"num": "749",
		"correct_answer": "a",
		"answers": {
			"a": "PSK (phase-shift keying)",
			"b": "FSK (frequency-shift keying)",
			"c": "ASK (amplitude-shift keying)",
			"d": "QAM (quadrature amplitude modulation)"
		}
	},
	{
		"question": "You are programming a buffer overflow exploit and you want to create a NOP sled of 200 bytes in the program exploit.c\nWhat is the hexadecimal value of NOP instruction?",
		"num": "750",
		"correct_answer": "d",
		"answers": {
			"a": "0x60",
			"b": "0x80",
			"c": "0x70",
			"d": "0x90"
		}
	},
	{
		"question": "Buffer Overflow occurs when an application writes more data to a block of memory, or buffer, than the buffer is allocated to hold. Buffer overflow attacks allow an attacker to modify the ___________ in order to control the process execution, crash the process and modify internal variables.",
		"num": "751",
		"correct_answer": "a",
		"answers": {
			"a": "Target process?s address space",
			"b": "Target remote access",
			"c": "Target rainbow table",
			"d": "Target SAM file"
		}
	},
	{
		"question": "It is an entity or event with the potential to adversely impact a system through unauthorized acces, destruction, disclosure, denial of service or modification of data.\nWhich of the following terms best matches the definition?",
		"num": "752",
		"correct_answer": "c",
		"answers": {
			"a": "Attack",
			"b": "Vulnerability",
			"c": "Threat",
			"d": "Risk"
		}
	},
	{
		"question": "You ping a target IP to check if the host is up.\nYou do not get a response.\nYou suspect ICMP is blocked at the firewall.\nNext you use hping2 tool to ping the target host and you get a response.\nWhy does the host respond to hping2 and not ping packet?",
		"num": "753",
		"correct_answer": "d",
		"answers": {
			"a": "Ping packets cannot bypass firewalls",
			"b": "You must use ping 10.2.3.4 switch",
			"c": "Hping2 uses stealth TCP packets to connect",
			"d": "Hping2 uses TCP instead of ICMP by default"
		}
	},
	{
		"question": "You have successfully gained access to a victim's computer using Windows 2003 Server SMB Vulnerability.\nWhich command will you run to disable auditing from the cmd?",
		"num": "754",
		"correct_answer": "d",
		"answers": {
			"a": "stoplog stoplog ?",
			"b": "EnterPol /nolog",
			"c": "EventViewer o service",
			"d": "auditpol.exe /disable"
		}
	},
	{
		"question": "Which of the following are password cracking tools? (Choose three.)",
		"num": "755",
		"correct_answer": "bce",
		"answers": {
			"a": "BTCrack",
			"b": "John the Ripper",
			"c": "KerbCrack",
			"d": "Nikto",
			"e": "Cain and Abel",
			"f": "Havij"
		}
	},
	{
		"question": "RSA is a public-key cryptosystem developed by MIT professors Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman in 1977 in an effort to help ensure Internet security. RSA uses modular arithmetic and elementary number theory to do computations using two very large prime numbers. Identify the statement which is true for RC6 algorithm: ",
		"num": "756",
		"correct_answer": "b",
		"answers": {
			"a": "Is a variable key-size stream cipher with byte-oriented operations and is based on the use of a random permutation",
			"b": "Includes integer multiplication and the use of four 4-bit working registers",
			"c": "Is a parameterized algorithm with a variable block size, key size, and a variable number of rounds",
			"d": "Is a 64 bit block cipher that uses a key length that can vary between 32 and 448 bits"
		}
	},
	{
		"question": "What is the least important information when you analyze a public IP address in a security alert?",
		"num": "757",
		"correct_answer": "a",
		"answers": {
			"a": "ARP",
			"b": "Whois",
			"c": "DNS",
			"d": "Geolocation"
		}
	},
	{
		"question": "An attacker is trying to redirect the traffic of a small office.\nThat office is using their own mail server, DNS server and NTP server because of the importance of their job.\nThe attacker gain access to the DNS server and redirect the direction www.google.com to his own IP address.\nNow when the employees of the office wants to go to Google they are being redirected to the attacker machine.\nWhat is the name of this kind of attack?",
		"num": "758",
		"correct_answer": "c",
		"answers": {
			"a": "MAC Flooding",
			"b": "Smurf Attack",
			"c": "DNS spoofing",
			"d": "ARP Polsoning"
		}
	},
	{
		"question": "During a recent security assessment, you discover the organization has one Domain Name Server (DNS) in a Demilitarized Zone (DMZ) and a second DNS server\non the internal network. What is this type of DNS configuration commonly called?",
		"num": "759",
		"correct_answer": "a",
		"answers": {
			"a": "Split DNS",
			"b": "DNSSEC",
			"c": "DNS Scheme",
			"d": "DynDNS"
		}
	},
	{
		"question": "Which of the following problems can be solved by using Wireshark?",
		"num": "760",
		"correct_answer": "a",
		"answers": {
			"a": "Troubleshooting communication resets between two systems",
			"b": "Tracking version changes of source code",
			"c": "Resetting the administrator password on multiple systems",
			"d": "Checking creation dates on all webpages on a server"
		}
	},
	{
		"question": "One advantage of an application-level firewall is the ability to",
		"num": "761",
		"correct_answer": "b",
		"answers": {
			"a": "filter packets at the network level.",
			"b": "filter specific commands, such as http:post.",
			"c": "retain state information for each packet.",
			"d": "monitor tcp handshaking."
		}
	},
	{
		"question": "This kind of malware is installed by criminals on your computer so they can lock it from a remote location.\nThis malware generates a popup window, webpage, or email warning from what looks like an official authority such as the FBI.\nIt explains your computer has been locked because of possible illegal activities and demands payment before you can access your files and programs again.\nWhich term best matches this definition?",
		"num": "762",
		"correct_answer": "d",
		"answers": {
			"a": "Spyware",
			"b": "Riskware",
			"c": "Adware",
			"d": "Ransomware"
		}
	},
	{
		"question": "An attacker attaches a rogue router in a network.\nHe wants to redirect traffic to a LAN attached to his router as part of a man-in-the-middle attack.\nWhat measure on behalf of the legitimate admin can mitigate this attack?",
		"num": "763",
		"correct_answer": "a",
		"answers": {
			"a": "Make sure that legitimate network routers are configured to run routing protocols with authentication.",
			"b": "Disable all routing protocols and only use static routes",
			"c": "Only using OSPFv3 will mitigate this risk.",
			"d": "Redirection of the traffic cannot happen unless the admin allows it explicitly."
		}
	},
	{
		"question": "Steganography can be detected by certain programs.",
		"num": "764",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "A Trojan horse is a destructive program that masquerades as a benign application.\nThe software initially appears to perform a desirable function for the user prior to installation and/or execution, but in addition to the expected function steals information or harms the system.\nThe challenge for an attacker is to send a convincing file attachment to the victim, which gets easily executed on the victim machine without raising any suspicion. Today's end users are quite knowledgeable about malwares and viruses. Instead of sending games and fun executables, Hackers today are quite successful in spreading the Trojans using Rogue security software.\nWhat is Rogue security software?",
		"num": "765",
		"correct_answer": "b",
		"answers": {
			"a": "A flash file extension to Firefox that gets automatically installed when a victim visits rogue software disabling websites",
			"b": "A Fake AV program that claims to rid a computer of malware, but instead installs spyware or other malware onto the computer. This kind of software is known as rogue security software.",
			"c": "Rogue security software is based on social engineering technique in which the attackers lures victim to visit spear phishing websites",
			"d": "This software disables firewalls and establishes reverse connecting tunnel between the victim's machine and that of the attacker"
		}
	},
	{
		"question": "A botnet can be managed through which of the following?",
		"num": "766",
		"correct_answer": "a",
		"answers": {
			"a": "IRC",
			"b": "E-Mail",
			"c": "Linkedin and Facebook",
			"d": "A vulnerable FTP server"
		}
	},
	{
		"question": "Bret is a web application administrator and has just read that there are a number of surprisingly common web application vulnerabilities that can be exploited by unsophisticated attackers with easily available tools\non the Internet. He has also read that when an organization deploys a web application, they invite the world to send HTTP requests. Attacks buried in these requests sail past firewalls, filters, platform hardening, SSL, and IDS without notice because they are inside legal HTTP requests. Bret is determined to weed out vulnerabilities.\n\nWhat are some of the common vulnerabilities in web applications that he should be concerned about?",
		"num": "767",
		"correct_answer": "a",
		"answers": {
			"a": "Non-validated parameters, broken access control, broken account and session management, cross-site scripting and buffer overflows are just a few common vulnerabilities",
			"b": "Visible clear text passwords, anonymous user account set as default, missing latest security patch, no firewall filters set and no SSL configured are just a few common vulnerabilities",
			"c": "No SSL configured, anonymous user account set as default, missing latest security patch, no firewall filters set and an inattentive system administrator are just a few common vulnerabilities",
			"d": "No IDS configured, anonymous user account set as default, missing latest security patch, no firewall filters set and visible clear text passwords are just a few common vulnerabilities"
		}
	},
	{
		"question": "You have several plain-text firewall logs that you must review to evaluate network traffic.\nYou know that in order to do fast, efficient searches of the logs you must use regular expressions.\nWhich command-line utility are you most likely to use?",
		"num": "768",
		"correct_answer": "d",
		"answers": {
			"a": "Relational Database",
			"b": "MS Excel",
			"c": "Notepad",
			"d": "Grep"
		}
	},
	{
		"question": "This method is used to determine the Operating system and version running on a remote target system.\nWhat is it called?",
		"num": "769",
		"correct_answer": "b",
		"answers": {
			"a": "Service Degradation",
			"b": "OS Fingerprinting",
			"c": "Manual Target System",
			"d": "Identification Scanning"
		}
	},
	{
		"question": "You are performing a penetration test. You achieved access via a buffer overflow exploit and you proceed to find interesting data, such as files with usernames and passwords.\nYou find a hidden folder that has the administrator's bank account password and login information for the administrator's bitcoin account.\nWhat should you do?",
		"num": "770",
		"correct_answer": "c",
		"answers": {
			"a": "Transfer money from the administrator's account to another account",
			"b": "Do not report it and continue the penetration test",
			"c": "Report immediately to the administrator",
			"d": "Do not transfer the money but steal the bitcoins"
		}
	},
	{
		"question": "There is a WEP encrypted wireless access point (AP) with no clients connected.\nIn order to crack the WEP key, a fake authentication needs to be performed.\nWhat information is needed when performing fake authentication to an AP? \n\nChoose two answers.",
		"num": "771",
		"correct_answer": "bc",
		"answers": {
			"a": "The IP address of the AP",
			"b": "The MAC address of the AP",
			"c": "The SSID of the wireless network",
			"d": "A failed authentication packet"
		}
	},
	{
		"question": "A penetration tester was hired to perform a penetration test for a bank.\nThe tester began searching for IP ranges owned by the bank, performing lookups on the bank's DNS servers, reading news articles online about the bank, watching what times the bank employees come into work and leave from work, searching the bank's job postings (paying special attention to IT related jobs), and visiting the local dumpster for the bank's corporate office.\nWhat phase of the penetration test is the tester currently in?",
		"num": "772",
		"correct_answer": "d",
		"answers": {
			"a": "Information reporting",
			"b": "Vulnerability assessment",
			"c": "Active information gathering",
			"d": "Passive information gathering"
		}
	},
	{
		"question": "When you are collecting information to perform a data analysis, Google commands are very useful to find sensitive information and files.\nThese files may contain information about passwords, system functions, or documentation.\nWhat command will help you to search files using Google as a search engine?",
		"num": "773",
		"correct_answer": "b",
		"answers": {
			"a": "inurl: target.com filename:xls username password email",
			"b": "site: target.com filetype:xls username password email site:",
			"c": "target.com file:xls username password email domain:",
			"d": "target.com archive:xls username password email"
		}
	},
	{
		"question": "Which of the following defines the role of a root Certificate Authority (CA) in a Public Key Infrastructure (PKI)?",
		"num": "774",
		"correct_answer": "b",
		"answers": {
			"a": "The root CA is the recovery agent used to encrypt data when a user's certificate is lost",
			"b": "The CA is the trusted root that issues certificates",
			"c": "The root CA is used to encrypt email messages to prevent unintended disclosure of data",
			"d": "The root CA stores the user's hash value for safekeeping."
		}
	},
	{
		"question": "Harold just got home from working at Henderson LLC where he works as an IT technician.\nHe was able to get off early because they were not too busy.\nWhen he walks into his home office, he notices his teenage daughter on the computer, apparently chatting with someone online.\nAs soon as she hears Harold enter the room, she closes all her windows and tries to act like she was playing a game.\nWhen Harold asks her what she was doing, she acts very nervous and does not give him a straight answer.\nHarold is very concerned because he does not want his daughter to fall victim to online predators and the sort.\nHarold doesn't necessarily want to install any programs that will restrict the sites his daughter goes to, because he doesn't want to alert her to his trying to figure out what she is doing.\nHarold wants to use some kind of program that will track her activities online, and send Harold an email of her activity once a day so he can see what she has been up to.\nWhat kind of software could Harold use to accomplish this?",
		"num": "775",
		"correct_answer": "b",
		"answers": {
			"a": "Install hardware Keylogger on her computer",
			"b": "Install screen capturing Spyware on her computer",
			"c": "Enable Remote Desktop on her computer",
			"d": "Install VNC on her computer"
		}
	},
	{
		"question": "How many bits encryption does SHA-1 use?",
		"num": "776",
		"correct_answer": "d",
		"answers": {
			"a": "64 bits",
			"b": "128 bits",
			"c": "256 bits",
			"d": "160 bits"
		}
	},
	{
		"question": "Which device in a wireless local area network (WLAN) determines the next network point to which a packet should be forwarded toward its destination?",
		"num": "777",
		"correct_answer": "c",
		"answers": {
			"a": "Wireless modem",
			"b": "Antenna",
			"c": "Wireless router",
			"d": "Mobile station"
		}
	},
	{
		"question": "An attacker has captured a target file that is encrypted with public key cryptography.\nWhich of the attacks below is likely to be used to crack the target file?",
		"num": "778",
		"correct_answer": "d",
		"answers": {
			"a": "Timing attack",
			"b": "Replay attack",
			"c": "Memory trade-off attack",
			"d": "Chosen plain-text attack"
		}
	},
	{
		"question": "Password cracking is a technique used to extract user?s password of application/files without the knowledge of the legitimate user. Which of the password cracking technique will the attacker use if he/she gets some information about the password to crack?",
		"num": "779",
		"correct_answer": "c",
		"answers": {
			"a": "Denial of Service Attack",
			"b": "Syllable Attack",
			"c": "Rule-based Attack",
			"d": "Distributed Network Attack (DNA)"
		}
	},
	{
		"question": "An attacker has installed a RAT on a host. The attacker wants to ensure that when a user attempts to go to \"www.MyPersonalBank.com\", that the user is directed to a phishing site.\nWhich file does the attacker need to modify?",
		"num": "780",
		"correct_answer": "a",
		"answers": {
			"a": "Hosts",
			"b": "Sudoers",
			"c": "Boot.ini",
			"d": "Networks"
		}
	},
	{
		"question": "Which of the following defines the role of a root Certificate Authority (CA) in a Public Key Infrastructure (PKI)?",
		"num": "781",
		"correct_answer": "c",
		"answers": {
			"a": "The root CA is the recovery agent used to encrypt data when a user's certificate is lost.",
			"b": "The root CA stores the user's hash value for safekeeping.",
			"c": "The CA is the trusted root that issues certificates.",
			"d": "The root CA is used to encrypt email messages to prevent unintended disclosure of data."
		}
	},
	{
		"question": "Which type of scan measures a person's external features through a digital video camera?",
		"num": "782",
		"correct_answer": "c",
		"answers": {
			"a": "Iris scan",
			"b": "Retinal scan",
			"c": "Facial recognition scan",
			"d": "Signature kinetics scan"
		}
	},
	{
		"question": "You have successfully gained access to a Linux server and would like to ensure that the succeeding outgoing traffic from this server will not be caught by Network-Based Intrusion Detection Systems (NIDS).\nWhat is the best way to evade the NIDS?",
		"num": "783",
		"correct_answer": "c",
		"answers": {
			"a": "Out of band signaling",
			"b": "Protocol Isolation",
			"c": "Encryption",
			"d": "Alternate Data Streams"
		}
	},
	{
		"question": "A consultant has been hired by the V.P. of a large financial organization to assess the company's security posture.\nDuring the security testing, the consultant comes across child pornography on the V.P. 's computer.\nWhat is the consultant's obligation to the financial organization?",
		"num": "784",
		"correct_answer": "b",
		"answers": {
			"a": "Say nothing and continue with the security testing.",
			"b": "Stop work immediately and contact the authorities.",
			"c": "Delete the pornography, say nothing, and continue security testing.",
			"d": "Bring the discovery to the financial organization's human resource department."
		}
	},
	{
		"question": "Bill is a security analyst for his company.\nAll the switches used in the company's office are Cisco switches.\nBill wants to make sure all switches are safe from ARP poisoning.\nHow can Bill accomplish this?",
		"num": "785",
		"correct_answer": "a",
		"answers": {
			"a": "Bill can use the command: ip dhcp snooping.",
			"b": "Bill can use the command: no ip snoop.",
			"c": "Bill could use the command: ip arp no flood.",
			"d": "He could use the command: ip arp no snoop."
		}
	},
	{
		"question": "Which of the following will perform an Xmas scan using NMAP?",
		"num": "786",
		"correct_answer": "c",
		"answers": {
			"a": "nmap -sA 192.168.1.254",
			"b": "nmap -sP 192.168.1.254",
			"c": "nmap -sX 192.168.1.254",
			"d": "nmap -sV 192.168.1.254"
		}
	},
	{
		"question": "During a penetration test, a tester finds a target that is running MS SQL 2000 with default credentials.\nThe tester assumes that the service is running with Local System account.\nHow can this weakness be exploited to access the system?",
		"num": "787",
		"correct_answer": "d",
		"answers": {
			"a": "Using the Metasploit psexec module setting the SA / Admin credential",
			"b": "Invoking the stored procedure xp_shell to spawn a Windows command shell",
			"c": "Invoking the stored procedure cmd_shell to spawn a Windows command shell",
			"d": "Invoking the stored procedure xp_cmdshell to spawn a Windows command shell"
		}
	},
	{
		"question": "Jesse receives an email with an attachment labeled \u201cCourt_Notice_21206.zip\u201d. Inside the zip file is a file named \u201cCourt_Notice_21206.docx.exe\u201d disguised as a word document.\nUpon execution, a window appears stating, \u201cThis word document is corrupt.\u201d. In the background, the file copies itself to Jesse APPDATA\\local directory and begins to beacon to a C2 server to download additional malicious binaries.\nWhat type of malware has Jesse encountered?",
		"num": "788",
		"correct_answer": "b",
		"answers": {
			"a": "Macro Virus",
			"b": "Trojan",
			"c": "Key-Logger",
			"d": "Worm"
		}
	},
	{
		"question": "This tool is an 802.11 WEP and WPA-PSK keys cracking program that can recover keys once enough data packets have been captured.\nIt implements the standard FMS attack along with some optimizations like KoreK attacks, as well as the PTW attack, thus making the attack much faster compared to other WEP cracking tools.\nWhich of the following tools is being described?",
		"num": "789",
		"correct_answer": "d",
		"answers": {
			"a": "wificracker",
			"b": "Airguard",
			"c": "WLAN-crack",
			"d": "Aircrack-ng"
		}
	},
	{
		"question": "Firewalls are categorized into two; namely hardware firewall and software firewall.\nIdentify the correct statement for a software firewall.\n",
		"num": "790",
		"correct_answer": "d",
		"answers": {
			"a": "Software firewall is placed between the desktop and the software components of the operating system",
			"b": "Software firewall is placed between the router and the networking components of the operating system",
			"c": "Software firewall is placed between the anti-virus application and the IDS components of the operating system",
			"d": "Software firewall is placed between the normal application and the networking components of the operating system"
		}
	},
	{
		"question": "This TCP flag instructs the sending system to transmit all buffered data immediately.",
		"num": "791",
		"correct_answer": "c",
		"answers": {
			"a": "SYN",
			"b": "RST",
			"c": "PSH",
			"d": "URG",
			"e": "FIN"
		}
	},
	{
		"question": "A Security Engineer at a medium-sized accounting firm has been tasked with discovering how much information can be obtained from the firm's public facing web servers.\nThe engineer decides to start by using netcat to port 80.\nThe engineer receives this output: \n\nHTTP/1.1 200 OK\nServer: Microsoft-IIS/6\nExpires: Tue, 17 Jan 2011 01:41:33 GMT\nContent-Type.text/html\nAccept-Ranges: bytes\nLast-Modified Wed, 28 Dec 2010 15:32:21 GMT\nETaG. \"b0aac0542e25c31:89d\"\nContent-Length: 7369\n\nWhich of the following is an example of what the engineer performed?",
		"num": "792",
		"correct_answer": "b",
		"answers": {
			"a": "Cross-site scripting",
			"b": "Banner grabbing",
			"c": "SQL injection",
			"d": "Whois database query"
		}
	},
	{
		"question": "If an attacker's computer sends an IPID of 24333 to a zombie (Idle Scanning) computer on a closed port, what will be the response?",
		"num": "793",
		"correct_answer": "a",
		"answers": {
			"a": "The zombie computer will respond with an IPID of 24334.",
			"b": "The zombie computer will respond with an IPID of 24333.",
			"c": "The zombie computer will not send a response.",
			"d": "The zombie computer will respond with an IPID of 24335."
		}
	},
	{
		"question": "You have successfully gained access to your client's internal network and successfully comprised a Linux server which is part of the internal IP network.\nYou want to know which Microsoft Windows workstations have file sharing enabled.\nWhich port would you see listening on these Windows machines in the network?",
		"num": "794",
		"correct_answer": "d",
		"answers": {
			"a": "1433",
			"b": "161",
			"c": "3389",
			"d": "445"
		}
	},
	{
		"question": "Enumeration is defined as the process of extracting user names, machine names, network resources, shares, and services from a system.\nWhich of the following command can be used in UNIX environment to enumerate the shared directories on a machine?",
		"num": "795",
		"correct_answer": "a",
		"answers": {
			"a": "showmount",
			"b": "finger",
			"c": "rpcinfo",
			"d": "rpcclient"
		}
	},
	{
		"question": "Which types of detection methods are employed by Network Intrusion Detection Systems (NIDS)?\n\nChoose two answers.",
		"num": "796",
		"correct_answer": "ab",
		"answers": {
			"a": "Signature",
			"b": "Anomaly",
			"c": "Passive",
			"d": "Reactive"
		}
	},
	{
		"question": "True or false, Steganalysis detection performance is specified by the receiver operating characteristic or OC curve. The Operating Characteristic (OC) curve is the\nprobability of detection versus the cumulative distribution.",
		"num": "797",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "When creating a security program, which approach would be used if senior management is supporting and enforcing the security policy?",
		"num": "798",
		"correct_answer": "b",
		"answers": {
			"a": "A bottom-up approach",
			"b": "A top-down approach",
			"c": "A senior creation approach",
			"d": "An IT assurance approach"
		}
	},
	{
		"question": "How does a denial-of-service attack work?",
		"num": "799",
		"correct_answer": "a",
		"answers": {
			"a": "A hacker prevents a legitimate user (or group of users) from accessing a service",
			"b": "A hacker uses every character, word, or letter he or she can think of to defeat authentication",
			"c": "A hacker tries to decipher a password by using a system, which subsequently crashes the network",
			"d": "A hacker attempts to imitate a legitimate user by confusing a computer or even another person"
		}
	},
	{
		"question": "Which of the following type of scanning utilizes automated process of proactively identifying vulnerabilities of the computing systems present on a network?",
		"num": "800",
		"correct_answer": "d",
		"answers": {
			"a": "Port Scanning",
			"b": "Single Scanning",
			"c": "External Scanning",
			"d": "Vulnerability Scanning"
		}
	},
	{
		"question": "RSA is a public-key cryptosystem developed by MIT professors Ronald L.Rivest, Adi Shamir, and Leonard M.Adleman in 1977 in an effort to help ensure Internet security.\nRSA uses modular arithmetic and elementary number theory to do computations using two very large prime numbers.\nIdentify the statement which is true for RC6 algorithm:",
		"num": "801",
		"correct_answer": "b",
		"answers": {
			"a": "Is a variable key-size stream cipher with byte-oriented operations and is based on the use of a random permutation",
			"b": "Includes integer multiplication and the use of four 4-bit working registers",
			"c": "Is a parameterized algorithm with a variable block size, key size, and a variable number of rounds",
			"d": "Is a 64 bit block cipher that uses a key length that can vary between 32 and 448 bits"
		}
	},
	{
		"question": "The Open Web Application Security Project (OWASP) is the worldwide not- for-profit charitable organization focused on improving the security of software.\nWhat item is the primary concern on OWASP's Top Ten Project Most Critical Web Application Security Risks?",
		"num": "802",
		"correct_answer": "c",
		"answers": {
			"a": "Cross Site Scripting",
			"b": "Cross Site Request Forgery",
			"c": "Injection",
			"d": "Path disclosure"
		}
	},
	{
		"question": "Attackers footprint target Websites using Google Hacking techniques. Google hacking is a term that refers to the art of creating complex search engine queries. It detects websites that are vulnerable to numerous exploits and vulnerabilities. Google operators are used to locate specific strings of text within the search results.\nThe configuration file contains both a username and a password for an SQL database. Most sites with forums run a PHP message base. This file gives you the keys to that forum, including FULL ADMIN access to the database. WordPress uses config.php that stores the database \n sername and Password.\nWhich of the below Google search string brings up sites with \"config.php\" files?",
		"num": "803",
		"correct_answer": "c",
		"answers": {
			"a": "Search:index config/php",
			"b": "Wordpress:index config.php",
			"c": "intitle:index.of config.php",
			"d": "Config.php:index list"
		}
	},
	{
		"question": "Which command line switch would be used in NMAP to perform operating system detection?",
		"num": "804",
		"correct_answer": "d",
		"answers": {
			"a": "-OS",
			"b": "-sO",
			"c": "-sP",
			"d": "-O"
		}
	},
	{
		"question": "Employees in a company are no longer able to access Internet web sites on their computers.\nThe network administrator is able to successfully ping IP address of web servers on the Internet and is able to open web sites by using an IP address in place of the URL.\nThe administrator runs the nslookup command for www.\neccouncil.\norg and receives an error message stating there is no response from the server.\nWhat should the administrator do next?",
		"num": "805",
		"correct_answer": "a",
		"answers": {
			"a": "Configure the firewall to allow traffic on TCP ports 53 and UDP port 53.",
			"b": "Configure the firewall to allow traffic on TCP ports 80 and UDP port 443.",
			"c": "Configure the firewall to allow traffic on TCP port 53.",
			"d": "Configure the firewall to allow traffic on TCP port 8080."
		}
	},
	{
		"question": "Which of the following are advantages of adopting a Single Sign On (SSO) system? (Choose two.)",
		"num": "806",
		"correct_answer": "ac",
		"answers": {
			"a": "A reduction in password fatigue for users because they do not need to know multiple passwords when accessing multiple applications",
			"b": "A reduction in network and application monitoring since all recording will be completed at the SSO system",
			"c": "A reduction in system administration overhead since any user login problems can be resolved at the SSO system",
			"d": "A reduction in overall risk to the system since network and application attacks can only happen at the SSO point"
		}
	},
	{
		"question": "An attacker gains access to a Web server's database and displays the contents of the table that holds all of the names, passwords, and other user information. The attacker did this by entering information into the Web site's user login page that the software's designers did not expect to be entered. This is an example of what kind of software design problem/issue?",
		"num": "807",
		"correct_answer": "b",
		"answers": {
			"a": "Insufficient firewall rules",
			"b": "Insufficient input validation",
			"c": "Insufficient exception handling",
			"d": "Insufficient anti-virus detection"
		}
	},
	{
		"question": "Which of the following program infects the system boot sector and the executable files at the same time?",
		"num": "808",
		"correct_answer": "d",
		"answers": {
			"a": "Stealth virus",
			"b": "Polymorphic virus",
			"c": "Macro virus",
			"d": "Multipartite Virus"
		}
	},
	{
		"question": "Information may be hidden into the slack space of a file.",
		"num": "809",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "In both pharming and phishing attacks an attacker can create websites that look similar to legitimate sites with the intent of collecting personal identifiable information from its victims.\nWhat is the difference between pharming and phishing attacks?",
		"num": "810",
		"correct_answer": "b",
		"answers": {
			"a": "Both pharming and phishing attacks are identical.",
			"b": "In a pharming attack a victim is redirected to a fake website by modifying their host configuration file or by exploiting vulnerabilities in DNS. In a phishing attack an attacker provides the victim with a URL that is either misspelled or looks similar to the actual websites domain name.",
			"c": "In a phishing attack a victim is redirected to a fake website by modifying their host configuration file or by exploiting vulnerabilities in DNS. In a phishing attack an attacker provides the victim with a URL that is either misspelled or looks similar to the actual websites domain name.",
			"d": "Both pharming and phishing attacks are purely technical and are not considered forms of social engineering"
		}
	},
	{
		"question": "Which of the following is considered the best way to protect Personally Identifiable Information (PII) from Web application vulnerabilities?",
		"num": "811",
		"correct_answer": "c",
		"answers": {
			"a": "Use a security token to log into all Web applications that use PII",
			"b": "Use full disk encryption on all hard drives to protect PII",
			"c": "Use encrypted communications protocols to transmit PII",
			"d": "Store all PII in encrypted format"
		}
	},
	{
		"question": "StackGuard can use the value of \"0\" as the canary value even though it is easily guessed by the attacker.",
		"num": "812",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "What is the process of logging, recording, and resolving events that take place in an organization?",
		"num": "813",
		"correct_answer": "c",
		"answers": {
			"a": "Security Policy",
			"b": "Internal Procedure",
			"c": "Incident Management Process",
			"d": "Metrics"
		}
	},
	{
		"question": "How do you defend against ARP Poisoning attack? (Select 2 answers)",
		"num": "814",
		"correct_answer": "ac",
		"answers": {
			"a": "Enable DHCP Snooping Binding Table",
			"b": "Restrict ARP Duplicates",
			"c": "Enable Dynamic ARP Inspection",
			"d": "Enable MAC snooping Table"
		}
	},
	{
		"question": "When comparing the testing methodologies of Open Web Application Security Project (OWASP) and Open Source Security Testing Methodology Manual (OSSTMM) the main difference is",
		"num": "815",
		"correct_answer": "d",
		"answers": {
			"a": "OWASP is for web applications and OSSTMM does not include web applications.",
			"b": "OSSTMM is gray box testing and OWASP is black box testing.",
			"c": "OWASP addresses controls and OSSTMM does not.",
			"d": "OSSTMM addresses controls and OWASP does not."
		}
	},
	{
		"question": "Which of the following security operations is used for determining the attack surface of an organization?",
		"num": "816",
		"correct_answer": "d",
		"answers": {
			"a": "Using configuration management to determine when and where to apply security patches",
			"b": "Training employees on the security policy regarding social engineering",
			"c": "Reviewing the need for a security clearance for each employee",
			"d": "Running a network scan to detect network services in the corporate DMZ"
		}
	},
	{
		"question": "What is the purpose of a demilitarized zone on a network?",
		"num": "817",
		"correct_answer": "b",
		"answers": {
			"a": "To scan all traffic coming through the DMZ to the internal network",
			"b": "To only provide direct access to the nodes within the DMZ and protect the network behind it",
			"c": "To provide a place to put the honeypot",
			"d": "To contain the network devices you wish to protect"
		}
	},
	{
		"question": "SSL has been seen as the solution to a lot of common security problems.\nAdministrator will often make use of SSL to encrypt communications from points A to point B.\nWhy do you think this could be a bad idea if there is an Intrusion Detection System deployed to monitor the traffic between point A and B?",
		"num": "818",
		"correct_answer": "d",
		"answers": {
			"a": "SSL is redundant if you already have IDS's in place",
			"b": "SSL will trigger rules at regular interval and force the administrator to turn them off",
			"c": "SSL will slow down the IDS while it is breaking the encryption to see the packet content",
			"d": "SSL will blind the content of the packet and Intrusion Detection Systems will not be able to detect them"
		}
	},
	{
		"question": "IP spoofing refers to the procedure of an attacker changing his or her IP address so that he or she appears to be someone else.\n\nWhich of the following IP spoofing detection technique succeed only when the attacker is in a different subnet?",
		"num": "819",
		"correct_answer": "a",
		"answers": {
			"a": "Direct TTL probes technique",
			"b": "IP identification number technique",
			"c": "TCP flow control method ",
			"d": "UDP flow control method"
		}
	},
	{
		"question": "What is the best defense against privilege escalation vulnerability?",
		"num": "820",
		"correct_answer": "c",
		"answers": {
			"a": "Patch systems regularly and upgrade interactive login privileges at the system administrator level.",
			"b": "Run administrator and applications on least privileges and use a content registry for tracking.",
			"c": "Run services with least privileged accounts and implement multi-factor authentication and authorization.",
			"d": "Review user roles and administrator privileges for maximum utilization of automation services."
		}
	},
	{
		"question": "A regional bank hires your company to perform a security assessment on their network after a recent data breach.\nThe attacker was able to steal financial data from the bank by compromising only a single server.\nBased on this information, what should be one of your key recommendations to the bank?",
		"num": "821",
		"correct_answer": "d",
		"answers": {
			"a": "Require all employees to change their anti-virus program with a new one",
			"b": "Move the financial data to another server on the same IP subnet",
			"c": "Issue new certificates to the web servers from the root certificate authority",
			"d": "Place a front-end web server in a demilitarized zone that only handles external web traffic"
		}
	},
	{
		"question": "Which tool allows analysts and pen testers to examine links between data using graphs and link analysis?",
		"num": "822",
		"correct_answer": "c",
		"answers": {
			"a": "Wireshark",
			"b": "Cain & Abel",
			"c": "Maltego",
			"d": "Metasploit"
		}
	},
	{
		"question": "Every company needs a formal written document which spells out to employees precisely what they are allowed to use the company's systems for, what is prohibited, and what will happen to them if they break the rules.\nTwo printed copies of the policy should be given to every employee as soon as possible after they join the organization.\nThe employee should be asked to sign one copy, which should be safely filed by the company.\nNo one should be allowed to use the company's computer systems until they have signed the policy in acceptance of its terms.\nWhat is this document called?",
		"num": "823",
		"correct_answer": "b",
		"answers": {
			"a": "Information Audit Policy (IAP)",
			"b": "Information Security Policy (ISP)",
			"c": "Penetration Testing Policy (PTP)",
			"d": "Company Compliance Policy (CCP)"
		}
	},
	{
		"question": "Most cases of insider abuse can be traced to individuals who are introverted, incapable of dealing with stress or conflict, and frustrated with their job, office politics, and lack of respect or promotion. Disgruntled employees may pass company secrets and intellectual property to competitors for monitory benefits. Here are some of the symptoms of a disgruntled employee:\n\nThese disgruntled employees are the biggest threat to enterprise security. How do you deal with these\nthreats? (Select 2 answers)",
		"num": "824",
		"correct_answer": "bc",
		"answers": {
			"a": "Frequently leaves work early, arrive late or call in sick",
			"b": "Spends time surfing the Internet or on the phone",
			"c": "Responds in a confrontational, angry, or overly aggressive way to simple requests or comments",
			"d": "Always negative; finds fault with everything",
			"e": "Limit access to the applications they can run on their desktop computers and enforce strict work hour rules",
			"f": "By implementing Virtualization technology from the desktop to the data centre, organizations can isolate different environments with varying levels of access and security to various employees",
			"g": "Organizations must ensure that their corporate data is centrally managed and delivered to users just and when needed"
		}
	},
	{
		"question": "Which of the following are valid types of rootkits? (Choose three.)",
		"num": "825",
		"correct_answer": "acd",
		"answers": {
			"a": "Hypervisor level",
			"b": "Network level",
			"c": "Kernel level",
			"d": "Application level",
			"e": "Physical level",
			"f": "Data access level"
		}
	},
	{
		"question": "Nmap is a free open source utility, which is designed to rapidly scan large networks.\nIdentify the Nmap Scan method that is often referred to as half open scan because it does not open a full TCP connection.\n",
		"num": "826",
		"correct_answer": "b",
		"answers": {
			"a": "ACK Scan",
			"b": "SYN Stealth",
			"c": "Rapid Scan",
			"d": "Windows Scan"
		}
	},
	{
		"question": "When you return to your desk after a lunch break, you notice a strange email in your inbox.\nThe sender is someone you did business with recently, but the subject line has strange characters in it.\nWhat should you do?",
		"num": "827",
		"correct_answer": "a",
		"answers": {
			"a": "Forward the message to your company\u2019s security response team and permanently delete the message from your computer.",
			"b": "Reply to the sender and ask them for more information about the message contents.",
			"c": "Delete the email and pretend nothing happened.",
			"d": "Forward the message to your supervisor and ask for her opinion on how to handle the situation."
		}
	},
	{
		"question": "To reduce the attack surface of a system, administrators should perform which of the following processes to remove unnecessary software, services, and insecure configuration settings?",
		"num": "828",
		"correct_answer": "c",
		"answers": {
			"a": "Harvesting",
			"b": "Windowing",
			"c": "Hardening",
			"d": "Stealthing"
		}
	},
	{
		"question": "You are doing a pen test against an organization that has just recovered from a major cyber-attack. The CISO and CIO want to completely and totally eliminate risk.\nWhat is one of the first things you should explain to these individuals?",
		"num": "829",
		"correct_answer": "a",
		"answers": {
			"a": "Explain that you cannot eliminate all risk but you will be able to reduce risk to acceptable levels.",
			"b": "Explain to them that they need to buy more services.",
			"c": "Tell him everything is going to a ok and collect that check!",
			"d": "Start the Wireshark application to sniff traffic"
		}
	},
	{
		"question": "Why attackers use proxy servers?",
		"num": "830",
		"correct_answer": "d",
		"answers": {
			"a": "To ensure the exploits used in the attacks always flip reverse vectors",
			"b": "Faster bandwidth performance and increase in attack speed",
			"c": "Interrupt the remote victim's network traffic and reroute the packets to attackers machine",
			"d": "To hide the source IP address so that an attacker can hack without any legal corollary"
		}
	},
	{
		"question": "For messages sent through an insecure channel, a properly implemented digital signature gives the receiver reason to believe the message was sent by the claimed sender.\nWhile using a digital signature, the message digest is encrypted with which key?",
		"num": "831",
		"correct_answer": "d",
		"answers": {
			"a": "Sender's public key",
			"b": "Receiver's private key",
			"c": "Receiver's public key",
			"d": "Sender's private key"
		}
	},
	{
		"question": "A company's Web development team has become aware of a certain type of security vulnerability in their Web software.\nTo mitigate the possibility of this vulnerability being exploited, the team wants to modify the software requirements to disallow users from entering HTML as input into their Web application.\nWhat kind of Web application vulnerability likely exists in their software?",
		"num": "832",
		"correct_answer": "a",
		"answers": {
			"a": "Cross-site scripting vulnerability",
			"b": "Session management vulnerability ",
			"c": "SQL injection vulnerability",
			"d": "Cross-site Request Forgery vulnerability"
		}
	},
	{
		"question": "During a routine assessment you discover information that suggests the customer is involved in human trafficking.",
		"num": "833",
		"correct_answer": "b",
		"answers": {
			"a": "Ignore the data complete the job collect a check. Keep it moving!",
			"b": "Immediately stop work and contact the proper legal authorities",
			"c": "Copy the data to a thumb drive and keep it as leverage.",
			"d": "Confront the client in a respectful manner and ask about the data"
		}
	},
	{
		"question": "Jake works as a system administrator at Acme Corp. Jason, an accountant of the firm befriends him at the\ncanteen and tags along with him on the pretext of appraising him about potential tax benefits. Jason waits\nfor Jake to swipe his access card and follows him through the open door into the secure systems area. How\nwould you describe Jason's behavior within a security context?",
		"num": "834",
		"correct_answer": "c",
		"answers": {
			"a": "Smooth Talking",
			"b": "Swipe Gating",
			"c": "Tailgating",
			"d": "Trailing"
		}
	},
	{
		"question": "A simple compiler technique used by programmers is to add a terminator 'canary word' containing four letters NULL (0x00), CR (0x0d), LF (0x0a) and EOF (0xff) so that most string operations are terminated.\nIf the canary word has been altered when the function returns, and the program responds by emitting an intruder alert into syslog, and then halts what does it indicate?",
		"num": "835",
		"correct_answer": "a",
		"answers": {
			"a": "A buffer overflow attack has been attempted",
			"b": "A buffer overflow attack has already occurred",
			"c": "A firewall has been breached and this is logged",
			"d": "An intrusion detection system has been triggered",
			"e": "The system has crashed"
		}
	},
	{
		"question": "Which of the following is assured by the use of a hash?",
		"num": "836",
		"correct_answer": "d",
		"answers": {
			"a": "Authentication",
			"b": "Confidentially",
			"c": "Availability",
			"d": "Integrity"
		}
	},
	{
		"question": "Wi-Fi Protected Access (WPA) is a data encryption method for WLANs based on 802.11 standards. It improves on the authentication and encryption features of WEP (Wired Equivalent Privacy). Temporal Key Integrity Protocol (TKIP) enhances WEP by adding a rekeying mechanism to provide fresh encryption and integrity keys. Temporal keys are changed for every ___________.",
		"num": "837",
		"correct_answer": "c",
		"answers": {
			"a": "1,000 packets",
			"b": "5,000 packets",
			"c": "10,000 packets",
			"d": "15,000 packets"
		}
	},
	{
		"question": "The tool 'snow' is a steganography tool.",
		"num": "838",
		"correct_answer": "a",
		"answers": {
			"a": "whitespace",
			"b": "blackspace",
			"c": "deep",
			"d": "deadspace"
		}
	},
	{
		"question": "Web servers are often the most targeted and attacked hosts on organizations' networks.\nAttackers may exploit software bugs in the Web server, underlying operating system, or active content to gain unauthorized access.\nIdentify the correct statement related to the above Web Server installation?",
		"num": "839",
		"correct_answer": "c",
		"answers": {
			"a": "Lack of proper security policy, procedures and maintenance",
			"b": "Bugs in server software, OS and web applications",
			"c": "Installing the server with default settings",
			"d": "Unpatched security flaws in the server software, OS and applications"
		}
	},
	{
		"question": "Which of the following methods would help best in preventing the malicious steganography?",
		"num": "840",
		"correct_answer": "d",
		"answers": {
			"a": "Routine server analysis",
			"b": "Specialized training",
			"c": "Hiring of internal developers",
			"d": "Policy that restricts installation of unauthorized programs on company's computers"
		}
	},
	{
		"question": "Which of the following does proper basic configuration of snort as a network intrusion detection system require?",
		"num": "841",
		"correct_answer": "a",
		"answers": {
			"a": "Limit the packets captured to the snort configuration file.",
			"b": "Capture every packet on the network segment.",
			"c": "Limit the packets captured to a single segment.",
			"d": "Limit the packets captured to the /var/log/snort directory."
		}
	},
	{
		"question": "ViruXine.W32 virus hides their presence by changing the underlying executable code.\nThis Virus code mutates while keeping the original algorithm intact, the code changes itself each time it runs, but the function of the code (its semantics) will not change at all.\n\nWhat is this technique called?",
		"num": "842",
		"correct_answer": "a",
		"answers": {
			"a": "Polymorphic Virus",
			"b": "Metamorphic Virus",
			"c": "Dravidic Virus",
			"d": "Stealth Virus"
		}
	},
	{
		"question": "Which of the following languages are the primary targets of cross-site scripting? (Choose two.)",
		"num": "843",
		"correct_answer": "ad",
		"answers": {
			"a": "HTML",
			"b": "SQL",
			"c": "XSLT",
			"d": "Javascript"
		}
	},
	{
		"question": "What is the correct PCAP filter to capture all TCP traffic going to or from host 192.168.0.125 on port 25?",
		"num": "844",
		"correct_answer": "d",
		"answers": {
			"a": "tcp.src == 25 and ip.host == 192.168.0.125",
			"b": "host 192.168.0.125:25",
			"c": "port 25 and host 192.168.0.125",
			"d": "tcp.port == 25 and ip.host == 192.168.0.125"
		}
	},
	{
		"question": "Which of the following encryption is NOT based on block cipher?",
		"num": "845",
		"correct_answer": "d",
		"answers": {
			"a": "DES",
			"b": "Blowfish",
			"c": "AES (Rijndael)",
			"d": "RC4"
		}
	},
	{
		"question": "Some viruses affect computers as soon as their code is executed; other viruses lie dormant until a pre-determined logical circumstance is met.\nIdentify the virus that modifies the directory table entries so that directory entries point to the virus code instead of the actual program.\n",
		"num": "846",
		"correct_answer": "b",
		"answers": {
			"a": "Macro Viruses",
			"b": "Cluster Viruses",
			"c": "Encryption Viruses",
			"d": "Boot Sector Viruses"
		}
	},
	{
		"question": "An IT employee got a call from one our best customers.\nThe caller wanted to know about the company\u2019s network infrastructure, systems, and team.\nNew opportunities of integration are in sight for both company and customer.\nWhat should this employee do?",
		"num": "847",
		"correct_answer": "c",
		"answers": {
			"a": "The employee can not provide any information: but, anyway, he/she will provide the name of the person in charge",
			"b": "Since the company\u2019s policy is all about Customer Service. he/she will provide information",
			"c": "The employee should not provide any information without previous management authorization",
			"d": "Disregarding the call, the employee should hang up"
		}
	},
	{
		"question": "An NMAP scan of a server shows port 69 is open.\nWhat risk could this pose?",
		"num": "848",
		"correct_answer": "a",
		"answers": {
			"a": "Unauthenticated access",
			"b": "Weak SSL version",
			"c": "Cleartext login",
			"d": "Web portal data leak"
		}
	},
	{
		"question": "What technique is used to ensure a buffer overflow will successfully execute the desired code by creating a padding in memory?",
		"num": "849",
		"correct_answer": "a",
		"answers": {
			"a": "NOP sled",
			"b": "Heap sled",
			"c": "Heap spray"
		}
	},
	{
		"question": "Wireless antenna is an electrical device which converts electric currents into radio waves, and vice versa.\nWhich of the following antenna used in wireless base stations and provides a 360 degree horizontal radiation pattern?",
		"num": "850",
		"correct_answer": "a",
		"answers": {
			"a": "Omnidirectional antenna",
			"b": "Parabolic grid antenna",
			"c": "Yagi antenna",
			"d": "Dipole antenna"
		}
	},
	{
		"question": "The SNMP Read-Only Community String is like a password.\nThe string is sent along with each SNMP Get- Request and allows (or denies) access to a device.\nMost network vendors ship their equipment with a default password of \"public\".\nThis is the so-called \"default public community string\".\nHow would you keep intruders from getting sensitive information regarding the network devices using SNMP?\n(Select 2 answers)",
		"num": "851",
		"correct_answer": "ac",
		"answers": {
			"a": "Enable SNMPv3 which encrypts username/password authentication",
			"b": "Use your company name as the public community string replacing the default 'public'",
			"c": "Enable IP filtering to limit access to SNMP device",
			"d": "The default configuration provided by device vendors is highly secure and you don't need to change anything"
		}
	},
	{
		"question": "Which method is used where a stego is sent in information embedded within normal traffic?",
		"num": "852",
		"correct_answer": "a",
		"answers": {
			"a": "Covert channels",
			"b": "Encryption",
			"c": "Hidden directory",
			"d": "Cipher text"
		}
	},
	{
		"question": "Bob learned that his username and password for a popular game has been compromised.\nHe contacts the company and resets all the information.\nThe company suggests he use two-factor authentication; which option below offers that?",
		"num": "853",
		"correct_answer": "a",
		"answers": {
			"a": "A fingerprint scanner and his username and password",
			"b": "His username and a stronger password",
			"c": "A new username and password",
			"d": "Disable his username and use just a fingerprint scanner"
		}
	},
	{
		"question": "Your team has won a contract to infiltrate an organization.\nThe company wants to have the attack be as realistic as possible; therefore, they did not provide any information besides the company name.\nWhat should be the first step in security testing the client?",
		"num": "854",
		"correct_answer": "a",
		"answers": {
			"a": "Reconnaissance",
			"b": "Escalation",
			"c": "Scanning",
			"d": "Enumeration"
		}
	},
	{
		"question": "Bob waits near a secured door, holding a box. He waits until an employee walks up to the secured door and\nuses the special card in order to access the restricted area of the target company. Just as the employee\nopens the door, Bob walks up to the employee (still holding the box) and asks the employee to hold the\ndoor open so that he can enter. What is the best way to undermine the social engineering activity of\ntailgating?\n\n",
		"num": "855",
		"correct_answer": "b",
		"answers": {
			"a": "Issue special cards to access secure doors at the company and provide a one-time only brief description of use of the special card",
			"b": "Educate and enforce physical security policies of the company to all the employees on a regular basis",
			"c": "Setup a mock video camera next to the special card reader adjacent to the secure door",
			"d": "Post a sign that states, \"no tailgating\" next to the special card reader adjacent to the secure door"
		}
	},
	{
		"question": "A majority of attacks come from insiders, people who have direct access to a company's computer system as part of their job function or a business relationship.\nWho is considered an insider?",
		"num": "856",
		"correct_answer": "b",
		"answers": {
			"a": "A competitor to the company because they can directly benefit from the publicity generated by making such an attack",
			"b": "Disgruntled employee, customers, suppliers, vendors, business partners, contractors, temps, and consultants",
			"c": "The CEO of the company because he has access to all of the computer systems",
			"d": "A government agency since they know the company's computer system strengths and weaknesses"
		}
	},
	{
		"question": "A well-intentioned researcher discovers a vulnerability on the web site of a major corporation.\nWhat should he do?",
		"num": "857",
		"correct_answer": "d",
		"answers": {
			"a": "Try to sell the information to a well-paying party on the dark web.",
			"b": "Exploit the vulnerability without harming the web site owner so that attention be drawn to the problem.",
			"c": "Ignore it.",
			"d": "Notify the web site owner so that corrective action be taken as soon as possible to patch the vulnerability."
		}
	},
	{
		"question": "Which of the following techniques does a vulnerability scanner use in order to detect a vulnerability on a target service?",
		"num": "858",
		"correct_answer": "d",
		"answers": {
			"a": "Port scanning",
			"b": "Banner grabbing",
			"c": "Injecting arbitrary data",
			"d": "Analyzing service response"
		}
	},
	{
		"question": "An IT employee got a call from one of our best customers.\nThe caller wanted to know about the company's network infrastructure, systems, and team.\nNew opportunities of integration are in sight for both company and customer.\nWhat should this employee do?",
		"num": "859",
		"correct_answer": "d",
		"answers": {
			"a": "The employees cannot provide any information; but, anyway, he/she will provide the name of the person in charge.",
			"b": "Since the company's policy is all about Customer Service, he/she will provide information.",
			"c": "Disregarding the call, the employee should hang up.",
			"d": "The employee should not provide any information without previous management authorization."
		}
	},
	{
		"question": "When using Wireshark to acquire packet capture on a network, which device would enable the capture of all traffic on the wire?",
		"num": "860",
		"correct_answer": "a",
		"answers": {
			"a": "Network tap",
			"b": "Layer 3 switch",
			"c": "Network bridge",
			"d": "Application firewall"
		}
	},
	{
		"question": "What is a \"Collision attack\" in cryptography?",
		"num": "861",
		"correct_answer": "b",
		"answers": {
			"a": "Collision attacks try to get the public key",
			"b": "Collision attacks try to find two inputs producing the same hash.",
			"c": "Collision attacks try to break the hash into two parts, with the same bytes in each part to get the private key.",
			"d": "Collision attacks try to break the hash into three parts to get the plaintext value."
		}
	},
	{
		"question": "Which tool can be used to silently copy files from USB devices?",
		"num": "862",
		"correct_answer": "b",
		"answers": {
			"a": "USB Grabber",
			"b": "USB Dumper",
			"c": "USB Sniffer",
			"d": "USB Snoopy"
		}
	},
	{
		"question": "What is the role of test automation in security testing?",
		"num": "863",
		"correct_answer": "d",
		"answers": {
			"a": "It is an option but it tends to be very expensive.",
			"b": "It should be used exclusively. Manual testing is outdated because of low spend and possible test setup inconsistencies.",
			"c": "Test automation is not usable in security due to the complexity of the tests.",
			"d": "It can accelerate benchmark tests and repeat them with a consistent test setup. But it cannot replace manual testing completely."
		}
	},
	{
		"question": "The \"black box testing\" methodology enforces which kind of restriction?",
		"num": "864",
		"correct_answer": "c",
		"answers": {
			"a": "Only the internal operation of a system is known to the tester.",
			"b": "The internal operation of a system is only partly accessible to the tester.",
			"c": "Only the external operation of a system is accessible to the tester.",
			"d": "The internal operation of a system is completely known to the tester."
		}
	},
	{
		"question": "A common technique for luring e-mail users into opening virus-launching attachments is to send messages\nthat would appear to be relevant or important to many of their potential recipients. One way of\naccomplishing this feat is to make the virus-carrying messages appear to come from some type of business\nentity retailing sites, UPS, FEDEX, CITIBANK or a major provider of a common service.\nHere is a fraudulent e-mail claiming to be from FedEx regarding a package that could not be delivered. This\nmail asks the receiver to open an attachment in order to obtain the FEDEX tracking number for picking up\nthe package. The attachment contained in this type of e-mail activates a virus.\nVendors send e-mails like this to their customers advising them not to open any files attached with the mail,\nas they do not include attachments.\nFraudulent e-mail and legit e-mail that arrives in your inbox contain the fedex.com as the sender of the mail.\nHow do you ensure if the e-mail is authentic and sent from fedex.com?",
		"num": "865",
		"correct_answer": "a",
		"answers": {
			"a": "Verify the digital signature attached with the mail, the fake mail will not have Digital ID at all",
			"b": "Check the Sender ID against the National Spam Database (NSD)",
			"c": "Fake mail will have spelling/grammatical errors",
			"d": "Fake mail uses extensive images, animation and flash content"
		}
	},
	{
		"question": "SYN Flood is a DOS attack in which an attacker deliberately violates the three-way handshake and opens a large number of half-open TCP connections.\nThe signature of attack for SYN Flood contains:",
		"num": "866",
		"correct_answer": "b",
		"answers": {
			"a": "The source and destination address having the same value",
			"b": "A large number of SYN packets appearing on a network without the corresponding reply packets",
			"c": "The source and destination port numbers having the same value",
			"d": "A large number of SYN packets appearing on a network with the corresponding reply packets"
		}
	},
	{
		"question": "An attacker gains access to a Web server's database and displays the contents of the table that holds all of the names, passwords, and other user information.\nThe attacker did this by entering information into the Web site's user login page that the software's designers did not expect to be entered.\nThis is an example of what kind of software design problem?",
		"num": "867",
		"correct_answer": "c",
		"answers": {
			"a": "Insufficient security management",
			"b": "Insufficient exception handling",
			"c": "Insufficient database hardening",
			"d": "Insufficient input validation"
		}
	},
	{
		"question": "IP spoofing refers to the procedure of an attacker changing his or her IP address so that he or she appears to be someone else.\nWhich of the following IP spoofing detection technique succeed only when the attacker is in a different subnet?",
		"num": "868",
		"correct_answer": "a",
		"answers": {
			"a": "Direct TTL probes technique",
			"b": "IP identification number technique",
			"c": "TCP flow control method",
			"d": "UDP flow control method"
		}
	},
	{
		"question": "Diffie-Hellman (DH) groups determine the strength of the key used in the key exchange process.\nWhich of the following is the correct bit size of the Diffie-Hellman (DH) group 5?",
		"num": "869",
		"correct_answer": "c",
		"answers": {
			"a": "768 bit key",
			"b": "1025 bit key",
			"c": "1536 bit key",
			"d": "2048 bit key"
		}
	},
	{
		"question": "On performing a risk assessment, you need to determine the potential impacts when some of the critical business process of the company interrupt its service.\nWhat is the name of the process by which you can determine those critical business?",
		"num": "870",
		"correct_answer": "d",
		"answers": {
			"a": "Risk Mitigation",
			"b": "Emergency Plan Response (EPR)",
			"c": "Disaster Recovery Planning (DRP)",
			"d": "Business Impact Analysis (BIA)"
		}
	},
	{
		"question": "Which of the following describes the characteristics of a Boot Sector Virus?",
		"num": "871",
		"correct_answer": "c",
		"answers": {
			"a": "Overwrites the original MBR and only executes the new virus code",
			"b": "Modifies directory table entries so that directory entries point to the virus code instead of the actual program",
			"c": "Moves the MBR to another location on the hard disk and copies itself to the original location of the MBR",
			"d": "Moves the MBR to another location on the RAM and copies itself to the original location of the MBR"
		}
	},
	{
		"question": "Sniffer turns the NIC of a system to the promiscuous mode so that it listens to all the data transmitted on its segment. It can constantly read all information entering the computer through the NIC by decoding the information encapsulated in the data packet. Passive sniffing is one of the types of sniffing. Passive sniffing refers to: ",
		"num": "872",
		"correct_answer": "a",
		"answers": {
			"a": "Sniffing through a hub",
			"b": "Sniffing through a router",
			"c": "Sniffing through a switch",
			"d": "Sniffing through a bridge"
		}
	},
	{
		"question": "A medium-sized healthcare IT business decides to implement a risk management strategy.\nWhich of the following is NOT one of the five basic responses to risk?",
		"num": "873",
		"correct_answer": "d",
		"answers": {
			"a": "Avoid",
			"b": "Mitigate",
			"c": "Accept",
			"d": "Delegate"
		}
	},
	{
		"question": "Defense-in-depth is a security strategy in which several protection layers are placed throughout an information system.\nIt helps to prevent direct attacks against an information system and data because a break in one layer only leads the attacker to the next layer.\n",
		"num": "874",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "A computer science student needs to fill some information into a secured Adobe PDF job application that was received from a prospective employer.\nInstead of requesting a new document that allowed the forms to be completed, the student decides to write a script that pulls passwords from a list of commonly used passwords to try against the secured PDF until the correct password is found or the list is exhausted.\nWhich cryptography attack is the student attempting?",
		"num": "875",
		"correct_answer": "c",
		"answers": {
			"a": "Man-in-the-middle attack",
			"b": "Brute-force attack",
			"c": "Dictionary attack",
			"d": "Session hijacking"
		}
	},
	{
		"question": "If a tester is attempting to ping a target that exists but receives no response or a response that states the destination is unreachable, ICMP may be disabled and the network may be using TCP.\nWhich other option could the tester use to get a response from a host using TCP?",
		"num": "876",
		"correct_answer": "a",
		"answers": {
			"a": "Hping",
			"b": "Traceroute",
			"c": "TCP ping",
			"d": "Broadcast ping"
		}
	},
	{
		"question": "A company has hired a security administrator to maintain and administer Linux and Windows- based systems.\nWritten in the nightly report file is the following:\n\nFirewall log files are at the expected value of 4 M The current time is 12am.\nExactly two hours later the size has decreased considerably.\nAnother hour goes by and the log files have shrunk in size again.\n\nWhich of the following actions should the security administrator take?",
		"num": "877",
		"correct_answer": "d",
		"answers": {
			"a": "Log the event as suspicious activity and report this behavior to the incident response team immediately.",
			"b": "Log the event as suspicious activity, call a manager, and report this as soon as possible.",
			"c": "Run an anti-virus scan because it is likely the system is infected by malware.",
			"d": "Log the event as suspicious activity, continue to investigate, and act according to the site's security policy."
		}
	},
	{
		"question": "Which of the following cryptographic attack refers to extraction of cryptographic secrets (e.g. the password to an encrypted file) from a person by coercion or torture?",
		"num": "878",
		"correct_answer": "d",
		"answers": {
			"a": "Ciphertext-only Attack ",
			"b": "Chosen-ciphertext Attack ",
			"c": "Adaptive Chosen-plaintext Attack ",
			"d": "Rubber Hose Attack "
		}
	},
	{
		"question": "Websites and web portals that provide web services commonly use the Simple Object Access Protocol (SOAP).\nWhich of the following is an incorrect definition or characteristics of the protocol?",
		"num": "879",
		"correct_answer": "b",
		"answers": {
			"a": "Based on XML",
			"b": "Only compatible with the application protocol HTTP",
			"c": "Exchanges data between web services",
			"d": "Provides a structured model for messaging"
		}
	},
	{
		"question": "An enterprise recently moved to a new office and the new neighborhood is a little risky.\nThe CEO wants to monitor the physical perimeter and the entrance doors 24 hours.\nWhat is the best option to do this job?",
		"num": "880",
		"correct_answer": "b",
		"answers": {
			"a": "Use fences in the entrance doors.",
			"b": "Install a CCTV with cameras pointing to the entrance doors and the street.",
			"c": "Use an IDS in the entrance doors and install some of them near the corners.",
			"d": "Use lights in all the entrance doors and along the company's perimeter."
		}
	},
	{
		"question": "Steganalysis is not the method that is used to detect stenography.",
		"num": "881",
		"correct_answer": "b",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Network Time Protocol (NTP) is designed to synchronize clocks of networked computers.\nWhich of the following port NTP uses as its primary means of communication?",
		"num": "882",
		"correct_answer": "a",
		"answers": {
			"a": "UDP port 123",
			"b": "UDP port 113",
			"c": "UDP port 161",
			"d": "UDP port 320"
		}
	},
	{
		"question": "Which of the following tools would be the best choice for achieving compliance with PCI Requirement 11?",
		"num": "883",
		"correct_answer": "c",
		"answers": {
			"a": "Truecrypt",
			"b": "Sub7",
			"c": "Nessus",
			"d": "Clamwin"
		}
	},
	{
		"question": "If the final set of security controls does not eliminate all risk in a system, what could be done next?",
		"num": "884",
		"correct_answer": "c",
		"answers": {
			"a": "Continue to apply controls until there is zero risk.",
			"b": "Ignore any remaining risk.",
			"c": "If the residual risk is low enough, it can be accepted.",
			"d": "Remove current controls since they are not completely effective."
		}
	},
	{
		"question": "Within the context of Computer Security, which of the following statements describes Social Engineering best?",
		"num": "885",
		"correct_answer": "c",
		"answers": {
			"a": "Social Engineering is the act of publicly disclosing information",
			"b": "Social Engineering is the means put in place by human resource to perform time accounting",
			"c": "Social Engineering is the act of getting needed information from a person rather than breaking into a system",
			"d": "Social Engineering is a training program within sociology studies"
		}
	},
	{
		"question": "Which of the following is the successor of SSL?",
		"num": "886",
		"correct_answer": "b",
		"answers": {
			"a": "IPSec",
			"b": "TLS",
			"c": "GRE",
			"d": "RSA"
		}
	},
	{
		"question": "Identify the web application attack where the attackers exploit vulnerabilities in dynamically generated web pages to inject client-side script into web pages viewed by other users.\n",
		"num": "887",
		"correct_answer": "b",
		"answers": {
			"a": "SQL injection attack",
			"b": "Cross-Site Scripting (XSS)",
			"c": "LDAP Injection attack",
			"d": "Cross-Site Request Forgery (CSRF)"
		}
	},
	{
		"question": "A digital signature is simply a message that is encrypted with the public key instead of the private key.",
		"num": "888",
		"correct_answer": "b",
		"answers": {
			"a": "true",
			"b": "false"
		}
	},
	{
		"question": "The security concept of \"separation of duties\" is most similar to the operation of which type of security device?",
		"num": "889",
		"correct_answer": "a",
		"answers": {
			"a": "Bastion host",
			"b": "Honeypot",
			"c": "Firewall",
			"d": "Intrusion Detection System"
		}
	},
	{
		"question": "What type of vulnerability/attack is it when the malicious person forces the user\u2019s browser to send an authenticated request to a server?",
		"num": "890",
		"correct_answer": "a",
		"answers": {
			"a": "Cross-site request forgery",
			"b": "Cross-site scripting",
			"c": "Session hijacking",
			"d": "Server side request forgery"
		}
	},
	{
		"question": "True or false? The properties of single files and entire directories can be changed to a hidden status to hide messages using the stego process?",
		"num": "891",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which Nmap option would you use if you were not concerned about being detected and wanted to perform a very fast scan?",
		"num": "892",
		"correct_answer": "b",
		"answers": {
			"a": "\u2013T0",
			"b": "\u2013T5",
			"c": "-O",
			"d": "-A"
		}
	},
	{
		"question": "It has been reported to you that someone has caused an information spillage on their computer.\nYou go to the computer, disconnect it from the network, remove the keyboard and mouse, and power it down.\nWhat step in incident handling did you just complete?",
		"num": "893",
		"correct_answer": "c",
		"answers": {
			"a": "Discovery",
			"b": "Recovery",
			"c": "Containment",
			"d": "Eradication"
		}
	},
	{
		"question": "True or false, JPEG images use the discrete cosine transform to achieve compression?",
		"num": "894",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "Which of the following programs is usually targeted at Microsoft Office products?",
		"num": "895",
		"correct_answer": "c",
		"answers": {
			"a": "Polymorphic virus",
			"b": "Multipart virus",
			"c": "Macro virus",
			"d": "Stealth virus"
		}
	},
	{
		"question": "Jane wishes to forward X-Windows traffic to a remote host as well as POP3 traffic.\nShe is worried that adversaries might be monitoring the communication link and could inspect captured traffic.\nShe would like to tunnel the information to the remote end but does not have VPN capabilities to do so.\nWhich of the following tools can she use to protect the link?",
		"num": "896",
		"correct_answer": "d",
		"answers": {
			"a": "MD5",
			"b": "PGP",
			"c": "RSA",
			"d": "SSH"
		}
	},
	{
		"question": "Attackers send an ACK probe packet with random sequence number, no response means port is filtered (Stateful firewall is present) and RST response means the port is not filtered. What type of Port Scanning is this?",
		"num": "897",
		"correct_answer": "d",
		"answers": {
			"a": "RST flag scanning",
			"b": "FIN flag scanning",
			"c": "SYN flag scanning",
			"d": "ACK flag scanning"
		}
	},
	{
		"question": "A common cryptographical tool is the use of XOR.\n\nXOR the following binary values:\n10110001\n00111010",
		"num": "898",
		"correct_answer": "a",
		"answers": {
			"a": "10001011",
			"b": "11011000",
			"c": "10111100",
			"d": "10011101"
		}
	},
	{
		"question": "Which of the following guidelines or standards is associated with the credit card industry?",
		"num": "899",
		"correct_answer": "d",
		"answers": {
			"a": "Control Objectives for Information and Related Technology (COBIT)",
			"b": "Sarbanes-Oxley Act (SOX)",
			"c": "Health Insurance Portability and Accountability Act (HIPAA)",
			"d": "Payment Card Industry Data Security Standards (PCI DSS)"
		}
	},
	{
		"question": "A security analyst is performing an audit on the network to determine if there are any deviations from the security policies in place.\nThe analyst discovers that a user from the IT department had a dial-out modem installed.\nWhich security policy must the security analyst check to see if dial-out modems are allowed?",
		"num": "900",
		"correct_answer": "c",
		"answers": {
			"a": "Firewall-management policy",
			"b": "Acceptable-use policy",
			"c": "Remote-access policy",
			"d": "Permissive policy"
		}
	},
	{
		"question": "It is possible to prevent buffer overflows by adding bounds checking to all buffers.",
		"num": "901",
		"correct_answer": "a",
		"answers": {
			"a": "True",
			"b": "False"
		}
	},
	{
		"question": "As an Ethical Hacker you are capturing traffic from your customer network with Wireshark and you need to find and verify just SMTP traffic.\nWhat command in Wireshark will help you to find this kind of traffic?",
		"num": "902",
		"correct_answer": "b",
		"answers": {
			"a": "request smtp 25",
			"b": "tcp.port eq 25",
			"c": "smtp port",
			"d": "tcp.contains port 25"
		}
	},
	{
		"question": "Penetration testing is a method of actively evaluating the security of an information system or network by simulating an attack from a malicious source.\n\nWhich of the following technique is used to simulate an attack from someone who is unfamiliar with the system?",
		"num": "903",
		"correct_answer": "a",
		"answers": {
			"a": "Black box pen testing",
			"b": "White box pen testing",
			"c": "Grey box pen testing",
			"d": "Maintaining Access",
			"e": "Announced pen testing"
		}
	},
	{
		"question": "The \"gray box testing\" methodology enforces what kind of restriction?",
		"num": "904",
		"correct_answer": "a",
		"answers": {
			"a": "The internal operation of a system is only partly accessible to the tester.",
			"b": "Only the external operation of a system is accessible to the tester.",
			"c": "The internal operation of a system is completely known to the tester.",
			"d": "Only the internal operation of a system is known to the tester"
		}
	},
	{
		"question": "How can a policy help improve an employee's security awareness?",
		"num": "905",
		"correct_answer": "a",
		"answers": {
			"a": "By implementing written security procedures, enabling employee security training, and promoting the benefits of security",
			"b": "By using informal networks of communication, establishing secret passing procedures, and immediately terminating employees",
			"c": "By sharing security secrets with employees, enabling employees to share secrets, and establishing a consultative help line",
			"d": "By decreasing an employee's vacation time, addressing ad-hoc employment clauses, and ensuring that managers know employee strengths"
		}
	},
	{
		"question": "To see how some of the hosts on your network react, Winston sends out SYN packets to an IP range.\nA number of IPs respond with a SYN/ACK response.\nBefore the connection is established he sends RST packets to those hosts to stop the session.\nWinston has done this to see how his intrusion detection system will log the traffic.\nWhat type of scan is Winston attempting here?",
		"num": "906",
		"correct_answer": "d",
		"answers": {
			"a": "Winston is attempting to find live hosts on your company's network by using an XMAS scan.",
			"b": "He is utilizing a SYN scan to find live hosts that are listening on your network.",
			"c": "This type of scan he is using is called a NULL scan.",
			"d": "He is using a half-open scan to find live hosts on your network."
		}
	},
	{
		"question": "A company firewall engineer has configured a new DMZ to allow public systems to be located away from the internal network.\nThe engineer has three security zones set:\nUntrust (Internet) (Remote network = 217.77.88.0/24)\nDMZ (DMZ) (11.12.13.0/24)\nTrust (Intranet) (192.168.0.0/24)\n\nThe engineer wants to configure remote desktop access from a fixed IP on the remote network to a remote desktop server in the DMZ.\nWhich rule would best fit this requirement?",
		"num": "907",
		"correct_answer": "b",
		"answers": {
			"a": "Permit 217.77.88.0/24 11.12.13.0/24 RDP 3389",
			"b": "Permit 217.77.88.12 11.12.13.50 RDP 3389",
			"c": "Permit 217.77.88.12 11.12.13.0/24 RDP 3389",
			"d": "Permit 217.77.88.0/24 11.12.13.50 RDP 3389"
		}
	},
	{
		"question": "You receive an e-mail like the one shown below. When you click on the link contained in the mail, you are redirected to a website seeking you to download free Anti-Virus software.\n\n\tDear valued customers,\n\tWe are pleased to announce the newest version of Antivirus 2010 for Windows which will probe you with total security against the latest spyware, malware, viruses, Trojans and other online threats. Simply visit the link below and enter your antivirus code.\n\t\n\tAntivirus code: 5014\n\thttp://www.juggyboy/virus/virus.html\n\t\n\tThank you for choosing us, the worldwide leader Antivirus solutions.\n\t\n\tMike Robertson\n\tPDF Reader Support\n\tCopyright Antivirus 2010 ?All rights reserved\n\t\n\tIf you want to stop receiving mail, please go to:\n\thttp://www.juggyboy.com\n\tor you may contact us at the following address: Media Internet Consultants, Edif. Neptuno, Planta Baja, Ave. Ricardo J. Alfaro, Tumba Muerto, n/a Panama\n\nHow will you determine if this is Real Anti-Virus or Fake Anti-Virus website?",
		"num": "908",
		"correct_answer": "c",
		"answers": {
			"a": "Look at the website design, if it looks professional then it is a Real Anti-Virus website",
			"b": "Connect to the site using SSL, if you are successful then the website is genuine",
			"c": "Search using the URL and Anti-Virus product name into Google and lookout for suspicious warnings against this site",
			"d": "Download and install Anti-Virus software from this suspicious looking site, your Windows 7 will prompt you and stop the installation if the downloaded file is a malware",
			"e": "Download and install Anti-Virus software from this suspicious looking site, your Windows 7 will prompt you and stop the installation if the downloaded file is a malware"
		}
	},
	{
		"question": "The collection of potentially actionable, overt, and publicly available information is known as",
		"num": "909",
		"correct_answer": "a",
		"answers": {
			"a": "Open-source intelligence",
			"b": "Human intelligence",
			"c": "Social intelligence",
			"d": "Real intelligence"
		}
	},
	{
		"question": "Some viruses affect computers as soon as their code is executed; other viruses lie dormant until a pre-determined logical circumstance is met.\nIdentify the virus that modifies the directory table entries so that directory entries point to the virus code instead of the actual program.\n",
		"num": "910",
		"correct_answer": "b",
		"answers": {
			"a": "Macro Viruses",
			"b": "Cluster Viruses",
			"c": "Encryption Viruses ",
			"d": "Boot Sector Viruses"
		}
	},
	{
		"question": "A security analyst in an insurance company is assigned to test a new web application that will be used by clients to help them choose and apply for an insurance plan.\nThe analyst discovers that the application is developed in ASP scripting language and it uses MSSQL as a database backend.\nThe analyst locates the application's search form and introduces the following code in the search input field.<\n\n<IMG SRC=vbscript:msgbox(\"Vulnerable\");> originalAttribute=\"SRC\" originalPath=\"vbscript:msgbox (\"Vulnerable\");>\"\n\nWhen the analyst submits the form, the browser returns a pop-up window that says \"Vulnerable\".\nWhich web applications vulnerability did the analyst discover?",
		"num": "911",
		"correct_answer": "c",
		"answers": {
			"a": "Cross-site request forgery",
			"b": "Command injection",
			"c": "Cross-site scripting",
			"d": "SQL injection"
		}
	},
	{
		"question": "What is the main disadvantage of the scripting languages as opposed to compiled programming languages?",
		"num": "912",
		"correct_answer": "d",
		"answers": {
			"a": "Scripting languages are hard to learn.",
			"b": "Scripting languages are not object-oriented.",
			"c": "Scripting languages cannot be used to create graphical user interfaces.",
			"d": "Scripting languages are slower because they require an interpreter to run the code."
		}
	},
	{
		"question": "While testing web applications, you attempt to insert the following test script into the search area on the company's web site:\n\n &lt;script&gt;alert('Testing Testing Testing')&lt;/script&gt;\n\nLater, when you press the search button, a pop up box appears on your screen with the text \"Testing Testing Testing\".\nWhat vulnerability is detected in the web application here?",
		"num": "913",
		"correct_answer": "a",
		"answers": {
			"a": "Cross Site Scripting",
			"b": "Password attacks",
			"c": "A Buffer Overflow",
			"d": "A hybrid attack"
		}
	},
	{
		"question": "What is considered to be a violation of memory safety?",
		"num": "914",
		"correct_answer": "e",
		"answers": {
			"a": "HTML",
			"b": "Null Characters",
			"c": "C++",
			"d": "Programming language",
			"e": "Buffer Overrun"
		}
	},
	{
		"question": "What is a successful method for protecting a router from potential smurf attacks?",
		"num": "915",
		"correct_answer": "d",
		"answers": {
			"a": "Placing the router in broadcast mode",
			"b": "Enabling port forwarding on the router",
			"c": "Installing the router outside of the network's firewall",
			"d": "Disabling the router from accepting broadcast ping messages"
		}
	},
	{
		"question": "Which of the following is a hashing algorithm?",
		"num": "916",
		"correct_answer": "c",
		"answers": {
			"a": "DES",
			"b": "ROT13",
			"c": "MD5",
			"d": "PGP"
		}
	},
	{
		"question": "You are performing information gathering for an important penetration test.\nYou have found pdf, doc, and images in your objective. You decide to extract metadata from these files and analyze it.\nWhat tool will help you with the task?",
		"num": "917",
		"correct_answer": "b",
		"answers": {
			"a": "cdpsnarf",
			"b": "Metagoofil",
			"c": "Armitage",
			"d": "Dimitry"
		}
	},
	{
		"question": "Which port, when configured on a switch receives a copy of every packet that passes through it?",
		"num": "918",
		"correct_answer": "c",
		"answers": {
			"a": "R-DUPE Port",
			"b": "MIRROR port",
			"c": "SPAN port",
			"d": "PORTMON"
		}
	},
	{
		"question": "An organization hires a tester to do a wireless penetration test.\nPrevious reports indicate that the last test did not contain management or control packets in the submitted traces.\nWhich of the following is the most likely reason for lack of management or control packets?",
		"num": "919",
		"correct_answer": "d",
		"answers": {
			"a": "The wireless card was not turned on.",
			"b": "The wrong network card drivers were in use by Wireshark.",
			"c": "On Linux and Mac OS X, only 802.11 headers are received in promiscuous mode.",
			"d": "Certain operating systems and adapters do not collect the management or control packets."
		}
	},
	{
		"question": "Which of the following is a primary service of the U.S. Computer Security Incident Response Team (CSIRT)?",
		"num": "920",
		"correct_answer": "a",
		"answers": {
			"a": "CSIRT provides an incident response service to enable a reliable and trusted single point of contact for reporting computer security incidents worldwide.",
			"b": "CSIRT provides a computer security surveillance service to supply a government with important intelligence information on individuals travelling abroad.",
			"c": "CSIRT provides a penetration testing service to support exception reporting on incidents worldwide by individuals and multi-national corporations.",
			"d": "CSIRT provides a vulnerability assessment service to assist law enforcement agencies with profiling an individual's property or company's asset."
		}
	},
	{
		"question": "Steganography is a technique of hiding a secret message within an ordinary message and extracting it at the destination to maintain confidentiality of data.\nWhich of the following steganography technique embed secret message in the frequency domain of a signal?",
		"num": "921",
		"correct_answer": "b",
		"answers": {
			"a": "Substitution techniques",
			"b": "Transform domain techniques",
			"c": "Spread spectrum techniques",
			"d": "Domain distortion techniques",
			"e": "Cover generation techniques"
		}
	},
	{
		"question": "Which of the layered approaches to security hides data in ICMP traffic:",
		"num": "922",
		"correct_answer": "a",
		"answers": {
			"a": "Covert channels",
			"b": "Unique",
			"c": "Hiding directories",
			"d": "Encryption"
		}
	},
	{
		"question": "Which initial procedure should an ethical hacker perform after being brought into an organization?",
		"num": "923",
		"correct_answer": "c",
		"answers": {
			"a": "Begin security testing.",
			"b": "Turn over deliverables.",
			"c": "Sign a formal contract with non-disclosure.",
			"d": "Assess what the organization is trying to protect."
		}
	},
	{
		"question": "You are performing a port scan with nmap.\nYou are in hurry and conducting the scans at the fastest possible speed.\nHowever, you don't want to sacrifice reliability for speed.\nIf stealth is not an issue, what type of scan should you run to get very reliable results?",
		"num": "924",
		"correct_answer": "b",
		"answers": {
			"a": "Stealth scan",
			"b": "Connect scan",
			"c": "Fragmented packet scan",
			"d": "XMAS scan"
		}
	},
	{
		"question": "Which of the following types of firewall inspects only header information in network traffic?",
		"num": "925",
		"correct_answer": "a",
		"answers": {
			"a": "Packet filter",
			"b": "Stateful inspection",
			"c": "Circuit-level gateway",
			"d": "Application-level gateway"
		}
	},
	{
		"question": "Keystroke loggers are stealth software packages that are used to monitor keyboard activities.\nWhich is the best location to place such keyloggers?",
		"num": "926",
		"correct_answer": "a",
		"answers": {
			"a": "Keyboard hardware and the operating system",
			"b": "UPS and keyboard",
			"c": "Operating system and UPS",
			"d": "Monitor and keyboard software"
		}
	},
	{
		"question": "Which of the following is a low-tech way of gaining unauthorized access to systems?",
		"num": "927",
		"correct_answer": "a",
		"answers": {
			"a": "Social Engineering",
			"b": "Eavesdropping",
			"c": "Scanning",
			"d": "Sniffing"
		}
	}
]


randomise, answers_on_the_fly = setup()

num_right, skipped_questions = 0, 0
answers_wrong = {}
for i, question in enumerate(questions, 1):
	try:
		# display question
		if randomise:
			print(f"\n{i} [q{question['num']}]) {question['question']}")
		else:
			print(f"\n{question['num']}) {question['question']}")
		for k, v in zip(question['answers'].keys(), question['answers'].values()):
			print(f"\t{k}) {v}")
		
		# seek and validate user input
		user_input = ""
		while not user_input or not all(map(lambda x: x in "abcdefgq" and user_input.count(x) == 1, user_input)):
			user_input = input("> ").lower().strip()
		questions[int(question["num"]) - 1]['user_answer'] = user_input		
		if "q" in user_input:
			raise KeyboardInterrupt

		# mark the user's input, display result
		if all(map(lambda x: x in user_input, question["correct_answer"])) and all(map(lambda x: x in question["correct_answer"], user_input)):
			num_right += 1
			if answers_on_the_fly:
				print(f"Correct! You have {num_right}/{len(questions)} correct so far. ({round((num_right / (i - skipped_questions)) * 100)}% of answered questions)")
		else:
			answers_wrong[question["num"]] = user_input
			if answers_on_the_fly:
				print(f"The correct answer is: {', '.join(question['correct_answer'])}. You have {num_right}/{len(questions)} correct so far. ({round((num_right / i) * 100)}% of answered questions)")
	except KeyboardInterrupt:
		skipped_questions += 1
		if "y" in input("\nDo you really wish to quit? y/N\n> "):
			break
		else:
			continue

exit_text = f"""
\n\nYou scored {num_right}/{i - skipped_questions} ({round((num_right / i) * 100)}%).
You were wrong on the following questions:
{', '.join(answers_wrong.keys())}

{'-' * 90}"""
for k, v in answers_wrong.items():
	q = questions[int(k) - 1]
	exit_text += f"\n{k}) {q['question']}\nYour answer: "
	if len(q["correct_answer"]) > 1:  # if multi-choice
		for char in v:
			exit_text += f"\n\t{char}) {q['answers'][char]}"
		exit_text += "\nCorrect answer:"
		for char in q["correct_answer"]:
			exit_text += f"\n\t{char}) {q['answers'][char]}"
		exit_text += f"\n{'-' * 90}"
	else:
		exit_text += f"{q['answers'][v]}\nCorrect answer: {q['answers'][q['correct_answer']]}\n{'-'*90}"
print(exit_text)

print_out = input("\nThe correct answers and results can be saved to file.\nSave results to file? y/N\n> ")
if "y" in print_out.lower():
	import os
	f = f"{os.getcwd()}\\CEH_test_results.txt"
	if not os.path.isfile(f) or (os.path.isfile(f) and "y" in input(f"{f} already exists. Overwrite? y/N\n> ")):
		with open(f, "w") as out_file:
			out_file.write(exit_text)
	print(f"Results saved to '{f}'.")

input("Press <enter> to exit.")
