import subprocess
import pyauc


def ping(host):
    # Run the ping command and capture the output
    output = subprocess.Popen(['ping', '-c', '4', host])

    # Decode the output from bytes to a string (use 'utf-8' encoding)
    output = output.decode('utf-8')

    # Split the output into lines
    lines = output.split('\n')

    # Extract the round-trip time from the last line (usually the fourth line)
    for line in lines:
        if "round-trip min/avg/max" in line:
            # Extract the average round-trip time (in milliseconds)
            parts = line.split('/')
            avg_time = float(parts[4])
            return avg_time


if __name__ == "__main__":
    # Replace with the hostname or IP address you want to ping
    host = "8.8.8.8 8.8.4.4"
    avg_ping_time = ping(host)

    if avg_ping_time is not None:
        print(f"Average ping time to {host}: {avg_ping_time} ms")
    else:
        print(f"Ping to {host} failed.")
