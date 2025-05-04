#!/usr/bin/env python3
"""
Internet Speed Test

This script measures your internet connection's download and upload speeds
using the speedtest-cli library.

Before running, ensure you have the library installed:
    pip install speedtest-cli

Author: AI Assistant
"""

import speedtest
import sys
import time
from datetime import datetime


def format_speed(speed_bps):
    """
    Convert speed from bits per second to Mbps and format it.
    
    Args:
        speed_bps (float): Speed in bits per second
        
    Returns:
        str: Formatted speed in Mbps
    """
    speed_mbps = speed_bps / 1_000_000  # Convert to Mbps
    return f"{speed_mbps:.2f} Mbps"


def run_speed_test():
    """
    Run the speed test and return download and upload speeds.
    
    Returns:
        tuple: (download_speed, upload_speed) in bits per second
        
    Raises:
        Exception: If there's an error during the speed test
    """
    print("Initializing speed test...")
    st = speedtest.Speedtest()
    
    # Get the best server based on ping
    print("Finding optimal server...")
    st.get_best_server()
    
    # Test download speed
    print("Testing download speed...")
    download_speed = st.download()
    
    # Test upload speed
    print("Testing upload speed...")
    upload_speed = st.upload()
    
    return download_speed, upload_speed


def main():
    """
    Main function that runs the speed test and displays results.
    """
    print("=" * 60)
    print(f"INTERNET SPEED TEST - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        # Run the test with a progress indicator
        download_speed, upload_speed = run_speed_test()
        
        # Display results
        print("\nRESULTS:")
        print("-" * 60)
        print(f"Download Speed: {format_speed(download_speed)}")
        print(f"Upload Speed: {format_speed(upload_speed)}")
        print("-" * 60)
        
    except speedtest.ConfigRetrievalError:
        print("\nERROR: Unable to retrieve configuration from speedtest.net servers.")
        print("Please check your internet connection and try again.")
        return 1
    except speedtest.NoMatchedServers:
        print("\nERROR: Could not find any suitable servers for testing.")
        return 1
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {str(e)}")
        return 1
        
    print("\nSpeed test completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

