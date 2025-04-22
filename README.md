# Diffie-Hellman Key Exchange in Python

This repository contains a Python implementation of the Diffie-Hellman key exchange algorithm. This algorithm allows two parties (Alice and Bob in this example) to securely establish a shared secret over an insecure communication channel without prior secret agreement.

## Overview

The Diffie-Hellman key exchange works by having Alice and Bob agree on a public prime number (`p`) and a primitive root (`g`) modulo `p`. Each party then generates a private secret key and calculates a public key based on the agreed-upon parameters and their private key. They exchange their public keys, and then each party can independently compute the same shared secret using their private key and the other party's public key.

This implementation includes the following functionalities:

* **`is_prime(n)`:** A function to check if a given number `n` is prime.
* **`generate_prime(min_val, max_val)`:** A function to generate a random prime number within a specified range.
* **`power(base, exp, mod)`:** A function to calculate `(base ** exp) % mod` efficiently using modular exponentiation.
* **`find_primitive_root(p)`:** A function to find a primitive root modulo a prime number `p`.
* **`diffie_hellman_key_exchange()`:** The main function that orchestrates the Diffie-Hellman key exchange process between Alice and Bob.

## How to Run

1.  **Save the code:** Save the provided Python code into a file named `dh_exchange.py` (or any other name with the `.py` extension).

2.  **Open a terminal or command prompt:**
    * **Windows:** Open Command Prompt (search for `cmd`).
    * **macOS:** Open Terminal (in Applications/Utilities).
    * **Linux:** Open your distribution's terminal application.

3.  **Navigate to the directory:** Use the `cd` command to go to the folder where you saved the `dh_exchange.py` file. For example:
    ```bash
    cd Downloads
    ```
    or
    ```bash
    cd Desktop/CryptoProjects
    ```

4.  **Run the script:** Execute the Python script using the `python` command:
    ```bash
    python main.py
    ```
    If you have both Python 2 and Python 3 installed, you might need to use `python3`:
    ```bash
    python3 main.py
    ```

5.  **Observe the output:** The script will output the following information:
    * The publicly agreed prime number (`p`).
    * The publicly agreed primitive root (`g`).
    * Alice's secret and public keys.
    * Bob's secret and public keys.
    * The shared secret calculated by Alice.
    * The shared secret calculated by Bob.
    * A confirmation message indicating if the shared secrets match.

## Important Notes on Security

* **Vulnerability to Man-in-the-Middle Attack:** This basic implementation of Diffie-Hellman is vulnerable to a man-in-the-middle (MITM) attack. An attacker can intercept the exchanged public keys and impersonate both Alice and Bob, establishing separate shared secrets with each of them.
* **Need for Authentication:** To mitigate the MITM attack, Diffie-Hellman should be combined with authentication mechanisms (e.g., digital signatures) to verify the identities of the communicating parties.
* **Choice of Parameters:** The security of Diffie-Hellman relies heavily on the choice of a large prime number `p` and a suitable primitive root `g`. The prime number should be large enough to make the discrete logarithm problem computationally infeasible for attackers. In real-world applications, standardized and well-vetted parameters are often used.
* **Educational Purpose:** This code is intended for educational purposes to demonstrate the principles of the Diffie-Hellman key exchange. For production systems, it is highly recommended to use well-established and secure cryptographic libraries that handle parameter generation and security considerations properly.

## Further Improvements (Optional)

* Implement protection against man-in-the-middle attacks (e.g., using digital signatures).
* Allow users to specify the prime number and primitive root.
* Integrate with a simple encryption/decryption mechanism using the shared secret.
* Add error handling and input validation.

## License

This code is provided under a simple open-source license (e.g., MIT License). See the `LICENSE` file for more details.

## Link Research
* [Diffie-Hellman: Hoạt động và Python](https://docs.google.com/document/d/1c0jbyEnYn_tpZCh_D8Ln81SOmzzi41PYJenZSH4MfvM/edit?usp=sharing)