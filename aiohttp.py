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


