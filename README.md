## How to local debug:
1. Run "npm install"
2. Run "gulp ngrok-serve"
3. Copy last lines of output information, including "PUBLIC_HOSTNAME: xxxxx", to output.txt
4. Run "python hostname-config.py" to update .env.local
5. F5 with "Debug (Edge Teams)"