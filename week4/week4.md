# Components of IoT Application

Gleb Bulygin<br>gbulygin@students.oamk.fi<br>DIN24SP<br>Autumn 2026

---

## Week 4

### 26. Use [Croc](https://github.com/schollz/croc) to move file or files between two or more hosts/devices. Answer shortly:

I have installed **croc** on Windows with `choco install croc` command (PowerShell as Admin).

I have installed **croc** on Android with `pkg install croc` (I use **termux** app).

![](./src/img/croc_win_send.png)

**_Figure 4.1_** — Sending files via **croc** from powershell

![](./src/img/Screenshot_20261005_223150_Termux.jpg)

**_Figure 4.2_** — Receive file via **croc** on Android.

> I accidentally cancelled the first file send, but on the second try it worked. Also, before the next screenshot I reinstalled the **termux** app. The one I used initially was the outdated version from the Google Playstore. It had quite a few issues. I installed latest version from the F-Droid.
>
> My phone in on cellular data and my windows host is connected to my home Wi-Fi.
>
> Then I have moved the screenshot above from my Android phone to my laptop.

![](./src/img/croc_send_android.png)

**_Figure 4.3_** — Send a file from Android via **croc**.

![](./src/img/croc_win_recieve.png)

**_Figure 4.4_** — Screenshot successfully received on Windows.

- **How the Croc works?**

  Both sides pick/generate a one-time code phrase. This phrase is used in a **PAKE** (Password Authenticated Key Exchange) handshake, which lets sender and receiver derive the same secret encryption key without ever sending the phrase itself over the network. Croc then encrypts the file (AES-256/ChaCha20) and transfers it directly between the two hosts if they can reach each other, falling back to a relay server otherwise.

- **How the Croc moves files if both hosts are not directly visible to each other? (for example, both are behind NATs or basic firewalls)**

  Both hosts only make **outbound** connections to a public (or self-hosted) **relay server** — no incoming ports or port-forwarding are needed. The relay server acts as a rendezvous point: it helps the two peers find each other and, if a direct peer-to-peer connection can't be made (common when both are behind NAT/firewalls), it simply pipes the already end-to-end encrypted traffic between them. Since the data is encrypted before it reaches the relay, the relay operator can't read the file contents.

### 27. Study how NTP protocol operates and analyse this [Python NTP client code](https://tl.oamk.fi/iot/dl/ntp_client.html). Also available here as [plain text](https://tl.oamk.fi/iot/dl/ntp_client.txt).

- **This Python script uses direct socket programming to access the NTP server. Comment individual socket programming related code lines. Also, answer these:**
  - **What is the NTP server (DNS) hostname?**

    `pool.ntp.org` — the default `host` parameter of the `ntp_time()` function.

  - **What is the destination port number being used?**

    Port **123**, the default `port` parameter of `ntp_time()` and the standard well-known port for the NTP protocol.

  - **Is this Python script using TCP or UDP? How do you know?**

    It's using **UDP**. The socket is created with `SOCK_DGRAM` (`socket(AF_INET, SOCK_DGRAM)`), which is the datagram/UDP socket type, as opposed to `SOCK_STREAM` which would indicate TCP. The code also uses `sendto()`/`recvfrom()` instead of `connect()`/`send()`/`recv()`, which is typical of connectionless UDP usage — the socket is never explicitly connected to the server before sending data.

- **Try to execute the app with Python**

  ![](./src/img/python_ntp_execution.png)

  **_Figure 4.5_** — `Python_NTP_client_code` execution in the terminal

### 28. Do these Python programming assignments with Windows or Linux (or with MacOS if you want and know how)

- **For example, use [https://realpython.com/python-sockets/](https://realpython.com/python-sockets/) or similar site(s) for socket programming example codes and create TCP client and TCP server Python scripts**
- **Establish a TCP connection between your client and server Python scripts (either as localhost traffic or between two separate hosts if you have access to two or more Python running hosts without firewall preventing the traffic)**
- **Transfer some ASCII text strings between the hosts**
  - **TCP client connects to the server, sends some plain text string and then disconnects**
  - **Server prints the text to the console or elsewhere**
  - **Save your source codes and work. You need scripts again during the course week #5 (Wireshark protocol analyzer assignments)**
- **Use netstat or similar command line tools to check the TCP connection status (for example the Python server script LISTENING the selected TCP port)**

![](./src/img/tcp.png)

**_Figure 4.6_** — sequence of socket API calls and data flow for TCP (source: [https://realpython.com/python-sockets/](https://realpython.com/python-sockets/))

I don't have access to another machine now, so my app will run on localhost. I have created two files `tcp_server.py` and `tcp_client.py`.

```python
# tcp_server.py
import socket

HOST = "0.0.0.0"  # listen on all interfaces so a remote client can connect too
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from {addr}: {data.decode('ascii')}")
            print(f"Disconnected: {addr}")

```

```python
# tcp_client.py
import socket

HOST = "127.0.0.1"  # localhost
PORT = 65432
MESSAGE = "Hello from the TCP client!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(MESSAGE.encode("ascii"))
    print(f"Sent: {MESSAGE}")
```

![](./src/img/tcp_client-server.png)

**_Figure 4.7_** — a line of text sent from the client and received by the server

![](./src/img/netstat_listening.png)

**_Figure 4.8_** — tcp_server.py app is listening for all incoming connections on port 65432

After I stop the server app the command above returns nothing.

---
