package main

import (
	"fmt"
	"net"
	"time"
)

func main() {
	var host string
	fmt.Print("Enter the host: ")
	fmt.Scan(&host)
	port := "80"
	timeout := time.Duration(1 * time.Second)
	start := time.Now()
	conn, err := net.DialTimeout("tcp", host+":"+port, timeout)
	elapsed := time.Since(start)
	if err != nil {
		fmt.Printf("%s %s %s\n", host, "not responding", err.Error())
	} else {
		ip, err := net.LookupIP(host)
		if err != nil {
			fmt.Printf("Could not get IPs: %v\n", err)
		} else {
			fmt.Printf("%s %s %s\n", host, "responding on port:", port)
			for _, ip := range ip {
				fmt.Printf("IP address: %s\n", ip.String())
			}
		}
	}
	fmt.Printf("Time taken: %s\n", elapsed)
	conn.Close()
}
