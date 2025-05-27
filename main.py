import random


def is_prime(n):
    """
    Kiểm tra một số có phải là số nguyên tố bằng phương pháp chia thử.

    Tham số:
        n: Số cần kiểm tra tính nguyên tố

    Trả về:
        bool: True nếu n là số nguyên tố, False nếu không phải

    Độ phức tạp thời gian: O(sqrt(n))
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_val, max_val):
    """
    Tạo một số nguyên tố ngẫu nhiên trong phạm vi xác định bằng cách kiểm tra các số ngẫu nhiên.

    Tham số:
        min_val: Giới hạn dưới của phạm vi
        max_val: Giới hạn trên của phạm vi

    Trả về:
        int: Một số nguyên tố ngẫu nhiên giữa min_val và max_val
    """
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num


def power(base, exp, mod):
    """
    Tính (base^exp) % mod một cách hiệu quả bằng thuật toán bình phương và nhân.
    Phương pháp này nhanh hơn nhiều so với lũy thừa thông thường cho các số lớn.

    Tham số:
        base: Số cơ sở
        exp: Số mũ
        mod: Số modulo

    Trả về:
        int: Kết quả của (base^exp) % mod

    Độ phức tạp thời gian: O(log(exp))
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:  # Nếu số mũ là số lẻ
            res = (res * base) % mod
        exp >>= 1  # Chia số mũ cho 2
        base = (base * base) % mod  # Bình phương cơ sở
    return res


def get_prime_factors(n):
    """
    Tìm tất cả các thừa số nguyên tố của n.

    Tham số:
        n: Số cần phân tích thừa số

    Trả về:
        set: Một tập hợp chứa tất cả các thừa số nguyên tố duy nhất của n

    Độ phức tạp thời gian: O(sqrt(n))
    """
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors


def find_primitive_root(p):
    """
    Tìm một căn nguyên thủy modulo p bằng cách kiểm tra các ứng viên tiềm năng.

    Một căn nguyên thủy g modulo p là một số nguyên sao cho g^1, g^2, ..., g^(p-1)
    đều khác nhau theo modulo p, nghĩa là g tạo ra toàn bộ nhóm nhân.

    Tham số:
        p: Số nguyên tố cần tìm căn nguyên thủy

    Trả về:
        int hoặc None: Căn nguyên thủy đầu tiên được tìm thấy, hoặc None nếu p không phải số nguyên tố
    """
    if not is_prime(p):
        return None
    phi = p - 1  # Hàm phi Euler cho số nguyên tố p là p-1

    # Tìm các thừa số nguyên tố của phi(p)
    factors = get_prime_factors(phi)

    # Kiểm tra từng số từ 2 đến p-1 để tìm căn nguyên thủy
    for res in range(2, p):
        if is_primitive_root(res, p, phi, factors):
            return res
    return None


def is_primitive_root(g, p, phi, factors):
    """
    Kiểm tra xem g có phải là căn nguyên thủy modulo p hay không.

    Một số g là căn nguyên thủy modulo p nếu với mỗi thừa số nguyên tố q của phi(p),
    g^(phi(p)/q) ≠ 1 (mod p).

    Tham số:
        g: Số cần kiểm tra
        p: Modulo nguyên tố
        phi: Hàm phi Euler của p (bằng p-1 đối với p nguyên tố)
        factors: Các thừa số nguyên tố của phi

    Trả về:
        bool: True nếu g là căn nguyên thủy modulo p, False nếu không phải
    """
    for factor in factors:
        if power(g, phi // factor, p) == 1:
            return False
    return True


def diffie_hellman_key_exchange():
    """
    Thực hiện giao thức trao đổi khóa Diffie-Hellman giữa Alice và Bob.

    Giao thức hoạt động như sau:
    1. Alice và Bob thống nhất các tham số công khai p (số nguyên tố) và g (căn nguyên thủy)
    2. Alice chọn một số bí mật 'a' và gửi cho Bob A = g^a mod p
    3. Bob chọn một số bí mật 'b' và gửi cho Alice B = g^b mod p
    4. Alice tính khóa bí mật chung s = B^a mod p
    5. Bob tính khóa bí mật chung s = A^b mod p
    6. Cả Alice và Bob đều có cùng một khóa bí mật chung s

    Cài đặt này minh họa các nguyên tắc toán học đằng sau giao thức trao đổi khóa
    Diffie-Hellman nhưng không an toàn để sử dụng trong môi trường sản xuất thực tế.
    """
    # 1. Thống nhất một số nguyên tố công khai (p) và một căn nguyên thủy (g)
    p = generate_prime(100, 500)
    g = find_primitive_root(p)

    if g is None:
        print(f"Không thể tìm thấy căn nguyên thủy cho {p}. Hủy bỏ.")
        return

    print(f"Số nguyên tố đã thống nhất công khai (p): {p}")
    print(f"Căn nguyên thủy đã thống nhất công khai (g): {g}")

    # 2. Khóa bí mật (a) và khóa công khai (A) của Alice
    alice_secret = random.randint(1, p - 1)
    alice_public = power(g, alice_secret, p)
    print(f"\nKhóa bí mật của Alice (a): {alice_secret}")
    print(f"Khóa công khai của Alice (A): {alice_public}")

    # 3. Khóa bí mật (b) và khóa công khai (B) của Bob
    bob_secret = random.randint(1, p - 1)
    bob_public = power(g, bob_secret, p)
    print(f"Khóa bí mật của Bob (b): {bob_secret}")
    print(f"Khóa công khai của Bob (B): {bob_public}")

    # 4. Trao đổi khóa công khai (A và B) - trong tình huống thực tế, điều này xảy ra qua mạng

    # 5. Alice tính toán khóa bí mật chung (s_a)
    alice_shared_secret = power(bob_public, alice_secret, p)
    print(f"\nAlice tính toán khóa bí mật chung (s_a): {alice_shared_secret}")

    # 6. Bob tính toán khóa bí mật chung (s_b)
    bob_shared_secret = power(alice_public, bob_secret, p)
    print(f"Bob tính toán khóa bí mật chung (s_b): {bob_shared_secret}")

    # Xác minh rằng các khóa bí mật chung là giống nhau
    if alice_shared_secret == bob_shared_secret:
        print("\nKhóa bí mật chung được thiết lập thành công!")
        print(f"Khóa bí mật chung: {alice_shared_secret}")
    else:
        print("\nLỗi: Các khóa bí mật chung không khớp nhau!")


if __name__ == "__main__":
    diffie_hellman_key_exchange()
