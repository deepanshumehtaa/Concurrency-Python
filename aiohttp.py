"""
The ClientSession class in aiohttp is a special type of session that provides a pool of connections that can be reused for multiple requests. It is designed to be used with asynchronous code and is particularly useful when making multiple requests to the same server or when you need to maintain a persistent connection to a server.
Some key features of ClientSession include:

Connection pooling:
  ClientSession maintains a pool of connections that can be reused for multiple requests,
  which can help improve performance and reduce the overhead of creating new connections for each request.

Persistent connections:
  ClientSession allows you to maintain a persistent connection to a server, which can be useful for 
  apps that require long-running connections, such as web sockets or streaming data.

Request and response handling:
  ClientSession provides methods for making requests and handling responses, including request() 
  for making HTTP requests and get(), post(), put(), and delete() for specific HTTP methods.

Async/await support:
  ClientSession is designed to work with async/await syntax, which allows you to write asynchronous code that is easier to read and maintain.
In summary, ClientSession in aiohttp is a powerful tool for making asynchronous HTTP requests and handling responses. Its connection pooling, persistent connections, and support for async/await syntax make it a popular choice for building scalable and efficient networked applications.
"""


import aiohttp

connector = aiohttp.TCPConnector(limit=100, ttl_dns_cache=300)
session = aiohttp.ClientSession(connector=connector)

"""
TCPConnector with a limit of 100 connections and a DNS cache TTL of 300 seconds
The TCPConnector class provides several configuration options that you can use to customize the behavior of the connection pool, including:

limit:
  The maximum number of connections that can be opened at the same time.
ttl_dns_cache:
  The time-to-live (TTL) of the DNS cache, in seconds.
keepalive_timeout:
  max time a connection can be idle before it is closed.
enable_cleanup_closed:
  Whether to enable automatic cleanup of closed connections.

"""

