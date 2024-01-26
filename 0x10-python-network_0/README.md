# Networking README

This README file provides an overview of basic networking concepts and includes information on IP addresses, protocols, ports, and common networking commands.

## Table of Contents
- [IP Addresses](#ip-addresses)
- [Protocols](#protocols)
- [Ports](#ports)
- [Common Networking Commands](#common-networking-commands)

## IP Addresses

An IP address is a numerical label assigned to each device participating in a computer network. There are two types of IP addresses: IPv4 and IPv6.

### IPv4
IPv4 addresses consist of four sets of numbers separated by dots (e.g., 192.168.0.1). Each set can have a value between 0 and 255.

### IPv6
IPv6 addresses are longer and are expressed in hexadecimal notation (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

## Protocols

Protocols define the rules for communication between devices on a network. Common networking protocols include:
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)
- HTTP/HTTPS (Hypertext Transfer Protocol/Secure)
- FTP (File Transfer Protocol)
- ICMP (Internet Control Message Protocol)

## Ports

Ports are logical endpoints for communication in a network. They allow different services or applications to share the same IP address. Common port numbers include:
- 80 (HTTP)
- 443 (HTTPS)
- 21 (FTP)
- 22 (SSH)
- 25 (SMTP)

## Common Networking Commands

### Ping
The `ping` command is used to test the reachability of a host on a network.
```bash
ping example.com
