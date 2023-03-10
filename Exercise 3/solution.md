# Exercise 3:

## 1
`create(topic, data)` creates a new file on the server and stores the hash of the data.
`get(topic)` requests the data from the server and verifies it against the hash stored on the client. If the hash is correct, the data is returned. If the hash is incorrect, an error is returned.
`update(topic, data)` updates the data on the server and updates the hash of the data on the client.
`delete(topic)` deletes the data on the server and deletes the hash on the client.

This is a very simple protocol. It uses the collision resistance of sha256 to ensure that the data has not been tampered with. It also uses the one-way nature of sha256 to ensure that the server cannot forge data.

## 2
### a
`solve(p, d)` takes a puzzle string `p` and a difficulty `d`. It then hashes generates a random 16 character ascii string, adds it to the puzzle string, and hashes it. If the hash starts with `d` zeros, it returns the random string. Otherwise, it generates a new random string and tries again.

### b
`verify(p, nonce)` takes a puzzle string `p` and a nonce `nonce`. It then hashes the puzzle string and the nonce and returns the number of leading zeros, thus verifying that the puzzle has been solved with the given difficulty.