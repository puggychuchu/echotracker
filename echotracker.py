import subprocess
import time
import statistics

def ping_server(server, count=4):
    """
    Pings a server a specified number of times and returns the ping times.
    """
    try:
        # Execute the ping command
        output = subprocess.check_output(
            ["ping", "-n", str(count), server],
            universal_newlines=True
        )
        
        # Extract the ping times from the output
        lines = output.splitlines()
        ping_times = []
        for line in lines:
            if "time=" in line:
                time_ms = line.split("time=")[-1].split("ms")[0].strip()
                ping_times.append(float(time_ms))
        
        return ping_times

    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {server}. Error: {e}")
        return None

def check_connectivity(servers):
    """
    Checks connectivity and speed for a list of servers.
    """
    results = {}
    for server in servers:
        print(f"Pinging {server}...")
        ping_times = ping_server(server)
        if ping_times:
            avg_time = statistics.mean(ping_times)
            min_time = min(ping_times)
            max_time = max(ping_times)
            results[server] = {
                "average_time": avg_time,
                "min_time": min_time,
                "max_time": max_time,
                "ping_times": ping_times
            }
            print(f"Results for {server}: Avg: {avg_time}ms, Min: {min_time}ms, Max: {max_time}ms")
        else:
            results[server] = None
            print(f"Could not retrieve results for {server}.")
    return results

def main():
    servers_to_ping = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]  # Example servers (Google DNS and Cloudflare DNS)
    
    while True:
        print("Starting connectivity check...")
        results = check_connectivity(servers_to_ping)
        print("Connectivity check complete.\n")
        
        # Sleep for a specific interval before the next check
        print("Waiting for the next check...")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()